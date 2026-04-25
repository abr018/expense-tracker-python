# Importamos o Flask (framework web)
from flask import Flask, render_template, request, redirect

# Importamos funções que já criaste no projeto
from services.expense_tracker import (
    carregar_transacoes,   # lê do JSON
    adicionar_transacao,   # adiciona nova transação
    guardar_transacoes     # guarda no JSON
)

# Criamos a aplicação Flask
app = Flask(__name__)


# ==========================================
# 🏠 ROTA PRINCIPAL (HOME)
# ==========================================
@app.route("/")
def index():
    # Carrega todas as transações do ficheiro
    transactions = carregar_transacoes()

    # Envia os dados para o HTML (index.html)
    return render_template("index.html", transactions=transactions)


# ==========================================
# ➕ ADICIONAR NOVA TRANSAÇÃO
# ==========================================
@app.route("/add", methods=["GET", "POST"])
def add():

    # Se o utilizador clicar em "Guardar" (POST)
    if request.method == "POST":

        # Criamos um dicionário com os dados do formulário
        nova = {
            "type": request.form["type"],
            "amount": float(request.form["amount"]),  # converter para número
            "category": request.form["category"],
            "date": request.form["date"],
            "description": request.form["description"]
        }

        # Carregamos as transações atuais
        transactions = carregar_transacoes()

        # Adicionamos a nova
        adicionar_transacao(transactions, nova)

        # Redirecionamos para a página principal
        return redirect("/")

    # Se for GET → mostrar o formulário
    return render_template("add.html")


# ==========================================
# 🗑 APAGAR TRANSAÇÃO
# ==========================================
@app.route("/delete/<int:index>")
def delete(index):

    # Carrega as transações
    transactions = carregar_transacoes()

    # Verifica se o índice existe
    if 0 <= index < len(transactions):

        # Remove a transação da lista
        transactions.pop(index)

        # Guarda novamente no JSON
        guardar_transacoes(transactions)

    # Volta para a página principal
    return redirect("/")


# ==========================================
# ✏️ EDITAR TRANSAÇÃO
# ==========================================
@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):

    # Carrega as transações
    transactions = carregar_transacoes()

    # Segurança: se índice inválido → volta para home
    if index < 0 or index >= len(transactions):
        return redirect("/")

    # Se o utilizador clicou em "Guardar"
    if request.method == "POST":

        # Atualizamos os dados da transação
        transactions[index]["type"] = request.form["type"]
        transactions[index]["amount"] = float(request.form["amount"])
        transactions[index]["category"] = request.form["category"]
        transactions[index]["date"] = request.form["date"]
        transactions[index]["description"] = request.form["description"]

        # Guardamos no ficheiro JSON
        guardar_transacoes(transactions)

        # Voltamos para a página principal
        return redirect("/")

    # Se for GET → mostrar formulário preenchido
    return render_template("edit.html", t=transactions[index])


# ==========================================
# 🚀 INICIAR SERVIDOR
# ==========================================
if __name__ == "__main__":
    # debug=True permite atualizar automaticamente ao guardar código
    app.run(debug=True)