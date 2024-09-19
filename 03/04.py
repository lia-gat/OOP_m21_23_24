class Date:
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    
    def __init__(self, month, day):
        self.month = month
        self.day = day

    def __sub__(self, other):
        def days_from_start(date):
            return sum(self.days_in_month[:date.month - 1]) + date.day
        
        return days_from_start(self) - days_from_start(other)

jan5 = Date(1, 5)
jan1 = Date(1, 1)

print(jan5 - jan1)
print(jan1 - jan5)
print(jan1 - jan1)
print(jan5 - jan5)

print()

mar5 = Date(3, 1)
jan1 = Date(1, 1)

print(mar5 - jan1)
print(jan1 - mar5)
print(jan1 - jan1)
print(mar5 - mar5)