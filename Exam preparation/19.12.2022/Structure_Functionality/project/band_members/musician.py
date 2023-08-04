from typing import List

from abc import ABC, abstractmethod


class Musician(ABC):
    VALID_TYPES = ["Guitarist", "Drummer", "Singer"]

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills: List[str] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value.strip() == "":
            raise ValueError("Musician name cannot be empty!")

        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 16:
            raise ValueError("Musicians should be at least 16 years old!")

        self.__age = value

    # @property
    # @abstractmethod
    # def available_types_of_skills(self):
    #     pass

    @abstractmethod
    def learn_new_skill(self, new_skill: str):
        # TYPES_SKILLS = [self.available_types_of_skills]
        # TYPES_SKILLS = []
        # if new_skill not in TYPES_SKILLS:
        #     raise ValueError(f"{new_skill} is not a needed skill!")
        #
        # if new_skill in self.skills:
        #     raise ValueError(f"{new_skill} is already learned!")
        #
        # self.skills.append(new_skill)  # forgot
        #
        # return f"{self.name} learned to {new_skill}."  # forgot
        pass