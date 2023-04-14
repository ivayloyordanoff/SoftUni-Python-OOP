class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = Worker("Peter", 1000, 10)

    def test_initialization(self):
        self.assertEqual(self.worker.name, "Peter")
        self.assertEqual(self.worker.salary, 1000)
        self.assertEqual(self.worker.energy, 10)

    def test_rest(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 11)

    def test_work_with_not_enough_energy(self):
        worker = Worker("Peter", 1000, 0)
        with self.assertRaises(Exception) as context:
            worker.work()
        self.assertEqual(str(context.exception), 'Not enough energy.')

    def test_work_and_increase_money(self):
        self.worker.work()
        self.assertEqual(self.worker.money, 1000)

    def test_work_and_decrease_energy(self):
        self.worker.work()
        self.assertEqual(self.worker.energy, 9)

    def test_get_info_returns_correct_string(self):
        self.assertEqual(self.worker.get_info(), 'Peter has saved 0 money.')


if __name__ == '__main__':
    unittest.main()
