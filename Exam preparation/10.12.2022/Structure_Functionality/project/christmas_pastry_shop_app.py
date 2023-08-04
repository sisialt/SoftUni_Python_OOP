from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACY_TYPES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    VALID_BOOTH_TYPES = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0

    def __find_delicacy_with_given_name(self, name):
        d = [d for d in self.delicacies if d.name == name]
        if d:
            return d[0]
        return False

    def __find_booth_with_given_number(self, number):
        b = [b for b in self.booths if b.booth_number == number]
        if b:
            return b[0]
        return False

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if self.__find_delicacy_with_given_name(name):
            raise Exception(f"{name} already exists!")

        if type_delicacy not in ChristmasPastryShopApp.VALID_DELICACY_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = ChristmasPastryShopApp.VALID_DELICACY_TYPES[type_delicacy](name, price)
        self.delicacies.append(delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if self.__find_booth_with_given_number(booth_number):
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in ChristmasPastryShopApp.VALID_BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = ChristmasPastryShopApp.VALID_BOOTH_TYPES[type_booth](booth_number, capacity)
        self.booths.append(booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        not_reserved_boots = [b for b in self.booths if not b.is_reserved]
        if not not_reserved_boots:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth = not_reserved_boots[0]
        if booth.capacity < number_of_people:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)

        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.__find_booth_with_given_number(booth_number)
        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = self.__find_delicacy_with_given_name(delicacy_name)
        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.__find_booth_with_given_number(booth_number)
        bill_for_booth = booth.price_for_reservation + sum([d.price for d in booth.delicacy_orders])

        self.income += bill_for_booth
        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0

        return (f"Booth {booth_number}:\n"
                f"Bill: {bill_for_booth:.2f}lv.")

    def get_income(self):
        return f"Income: {self.income:.2f}lv."