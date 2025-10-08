import random

class Handgun:
    def __init__(self, name: str, damage: int, rounds: str):
        self.name = name
        self.damage = damage
        self.rounds = rounds

    def do_shot(self, inventory: list) -> bool:
        for item in inventory:
            if self.rounds in item:
                inventory.remove(item)
                return True
        return False

class Hero:
    def __init__(self, name: str, health: int, hand_gun: Handgun, accuracy: float, defense: int):
        self.name = name
        self.health = health
        self.max_health = health
        self.hand_gun = hand_gun
        self.accuracy = accuracy
        self.defense = defense
        self.inventory = ['2x Green Herb', '1x Grenade', '1x Box of 9mm Rounds'] # on spawn inventory

    def attack(self, target):
        print(f"-- {self.name} стріляє в {target.name}")
        if self.hand_gun != None and self.hand_gun.do_shot(self.inventory):
            if random.random() <= self.accuracy:
                damage = max(0, self.hand_gun.damage - target.defense) 
                target.health = max(0, target.health - damage)
                print(f"-- {self.name} влучає в ціль")
            else:
                print(f"-- {self.name} промахується")

    def is_alive(self) -> bool:
        return self.health > 0

    def get_stats(self):
        return f"=== {self.name} ===\nHP: {self.health}/{self.max_health}\nВ руках: " + (f"{self.hand_gun.name} ({self.hand_gun.damage} шкоди)" if self.hand_gun != None else "нічого") + f"\nЗахист: {self.defense}"

class Enemy:
    def __init__(self, name: str, health: int, attack_power: int, defense: int):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.defense = defense

    def attack(self, target):
        damage = max(0, self.attack_power - target.defense)
        target.health = max(0, target.health - damage)
        print(f"-- {self.name} кусає {target.name}")

    def is_alive(self) -> bool:
        return self.health > 0

    def get_stats(self):
        return f"=== {self.name} ===\nHP: {self.health}/{self.max_health}\nАтака: 20\nЗахист: {self.defense}"

def game():
    player = Hero('Leon S. Kennedy', 5, Handgun('Pistol', 20, 'Box of 9mm Rounds'), 0.5, 2)
    zombie = Enemy('Zombie', 20, 9, 0)

    print(player.get_stats())
    print(zombie.get_stats())

    player.attack(zombie)

    print(zombie.get_stats())
    if zombie.is_alive():
        print('-- Zombie не помер!')
        zombie.attack(player)

    print(player.get_stats())
    if not player.is_alive():
        print('=== Ви програли! ===')
        return
    print('=== Ви виграли! ===')

game()