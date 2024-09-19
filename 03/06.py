class SparseArray:
    def __init__(self):
        self. array = [0]

    def __getitem__(self, key):
        if len(self.array) < key + 1:
            self.__setitem__(key, 0)
        return self.array[key]

    def __setitem__(self, key, value):
        if len(self.array) < key+1:
            for _ in range(key - len(self.array)+2):
                self.array.append(0)
        self.array[key] = value

arr = SparseArray()
arr[1] = 10
arr[8] = 20
for i in range(10):
    print('arr[{}] = {}'.format(i, arr[i]))
    
print()

arr = SparseArray()
arr[10] = 123
for i in range(8, 13):
    print('arr[{}] = {}'.format(i, arr[i]))
    
print()

def print_elem(array, ind):
    print('arr[{}] = {}'.format(ind, array[ind]))


arr = SparseArray()
index = 1000000000
arr[index] = 123

print_elem(arr, index - 1)
print_elem(arr, index)
print_elem(arr, index + 1)