from flask import Flask, render_template, request, make_response, redirect
import pymysql
import logging
import re

# Configuração do logger para registrar mensagens de erro e informações
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.secret_key = "hkjh4k2j34jgj234lgbvjkjg243"


# Função para obter uma conexão com o banco de dados
def get_db_connection():
    return pymysql.connect(
        host="localhost", user="root", 
        password="429028My", database="exemplo_db"
    )


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
    
    # Validação do CPF
    if len(cpf) != 11:
        return "CPF deve ter 11 dígitos", 400

    # Verifique se os valores estão sendo capturados corretamente
    print(f"Nome: {nome}, Email: {email}, CPF: {cpf}")
    
    sql = "UPDATE clientes SET nome = %s, email = %s, cpf = %s WHERE id = %s"
    execute_non_query(sql, (nome, email, cpf, cliente_id))
    return redirect("/")


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form["nome"]
    email = request.form["email"]
    cpf = request.form["cpf"]
    # Remover a máscara do CPF
    cpf = re.sub(r"\D", "", cpf)
    
    # Validação do CPF
    if len(cpf) != 11:
        return "CPF deve ter 11 dígitos", 400

    # Verifique se os valores estão sendo capturados corretamente
    print(f"Nome: {nome}, Email: {email}, CPF: {cpf}")

    sql = "INSERT INTO clientes (nome, email, cpf) VALUES (%s, %s, %s)"
    print(sql, (nome, email, cpf))
    execute_non_query(sql, (nome, email, cpf))
    return redirect("/")


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

        return render_template("index.html", content=tb_clientes)
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
