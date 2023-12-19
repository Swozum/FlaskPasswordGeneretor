# Use a imagem base do Python mais leve (Alpine)
FROM python:3.10-alpine

# Instalar o virtualenv
RUN pip install --no-cache-dir virtualenv

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Cria e ativa um ambiente virtual
RUN python -m venv venv
ENV PATH="/app/venv/bin:$PATH"

# Copia o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências no ambiente virtual
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos para o contêiner
COPY . .

RUN chmod -R +r .

# Define a porta em que o Flask irá escutar
EXPOSE 5000

# Define variáveis de ambiente para o Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Comando para iniciar o aplicativo Flask
CMD ["flask", "run"]
