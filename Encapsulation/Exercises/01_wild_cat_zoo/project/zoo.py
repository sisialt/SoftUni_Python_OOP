from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"

        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price

        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"

        self.workers.append(worker)

        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        worker = [w for w in self.workers if w.name == worker_name]

        if not worker:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker[0])

        return f"{worker_name} fired successfully"

    def pay_workers(self) -> str:
        total_salaries = sum([w.salary for w in self.workers])

        if total_salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= total_salaries

        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        total_cost_for_animals_care = sum([a.money_for_care for a in self.animals])

        if total_cost_for_animals_care > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= total_cost_for_animals_care

        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        lions, tigers, cheetahs = [], [], []

        for a in self.animals:
            if a.__class__.__name__ == "Lion":
                lions.append(a)
            elif a.__class__.__name__ == "Tiger":
                tigers.append(a)
            else:
                cheetahs.append(a)

        lions_info = '\n'.join([l.__repr__() for l in lions])
        tigers_info = '\n'.join([t.__repr__() for t in tigers])
        cheetahs_info = '\n'.join([c.__repr__() for c in cheetahs])

        return f"You have {len(self.animals)} animals\n" \
               f"----- {len(lions)} Lions:\n" \
               f"{lions_info}\n" \
               f"----- {len(tigers)} Tigers:\n" \
               f"{tigers_info}\n" \
               f"----- {len(cheetahs)} Cheetahs:\n" \
               f"{cheetahs_info}"

    def workers_status(self) -> str:
        keepers, caretakers, vets = [], [], []

        for w in self.workers:
            if w.__class__.__name__ == "Keeper":
                keepers.append(w)
            elif w.__class__.__name__ == "Caretaker":
                caretakers.append(w)
            else:
                vets.append(w)

        keepers_info = '\n'.join([k.__repr__() for k in keepers])
        caretakers_info = '\n'.join([c.__repr__() for c in caretakers])
        vets_info = '\n'.join([v.__repr__() for v in vets])

        return f"You have {len(self.workers)} workers\n" \
               f"----- {len(keepers)} Keepers:\n" \
               f"{keepers_info}\n" \
               f"----- {len(caretakers)} Caretakers:\n" \
               f"{caretakers_info}\n" \
               f"----- {len(vets)} Vets:\n" \
               f"{vets_info}"


