class Blockchain:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, sender, message):
        self.transactions.append((sender, message))
