from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken: bool = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        result = self.set_range_speed_limit()
        if not result[0] <= value <= result[1]:
            raise ValueError(f"Invalid speed limit! Must be between {result[0]} and {result[1]}!")
        self.__speed_limit = value

    @abstractmethod
    def set_range_speed_limit(self):
        pass

