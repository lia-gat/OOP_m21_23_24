def check_password(password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user_password = input("Введите пароль для доступа: ")
            if user_password == password:
                return func(*args, **kwargs)
            else:
                print("Неверный пароль. Доступ закрыт.")
        return wrapper
    return decorator

@check_password('password')
def make_burger(typeOfMeat, withOnion=False, withTomato=True):
    burger = f"Бургер с {typeOfMeat}."
    if withOnion:
        burger += " С луком."
    if withTomato:
        burger += " С помидорами."
    return burger


