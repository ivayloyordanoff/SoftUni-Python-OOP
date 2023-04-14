import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("test name", "test type", "test sound")

    def test_constructor(self):
        self.assertEqual(self.mammal.name, "test name")
        self.assertEqual(self.mammal.type, "test type")
        self.assertEqual(self.mammal.sound, "test sound")

    def test_make_sound_return(self):
        self.assertEqual(self.mammal.make_sound(), "test name makes test sound")

    def test_get_kingdom_return(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_info_return(self):
        self.assertEqual(self.mammal.info(), "test name is of type test type")


if __name__ == "__main__":
    unittest.main()
