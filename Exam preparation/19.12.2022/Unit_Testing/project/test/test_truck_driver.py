import unittest

from project.truck_driver import TruckDriver


class TestsTruckDriver(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver("Peter", 10.5)

    def test_initialize_truck_driver(self):
        self.assertEqual("Peter", self.driver.name)
        self.assertEqual(10.5, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_negative_money_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1

        self.assertEqual("Peter went bankrupt.", str(ve.exception))

    def test_add_cargo_offer_when_offer_already_exists_raises_exception(self):
        self.driver.available_cargos = {"sofia": 10}

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("sofia", 10)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer_successful(self):
        result = self.driver.add_cargo_offer("sofia", 10)

        self.assertEqual({"sofia": 10}, self.driver.available_cargos)  # forgot
        self.assertEqual("Cargo for 10 to sofia was added as an offer.", result)

    def test_drive_best_cargo_offer_with_empty_cargos_return_value_error(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_drive_best_cargo_offer_successful(self):
        self.driver.available_cargos = {"sofia": 10, "varna": 500}
        result = self.driver.drive_best_cargo_offer()

        # self.assertEqual(525, self.driver.earned_money)
        self.assertEqual(500, self.driver.miles)

        self.assertEqual(5210, self.driver.earned_money)
        self.assertEqual("Peter is driving 500 to varna.", result)

    def test_check_for_activities(self):
        self.driver.earned_money = 10000
        self.driver.check_for_activities(5000)

        self.assertEqual(7875, self.driver.earned_money)

    def test_eat_when_mile_divisible_by_250(self):
        self.driver.earned_money = 100
        self.driver.eat(500)

        self.assertEqual(80, self.driver.earned_money)

    def test_eat_when_mile_not_divisible_by_250(self):
        self.driver.earned_money = 100
        self.driver.eat(400)

        self.assertEqual(100, self.driver.earned_money)

    def test_sleep_when_mile_divisible_by_1000(self):
        self.driver.earned_money = 100
        self.driver.sleep(2000)

        self.assertEqual(55, self.driver.earned_money)

    def test_sleep_with_mile_non_divisible_by_1000(self):
        self.driver.earned_money = 100
        self.driver.sleep(1500)

        self.assertEqual(100, self.driver.earned_money)

    def test_pump_gas_when_mile_divisible_by_1500(self):
        self.driver.earned_money = 1000
        self.driver.pump_gas(3000)

        self.assertEqual(500, self.driver.earned_money)

    def test_pump_gas_when_mile_non_divisible_by_1500(self):
        self.driver.earned_money = 1000
        self.driver.pump_gas(2000)

        self.assertEqual(1000, self.driver.earned_money)

    def test_repair_truck_when_mile_divisible_by_10000(self):
        self.driver.earned_money = 10000
        self.driver.repair_truck(20000)

        self.assertEqual(2500, self.driver.earned_money)

    def test_repair_truck_when_mile_non_divisible_by_10000(self):
        self.driver.earned_money = 10000
        self.driver.repair_truck(1000)

        self.assertEqual(10000, self.driver.earned_money)

    def test___repr__(self):
        self.driver.miles = 100

        self.assertEqual("Peter has 100 miles behind his back.", self.driver.__repr__())

if __name__ == "__main__":
    unittest.main()
