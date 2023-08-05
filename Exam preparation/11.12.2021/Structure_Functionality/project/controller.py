from typing import List

from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.race import Race
from project.driver import Driver


class Controller:
    VALID_CAR_TYPES = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars: List[Car] = []
        self.races: List[Race] = []
        self.drivers: List[Driver] = []

    def __find_car(self, car_type):
        c = [c for c in self.cars if c.__class__.__name__ == car_type]
        if c:
            return c[0]

    def __find_driver(self, driver_name):
        d = [d for d in self.drivers if d.name == driver_name]
        if d:
            return d[0]

    def __find_race(self, race_name):
        r = [r for r in self.races if r.name == race_name]
        if r:
            return r[0]

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in Controller.VALID_CAR_TYPES:
            return

        car_with_same_model = [c for c in self.cars if c.model == model]
        if car_with_same_model:
            raise Exception(f"Car {model} is already created!")

        car = Controller.VALID_CAR_TYPES[car_type](model, speed_limit)
        self.cars.append(car)

        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver_with_same_name = self.__find_driver(driver_name)
        if driver_with_same_name:
            raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)

        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        race_with_same_name = self.__find_race(race_name)
        if race_with_same_name:
            raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)
        self.races.append(race)

        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver_with_same_name = self.__find_driver(driver_name)
        if not driver_with_same_name:
            raise Exception(f"Driver {driver_name} could not be found!")

        car_with_same_name = self.__find_car(car_type)
        if not car_with_same_name:
            raise Exception(f"Car {car_type} could not be found!")

        free_cars = [c for c in self.cars if not c.is_taken]
        if not free_cars:
            raise Exception(f"Car {car_type} could not be found!")

        car = free_cars[-1]

        if driver_with_same_name.car:
            old_model = driver_with_same_name.car.model
            driver_with_same_name.car.is_taken = False

            driver_with_same_name.car = car
            car.is_taken = True

            return f"Driver {driver_name} changed his car from {old_model} to {car.model}."

        else:
            driver_with_same_name.car = car
            car.is_taken = True

            return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race_with_same_name = self.__find_race(race_name)
        if not race_with_same_name:
            raise Exception(f"Race {race_name} could not be found!")

        driver_with_same_name = self.__find_driver(driver_name)
        if not driver_with_same_name:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver_with_same_name.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver_with_same_name in race_with_same_name.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race_with_same_name.drivers.append(driver_with_same_name)

        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race_with_same_name = self.__find_race(race_name)
        if not race_with_same_name:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race_with_same_name.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        sorted_drivers = sorted([d for d in race_with_same_name.drivers], key=lambda x: -x.car.speed_limit) # wrong sort
        first_three_fastest_drivers = sorted_drivers[:3]

        result = []

        for d in first_three_fastest_drivers:
            d.number_of_wins += 1

            result.append(f"Driver {d.name} wins the {race_name} race with a speed of {d.car.speed_limit}.")

        return "\n".join(result)



