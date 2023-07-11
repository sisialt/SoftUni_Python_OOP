from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit, Seed


class Mouse(Mammal):
    @staticmethod
    def make_sound():
        return "Squeak"

    def feed(self, food):
        increase_factor = 0.10

        if not isinstance(food, Vegetable) and not isinstance(food, Fruit):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.increase_food_eaten_and_weight(increase_factor, food)


class Dog(Mammal):
    @staticmethod
    def make_sound():
        return "Woof!"

    def feed(self, food):
        increase_factor = 0.40
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.increase_food_eaten_and_weight(increase_factor, food)


class Cat(Mammal):
    @staticmethod
    def make_sound():
        return "Meow"

    def feed(self, food):
        increase_factor = 0.30
        if not isinstance(food, Vegetable) and not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.increase_food_eaten_and_weight(increase_factor, food)


class Tiger(Mammal):
    @staticmethod
    def make_sound():
        return "ROAR!!!"

    def feed(self, food):
        increase_factor = 1.00
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.increase_food_eaten_and_weight(increase_factor, food)
