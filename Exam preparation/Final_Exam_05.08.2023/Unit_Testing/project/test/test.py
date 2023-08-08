import unittest

from project.second_hand_car import SecondHandCar


class TestsSecondHandCar(unittest.TestCase):
    def setUp(self) -> None:
        self.car = SecondHandCar("BMW", "F11", 150000, 20000)

    def test_initialize_car(self):
        self.assertEqual("BMW", self.car.model)
        self.assertEqual("F11", self.car.car_type)
        self.assertEqual(150000, self.car.mileage)
        self.assertEqual(20000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_equal_to_1_raises_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1.0

        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

    def test_price_negative_raises_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = -1

        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

    def test_mileage_equal_to_100_raises_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100

        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ve.exception))

    def test_mileage_less_than_100_raises_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 0

        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ve.exception))

    def test_set_promotional_price_new_price_equal_raises_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(20000)

        self.assertEqual("You are supposed to decrease the price!", str(ve.exception))

    def test_set_promotional_price_new_price_greater_raises_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(25000)

        self.assertEqual("You are supposed to decrease the price!", str(ve.exception))

    def test_set_promotional_price_successful(self):
        result = self.car.set_promotional_price(19000)

        self.assertEqual(19000, self.car.price)
        self.assertEqual("The promotional price has been successfully set.", result)

    def test_need_repair_when_repair_price_greater_than_cars_price(self):
        result = self.car.need_repair(21000, "engine replacement")

        self.assertEqual("Repair is impossible!", result)
        self.assertEqual(20000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_need_repair_successful(self):
        result = self.car.need_repair(5000, "engine replacement")

        self.assertEqual("Price has been increased due to repair charges.", result)
        self.assertEqual(25000, self.car.price)
        self.assertEqual(["engine replacement"], self.car.repairs)

    def test__gt__method_cars_not_same_type_not_successful(self):
        other_car = SecondHandCar("BMW", "F10", 200000, 15000)

        result = self.car.__gt__(other_car)

        self.assertEqual("Cars cannot be compared. Type mismatch!", result)

    def test__gt__method_successful(self):
        other_car = SecondHandCar("BMW", "F11", 200000, 15000)

        result = self.car.__gt__(other_car)
        expected = self.car.price > other_car.price

        self.assertEqual(expected, result)

        result2 = other_car.__gt__(self.car)
        expected2 = other_car.price > self.car.price

        self.assertEqual(expected2, result2)

    def test__str__method(self):
        result = self.car.__str__()
        expected = f"""Model BMW | Type F11 | Milage 150000km
Current price: 20000.00 | Number of Repairs: 0"""

        self.assertEqual(expected, result)

        self.car.repairs = ["repair1", "repair2"]
        result2 = self.car.__str__()
        expected2 = f"""Model BMW | Type F11 | Milage 150000km
Current price: 20000.00 | Number of Repairs: 2"""

        self.assertEqual(expected2, result2)


if __name__ == "__main__":
    unittest.main()

