from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    VALID_ASTRONAUT_TYPES = {"Biologist": Biologist, "Geodesist": Geodesist, "Meteorologist": Meteorologist}

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.completed_missions = 0
        self.not_completed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in SpaceStation.VALID_ASTRONAUT_TYPES:
            raise Exception("Astronaut type is not valid!")

        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        astronaut = SpaceStation.VALID_ASTRONAUT_TYPES[astronaut_type](name)
        self.astronaut_repository.add(astronaut)

        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        items_as_list = items.split(", ")

        planet = Planet(name)
        planet.items.extend(items_as_list)
        self.planet_repository.add(planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        if not self.astronaut_repository.find_by_name(name):
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(self.astronaut_repository.find_by_name(name))

        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")

        suitable_astronauts = [a for a in self.astronaut_repository.astronauts if a.oxygen > 30]
        if not suitable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        if len(suitable_astronauts) > 5:
            suitable_astronauts = suitable_astronauts[:5]

        suitable_astronauts = sorted(suitable_astronauts, key=lambda x: -x.oxygen)

        participated_astronauts = 0

        for astronaut in suitable_astronauts:
            participated_astronauts += 1

            for i in range(len(planet.items) - 1, -1, -1):
                item = planet.items[i]

                astronaut.backpack.append(item)
                astronaut.breathe()

                planet.items.pop()

                if astronaut.oxygen <= 0:
                    break

            if not planet.items:
                break

        if not planet.items:
            self.completed_missions += 1
            return f"Planet: {planet_name} was explored. {participated_astronauts} astronauts participated in collecting items."
        else:
            self.not_completed_missions += 1
            return "Mission is not completed."

    def report(self):
        result = [f"{self.completed_missions} successful missions!\n"
                  f"{self.not_completed_missions} missions were not completed!\n"
                  f"Astronauts' info:"]

        for a in self.astronaut_repository.astronauts:
            if not a.backpack:
                result_backpack = "none"
            else:
                result_backpack = ", ".join(a.backpack)

            result.append(f"Name: {a.name}\n"
                          f"Oxygen: {a.oxygen}\n"
                          f"Backpack items: {result_backpack}")

        return "\n".join(result)