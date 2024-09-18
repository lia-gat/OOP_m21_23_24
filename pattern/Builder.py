class Engine:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f"Engine(type={self.type})"

class Transmission:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f"Transmission(type={self.type})"

class Body:
    def __init__(self, type, color):
        self.type = type
        self.color = color

    def __str__(self):
        return f"Body(type={self.type}, color={self.color})"

class Car:
    def __init__(self):
        self.brand = None
        self.model = None
        self.engine = None
        self.transmission = None
        self.body = None

    def __str__(self):
        return (f"Car(brand={self.brand}, model={self.model}, "
                f"{self.engine}, {self.transmission}, {self.body})")

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_brand(self, brand):
        self.car.brand = brand
        return self

    def set_model(self, model):
        self.car.model = model
        return self

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def set_transmission(self, transmission):
        self.car.transmission = transmission
        return self

    def set_body(self, body):
        self.car.body = body
        return self

    def get_car(self):
        return self.car

class SedanBuilder(CarBuilder):
    def __init__(self):
        super().__init__()

    def build(self):
        return (self.set_brand("Toyota")
                    .set_model("Camry")
                    .set_engine(Engine("V6"))
                    .set_transmission(Transmission("Automatic"))
                    .set_body(Body("Sedan", "Black"))
                    .get_car())

class SUVBuilder(CarBuilder):
    def __init__(self):
        super().__init__()

    def build(self):
        return (self.set_brand("Ford")
                    .set_model("Explorer")
                    .set_engine(Engine("V8"))
                    .set_transmission(Transmission("Automatic"))
                    .set_body(Body("SUV", "White"))
                    .get_car())

class SportsCarBuilder(CarBuilder):
    def __init__(self):
        super().__init__()

    def build(self):
        return (self.set_brand("Ferrari")
                    .set_model("488")
                    .set_engine(Engine("V8"))
                    .set_transmission(Transmission("Manual"))
                    .set_body(Body("Sports Car", "Red"))
                    .get_car())

class CarDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_car(self):
        return self.builder.build()

sedan_builder = SedanBuilder()
director = CarDirector(sedan_builder)
sedan = director.construct_car()
print("Создан седан:", sedan)

suv_builder = SUVBuilder()
director = CarDirector(suv_builder)
suv = director.construct_car()
print("Создан SUV:", suv)

sports_car_builder = SportsCarBuilder()
director = CarDirector(sports_car_builder)
sports_car = director.construct_car()
print("Создан спортивный автомобиль:", sports_car)
