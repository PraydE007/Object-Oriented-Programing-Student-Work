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
        self.__name = name
        self.__health = health
        self.__max_health = health
        self.__hand_gun = hand_gun
        self.__accuracy = accuracy
        self.__defense = defense
        self.__inventory = ['2x Green Herb', '1x Grenade', '1x Box of 9mm Rounds']

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or not isinstance(value, str):
            print("Ім'я не може бути порожнім або не рядком.")
        else:
            self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if not isinstance(value, (int, float)):
            print("Здоров'я має бути числом.")
            return
        if value < 0:
            self.__health = 0
        elif value > self.__max_health:
            print("Здоров'я не може перевищувати максимальне. Встановлено максимум.")
            self.__health = self.__max_health
        else:
            self.__health = value

    @property
    def defense(self):
        return self.__defense

    @defense.setter
    def defense(self, value):
        if value < 0:
            print("Захист не може бути від’ємним.")
        else:
            self.__defense = value

    @property
    def accuracy(self):
        return self.__accuracy

    @accuracy.setter
    def accuracy(self, value):
        if not (0 <= value <= 1):
            print("Точність повинна бути між 0 і 1.")
        else:
            self.__accuracy = value

    @property
    def hand_gun(self):
        return self.__hand_gun

    @hand_gun.setter
    def hand_gun(self, gun):
        if gun is not None and not isinstance(gun, Handgun):
            print("В руках може бути лише Handgun або нічого.")
        else:
            self.__hand_gun = gun

    @property
    def max_health(self):
        return self.__max_health

    @property
    def is_alive(self):
        return self.__health > 0

    @property
    def health_percentage(self):
        return round((self.__health / self.__max_health) * 100, 1)

    def __calculate_damage(self, base_damage, target_defense):
        """Приватний метод для розрахунку шкоди з урахуванням захисту."""
        return max(0, base_damage - target_defense)

    def attack(self, target):
        print(f"-- {self.__name} стріляє в {target.name}")
        if self.__hand_gun and self.__hand_gun.do_shot(self.__inventory):
            if random.random() <= self.__accuracy:
                damage = self.__calculate_damage(self.__hand_gun.damage, target.defense)
                target.health -= damage
                print(f"-- {self.__name} влучає в ціль ({damage} шкоди)")
            else:
                print(f"-- {self.__name} промахується")
        else:
            print(f"-- {self.__name} не має набоїв!")

    def get_stats(self):
        weapon_info = f"{self.__hand_gun.name} ({self.__hand_gun.damage} шкоди)" if self.__hand_gun else "нічого"
        return (
            f"=== {self.__name} ===\n"
            f"HP: {self.__health}/{self.__max_health} ({self.health_percentage}%)\n"
            f"В руках: {weapon_info}\n"
            f"Захист: {self.__defense}\n"
            f"Точність: {self.__accuracy}"
        )

class Enemy:
    def __init__(self, name: str, health: int, attack_power: int, defense: int):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.defense = defense

    def attack(self, target):
        damage = max(0, self.attack_power - target.defense)
        target.health -= damage
        print(f"-- {self.name} кусає {target.name} ({damage} шкоди)")

    def is_alive(self):
        return self.health > 0

    def get_stats(self):
        return f"=== {self.name} ===\nHP: {self.health}/{self.max_health}\nАтака: {self.attack_power}\nЗахист: {self.defense}"

def game():
    player = Hero('Leon S. Kennedy', 50, Handgun('Pistol', 20, 'Box of 9mm Rounds'), 0.5, 2)
    zombie = Enemy('Zombie', 40, 9, 0)

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

if __name__ == "__main__":
    game()
