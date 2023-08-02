import unittest

from project.robot import Robot


class TestsRobot(unittest.TestCase):
    def setUp(self) -> None:
        self.robot = Robot("id1", "Military", 5, 100.5)
        self.other_robot = Robot("id2", "Military", 5, 50)

    def test_initialize_robot(self):
        self.assertEqual("id1", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(5, self.robot.available_capacity)
        self.assertEqual(100.5, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)
        self.assertEqual(['Military', 'Education', 'Entertainment', 'Humanoids'], Robot.ALLOWED_CATEGORIES)
        self.assertEqual(['Military', 'Education', 'Entertainment', 'Humanoids'], self.robot.ALLOWED_CATEGORIES)
        self.assertEqual(1.5, Robot.PRICE_INCREMENT)
        self.assertEqual(1.5, self.robot.PRICE_INCREMENT)

    def test_category_not_allowed_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "some"

        self.assertEqual(f"Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'", str(ve.exception))

    def test_price_negative_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1

        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_hardware_component_exists(self):
        self.robot.hardware_upgrades = ["some upgrade"]
        result = self.robot.upgrade("some upgrade", 10)
        self.assertEqual("Robot id1 was not upgraded.", result)

    def test_upgrade_successful(self):
        result = self.robot.upgrade("some upgrade", 10)
        self.assertEqual(["some upgrade"], self.robot.hardware_upgrades)
        self.assertEqual(115.5, self.robot.price)
        self.assertEqual("Robot id1 was upgraded with some upgrade.", result)

    def test_update_with_no_software_updates_and_valid_version_not_successful(self):
        self.assertEqual([], self.robot.software_updates)
        result = self.robot.update(5, 1)
        self.assertEqual("Robot id1 was not updated.", result)

    def test_update_with_software_updates_and_lower_version_not_successful(self):
        self.robot.software_updates.append(2.0)
        result = self.robot.update(1.0, 1)
        self.assertEqual("Robot id1 was not updated.", result)

    def test_update_with_software_updates_and_valid_version_and_not_enough_capacity_not_successful(self):
        self.robot.software_updates.append(2.0)

        result = self.robot.update(4.0, 10)

        self.assertTrue(self.robot.available_capacity < 10)
        self.assertEqual("Robot id1 was not updated.", result)

    def test_update_with_software_updates_and_valid_version_and_enough_capacity_successful(self):
        self.robot.software_updates.append(2.0)
        self.robot.software_updates.append(3.0)

        result = self.robot.update(4.0, 1)

        self.assertEqual([2.0, 3.0, 4.0], self.robot.software_updates)
        self.assertEqual(4, self.robot.available_capacity)
        self.assertEqual("Robot id1 was updated to version 4.0.", result)

    def test__gt__method_when_first_robot_price_greater(self):
        result = self.robot.__gt__(self.other_robot)
        self.assertTrue(self.robot.price > self.other_robot.price)
        self.assertEqual("Robot with ID id1 is more expensive than Robot with ID id2.", result)

    def test__gt__method_when_equal_robots_prices(self):
        self.robot.price = 50
        result = self.robot.__gt__(self.other_robot)
        self.assertTrue(self.robot.price == self.other_robot.price)
        self.assertEqual("Robot with ID id1 costs equal to Robot with ID id2.", result)

    def test__gt__method_when_other_robot_price_greater(self):
        self.robot.price = 10
        result = self.robot.__gt__(self.other_robot)
        self.assertTrue(self.robot.price < self.other_robot.price)
        self.assertEqual("Robot with ID id1 is cheaper than Robot with ID id2.", result)


if __name__ == "__main__":
    unittest.main()
