import unittest

from project.plantation import Plantation


class TestsPlantation(unittest.TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(100)

    def test_initialize_plantation(self):
        self.assertEqual(100, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_negative_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1

        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_who_is_already_hired_raises_value_error(self):
        self.plantation.hire_worker("John")

        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("John")

        self.assertEqual("Worker already hired!", str(ve.exception))
        # self.assertEqual(1, len(self.plantation.workers))

    def test_hire_worker_successful(self):
        result = self.plantation.hire_worker("John")
        self.assertEqual(["John"], self.plantation.workers)  # forgot
        self.assertEqual(f"John successfully hired.", result)

    def test__len__method(self):
        result = self.plantation.__len__()
        self.assertEqual(0, result)

        self.plantation.plants = {"worker": ["plant"], "worker2": ["plant2"]}

        result2 = self.plantation.__len__()
        self.assertEqual(2, result2)

    def test_planting_non_existing_worker_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("John", "plant")

        self.assertEqual(f"Worker with name John is not hired!", str(ve.exception))

    def test_planting_plantation_full_raises_value_error(self):
        self.plantation.size = 4
        self.plantation.workers = ["John", "Peter"]
        self.plantation.plants = {"John": ["plant", "plant2"], "Peter": ["p1", "p2"]}

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("John", "plant3")

        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_with_existing_worker(self):
        self.plantation.workers = ["John"]
        self.plantation.plants = {"John": ["plant"]}
        result = self.plantation.planting("John", "plant2")

        self.assertEqual({"John": ["plant", "plant2"]}, self.plantation.plants)  # forgot
        self.assertEqual(f"John planted plant2.", result)

    def test_planting_with_non_existing_worker(self):
        self.plantation.workers = ["John"]
        result = self.plantation.planting("John", "plant")

        self.assertEqual({"John": ["plant"]}, self.plantation.plants)  # forgot
        self.assertEqual(f"John planted it's first plant.", result)

    def test__str__method(self):
        self.plantation.workers = ["John", "Peter"]
        self.plantation.plants = {"John": ["plant", "plant2"], "Peter": ["p1"]}

        expected = (f"Plantation size: 100\n"
                    f"John, Peter\n"
                    f"John planted: plant, plant2\n"
                    f"Peter planted: p1")

        self.assertEqual(expected, str(self.plantation))

    def test__repr__method(self):
        self.plantation.workers = ["John", "Peter"]

        expected = ("Size: 100\n"
                    "Workers: John, Peter")

        self.assertEqual(expected, self.plantation.__repr__())


if __name__ == "__main__":
    unittest.main()
