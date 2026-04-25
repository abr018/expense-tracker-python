# Classe que representa uma transação (receita ou despesa)
class Transaction:

    # Construtor da classe (quando criamos um objeto)
    def __init__(self, type, amount, category, date, description):
        # Tipo da transação: "receita" ou "despesa"
        self.type = type

        # Valor da transação
        self.amount = amount

        # Categoria (ex: comida, salário, lazer...)
        self.category = category

        # Data no formato AAAA-MM-DD
        self.date = date

        # Descrição da transação
        self.description = description

    # Converter objeto para dicionário (para guardar em JSON)
    def to_dict(self):
        return {
            "type": self.type,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description
        }