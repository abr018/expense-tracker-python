# Importamos a classe Transaction
from models.transaction import Transaction

# Importamos as funções do serviço
from services.expense_tracker import (
    carregar_transacoes,
    adicionar_transacao,
    listar_transacoes,
    calcular_saldo,
    filtrar_por_mes,
    resumo_por_categoria,
    editar_transacao,
    apagar_transacao
)
# 👉 Carregar dados do ficheiro
transactions = carregar_transacoes()

# 👉 Loop infinito (menu contínuo)
while True:

    # Mostrar menu
    print("\n=== Menu Expense Tracker ===")
    print("1- Adicionar transação")
    print("2- Listar transações")
    print("3- Ver saldo")
    print("4- Filtrar por mês")
    print("5- Resumo por categoria")
    print("6- Apagar transação")
    print("7- Editar transação")
    print("0- Sair")

    # Ler opção do utilizador
    opcao = input("Escolhe uma opção: ")

    # =========================
    # 👉 OPÇÃO 1 - Adicionar
    # =========================
    if opcao == "1":

        print("\n=== Adicionar Transação ===")

        # Tipo
        tipo = input("Tipo (receita/despesa): ").strip().lower()

        # Validação
        if tipo != "receita" and tipo != "despesa":
            print("Tipo inválido.")
            continue

        # Restantes dados
        valor = float(input("Valor: "))
        categoria = input("Categoria: ")
        data = input("Data (AAAA-MM-DD): ")
        descricao = input("Descrição: ")

        # Criar objeto
        nova = Transaction(tipo, valor, categoria, data, descricao)

        # Guardar
        adicionar_transacao(transactions, nova.to_dict())

        print("Transação adicionada com sucesso!")

  
    elif opcao == "2":
        listar_transacoes(transactions)

    
    elif opcao == "3":
        calcular_saldo(transactions)

   
    elif opcao == "4":
        mes = input("Escreve o mês (MM): ")
        filtrar_por_mes(transactions, mes)

    elif opcao == "5":
        resumo_por_categoria(transactions)

    elif opcao == "6":
        apagar_transacao(transactions)

    elif opcao == "7":
        editar_transacao(transactions)

   
    elif opcao == "0":
        print("A sair da aplicação...")
        break

    
    else:
        print("Opção inválida.")