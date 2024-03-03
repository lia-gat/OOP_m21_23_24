class BoundingRectangle:
    def __init__(self):
        self._min_x = float('inf')
        self._min_y = float('inf')
        self._max_x = float('-inf')
        self._max_y = float('-inf')
    
    def add_point(self, x, y):
        if x < self._min_x:
            self._min_x = x
        if y < self._min_y:
            self._min_y = y
        if x > self._max_x:
            self._max_x = x
        if y > self._max_y:
            self._max_y = y
    
    def width(self):
        return self._max_x - self._min_x

    
    def height(self):
        return self._max_y - self._min_y
    
    def bottom_y(self):
        return self._min_y
    
    def top_y(self):
        return self._max_y
    
    def left_x(self):
        return self._min_x
    
    def right_x(self):
        return self._max_x
    
# Ваш код

rect = BoundingRectangle()
rect.add_point(-1, -2)
rect.add_point(3, 4)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())

print('***')

# Ваш код

rect = BoundingRectangle()
rect.add_point(10, 20)
rect.add_point(5, 7)
rect.add_point(6, 3)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())

print('***')    

# Ваш код

rect = BoundingRectangle()
rect.add_point(-11, -12)
rect.add_point(13, -14)
rect.add_point(-15, 10)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
print()
rect.add_point(-21, -12)
rect.add_point(13, -14)
rect.add_point(-15, 36)
print(rect.width(), rect.height())
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print()
rect.add_point(-21, 78)
rect.add_point(13, -14)
rect.add_point(-55, 36)
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
print(rect.left_x(), rect.right_x())