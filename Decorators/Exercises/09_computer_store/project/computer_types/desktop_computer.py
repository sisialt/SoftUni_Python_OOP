import math

from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    AVAILABLE_PROCESSORS = {
        "AMD Ryzen 7 5700G": 500,
        "Intel Core i5-12600K": 600,
        "Apple M1 Max": 1800
    }

    MAX_RAM = 128

    def powers_of_two(self):
        start = 2
        valid_powers = [2]
        while start < DesktopComputer.MAX_RAM:
            start *= 2
            valid_powers.append(start)

        return valid_powers

    def configure_computer(self, processor: str, ram: int):
        if processor not in DesktopComputer.AVAILABLE_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")

        if ram not in self.powers_of_two():
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram

        self.price = DesktopComputer.AVAILABLE_PROCESSORS[processor] + int(math.log2(ram)) * 100
        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."

# line 34: forgot * 100

# from project.computer_types.computer import Computer
#
#
# class DesktopComputer(Computer):
#
#     @property
#     def type(self):
#         return "desktop computer"
#
#     @property
#     def available_processors(self):
#         return {
#             "AMD Ryzen 7 5700G": 500,
#             "Intel Core i5-12600K": 600,
#             "Apple M1 Max": 1800,
#         }
#
#     @property
#     def max_ram(self):
#         return 128