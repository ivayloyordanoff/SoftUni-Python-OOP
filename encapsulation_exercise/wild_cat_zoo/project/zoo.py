from typing import List
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List = []
        self.workers: List = []

    def add_animal(self, animal: Lion or Tiger or Cheetah, price: int):
        if self.__animal_capacity > len(self.animals):
            if self.__budget >= price:
                self.animals.append(animal)
                self.__budget -= price

                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Keeper or Caretaker or Vet):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)

            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name: str):
        try:
            worker = next(filter(lambda w: w.name == worker_name, self.workers))
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

        self.workers.remove(worker)

        return f"{worker_name} fired successfully"

    def pay_workers(self):
        salaries = sum(worker.salary for worker in self.workers)

        if self.__budget >= salaries:
            self.__budget -= salaries

            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        money_for_care = sum(animal.money_for_care for animal in self.animals)

        if self.__budget >= money_for_care:
            self.__budget -= money_for_care

            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        lions = list(filter(lambda x: x.__class__.__name__ == 'Lion', self.animals))
        lions_str = "\n".join(str(x) for x in lions)
        tigers = list(filter(lambda x: x.__class__.__name__ == 'Tiger', self.animals))
        tigers_str = "\n".join(str(x) for x in tigers)
        cheetahs = list(filter(lambda x: x.__class__.__name__ == 'Cheetah', self.animals))
        cheetahs_str = "\n".join(str(x) for x in cheetahs)

        return f"You have {len(self.animals)} animals\n" \
               f"----- {len(lions)} Lions:\n" \
               f"{lions_str}\n" \
               f"----- {len(tigers)} Tigers:\n" \
               f"{tigers_str}\n" \
               f"----- {len(cheetahs)} Cheetahs:\n" \
               f"{cheetahs_str}"

    def workers_status(self):
        keepers = list(filter(lambda x: x.__class__.__name__ == 'Keeper', self.workers))
        keepers_str = "\n".join(str(x) for x in keepers)
        caretakers = list(filter(lambda x: x.__class__.__name__ == 'Caretaker', self.workers))
        caretakers_str = "\n".join(str(x) for x in caretakers)
        vets = list(filter(lambda x: x.__class__.__name__ == 'Vet', self.workers))
        vets_str = "\n".join(str(x) for x in vets)

        return f"You have {len(self.workers)} workers\n" \
               f"----- {len(keepers)} Keepers:\n" \
               f"{keepers_str}\n" \
               f"----- {len(caretakers)} Caretakers:\n" \
               f"{caretakers_str}\n" \
               f"----- {len(vets)} Vets:\n" \
               f"{vets_str}"
