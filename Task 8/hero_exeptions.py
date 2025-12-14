class Hero:
    def __init__(self, name, health=100, mana=50, gold=100):
        self.name = name
        self.health = health
        self.mana = mana
        self.gold = gold
        self.inventory = []

    def cast_spell(self, spell_name, mana_cost):
        """Використовує закляття, витрачаючи ману"""
        if self.mana < mana_cost:
            print(f"{self.name} намагався використати {spell_name}, але не вистачає мани!")
            return 0

        self.mana -= mana_cost
        damage = mana_cost * 2
        print(f"{self.name} використав {spell_name}, завдав {damage} шкоди!")
        return damage

    def remove_from_inventory(self, item):
        """Видаляє предмет з інвентарю"""
        try:
            self.inventory.remove(item)
            print(f"Видалено '{item}' з інвентарю")
        except ValueError:
            print(f"Предмет '{item}' не знайдено в інвентарі")

    def get_item_at_index(self, index):
        """Повертає предмет за індексом"""
        try:
            return self.inventory[index]
        except IndexError:
            print("Неправильний індекс інвентарю")
            return None

    def divide_gold(self, num_players):
        """Ділить золото між гравцями"""
        try:
            share = self.gold / num_players
            print(f"Кожен гравець отримає {share} золота")
            return share
        except ZeroDivisionError:
            print("Неможливо поділити золото на 0 гравців")
            return 0

    def status(self):
        print(
            f"Герой: {self.name} | HP: {self.health} | "
            f"Мана: {self.mana} | Золото: {self.gold}"
        )
        print(f"Інвентар: {self.inventory}")



# ============================================================
# ТЕСТИ - цей код зараз ламає програму!
# Після ваших змін в класі всі тести мають пройти без падінь
# ============================================================

def run_tests():
    hero = Hero("Артур")
    hero.inventory = ["меч", "щит", "зілля"]
    hero.status()
    
    print("\n[Тест 1] Закляття з недостатньою маною")
    hero.cast_spell("Вогняна куля", 30)  # OK
    hero.cast_spell("Блискавка", 50)      # ПРОБЛЕМА: мани лише 20!
    print(f"Мана після тесту: {hero.mana}")
    
    print("\n[Тест 2] Видалення неіснуючого предмета")
    hero.remove_from_inventory("сокира")  # ПРОБЛЕМА: такого немає!
    
    print("\n[Тест 3] Доступ за неіснуючим індексом")
    item = hero.get_item_at_index(99)  # ПРОБЛЕМА: індекс за межами!
    print(f"Знайдено: {item}")
    
    print("\n[Тест 4] Ділення на нуль")
    hero.divide_gold(0)  # ПРОБЛЕМА: ділення на нуль!
    
    print("\n" + "=" * 40)
    print("✅ ВСІ ТЕСТИ ПРОЙДЕНО!")
    hero.status()

run_tests()