from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    @property
    def maximum_speed(self):
        return 120

    def train(self):
        self.speed = min(self.speed + 2, self.maximum_speed)

    # @property
    # def speed(self):
    #     return self.__speed
    #
    # @speed.setter
    # def speed(self, value):
    #     if value > self.maximum_speed:
    #         raise ValueError("Horse speed is too high!")
    #     self.__speed = value
