class NonNegative:
    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr] 

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Введеные данные не могут быть отрицательными! ')
        instance.__dict__[self.my_attr] = value 

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    length = NonNegative()
    width = NonNegative()
    weigth = None
    tickness = None

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def intake(self):
        self.weigth = 25
        self.tickness = 0.05
        intake = self.length * self.width * self.weigth * self.tickness / 1000
        print(f'Требуется {intake} тонн для покрытия 1 кв. метра')


road_to_village = Road(100, 5)
road_to_village.intake()
