def print(*args, **kwargs):
    upper_text = ' '.join(map(str, args)).upper()
    __builtins__.print(upper_text, **kwargs)

print('Нельзя ли потише?')