from Ordinaria2023.gui import run_gui
from flask import Flask, jsonify
from Ordinaria2023.pokemon import PokemonBattleSimulator

app = Flask(__name__)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    # Implementar la lógica para agregar una transacción a la blockchain
    # Puedes acceder a los objetos simulator y blockchain aquí

    return jsonify({"message": "Transaction added successfully"})

def run_simulation():
    simulator = PokemonBattleSimulator()
    simulator.start_simulation()

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
    run_simulation()
