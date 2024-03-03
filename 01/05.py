class BigBell:
    def __init__(self):
        self._ring = "ding"

    def sound(self):
        print(self._ring)
        if self._ring == "ding":
            self._ring = "dong"
        else:
            self._ring = "ding"
            
# Ваш код

bell = BigBell()
bell.sound()
bell.sound()
bell.sound()
