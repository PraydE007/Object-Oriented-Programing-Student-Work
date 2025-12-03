# Банківський рахунок
# Можна поповнювати, знімати гроші, перевіряти баланс
# Зберігається історія транзакцій

class account:
    def __init__(self, name: str):
        self.__name = name
        self.__balance = 0
        self.__history = []

    def getName(self):
        return self.__name

    def getBalance(self):
        return self.__balance

    def __balanceOperation(self, value: float, htext: str):
        self.__balance = self.__balance + value
        self.__history.append(htext + str(abs(value)))
        return True

    def deposit(self, value: float) -> bool:
        if not value > 0:
            return False
        return self.__balanceOperation(value, "Поповнення: +")

    def withdraw(self, value: float) -> bool:
        if not value > 0 & value <= self.__balance:
            return False
        return self.__balanceOperation(-value, "Зняття: -")

    def printHistory(self):
        for record in self.__history:
            print(record)

    def printInfo(self):
        print(f"Власник: {self.__name}, Баланс: {str(self.__balance)}")


# Приклад використання:
a = account("Іван")
a.deposit(1000)      # поповнити на 1000
a.withdraw(300)        # зняти 300
a.printInfo()    # Власник: Іван, Баланс: 700
a.printHistory()       # історія транзакцій