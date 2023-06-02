from gui import run_gui
from flask import Flask, jsonify
from pokemon import PokemonBattleSimulator

app = Flask(__name__)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    # Implement the logic to add a transaction to the blockchain
    # You can access the simulator and the blockchain objects here

    return jsonify({"message": "Transaction added successfully"})

def run_simulation():
    simulator = PokemonBattleSimulator()
    simulator.start_simulation()

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
    run_simulation()
