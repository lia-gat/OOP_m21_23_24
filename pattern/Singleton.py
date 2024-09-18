class GameSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(GameSettings, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.volume = 50
            self.difficulty = "Normal"
            self._initialized = True

    @staticmethod
    def get_instance():
        if not GameSettings._instance:
            GameSettings()
        return GameSettings._instance


# Пример использования
settings1 = GameSettings.get_instance()
settings2 = GameSettings.get_instance()

# Проверим, что это один и тот же объект
print(settings1 is settings2)  # Выведет True

# Меняем настройки в одном объекте
settings1.volume = 70
settings1.difficulty = "Hard"

# Проверяем, что настройки изменились в обоих объектах
print(settings2.volume)  # Выведет 70
print(settings2.difficulty)  # Выведет "Hard"
