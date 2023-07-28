import math

from project.computer_types.computer import Computer


class Laptop(Computer):
    AVAILABLE_PROCESSORS = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200
    }

    MAX_RAM = 64

    def powers_of_two(self):
        start = 2
        while start <= Laptop.MAX_RAM:
            yield start
            start *= 2

    def configure_computer(self, processor: str, ram: int):
        if processor not in Laptop.AVAILABLE_PROCESSORS:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")

        if ram not in self.powers_of_two():
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram

        self.price = Laptop.AVAILABLE_PROCESSORS[processor] + int(math.log2(ram)) * 100
        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$."

# line 31: forgot * 100

# from project.computer_types.computer import Computer
#
#
# class Laptop(Computer):
#
#     @property
#     def type(self):
#         return "laptop"
#
#     @property
#     def available_processors(self):
#         return {
#             "AMD Ryzen 9 5950X": 900,
#             "Intel Core i9-11900H": 1050,
#             "Apple M1 Pro": 1200,
#         }
#
#     @property
#     def max_ram(self):
#         return 64
