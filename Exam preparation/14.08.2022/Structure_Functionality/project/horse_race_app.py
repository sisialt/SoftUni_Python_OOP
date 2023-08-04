from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_TYPES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}
    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def __find_horse(self, name):
        h = [h for h in self.horses if h.name == name]
        if h:
            return h[0]

    def __find_jockey(self, name):
        j = [j for j in self.jockeys if j.name == name]
        if j:
            return j[0]

    def __find_race(self, race_type):
        r = [r for r in self.horse_races if r.race_type == race_type]
        if r:
            return r[0]

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.VALID_HORSE_TYPES:
            return

        horse_with_same_name = self.__find_horse(horse_name)
        if horse_with_same_name:
            raise Exception(f"Horse {horse_name} has been already added!")

        horse = self.VALID_HORSE_TYPES[horse_type](horse_name, horse_speed)
        self.horses.append(horse)

        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey_with_same_name = self.__find_jockey(jockey_name)
        if jockey_with_same_name:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        race_with_same_type = self.__find_race(race_type)
        if race_with_same_type:
            raise Exception(f"Race {race_type} has been already created!")

        horse_race = HorseRace(race_type)
        self.horse_races.append(horse_race)

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__find_jockey(jockey_name)
        if jockey not in self.jockeys:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horse = [h for h in self.horses if h.__class__.__name__ == horse_type]
        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        available_horses = [h for h in horse if not h.is_taken]
        if not available_horses:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        last_horse = available_horses[-1]
        jockey.horse = last_horse

        return f"Jockey {jockey_name} will ride the horse {last_horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.__find_race(race_type)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self.__find_jockey(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)

        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.__find_race(race_type)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        highest_speed = 0
        winner_jockey_name = ""
        winner_horse_name = ""

        for j in race.jockeys:
            if j.horse.speed > highest_speed:
                highest_speed = j.horse.speed
                winner_jockey_name = j.name
                winner_horse_name = j.horse.name

        return (f"The winner of the {race_type} race, "
                f"with a speed of {highest_speed}km/h is {winner_jockey_name}! "
                f"Winner's horse: {winner_horse_name}.")