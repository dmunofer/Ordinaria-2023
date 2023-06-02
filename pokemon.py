import threading
from multiprocessing import Pool
import time

class Pokemon:
    def __init__(self, name):
        self.name = name
        self.attacks = []
        self.opponent = None

    def add_attack(self, attack):
        self.attacks.append(attack)

    def set_opponent(self, opponent):
        self.opponent = opponent

    def perform_attack(self, attack):
        print(f"{self.name} realiza {attack} en {self.opponent.name}")
        time.sleep(1)

def pokemon_thread(pokemon):
    while True:
        if pokemon.opponent:
            if pokemon.attacks:
                attack = pokemon.attacks.pop(0)
                pokemon.perform_attack(attack)
            else:
                print(f"{pokemon.name} no tiene ataques disponibles.")
        time.sleep(1)

def battle_simulation():
    # Crear los Pokémon
    pikachu = Pokemon("Pikachu")
    charizard = Pokemon("Charizard")

    # Configurar los ataques de los Pokémon
    pikachu.add_attack("Impactrueno")
    charizard.add_attack("Lanzallamas")

    # Establecer los oponentes de los Pokémon
    pikachu.set_opponent(charizard)
    charizard.set_opponent(pikachu)

    # Crear el pool de procesos para los hilos
    pool = Pool(processes=2)

    # Ejecutar los hilos de los Pokémon en el pool
    pool.apply_async(pokemon_thread, args=(pikachu,))
    pool.apply_async(pokemon_thread, args=(charizard,))

    # Cerrar el pool y esperar a que todos los hilos terminen
    pool.close()
    pool.join()
