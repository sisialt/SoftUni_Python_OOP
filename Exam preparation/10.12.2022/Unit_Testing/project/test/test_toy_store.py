import unittest

from project.toy_store import ToyStore


class TestsToyStore(unittest.TestCase):
    def setUp(self) -> None:
        self.shelf = ToyStore()

    def test_initialize_toy_store(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.shelf.toy_shelf)

    def test_add_toy_on_non_existing_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.shelf.add_toy("a", "toy1")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_with_existing_toy_raises_exception(self):
        self.shelf.toy_shelf["A"] = "toy1"

        with self.assertRaises(Exception) as ex:
            self.shelf.add_toy("A", "toy1")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_when_shelf_is_taken_raises_exception(self):
        self.shelf.toy_shelf["A"] = "toy1"

        with self.assertRaises(Exception) as ex:
            self.shelf.add_toy("A", "toy2")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_successful(self):
        result = self.shelf.add_toy("A", "toy1")

        expected = {"A": "toy1",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,}

        self.assertEqual(expected, self.shelf.toy_shelf)
        self.assertEqual("Toy:toy1 placed successfully!", result)

    def test_remove_toy_from_non_existing_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.shelf.remove_toy("a", "toy1")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_non_existing_toy(self):
        with self.assertRaises(Exception) as ex:
            self.shelf.remove_toy("A", "toy1")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

        self.shelf.toy_shelf["A"] = "toy2"
        with self.assertRaises(Exception) as ex:
            self.shelf.remove_toy("A", "toy1")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_successful(self):
        self.shelf.add_toy("A", "toy1")

        result = self.shelf.remove_toy("A", "toy1")

        expected = {"A": None,
                    "B": None,
                    "C": None,
                    "D": None,
                    "E": None,
                    "F": None,
                    "G": None, }

        self.assertEqual(expected, self.shelf.toy_shelf)
        self.assertEqual("Remove toy:toy1 successfully!", result)

if __name__ == "__main__":
    unittest.main()
