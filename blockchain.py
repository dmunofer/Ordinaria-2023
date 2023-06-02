import hashlib
from datetime import datetime
from flask import Flask, jsonify, request
from blaze import Data
from multiprocessing import Pool

class Transaction:
    def __init__(self, sender, receiver, attack):
        self.sender = sender
        self.receiver = receiver
        self.attack = attack
        self.timestamp = datetime.now()

    def calculate_hash(self):
        transaction_string = f"{self.sender}{self.receiver}{self.attack}{self.timestamp}"
        return hashlib.sha256(transaction_string.encode()).hexdigest()

app = Flask(__name__)

transactions = Data([])

@app.route('/transaction', methods=['POST'])
def add_transaction():
    # Obtener los datos de la transacción desde la solicitud
    data = request.get_json()
    sender = data['sender']
    receiver = data['receiver']
    attack = data['attack']

    # Crear un objeto Transaction y añadirlo a la blockchain
    transaction = Transaction(sender, receiver, attack)
    transactions.extend([transaction.__dict__])

    return jsonify({"message": "Transaction added successfully"})

@app.route('/blockchain', methods=['GET'])
def get_blockchain():
    # Devolver la blockchain como respuesta
    return jsonify(transactions)

if __name__ == '__main__':
    # Crear el pool de procesos para la aplicación Flask
    pool = Pool(processes=1)

    # Ejecutar la aplicación Flask en un proceso del pool
    pool.apply_async(app.run)

    # Cerrar el pool y esperar a que la aplicación termine
    pool.close()
    pool.join()
