# Importamos json para ler e escrever ficheiros JSON
import json

# Caminho do ficheiro onde guardamos as transações
FILE_PATH = "data/transactions.json"


# 👉 Função para carregar (ler) transações do ficheiro
def carregar_transacoes():
    # Abrimos o ficheiro em modo leitura
    with open(FILE_PATH, "r") as file:
        # Convertendo JSON → lista Python
        return json.load(file)


# 👉 Função para guardar transações no ficheiro
def guardar_transacoes(transactions):
    # Abrimos o ficheiro em modo escrita
    with open(FILE_PATH, "w") as file:
        # Guardamos a lista no ficheiro com formatação bonita
        json.dump(transactions, file, indent=4)


# 👉 Função para adicionar nova transação
def adicionar_transacao(transactions, nova_transacao):
    # Adicionamos à lista
    transactions.append(nova_transacao)

    # Guardamos no ficheiro
    guardar_transacoes(transactions)


# 👉 Função para listar todas as transações
def listar_transacoes(transactions):
    print("\n=== Lista de Transações ===")

    # Verifica se está vazio
    if len(transactions) == 0:
        print("Ainda não existem transações.")
        return

    # Percorrer todas as transações
    for t in transactions:
        print("----------------------------")
        print("Tipo:", t["type"])
        print("Valor:", t["amount"])
        print("Categoria:", t["category"])
        print("Data:", t["date"])
        print("Descrição:", t["description"])


# 👉 Função para calcular saldo
def calcular_saldo(transactions):

    # Variáveis para acumular valores
    total_receita = 0
    total_despesa = 0

    # Percorrer transações
    for t in transactions:

        # Se for receita soma nas receitas
        if t["type"] == "receita":
            total_receita += t["amount"]

        # Se for despesa soma nas despesas
        elif t["type"] == "despesa":
            total_despesa += t["amount"]

    # Calcular saldo final
    saldo = total_receita - total_despesa

    # Mostrar resultado
    print("\n=== Resumo ===")
    print("Total Receitas:", total_receita)
    print("Total Despesas:", total_despesa)
    print("Saldo Final:", saldo)


# 👉 Função para filtrar por mês
def filtrar_por_mes(transactions, mes_procurado):

    print(f"\n=== Transações do mês {mes_procurado} ===")

    # Variável para saber se encontrou resultados
    encontrou = False

    # Percorrer transações
    for t in transactions:

        # Extrair mês da data (AAAA-MM-DD → MM)
        mes = t["date"].split("-")[1]

        # Comparar com o mês procurado
        if mes == mes_procurado:
            encontrou = True

            print("----------------------------")
            print("Tipo:", t["type"])
            print("Valor:", t["amount"])
            print("Categoria:", t["category"])
            print("Data:", t["date"])
            print("Descrição:", t["description"])

    # Se não encontrou nada
    if not encontrou:
        print("Nenhuma transação encontrada nesse mês.")

# 👉 Função para mostrar resumo por categoria
def resumo_por_categoria(transactions):

    print("\n=== Resumo por Categoria ===")

    categorias = {}

    for t in transactions:
        categoria = t["category"]
        valor = t["amount"]

        if categoria not in categorias:
            categorias[categoria] = 0

        if t["type"] == "receita":
            categorias[categoria] += valor
        elif t["type"] == "despesa":
            categorias[categoria] -= valor

    if len(categorias) == 0:
        print("Ainda não existem transações.")
        return

    for categoria, total in categorias.items():
        print("----------------------------")
        print("Categoria:", categoria)
        print("Total:", total)        
# 👉 Apagar transação
def apagar_transacao(transactions):

    print("\n=== Apagar Transação ===")

    # Verificar se há transações
    if len(transactions) == 0:
        print("Não existem transações para apagar.")
        return

    # Mostrar lista numerada
    for i, t in enumerate(transactions):
        print(f"\n[{i}]")
        print("Tipo:", t["type"])
        print("Valor:", t["amount"])
        print("Categoria:", t["category"])
        print("Data:", t["date"])
        print("Descrição:", t["description"])

    # Escolher índice
    try:
        indice = int(input("\nEscolhe o número da transação a apagar: "))

        if indice < 0 or indice >= len(transactions):
            print("Índice inválido.")
            return

        # Remover
        removida = transactions.pop(indice)

        # Guardar no ficheiro
        guardar_transacoes(transactions)

        print("Transação removida com sucesso!")

    except ValueError:
        print("Tens de inserir um número.")        
# 👉 Editar transação
def editar_transacao(transactions):

    print("\n=== Editar Transação ===")

    # Verificar se existem transações
    if len(transactions) == 0:
        print("Não existem transações.")
        return

    # Mostrar lista numerada
    for i, t in enumerate(transactions):
        print(f"\n[{i}]")
        print("Tipo:", t["type"])
        print("Valor:", t["amount"])
        print("Categoria:", t["category"])
        print("Data:", t["date"])
        print("Descrição:", t["description"])

    try:
        indice = int(input("\nEscolhe o número da transação a editar: "))

        if indice < 0 or indice >= len(transactions):
            print("Índice inválido.")
            return

        t = transactions[indice]

        print("\nDeixa vazio para manter o valor atual")

        # Novos dados (ou manter os antigos)
        novo_tipo = input(f"Tipo ({t['type']}): ") or t["type"]
        novo_valor = input(f"Valor ({t['amount']}): ")
        novo_categoria = input(f"Categoria ({t['category']}): ") or t["category"]
        nova_data = input(f"Data ({t['date']}): ") or t["date"]
        nova_descricao = input(f"Descrição ({t['description']}): ") or t["description"]

        # Converter valor se for alterado
        if novo_valor == "":
            novo_valor = t["amount"]
        else:
            novo_valor = float(novo_valor)

        # Atualizar
        t["type"] = novo_tipo
        t["amount"] = novo_valor
        t["category"] = novo_categoria
        t["date"] = nova_data
        t["description"] = nova_descricao

        # Guardar
        guardar_transacoes(transactions)

        print("Transação atualizada com sucesso!")

    except ValueError:
        print("Entrada inválida.")        