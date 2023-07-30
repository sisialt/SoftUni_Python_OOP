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


class IntegerListTests(unittest.TestCase):
    def setUp(self) -> None:
        self.int_list = IntegerList(1, 2)

    def test_init_list_with_integers(self):
        int_list = IntegerList(1, 2)
        self.assertEqual(2, len(int_list.get_data()))
        self.assertEqual(2, len(int_list._IntegerList__data))

    def test_init_list_with_not_all_integers(self):
        int_list = IntegerList(1, 2.6, "a", {}, [])
        self.assertEqual(1, len(int_list.get_data()))
        self.assertEqual([1], int_list.get_data())

    def test_get_data(self):
        self.assertEqual([1, 2], self.int_list.get_data())

    def test_add_integer_element(self):
        self.int_list.add(3)
        self.assertEqual([1, 2, 3], self.int_list.get_data())

    def test_add_not_integer_element_raises(self):
        for el in [3.5, {}, [], "a"]:

            with self.assertRaises(ValueError) as ex:
                self.int_list.add(el)

            self.assertEqual("Element is not Integer", str(ex.exception))

        self.assertEqual([1, 2], self.int_list.get_data())

    def test_remove_index_valid_index(self):
        removed_element = self.int_list.remove_index(0)
        self.assertEqual([2], self.int_list.get_data())
        self.assertEqual(1, removed_element)

    def test_remove_index_invalid_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.int_list.remove_index(3)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual(2, len(self.int_list.get_data()))

    def test_get_valid_index(self):
        self.assertEqual(1, self.int_list.get(0))

    def test_get_invalid_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.int_list.get(2)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([1, 2], self.int_list.get_data())

    def test_insert_integer_on_valid_index(self):
        self.int_list.insert(0, 0)

        self.assertEqual([0, 1, 2], self.int_list.get_data())

    def test_insert_integer_on_invalid_index_raises(self):
        with self.assertRaises(IndexError) as ex:
            self.int_list.insert(2, 0)

        self.assertEqual("Index is out of range", str(ex.exception))

        self.assertEqual([1, 2], self.int_list.get_data())

    def test_insert_not_integer_on_valid_index_raises(self):
        for el in [2.0, "a", {}, []]:
            with self.assertRaises(ValueError) as ex:
                self.int_list.insert(0, el)

            self.assertEqual("Element is not Integer", str(ex.exception))

        self.assertEqual([1, 2], self.int_list.get_data())

    def test_get_biggest(self):
        self.int_list = IntegerList(2, 80, 6, -9, 75)
        biggest_num = self.int_list.get_biggest()

        self.assertEqual(80, biggest_num)

    def test_get_index(self):
        self.assertEqual(0, self.int_list.get_index(1))


if __name__ == "__main__":
    unittest.main()

