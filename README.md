# 💰 Projeto Financeiro com Django REST Framework

Este repositório contém o desenvolvimento de uma API financeira utilizando o framework **Django REST Framework (DRF)**. O projeto foi realizado como parte do curso oferecido pela **OxeTech**.

## 🚀 Objetivo

Construir uma API REST robusta e bem estruturada para controle financeiro pessoal ou empresarial, com foco em boas práticas como:

- Separação de responsabilidades (Domain, Repositories, Serializers, Views)
- Validações personalizadas
- Lançamentos com repetição mensal
- Regras de negócio aplicadas em tempo de serialização

## 🧱 Funcionalidades

- Cadastro de **categorias** e **formas de pagamento**
- Registro de **lançamentos** (receitas e despesas)
- Validações:
  - Lançamentos não aceitam valor zero
  - Receitas/Despesas não podem ter valor negativo
  - Lançamentos podem ser parciais ou mensais
- Regras de repetição de lançamentos mensais automáticos

## 🛠 Tecnologias Utilizadas

- **Python 3.12+**
- **Django 5**
- **Django REST Framework**
- **PostgreSQL** (ou SQLite, dependendo da configuração)
- Organização seguindo princípios do **Repository Pattern**

## ⚙️ Instalação

```bash
# Clone o projeto
git clone https://github.com/ZamohtX/OxeTech.git
cd projeto-financeiro

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Rode as migrações
python manage.py migrate

# Inicie o servidor
python manage.py runserver
