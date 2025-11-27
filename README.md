# 📘 Projeto Antlia Cambio

Sistema desenvolvido em **Python + Flask** que permita cadastrar compras de dólares e calcular informações da carteira com base nas cotações do Banco Central do Brasil (BCB).

---

# 1️⃣ Banco de Dados

Utilizamos **PostgreSQL** com a seguinte URL de conexão:

```
postgresql://appuser:t0rk4sk1@189.126.106.110:5432/dbantlia
```

> Certifique-se de que o servidor esteja acessível e que o usuário possua permissões de leitura e escrita.

---

# 2️⃣ Repositório do Projeto

O código-fonte está disponível em:

```
https://github.com/CecilioBSantos/antlia-cambio.git
```

Clone o repositório:

```bash
git clone https://github.com/CecilioBSantos/antlia-cambio.git
cd antlia-cambio
```

---

# 3️⃣ Endpoints da API

## **Compras**

### ➤ `GET /`

Retorna a lista de compras cadastradas e a visão geral da carteira.

### ➤ `GET /compras/new`

Exibe formulário de cadastro de nova compra.

### ➤ `POST /compras/new`

Registra uma nova compra de dólares.

**Payload esperado:**

```json
{
  "data_compra": "YYYY-MM-DD",
  "quantidade_usd": "1000.00"
}
```

---

# 4️⃣ Roadmap

* [x] Estrutura inicial do projeto Flask
* [x] Integração com Banco Central (BCB - PTAX)
* [x] Cadastro de compras
* [x] Cálculo de custo médio ponderado
* [x] Listagem com totais da carteira
* [ ] API REST completa
* [ ] Autenticação (JWT/Login) opcional
* [ ] Dockerfile e docker-compose
* [ ] Testes automatizados (PyTest)
* [ ] Deploy em servidor Linux

---

# 5️⃣ Fases de Desenvolvimento

1. **Planejamento e modelagem do banco**
2. **Criação do ambiente Flask + virtualenv**
3. **Construção dos modelos e consultas**
4. **Integração com API PTAX (BCB)**
5. **Implementação dos endpoints e templates**
6. **Cálculo da carteira e custo médio**
7. **Melhorias de UI e validações**
8. **Testes, logs e monitoramento**

---

# 6️⃣ Ambiente Virtual

Crie o ambiente virtual:

```bash
python3 -m venv venv
```

Ative o ambiente:

### Linux/macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

# 7️⃣ Bibliotecas

* Flask
* Flask SQLAlchemy
* psycopg2 / sqlalchemy
* Requests
* python-dotenv
* pytz

---

# 8️⃣ Dependências

Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

Arquivo `requirements.txt` sugerido:

```
Flask
Flask-SQLAlchemy
psycopg2-binary
python-dotenv
requests
pytz
```

---

# 9️⃣ Inicialize o banco de dados

Se o banco ainda não possuir a tabela `Compra`, execute o comando de criação automática:

```python
from app import db
from models import Compra
db.create_all()
```

Ou utilize migrations (caso configurado):

```bash
flask db upgrade
```

---

# 🔟 Execute o Projeto

Com o ambiente virtual ativo:

```bash
flask run
```

Ou, se estiver usando o app direto:

```bash
python app.py
```

Acesse no navegador:

```
http://127.0.0.1:5000/
```

---

Se quiser, posso **ajustar, expandir ou padronizar** este README no estilo profissional, corporativo ou técnico. Basta pedir!
