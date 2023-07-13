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

# from project.animals.animal import Bird
# from project.food import Meat, Vegetable, Fruit, Seed
#
#
# class Owl(Bird):
#
#     @property
#     def food_that_eats(self) -> list:
#         return [Meat]
#
#     @property
#     def gained_weight(self) -> float:
#         return 0.25
#
#     def make_sound(self) -> str:
#         return "Hoot Hoot"
#
#
# class Hen(Bird):
#
#     @property
#     def food_that_eats(self) -> list:
#         return [Meat, Vegetable, Fruit, Seed]
#
#     @property
#     def gained_weight(self) -> float:
#         return 0.35
#
#     def make_sound(self) -> str:
#         return "Cluck"