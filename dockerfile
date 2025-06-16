# Dockerfile

# 1. Usar uma imagem base oficial do Python
FROM python:3.11-slim

# 2. Definir variáveis de ambiente para o Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Definir o diretório de trabalho dentro do contêiner
WORKDIR /financeiro

# 4. Copiar o arquivo de dependências
COPY requirements.txt /financeiro/

# 5. Instalar as dependências
RUN pip install -r requirements.txt

# 6. Copiar todo o código do projeto para o diretório de trabalho
COPY . /financeiro/