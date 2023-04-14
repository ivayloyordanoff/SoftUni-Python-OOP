from project.toy_store import ToyStore
import unittest


class TestToyStore(unittest.TestCase):

    def setUp(self):
        self.store = ToyStore()

    def test_add_toy_success(self):
        result = self.store.add_toy("A", "Barbie")
        self.assertEqual(result, "Toy:Barbie placed successfully!")
        self.assertEqual(self.store.toy_shelf["A"], "Barbie")

    def test_add_toy_already_in_shelf(self):
        self.store.add_toy("A", "Barbie")
        with self.assertRaises(Exception) as context:
            self.store.add_toy("A", "Barbie")
        self.assertEqual(str(context.exception), "Toy is already in shelf!")

    def test_add_toy_shelf_already_taken(self):
        self.store.add_toy("A", "Barbie")
        with self.assertRaises(Exception) as context:
            self.store.add_toy("A", "Hot Wheels")
        self.assertEqual(str(context.exception), "Shelf is already taken!")

    def test_add_toy_invalid_shelf(self):
        with self.assertRaises(Exception) as context:
            self.store.add_toy("H", "Barbie")
        self.assertEqual(str(context.exception), "Shelf doesn't exist!")

    def test_remove_toy_success(self):
        self.store.add_toy("A", "Barbie")
        result = self.store.remove_toy("A", "Barbie")
        self.assertEqual(result, "Remove toy:Barbie successfully!")
        self.assertIsNone(self.store.toy_shelf["A"])

    def test_remove_toy_invalid_toy(self):
        self.store.add_toy("A", "Barbie")
        with self.assertRaises(Exception) as context:
            self.store.remove_toy("A", "Hot Wheels")
        self.assertEqual(str(context.exception), "Toy in that shelf doesn't exists!")

    def test_remove_toy_invalid_shelf(self):
        with self.assertRaises(Exception) as context:
            self.store.remove_toy("H", "Barbie")
        self.assertEqual(str(context.exception), "Shelf doesn't exist!")


if __name__ == '__main__':
    unittest.main()
