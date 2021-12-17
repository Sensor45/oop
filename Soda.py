class Soda:
    def __init__(self, add_tasty='Обычная газировка'):
        self.add_tasty = add_tasty

    def show_my_drink(self):
        if soda.add_tasty == 'Обычная газировка':
            return ('Обычная газировка')
        else:
            return(f'Газировка и {soda.add_tasty}')

soda = Soda('клубника')
print(soda.show_my_drink())