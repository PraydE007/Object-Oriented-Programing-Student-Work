# ============================================
# РАСИ - дають расові характеристики
# ============================================

class Human:
    """Людина - збалансовані характеристики"""
    race_name = "Людина"
    
    def __init__(self, **kwargs):
        # Расові бонуси
        self.strength_bonus = 0
        self.agility_bonus = 0
        self.intelligence_bonus = 0
        self.max_health_bonus = 10
        
        # Расова здібність
        self.adaptability = True

        super().__init__(**kwargs)
    
    def racial_ability(self):
        return f"{self.name} використовує людську адаптивність - отримує +10% досвіду"

class Elf:
    """Ельф - швидкість та спритність"""
    race_name = "Ельф"
    
    def __init__(self, **kwargs):
        # Расові бонуси
        self.strength_bonus = -2
        self.agility_bonus = 5
        self.intelligence_bonus = 3
        self.max_health_bonus = 0
        
        # Расова здібність
        self.night_vision = True

        super().__init__(**kwargs)
    
    def racial_ability(self):
        return f"{self.name} використовує ельфійську грацію - ухиляється від атаки"

class Dwarf:
    """Гном - сила та витривалість"""
    race_name = "Гном"
    
    def __init__(self, **kwargs):
        # Расові бонуси
        self.strength_bonus = 4
        self.agility_bonus = -2
        self.intelligence_bonus = 0
        self.max_health_bonus = 30
        
        # Расова здібність
        self.stone_skin = True

        super().__init__(**kwargs)
    
    def racial_ability(self):
        return f"{self.name} використовує гномячу стійкість - зменшує шкоду на 20%"


# ============================================
# КЛАСИ - дають професійні вміння
# ============================================

class Warrior:
    """Воїн - ближній бій та висока витривалість"""
    class_name = "Воїн"
    
    def __init__(self, **kwargs):
        # Базові характеристики класу
        self.base_health = 150
        self.base_attack = 40
        self.base_defense = 30
        
        # Професійні атрибути
        self.weapon = "Меч"
        self.armor_type = "Важка броня"

        super().__init__(**kwargs)
    
    def class_ability(self):
        damage = self.base_attack * 2
        return f"{self.name} використовує Потужний Удар на {damage} шкоди!"
    
    def special_attack(self):
        return f"{self.name} робить обертовий удар мечем!"

class Mage:
    """Маг - магічні закляття"""
    class_name = "Маг"
    
    def __init__(self):
        # Базові характеристики класу
        self.base_health = 80
        self.base_attack = 15
        self.base_defense = 10
        
        # Професійні атрибути
        self.weapon = "Посох"
        self.mana = 200

        super().__init__(**kwargs)
    
    def class_ability(self):
        if self.mana >= 50:
            self.mana -= 50
            return f"{self.name} кастує Вогняну Кулю на 80 шкоди! Мана: {self.mana}"
        return f"{self.name} не має мани для закляття"
    
    def special_attack(self):
        return f"{self.name} використовує магічну блискавку!"

class Ranger:
    """Рейнджер - дистанційні атаки та скритність"""
    class_name = "Рейнджер"
    
    def __init__(self, **kwargs):
        # Базові характеристики класу
        self.base_health = 100
        self.base_attack = 35
        self.base_defense = 15
        
        # Професійні атрибути
        self.weapon = "Лук"
        self.arrows = 50

        super().__init__(**kwargs)
    
    def class_ability(self):
        if self.arrows > 0:
            self.arrows -= 1
            return f"{self.name} робить точний постріл! Стріл залишилось: {self.arrows}"
        return f"{self.name} закінчились стріли"
    
    def special_attack(self):
        return f"{self.name} випускає град стріл!"


# ============================================
# БАЗОВИЙ ГЕРОЙ - загальна функціональність
# ============================================

class Hero:
    """Базовий клас для всіх героїв"""
    
    def __init__(self, **kwargs):
        self.name = kwargs.pop("name", None)
        self.level = 1
        self.experience = 0
        
        # Викликаємо батьківські __init__
        # Тут спрацює MRO і ініціалізуються раса та клас
        super().__init__(**kwargs)
        
        # Обчислюємо фінальні характеристики
        self.max_health = self.base_health + self.max_health_bonus
        self.health = self.max_health
        self.attack = self.base_attack + self.strength_bonus
        self.defense = self.base_defense
        self.agility = 10 + self.agility_bonus
        self.intelligence = 10 + self.intelligence_bonus
    
    def get_info(self):
        return f"""
        ╔══════════════════════════════════════╗
          {self.name} - {self.race_name} {self.class_name}
        ╠══════════════════════════════════════╣
          Рівень: {self.level}
          HP: {self.health}/{self.max_health}
          Атака: {self.attack}
          Захист: {self.defense}
          Спритність: {self.agility}
          Інтелект: {self.intelligence}
          Зброя: {self.weapon}
        ╚══════════════════════════════════════╝
        """
    
    def attack_enemy(self, enemy):
        damage = max(1, self.attack - enemy.defense)
        enemy.health -= damage
        return f"{self.name} атакує {enemy.name} на {damage} шкоди!"

# ============================================
# Виконання завдання
# ============================================

class HumanWarrior(Warrior, Human, Hero):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

if __name__ == "__main__":
    aragorn = HumanWarrior(name="Арагорн")
    print(aragorn.get_info()) 
    print(aragorn.class_ability()) 
    print(aragorn.racial_ability())