class Life:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"This is a living organism: {self.name}"

class Acellularia(Life):
    def describe(self):
        return f"This is an acellular organism: {self.name}"

class Cellularia(Life):
    def describe(self):
        return f"This is a cellular organism: {self.name}"

class Prokaryota(Cellularia):
    def describe(self):
        return f"This is a prokaryote (no cell nucleus): {self.name}"

class Eukaryota(Cellularia):
    def describe(self):
        return f"This is a eukaryote (has cell nucleus): {self.name}"

class Unicellularia(Eukaryota):
    def describe(self):
        return f"This is a unicellular eukaryote: {self.name}"

class Fungi(Eukaryota):
    def describe(self):
        return f"This is a fungus: {self.name}"

class Plantae(Eukaryota):
    def describe(self):
        return f"This is a plant: {self.name}"

class Animalia(Eukaryota):
    def describe(self):
        return f"This is an animal: {self.name}"

