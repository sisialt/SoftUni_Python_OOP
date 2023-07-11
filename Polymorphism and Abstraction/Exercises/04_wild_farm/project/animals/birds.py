from project.animals.animal import Bird
from project.food import Meat


class Owl(Bird):
    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    def feed(self, food):
        increase_factor = 0.25

        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.increase_food_eaten_and_weight(increase_factor, food)


class Hen(Bird):
    @staticmethod
    def make_sound():
        return "Cluck"

    def feed(self, food):
        increase_factor = 0.35
        self.increase_food_eaten_and_weight(increase_factor, food)
