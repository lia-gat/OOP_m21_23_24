class Queue:
    def __init__(self, *values):
        self.queue = list(values)

    def append(self, *values):
        self.queue.extend(values)

    def copy(self):
        return Queue(*self.queue)

    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return None
  
    def extend(self, queue):
        self.queue.extend(queue.queue)
  
    def next(self):
        if self.queue:
            return Queue(*self.queue[1:])
        else:
            return Queue()


    def __str__(self):
        return f"[{' -> '.join(map(str, self.queue))}]"
  
    def __add__(self, other):
        result = self.copy()
        result.extend(other)
        return result

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __eq__(self, other):
        return self.queue == other.queue

    def __rshift__(self, n):
        if n < len(self.queue):
            return Queue(*self.queue[n:])
        else:
            return Queue()

    def __iter__(self):
        return iter(self.queue)

    def __next__(self):
        return self.next()
    
q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)
q2 = q1.copy()
print(q2)
print(q1 == q2, id(q1) == id(q2))
q3 = q2.next()
print(q1, q2, q3, sep = '\n')
print(q1 + q3)
q3.extend(Queue(1, 2))
print(q3)
q4 = Queue(1, 2)
q4 += q3 >> 4
print(q4)
q5 = next(q4)
print(q4)
print(q5)
