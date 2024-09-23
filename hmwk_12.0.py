class House:
    houses_history = []
    __instance = None

    def __new__(cls, *args, **kwargs):
        # print('Я в ньюшке')
        cls.houses_history.append(args[0])

        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, *args, name='Name', number_of_floors=10):
        # print('Я в ините, ничо нинаю')
        self.args = args
        self.name = args[0]
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i + 1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        isinstance(other, int)
        if self.number_of_floors == other:
            return True
        else:
            return False

    def __lt__(self, other):
        isinstance(other, int)
        if self.number_of_floors < other:
            return True
        else:
            return False

    def __le__(self, other):
        isinstance(other, int)
        if self.number_of_floors <= other:
            return True
        else:
            return False

    def __gt__(self, other):
        isinstance(other, int)
        if self.number_of_floors > other:
            return True
        else:
            return False

    def __ge__(self, other):
        isinstance(other, int)
        if self.number_of_floors >= other:
            return True
        else:
            return False

    def __ne__(self, other):
        isinstance(other, int)
        if self.number_of_floors != other:
            return True
        else:
            return False

    def __add__(self, value):
        isinstance(value, int)
        self.number_of_floors = self.number_of_floors + value
        return self

    def __radd__(self, value):
        isinstance(value, int)
        self.number_of_floors = value + self.number_of_floors
        return self

    def __iadd__(self, value):
        isinstance(value, int)
        self.number_of_floors += value
        return self

    def __del__(self):
        print(f'{self.name} снесён, но останется в истории')



h1_1 = ['ЖК Эльбрус', 10]
h2_2 = ['ЖК Акация', 20]
h3_3 = ['ЖК Матрёшки', 20]
h1 = House(*h1_1)
print(House.houses_history)
h2 = House(*h2_2)
print(House.houses_history)
h3 = House(*h3_3)
print(House.houses_history)

del h3

print(House.houses_history)
