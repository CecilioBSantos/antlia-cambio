
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Compra(db.Model):
    __tablename__ = 'compra'

    ID = db.Column(db.Integer, primary_key=True)
    data_compra = db.Column(db.Date, nullable=False)
    quantidade_usd = db.Column(db.Numeric(18, 4), nullable=False)
    cotacao_usd_brl = db.Column(db.Numeric(18, 6), nullable=False)
    valor_total_brl = db.Column(db.Numeric(18, 2), nullable=False)
    datahora_cotacao = db.Column(db.DateTime, nullable=True)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<Compra {self.ID} {self.data_compra} {self.quantidade_usd}USD>"
