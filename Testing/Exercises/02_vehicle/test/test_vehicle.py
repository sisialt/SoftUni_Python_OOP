import unittest

from project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.my_vehicle = Vehicle(50.0, 100.0)

    def test_initialize_vehicle(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)
        self.assertEqual(1.25, self.my_vehicle.DEFAULT_FUEL_CONSUMPTION)
        self.assertEqual(50.0, self.my_vehicle.fuel)
        self.assertEqual(50.0, self.my_vehicle.capacity)
        self.assertEqual(100.0, self.my_vehicle.horse_power)
        self.assertEqual(1.25, self.my_vehicle.fuel_consumption)

    def test_drive_with_enough_fuel(self):
        self.my_vehicle.drive(10)
        expected_needed_fuel = self.my_vehicle.fuel_consumption * 10
        self.assertEqual(50.0 - expected_needed_fuel, self.my_vehicle.fuel)

    def test_drive_with_not_enough_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.my_vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))
        self.assertEqual(50.0, self.my_vehicle.fuel)

    def test_refuel_with_valid_fuel(self):
        self.my_vehicle.drive(20)
        expected_added_fuel = 10
        expected_fuel_in_vehicle = self.my_vehicle.fuel + expected_added_fuel

        self.my_vehicle.refuel(10)

        self.assertEqual(expected_fuel_in_vehicle, self.my_vehicle.fuel)

    def test_refuel_with_invalid_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.my_vehicle.refuel(10)

        self.assertEqual("Too much fuel", str(ex.exception))
        self.assertEqual(50.0, self.my_vehicle.fuel)

    def test_str(self):
        self.assertEqual(
            "The vehicle has 100.0 horse power with 50.0 fuel left and 1.25 fuel consumption",
            str(self.my_vehicle))


if __name__ == "__main__":
    unittest.main()
