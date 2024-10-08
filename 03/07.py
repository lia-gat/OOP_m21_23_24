class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients
    
    def __call__(self, x):
        return sum(c * x ** i for i, c in enumerate(self.coefficients))
    
    def __add__(self, other):
        new_coefficients = []
        max_len = max(len(self.coefficients), len(other.coefficients))
        
        for i in range(max_len):
            coeff1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coeff2 = other.coefficients[i] if i < len(other.coefficients) else 0
            new_coefficients.append(coeff1 + coeff2)
            
        return Polynomial(new_coefficients)
    
poly = Polynomial([10, -1])
print(poly(0))
print(poly(1))
print(poly(2))

print("*********************************")

poly1 = Polynomial([0, 0, 1])
print(poly1(-2))
print(poly1(-1))
print(poly1(0))
print(poly1(1))
print(poly1(2))
print()

poly2 = Polynomial([0, 0, 2])
print(poly2(-2))
print(poly2(-1))
print(poly2(0))
print(poly2(1))
print(poly2(2))
print()

poly3 = poly1 + poly2
print(poly3(-2))
print(poly3(-1))
print(poly3(0))
print(poly3(1))
print(poly3(2))
print()

print("*********************************")

poly1 = Polynomial([0, 1])
poly2 = Polynomial([10])
poly3 = poly1 + poly2
poly4 = poly2 + poly1

print(poly3(-2), poly4(-2))
print(poly3(-1), poly4(-1))
print(poly3(0), poly4(0))
print(poly3(1), poly4(1))
print(poly3(2), poly4(2))