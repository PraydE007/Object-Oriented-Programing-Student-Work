# Калькулятор вартості замовлення в інтернет-магазині
# Податок (ПДВ) = 20%
# Знижка передається як десятковий дріб (0.1 = 10%)

PDV = 1.2

# Метод розраховує суму замовлення (з податком або без)
def calc(prices_lst, tax):
    result = sum(prices_lst)
    if tax:
        return result * PDV
    return result

# Метод розраховує суму замовлення зі знижкою (з податком або без)
def calcWithDiscount(prices_lst, tax, discont):
    return calc(prices_lst, tax) * (1 - discont)


# Приклад використання:
prices = [100, 200, 50]  # ціни товарів
print(calc(prices, True))       # сума з ПДВ → 420.0
print(calc(prices, False))      # сума без ПДВ → 350
print(calcWithDiscount(prices, True, 0.1))  # сума з ПДВ мінус 10% → 378.0