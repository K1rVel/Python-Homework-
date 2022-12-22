class Genius():
    def __init__(self, name):
        self.name = name

    def plus(self):
        print(self.name + ' гений')


class Bad(Genius):
    def plus_plus(self):
        super().plus(), print('но его отчислят если он не будет учить ООП')



yana = Bad('Кирилл')
yana.plus_plus()