class SpaceObject():
    def __init__(self, size):
        self.size = size


class Star(SpaceObject):
    def __init__(self, size, light):
        super().__init__(light)
        self.light = light

    def to_light(self):
        print(self.light)


class Planet(SpaceObject):
    def __init__(self, size, light, population, plus_people):
        super().__init__(population)
        super().__init__(plus_people)
        self.population = population
        self.plus_people = plus_people

    def years(self, year):
        print(self.population + (year * self.plus_people))


sun = Star(111, 777)
Earth = Planet(123, 444, 2, 4)
Earth.years(7)