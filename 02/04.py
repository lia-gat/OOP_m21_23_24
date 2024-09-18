class MinStat:
    def __init__(self):
        self.numbers = []
    
    def add_number(self, number):
        self.numbers.append(number)
    
    def result(self):
        return min(self.numbers) if self.numbers else None

class MaxStat:
    def __init__(self):
        self.numbers = []
    
    def add_number(self, number):
        self.numbers.append(number)
    
    def result(self):
        return max(self.numbers) if self.numbers else None

class AverageStat:
    def __init__(self):
        self.numbers = []
    
    def add_number(self, number):
        self.numbers.append(number)
    
    def result(self):
        if not self.numbers:
            return None
        return sum(self.numbers) / len(self.numbers)

values = [1, 2, 4, 5]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))

mins = MinStat()
maxs = MaxStat()
average = AverageStat()

print(mins.result(), maxs.result(), average.result())

values = [1, 0, 0]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))
