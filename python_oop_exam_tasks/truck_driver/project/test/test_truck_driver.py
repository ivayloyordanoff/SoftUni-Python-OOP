from project.truck_driver import TruckDriver
import unittest


class TestTruckDriver(unittest.TestCase):

    def setUp(self):
        self.truck_driver = TruckDriver("John", 2.5)

    def test_initialization(self):
        self.assertEqual(self.truck_driver.name, "John")
        self.assertEqual(self.truck_driver.money_per_mile, 2.5)
        self.assertEqual(self.truck_driver.available_cargos, {})
        self.assertEqual(self.truck_driver.earned_money, 0)
        self.assertEqual(self.truck_driver.miles, 0)

    def test_add_cargo_offer_raises_exception(self):
        self.truck_driver.add_cargo_offer("New York", 300)
        with self.assertRaises(Exception) as context:
            self.truck_driver.add_cargo_offer("New York", 300)
        self.assertEqual(str(context.exception), "Cargo offer is already added.")

    def test_add_cargo_offer_to_available_cargos(self):
        self.truck_driver.add_cargo_offer("New York", 300)
        self.assertEqual(self.truck_driver.available_cargos, {"New York": 300})

    def test_add_cargo_offer_return(self):
        result = self.truck_driver.add_cargo_offer("New York", 300)
        self.assertEqual(result, "Cargo for 300 to New York was added as an offer.")

    def test_drive_best_cargo_offer_raises_value_error(self):
        result = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(result, "There are no offers available.")

    def test_drive_best_cargo_offer(self):
        self.truck_driver.add_cargo_offer("New York", 500)
        self.truck_driver.add_cargo_offer("Miami", 300)
        self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(self.truck_driver.earned_money, 1210)
        self.assertEqual(self.truck_driver.miles, 500)

    def test_drive_best_cargo_offer_return(self):
        self.truck_driver.add_cargo_offer("New York", 500)
        result = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(result, "John is driving 500 to New York.")

    def test_earned_money_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.truck_driver.earned_money = -100
        self.assertEqual(str(context.exception), "John went bankrupt.")

    def test_earned_money_setter_with_correct_value(self):
        self.truck_driver.earned_money = 500
        self.assertEqual(self.truck_driver.earned_money, 500)

    def test_check_for_activities_eat(self):
        self.truck_driver.earned_money = 100
        self.truck_driver.check_for_activities(250)
        self.assertEqual(self.truck_driver.earned_money, 80)

    def test_check_for_activities_sleep(self):
        self.truck_driver.earned_money = 1000
        self.truck_driver.check_for_activities(1000)
        self.assertEqual(self.truck_driver.earned_money, 875)

    def test_check_for_activities_pump_gas(self):
        self.truck_driver.earned_money = 1000
        self.truck_driver.check_for_activities(1500)
        self.assertEqual(self.truck_driver.earned_money, 335)

    def test_check_for_activities_repair_truck(self):
        self.truck_driver.earned_money = 100000
        self.truck_driver.check_for_activities(10000)
        self.assertEqual(self.truck_driver.earned_money, 88250)

    def test_check_for_activities_no_activities(self):
        self.truck_driver.check_for_activities(100)
        self.assertEqual(self.truck_driver.earned_money, 0)

    def test__repr__(self):
        self.truck_driver.miles = 100
        self.assertEqual(self.truck_driver.__repr__(), "John has 100 miles behind his back.")


if __name__ == '__main__':
    unittest.main()
