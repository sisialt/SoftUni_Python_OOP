from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    VALID_TYPES = ["Desktop Computer", "Laptop"]
    """
    VALID_COMPUTERS = {
        "Desktop Computer": DesktopComputer,
        "Laptop": Laptop,
    }
    """

    def __init__(self):
        self.warehouse: list = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in ComputerStoreApp.VALID_TYPES:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        if type_computer == "Laptop":
            new_comp = Laptop(manufacturer, model)
        else:
            new_comp = DesktopComputer(manufacturer, model)

        """
        try:
            computer = self.VALID_COMPUTERS[type_computer](manufacturer, model)
        except KeyError:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        """

        result = new_comp.configure_computer(processor, ram)

        self.warehouse.append(new_comp)

        return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for comp in self.warehouse:
            if comp.price > client_budget:
                continue

            if comp.processor != wanted_processor:
                continue

            if comp.ram < wanted_ram:
                continue

            self.profits += client_budget - comp.price
            self.warehouse.remove(comp)

            return f"{comp} sold for {client_budget}$."

        raise Exception("Sorry, we don't have a computer for you.")

# line 56: it was return, not raise Exception
# forgot line 52 (not tested in judge)
