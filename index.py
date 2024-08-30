from flask import Flask, render_template, request, make_response, redirect
import pymysql
import logging
import re
<<<<<<< HEAD
import os

from dotenv import load_dotenv

load_dotenv()

=======
>>>>>>> 6d9d48f972b487cc46f3c4366fc9cae85605fda6

# Configuração do logger para registrar mensagens de erro e informações
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.secret_key = "hkjh4k2j34jgj234lgbvjkjg243"


# Função para obter uma conexão com o banco de dados
def get_db_connection():
<<<<<<< HEAD
    # try catch da conexão
    try:
        # Conecta-se ao banco de dados
        return pymysql.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DB"),
        )
        logging.info("Conexão com o banco de dados estabelecida com sucesso.")
    except pymysql.MySQLError as err:
        logging.error(f"Erro ao conectar ao banco de dados: {err}")
        return None


# Exemplo de rota para testar a conexão com o banco de dados
@app.route("/test_db")
def test_db():
    connection = get_db_connection()
    if connection:
        return "Conexão com o banco de dados bem-sucedida!"
    else:
        return "Falha na conexão com o banco de dados."
=======
    return pymysql.connect(
        host="localhost", user="root", 
        password="429028My", database="exemplo_db"
    )
>>>>>>> 6d9d48f972b487cc46f3c4366fc9cae85605fda6


# Função para executar consultas que retornam resultados (SELECT)
def execute_query(query, params=None):
    try:
        with get_db_connection() as db:
            with db.cursor() as cursor:
                cursor.execute(query, params)
                # Obtém todos os resultados da consulta
                results = cursor.fetchall()
                db.commit()  # Confirma a transação
                return results
    except pymysql.MySQLError as err:
        logging.error(f"Erro ao executar consulta: {err}")
        return None


# Função para executar comandos que não
# retornam resultados (INSERT, UPDATE, DELETE)
def execute_non_query(query, params=None):
    try:
        with get_db_connection() as db:
            with db.cursor() as cursor:
                cursor.execute(query, params)
                db.commit()  # Confirma a transação
    except pymysql.MySQLError as err:
        logging.error(f"Erro ao executar comando: {err}")


# Rota para deletar um cliente do banco de dados
@app.route("/deletar", methods=["GET", "POST"])
def deletar():
    sql = "DELETE FROM clientes WHERE id = %s"
    execute_non_query(sql, (request.args.get("id"),))
    return redirect("/")


@app.route("/atualizar", methods=["GET"])
def atualizar_form():
    cliente_id = request.args.get("id")
    print(cliente_id)
    sql = "SELECT * FROM clientes WHERE id = %s"
    cliente = execute_query(sql, (cliente_id,))
    if cliente:
        cliente = cliente[0]
        cliente_dict = {
            "id": cliente[0],
            "nome": cliente[1],
            "email": cliente[2],
            "cpf": cliente[3],
        }
        print(cliente_dict)  # Adicione esta linha para verificar os dados
        return render_template("atualizar.html", cliente=cliente_dict)
    return "Cliente não encontrado"


@app.route("/atualizar", methods=["POST"])
def atualizar():
    print(request.form)
    cliente_id = request.form["id"]
    nome = request.form["nome"]
    email = request.form["email"]
    cpf = request.form["cpf"]
    # Remover a máscara do CPF
    cpf = re.sub(r"\D", "", cpf)
<<<<<<< HEAD

=======
    
>>>>>>> 6d9d48f972b487cc46f3c4366fc9cae85605fda6
    # Validação do CPF
    if len(cpf) != 11:
        return "CPF deve ter 11 dígitos", 400

    # Verifique se os valores estão sendo capturados corretamente
    print(f"Nome: {nome}, Email: {email}, CPF: {cpf}")
<<<<<<< HEAD

=======
    
>>>>>>> 6d9d48f972b487cc46f3c4366fc9cae85605fda6
    sql = "UPDATE clientes SET nome = %s, email = %s, cpf = %s WHERE id = %s"
    execute_non_query(sql, (nome, email, cpf, cliente_id))
    return redirect("/")


<<<<<<< HEAD
"""
Esta função lida com a requisição GET para a rota '/atualizar'.
Ela recupera o ID do cliente dos argumentos da requisição, executa uma
consulta SQL para buscar os dados do cliente,
e retorna uma template renderizada com os dados do cliente se encontrado,
ou uma mensagem 'Cliente não encontrado' caso contrário.
"""


=======
>>>>>>> 6d9d48f972b487cc46f3c4366fc9cae85605fda6
@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form["nome"]
    email = request.form["email"]
    cpf = request.form["cpf"]
    # Remover a máscara do CPF
    cpf = re.sub(r"\D", "", cpf)
<<<<<<< HEAD

=======
    
>>>>>>> 6d9d48f972b487cc46f3c4366fc9cae85605fda6
    # Validação do CPF
    if len(cpf) != 11:
        return "CPF deve ter 11 dígitos", 400

    # Verifique se os valores estão sendo capturados corretamente
    print(f"Nome: {nome}, Email: {email}, CPF: {cpf}")

    sql = "INSERT INTO clientes (nome, email, cpf) VALUES (%s, %s, %s)"
    print(sql, (nome, email, cpf))
    execute_non_query(sql, (nome, email, cpf))
    return redirect("/")


<<<<<<< HEAD
"""
Esta função lida com requisições GET e POST para a rota '/'.
Ela verifica se o usuário tem um cookie 'usuario' e, se não tiver, cria um.
Em seguida, executa uma consulta SQL para buscar todos os clientes e retorna
uma template renderizada com os dados dos clientes.
Caso a requisição seja POST, ela retorna o nome do usuário do formulário.
"""


=======
>>>>>>> 6d9d48f972b487cc46f3c4366fc9cae85605fda6
# Rota principal que exibe a lista de clientes
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        if request.cookies.get("usuario"):
            resp = make_response("Meu website com cookie setado.")
        else:
            resp = make_response("Meu website sem cookie!")
            resp.set_cookie("usuario", "Eduardo")

        sql = "SELECT * FROM clientes"
        tb_clientes = execute_query(sql)
        if tb_clientes is None:
            return "Erro ao buscar clientes."

        # Converte o resultado da consulta em um dicionário
        tb_clientes = [
            {"id": x[0], "nome": x[1], "email": x[2], "cpf": x[3]} for x in tb_clientes
        ]

<<<<<<< HEAD
        try:
            logging.info("Rota principal acessada.")
            return render_template("index.html", content=tb_clientes)
        except Exception as e:
            logging.error(f"Erro na rota principal: {e}")
            return "Erro ao carregar a página principal", 500
=======
        return render_template("index.html", content=tb_clientes)
>>>>>>> 6d9d48f972b487cc46f3c4366fc9cae85605fda6
    else:
        return "O que veio do meu form: " + request.form["nome"]


# Rota para a página "Sobre"
@app.route("/sobre")
def sobre():
    return "<h2>Sobre</h2>"


# Rota para exibir notícias com base no slug
@app.route("/noticia/<slug>")
def noticia(slug):
    return f"<h2>Noticia: {slug}</h2>"


if __name__ == "__main__":
    app.run(debug=True)
