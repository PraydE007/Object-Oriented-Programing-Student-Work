class Hero:
    def __init__(self, name, attack_power, defense):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.attack_power = attack_power
        self.defense = defense

    def attack(self):
        return self.attack_power

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        actual_damage = max(damage - self.defense, 0)
        self.health -= actual_damage
        if self.health < 0:
            self.health = 0
        return actual_damage

    def __str__(self):
        return (f"Герой: {self.name}, Здоров'я: {self.health}/{self.max_health}, "
                f"Атака: {self.attack_power}, Захист: {self.defense}")

class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name, attack_power=15, defense=10)
        self.rage = 0

    def attack(self):
        self.rage += 5
        return self.attack_power

    def rage_attack(self):
        if self.rage >= 20:
            damage = self.attack_power * 2
            self.rage = 0
            return damage
        else:
            print("Не достатньо люті!")
            return self.attack()

    def __str__(self):
        return super().__str__() + f", Лють: {self.rage}"


class Mage(Hero):
    def __init__(self, name):
        super().__init__(name, attack_power=10, defense=5)
        self.mana = 50

    def attack(self):
        if self.mana >= 5:
            self.mana -= 5
            return self.attack_power + 5
        else:
            print("Не достатньо мани!")
            return self.attack_power

    def cast_spell(self, spell_cost):
        if self.mana >= spell_cost:
            self.mana -= spell_cost
            return self.attack_power + spell_cost * 2
        else:
            print("Не достатньо мани!")
            return 0

    def __str__(self):
        return super().__str__() + f", Мана: {self.mana}"


class Archer(Hero):
    def __init__(self, name):
        super().__init__(name, attack_power=12, defense=7)
        self.arrows = 10

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            return self.attack_power
        else:
            print("Стріли скінчилися!")
            return 0

    def precise_shot(self):
        if self.arrows > 0:
            self.arrows -= 1
            return self.attack_power * 2
        else:
            print("Стріли скінчилися!")
            return 0

    def __str__(self):
        return super().__str__() + f", Стріли: {self.arrows}"

class Paladin(Warrior):
    def __init__(self, name):
        super().__init__(name)
        self.holy_power = 30

        self.health = 120
        self.max_health = 120
        self.attack_power = 18
        self.defense = 12

    def heal(self):
        if self.holy_power >= 10:
            heal_amount = 20
            self.health += heal_amount
            if self.health > self.max_health:
                self.health = self.max_health
            self.holy_power -= 10
            return heal_amount
        else:
            print("Не достатньо святої сили!")
            return 0

    def attack(self):
        damage = super().attack()
        if self.holy_power >= 5:
            damage += 2
            self.holy_power -= 5
        return damage

    def __str__(self):
        return super().__str__() + f", Свята сила: {self.holy_power}"

if __name__ == "__main__":
    warrior = Warrior("Тор")
    archer = Archer("Робін")
    mage = Mage("Дамблдор")
    paladin = Paladin("Таріель")

    print("Герої:")
    print(warrior)
    print(mage)
    print(archer)
    print(paladin)

    print("\nАтаки:")
    print(f"{warrior.name} атакує {warrior.attack()}")
    print(f"{mage.name} атакує {mage.attack()}")
    print(f"{archer.name} атакує {archer.attack()}")
    print(f"{paladin.name} атакує {paladin.attack()}")

    print("\nЗдібності:")
    print(f"{warrior.name} атака люті {warrior.rage_attack()}")
    print(f"{mage.name} заклинає {mage.cast_spell(20)}")
    print(f"{archer.name} точний постріл {archer.precise_shot()}")
    print(f"{paladin.name} лікується {paladin.heal()}")

    # 4. Демонстрація отримання пошкоджень
    print("\nБій:")
    damage = 25
    print(f"{warrior.name} отримує {damage} пошкодження: {warrior.take_damage(damage)}")
    print(f"{mage.name} отримує {damage} пошкодження: {mage.take_damage(damage)}")
    print(f"{archer.name} отримує {damage} пошкодження: {archer.take_damage(damage)}")
    print(f"{paladin.name} отримує {damage} пошкодження: {paladin.take_damage(damage)}")

    print("Герої:")
    print(warrior)
    print(mage)
    print(archer)
    print(paladin)
