
from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Compra
from utils import fetch_bcb_quote_for_date, previous_business_day, is_business_day
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key')

    db.init_app(app)

    @app.route('/')
    def index():
        compras = Compra.query.order_by(Compra.data_compra.desc(), Compra.ID.desc()).all()

        total_usd = sum([float(c.quantidade_usd) for c in compras]) if compras else 0
        total_brl = sum([float(c.valor_total_brl) for c in compras]) if compras else 0

        custo_medio = None
        if total_usd > 0:
            custo_medio = (Decimal(total_brl) / Decimal(total_usd)).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)

        last_cotacao = None
        if compras:
            dts = [c.datahora_cotacao for c in compras if c.datahora_cotacao is not None]
            last_cotacao = max(dts) if dts else None

        return render_template('index.html', compras=compras,
                               total_usd=total_usd, total_brl=total_brl,
                               custo_medio=custo_medio, last_cotacao=last_cotacao)

    @app.route('/compras/new', methods=['GET', 'POST'])
    def new_purchase():
        if request.method == 'POST':
            data_compra_str = request.form.get('data_compra')
            quantidade_str = request.form.get('quantidade_usd')

            # Validações básicas
            try:
                data_compra = datetime.strptime(data_compra_str, '%Y-%m-%d').date()
            except Exception:
                flash('Data inválida. Use AAAA-MM-DD.', 'danger')
                return redirect(url_for('new_purchase'))

            if not is_business_day(data_compra):
                flash('A data da compra precisa ser um dia útil (segunda a sexta).', 'danger')
                return redirect(url_for('new_purchase'))

            try:
                quantidade = Decimal(quantidade_str)
            except Exception:
                flash('Quantidade inválida.', 'danger')
                return redirect(url_for('new_purchase'))

            if quantidade <= 0:
                flash('Quantidade deve ser maior que zero.', 'danger')
                return redirect(url_for('new_purchase'))

            data_cotacao = previous_business_day(data_compra)

            try:
                quote = fetch_bcb_quote_for_date(data_cotacao)
            except Exception as e:
                flash(f'Erro ao consultar BCB: {e}', 'danger')
                return redirect(url_for('new_purchase'))

            if not quote:
                flash(f'Nenhuma cotação encontrada para {data_cotacao}.', 'warning')
                return redirect(url_for('new_purchase'))

            cotacao = Decimal(str(quote['cotacaoCompra'])).quantize(Decimal('0.0001'))
            valor_total_brl = (quantidade * cotacao).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

            try:
                dh = datetime.fromisoformat(quote['dataHoraCotacao'].replace('Z', '+00:00'))
            except Exception:
                dh = None

            compra = Compra(
                data_compra=data_compra,
                quantidade_usd=quantidade,
                cotacao_usd_brl=cotacao,
                valor_total_brl=valor_total_brl,
                datahora_cotacao=dh
            )
            db.session.add(compra)
            db.session.commit()
            flash('Compra registrada com sucesso.', 'success')
            return redirect(url_for('index'))

        return render_template('new_purchase.html')

    return app


if __name__ == '__main__':
    app = create_app()
    # app.run(debug=True)  ## rodar local
    app.run(host="0.0.0.0", port=5000, debug=True)

