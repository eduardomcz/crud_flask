FROM python:3.9

# Definir o diretório de trabalho como a raiz do contêiner
WORKDIR /

# Copiar os arquivos de requisitos e instalar as dependências
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt && pip check

# Copiar o restante do código do aplicativo
COPY . .

# Definir a variável de ambiente para o Flask
ENV FLASK_APP=index.py

# Expor a porta que o Flask usará
EXPOSE 5000

# Comando para rodar o aplicativo
CMD ["flask", "run", "--host=0.0.0.0"]
