class ReversedList:
    def __init__(self, lst):
        self.lst = lst

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, index):
        return self.lst[len(self.lst) - 1 - index]

rl = ReversedList([10, 20, 30])
for i in range(len(rl)):
    print(rl[i])

print()

rl = ReversedList([])
print(len(rl))

print()

rl = ReversedList([10])
print(len(rl))
print(rl[0])