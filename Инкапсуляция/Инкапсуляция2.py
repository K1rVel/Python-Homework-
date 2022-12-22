class Hero:
    def __init__(self, health, power, rank):
        self.health = health
        self.power = power
        self.__rank = rank

    def sett_rank(self, rank):
        self.__rank = rank

    def gett_rank(self):
        return self.__rank

    def dell_rank(self):
        del self.__rank

    def fightt(self, enemy):
        while self.power > 0:
            enemy.health -= 5
            self.power -= 15
        if enemy.health < 0:
            self.sett_rank('Победитель арены')
            print(self.gett_rank())
        else:
            self.dell_rank()
            print('Проигравший')


def main():
    hero1 = Hero(17, 50, ' - 0')
    hero2 = Hero(14, 117, ' - 0')
    hero1.fightt(hero2)


main()