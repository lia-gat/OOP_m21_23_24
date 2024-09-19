def check_password(f):
    def wrapper(*args, **kwargs):
        password = input("Введите пароль: ")
        correct_password = "secret"  
        
        if password != correct_password:
            print("В доступе отказано")
            return None
        
        return f(*args, **kwargs)
    
    return wrapper

@check_password
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence

num = int(input("Введите количество чисел Фибоначчи для вычисления: "))
result = fibonacci(num)

if result is not None:
    print("Последовательность Фибоначчи:", result)
