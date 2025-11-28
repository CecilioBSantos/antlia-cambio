# Antlia Cambio — Documentação Técnica Profissional

Sistema desenvolvido em **Python + Flask**, integrado à API **PTAX do Banco Central do Brasil**, para registrar compras de moeda estrangeira (USD), calcular custo médio ponderado e exibir visão consolidada da carteira.

---

## 1. Visão Geral

O **Antlia Cambio** é uma aplicação modular e extensível voltada ao registro de operações cambiais pessoais ou corporativas. Seu objetivo é fornecer:

* Controle estruturado das compras de USD
* Consulta automática da cotação PTAX (D-1)
* Cálculo de custo médio ponderado (CMP)
* Consolidação da carteira em BRL
* Suporte para futura API REST
* Arquitetura preparada para growth

A solução utiliza **Python, Flask, SQLAlchemy, PostgreSQL e Bootstrap**, com integração direta ao serviço oficial de cotações do **Banco Central do Brasil**.

---

## 2. Banco de Dados & Estrutura do Sistema

### 2.1 Banco de Dados

O sistema se conecta a um banco PostgreSQL conforme a URL:

```
postgresql://appuser:t0rk4sk1@189.126.106.110:5432/dbantlia
```

### 2.2 Estrutura do Projeto

```
antlia-cambio/
├── app.py                  # Aplicação principal Flask
├── models.py               # Modelos ORM (Compra)
├── utils.py                # Funções auxiliares (PTAX, datas úteis)
├── requirements.txt        # Dependências do projeto
├── .env                    # Variáveis de ambiente
├── templates/              # Templates Jinja2
│   ├── base.html
│   ├── index.html
│   └── new_purchase.html
├── static/                 # Arquivos estáticos (CSS, JS, imagens)
│   ├── storage
│   ├── css
│   │   └── style.css
│   ├── img
│   │   └── logo-Antlia.webp
│   ├── favicon.ico
│   ├── js

```

---

## 3. Repositório Oficial

Código-fonte hospedado em:

```
https://github.com/CecilioBSantos/antlia-cambio.git
```

Clone o repositório:

```bash
git clone https://github.com/CecilioBSantos/antlia-cambio.git
cd antlia-cambio
```

---

## 4. Endpoints da Aplicação

### 4.1 Endpoints Implementados

| Status | Método | Rota           | Descrição                                     |
| ------ | ------ | -------------- | --------------------------------------------- |
| ✔️     | GET    | `/`            | Lista compras e exibe visão geral da carteira |
| ✔️     | GET    | `/compras/new` | Formulário de nova compra                     |
| ✔️     | POST   | `/compras/new` | Registra nova compra                          |

### 4.2 Endpoints Planejados (API REST)

| Status  | Método | Rota            | Descrição                      |
| ------- | ------ | --------------- | ------------------------------ |
| ⬜      | GET    | `/api/compras`  | Lista compras em formato JSON  |
| ⬜      | POST   | `/api/compras`  | Registro de compras via API    |
| ⬜      | GET    | `/api/carteira` | Dados consolidados da carteira |

Legenda: ✔️ Concluído — ⬜ Pendente

---

## 5. Roadmap Técnico

| Item | Descrição                                | Status |
| ---- | ---------------------------------------- | ------ |
| 1    | Estrutura inicial do projeto Flask       | ✔️     |
| 2    | Integração com API PTAX do BCB           | ✔️     |
| 3    | Registro de compras USD                  | ✔️     |
| 4    | Cálculo de custo médio                   | ✔️     |
| 5    | Templates base com Bootstrap / style     | ✔️     |
| 6    | Implementação da API REST                | ⬜      |
| 7    | Autenticação JWT                         | ⬜      |
| 8    | Dockerfile e docker-compose              | ⬜      |
| 9    | Testes automatizados (PyTest)            | ⬜      |
| 10   | Deploy Linux (Nginx + Gunicorn)          | ⬜      |

---

## 6. Fases do Desenvolvimento

| Fase | Objetivo                                  | Status |
| ---- | ----------------------------------------- | ------ |
| 1    | Planejamento e levantamento de requisitos | ✔️     |
| 2    | Setup do ambiente e virtualenv            | ✔️     |
| 3    | Implementação dos modelos ORM             | ✔️     |
| 4    | Integração com PTAX (BCB)                 | ✔️     |
| 5    | Endpoints e templates                     | ✔️     |
| 6    | Processamento e cálculos financeiros      | ✔️     |
| 7    | Validações de dados e UX                  | ⬜      |
| 8    | Testes unitários e logs                   | ⬜      |

---

## 7. Configuração do Ambiente Virtual

Criação do ambiente virtual:

```bash
python3 -m venv venv
```

Ativação:
**Linux/macOS:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

---

## 8. Dependências e Bibliotecas

Instale todas as dependências:

```bash
pip install -r requirements.txt
```

### Bibliotecas Principais

* Flask — Framework Web
* Flask SQLAlchemy — ORM
* psycopg2 — Driver PostgreSQL
* python-dotenv — Manipulação de variáveis de ambiente
* requests — Consumo da API PTAX
* pytz — Gestão de datas e timezones

### requirements.txt sugerido

```
Flask
Flask-SQLAlchemy
psycopg2-binary
python-dotenv
requests
pytz
```

---

## 9. Inicialização do Banco de Dados

Criar as tabelas automaticamente:

```python
from app import db
from models import Compra

with app.app_context():
    db.create_all()
```

Ou aplicar migrations:

```bash
flask db upgrade
```

---

## 10. Execução do Sistema

Inicie o sistema via Flask:

```bash
flask run
```

Ou diretamente:

```bash
python app.py
```

Aplicação disponível em:

```
http://127.0.0.1:5000/
```

---

## 11. Próximas Expansões

* Finalização da API REST
* Autenticação com JWT
* Conteinerização com Docker
* Testes unitários e mocks da API PTAX
* Pipeline CI/CD
* Deploy em ambiente Linux (Nginx + Gunicorn)

---
