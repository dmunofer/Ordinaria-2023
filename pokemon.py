import time
import queue
import threading
from multiprocessing import Pool
from blaze import Blockchain

class Pokemon:
    def __init__(self, name, opponent, blockchain):
        self.name = name
        self.opponent = opponent
        self.attack_queue = queue.Queue()
        self.blockchain = blockchain

    def generate_attack(self):
        while True:
            attack = f"Attack from {self.name} - {time.strftime('%H:%M:%S')}"
            self.attack_queue.put(attack)
            self.blockchain.add_transaction(self.name, attack)
            time.sleep(1)

    def consume_attack(self):
        while True:
            if not self.attack_queue.empty():
                attack = self.attack_queue.get()
                print(f"{self.name} received attack: {attack}")
                time.sleep(1)

    def start_battle(self):
        pool = Pool(processes=2)
        pool.apply_async(self.generate_attack)
        pool.apply_async(self.consume_attack)
        pool.close()
        pool.join()

class PokemonBattleSimulator:
    def __init__(self):
        self.blockchain = Blockchain()
        self.pokemon1 = Pokemon("Charizard", "Blastoise", self.blockchain)
        self.pokemon2 = Pokemon("Blastoise", "Charizard", self.blockchain)

    def start_simulation(self):
        thread1 = threading.Thread(target=self.pokemon1.start_battle)
        thread2 = threading.Thread(target=self.pokemon2.start_battle)

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

