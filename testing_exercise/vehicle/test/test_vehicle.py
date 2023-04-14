import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(30.5, 160.5)

    def test_constructor(self):
        self.assertEqual(self.vehicle.fuel, 30.5)
        self.assertEqual(self.vehicle.capacity, self.vehicle.fuel)
        self.assertEqual(self.vehicle.horse_power, 160.5)
        self.assertEqual(self.vehicle.fuel_consumption, self.vehicle.DEFAULT_FUEL_CONSUMPTION)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, 1.25)

    def test_drive_with_not_enough_fuel(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(100)
        self.assertEqual(str(context.exception), "Not enough fuel")

    def test_drive_with_enough_fuel(self):
        self.vehicle.drive(10)
        self.assertEqual(self.vehicle.fuel, 18)

    def test_over_refuel(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(1)
        self.assertEqual(str(context.exception), "Too much fuel")

    def test_correct_refuel(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(1)
        self.assertEqual(self.vehicle.fuel, 1)

    def test__str__return(self):
        self.assertEqual(self.vehicle.__str__(),
                         "The vehicle has 160.5 horse power with 30.5 fuel left and 1.25 fuel consumption")


if __name__ == '__main__':
    unittest.main()
