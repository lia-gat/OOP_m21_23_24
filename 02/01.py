class Selector:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_odds(self):
        return [num for num in self.numbers if num % 2 != 0]

    def get_evens(self):
        return [num for num in self.numbers if num % 2 == 0]

# Примеры использования
values1 = [11, 12, 13, 14, 15, 16, 22, 44, 66]
selector1 = Selector(values1)
odds1 = selector1.get_odds()
evens1 = selector1.get_evens()
print(' '.join(map(str, odds1)))
print(' '.join(map(str, evens1)))

values2 = [6, 6, 0, 4, 8, 7, 6, 4, 7, 5]
selector2 = Selector(values2)
odds2 = selector2.get_odds()
evens2 = selector2.get_evens()
print(' '.join(map(str, odds2)))
print(' '.join(map(str, evens2)))

values3 = []
selector3 = Selector(values3)
odds3 = selector3.get_odds()
evens3 = selector3.get_evens()
print(' '.join(map(str, odds3)))
print(' '.join(map(str, evens3)))
