import random

class Hero:
    def __init__(self, name, attack_power=0, defense=0, **kwargs):
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
    def __init__(self, name, attack_power=15, defense=10, **kwargs):
        super().__init__(name=name, attack_power=attack_power, defense=defense, **kwargs)
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
    def __init__(self, name, attack_power=10, defense=5, **kwargs):
        super().__init__(name=name, attack_power=attack_power, defense=defense, **kwargs)
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
    def __init__(self, name, attack_power=12, defense=7, **kwargs):
        super().__init__(name=name, attack_power=attack_power, defense=defense, **kwargs)
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
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)
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


class FireMixin:
    def __init__(self, fire_damage=5, **kwargs):
        self.fire_damage = fire_damage
        super().__init__(**kwargs)

    def ignite(self, target):
        burn_turns = 3
        total_damage = 0
        print(f"{self.name} підпалює {target.name}!")
        for turn in range(1, burn_turns + 1):
            print(f"  Хід {turn}: {target.name} отримує {self.fire_damage} вогняного пошкодження")
            target.take_damage(self.fire_damage)
            total_damage += self.fire_damage
        return total_damage

    def flame_burst(self, targets):
        print(f"{self.name} виконує вибух вогню!")
        for t in targets:
            dmg = self.attack() + self.fire_damage
            print(f"  {t.name} отримує {dmg} пошкодження")
            t.take_damage(dmg)

    def attack(self):
        return super().attack() + self.fire_damage


class IceMixin:
    def __init__(self, ice_damage=4, **kwargs):
        self.ice_damage = ice_damage
        self.frozen_turns = 0
        self.ice_shield_value = 0
        super().__init__(**kwargs)

    def freeze(self, target):
        target.frozen_turns = 2
        print(f"{target.name} заморожений на 2 ходи!")
        target.take_damage(self.ice_damage)
        return self.ice_damage

    def ice_shield(self):
        self.ice_shield_value = 15
        print(f"{self.name} отримує крижаний щит, що поглинає {self.ice_shield_value} пошкодження!")

    def take_damage(self, damage):
        if hasattr(self, 'ice_shield_value') and self.ice_shield_value > 0:
            shield_absorb = min(damage, self.ice_shield_value)
            self.ice_shield_value -= shield_absorb
            damage -= shield_absorb
            print(f"{self.name}'s крижаний щит поглинає {shield_absorb} пошкодження")
        return super().take_damage(damage)

    def attack(self):
        return super().attack() + self.ice_damage


class LightningMixin:
    def __init__(self, lightning_damage=6, **kwargs):
        self.lightning_damage = lightning_damage
        self.charge = 0
        super().__init__(**kwargs)

    def chain_lightning(self, targets):
        dmg = self.attack()
        print(f"{self.name} запускає ланцюгову блискавку!")
        for i, t in enumerate(targets):
            reduced_dmg = max(dmg - i*2, 0)
            print(f"  {t.name} отримує {reduced_dmg} пошкодження")
            t.take_damage(reduced_dmg)

    def thunderstrike(self, target):
        dmg = self.attack() + self.lightning_damage * 2
        print(f"{self.name} атакує {target.name} грозовим ударом!")
        if random.random() < 0.3:
            print(f"{target.name} оглушений!")
        target.take_damage(dmg)
        self.charge += 1

    def attack(self):
        return super().attack() + self.lightning_damage


class FireWarrior(FireMixin, Warrior):
    def __init__(self, name):
        super().__init__(name=name, fire_damage=8)

class IceMage(IceMixin, Mage):
    def __init__(self, name):
        super().__init__(name=name, ice_damage=7)

class LightningArcher(LightningMixin, Archer):
    def __init__(self, name):
        super().__init__(name=name, lightning_damage=6)


if __name__ == "__main__":
    fw = FireWarrior("Тор Вогняний")
    im = IceMage("Гаррі Крижаний")
    la = LightningArcher("Робін Блискавка")
    enemies = [Warrior("Скелет1"), Warrior("Скелет2")]

    print(fw)
    print(im)
    print(la)

    print("\nАтаки з міксіном:")
    print(f"{fw.name} атакує {fw.attack()}")
    fw.ignite(enemies[0])
    fw.flame_burst(enemies)

    print(f"{im.name} атакує {im.attack()}")
    im.ice_shield()
    im.freeze(enemies[1])

    print(f"{la.name} атакує {la.attack()}")
    la.chain_lightning(enemies)
    la.thunderstrike(enemies[0])
