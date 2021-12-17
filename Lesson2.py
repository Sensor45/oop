class City:
    def __init__(self, name, population, area, ):
        self._name = name
        self._population = population
        self._area = area
    def set_name(self, name):
        if isinstance(name, str):
            self._name = name

    def set_population(self, population):
        if isinstance(population, str):
            self._population = population

    def set_area(self, area):
        if isinstance(area, float):
            self._area = area

    def display_info(self):
        return f'Название : {self._name}\n' \
                f'Население : {self._population}\n' \
                f'Площядь : {self._area}'

class EuroCity(City):
    def __init__(self, name, population, area, id):
        super(EuroCity,self).__init__(name, population, area)
        self.id = id

moscow = City('Москва', 16000000, 35252523)
madrid = City('Мадрид', 16000000, 35252523)
print(madrid.display_info())

