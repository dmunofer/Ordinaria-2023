import tkinter as tk
from flask import Flask, jsonify
from Ordinaria2023.pokemon import PokemonBattleSimulator

class GUI:
    def __init__(self):
        self.simulator = PokemonBattleSimulator()

    def start_simulation(self):
        self.simulator.start_simulation()

    def show_gui(self):
        window = tk.Tk()
        window.title("Pokemon Battle Simulator")
        window.geometry("400x200")

        start_button = tk.Button(window, text="Start Simulation", command=self.start_simulation)
        start_button.pack(pady=50)

        window.mainloop()

app = Flask(__name__)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    # Implementar la lógica para agregar una transacción a la blockchain
    # Puedes acceder a los objetos simulator y blockchain aquí

    return jsonify({"message": "Transaction added successfully"})

def run_gui():
    gui = GUI()
    gui.show_gui()
