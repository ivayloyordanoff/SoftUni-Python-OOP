class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class TestIntegerList(unittest.TestCase):
    def setUp(self) -> None:
        self.integer_list = IntegerList(1, 2, 3, "4", 4.5, "test")

    def test_constructor(self):
        self.assertEqual(self.integer_list.get_data(), [1, 2, 3])

    def test_add_an_element(self):
        self.assertEqual(self.integer_list.add(4), [1, 2, 3, 4])

    def test_add_error(self):
        with self.assertRaises(ValueError) as context:
            self.integer_list.add("4")
        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_remove_index_return(self):
        self.assertEqual(self.integer_list.remove_index(2), 3)

    def test_remove_index_error(self):
        with self.assertRaises(IndexError) as context:
            self.integer_list.remove_index(5)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_get_return(self):
        self.assertEqual(self.integer_list.get(0), 1)

    def test_get_index_error(self):
        with self.assertRaises(IndexError) as context:
            self.integer_list.get(10)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_insert_valid_index(self):
        self.integer_list.insert(1, 2)
        self.assertEqual(self.integer_list.get_data(), [1, 2, 2, 3])

    def test_insert_index_error(self):
        with self.assertRaises(IndexError) as context:
            self.integer_list.insert(10, 2)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_insert_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.integer_list.insert(0, "test")
        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_get_biggest(self):
        self.assertEqual(self.integer_list.get_biggest(), 3)

    def test_get_index(self):
        self.assertEqual(self.integer_list.get_index(1), 0)


if __name__ == "__main__":
    unittest.main()
