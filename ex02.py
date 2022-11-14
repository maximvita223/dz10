class NonNegative:
    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Введеные данные не могут быть отрицательными! ')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

class Worker:

    name = None
    surname = None
    position = None
    profit = NonNegative()
    bonus = NonNegative()

    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.profit = profit
        self.bonus = bonus


class Position(Worker):
    def __init__(self, name, surname, position, profit, bonus):
        super().__init__(name, surname, position, profit, bonus)
        self.__income = {'Оклад': self.profit, 'Премия': self.bonus}

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_full_profit(self):
        self.__income = self.profit + self.bonus
        return self.__income


manager = Position('Иван', 'Иванович', 'Тестеровщик', 500, 100)
print(manager.get_full_name(), manager.get_full_profit())
