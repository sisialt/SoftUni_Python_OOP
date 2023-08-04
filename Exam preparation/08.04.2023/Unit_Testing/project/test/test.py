import unittest

from project.tennis_player import TennisPlayer


class TestsTennisPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer("Test", 30, 50.5)
        self.other_player = TennisPlayer("Test2", 20, 100)

    def test_initialize_player(self):
        self.assertEqual("Test", self.player.name)
        self.assertEqual(30, self.player.age)
        self.assertEqual(50.5, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name_less_or_equal_to_2_symbols_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "T"

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.player.name = "Te"

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_under_18_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 10

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_non_existing_tournament_name_successful(self):
        self.assertEqual([], self.player.wins)
        self.player.add_new_win("T1")
        self.assertEqual(["T1"], self.player.wins)

    def test_add_new_win_existing_tournament_name_not_successful(self):
        self.player.wins = ["T1"]
        self.assertEqual(["T1"], self.player.wins)

        result = self.player.add_new_win("T1")
        expected = "T1 has been already added to the list of wins!"

        self.assertEqual(expected, result)
        self.assertEqual(["T1"], self.player.wins)

    def test__lt__method_when_first_points_less_than_other_points(self):
        result = self.player.__lt__(self.other_player)
        expected = "Test2 is a top seeded player and he/she is better than Test"

        self.assertEqual(expected, result)

    def test__lt__method_when_first_points_greater_or_equal_to_other_points(self):
        self.other_player.points = 50.5

        result = self.player.__lt__(self.other_player)
        expected = "Test is a better player than Test2"

        self.assertEqual(expected, result)

        self.other_player.points = 10

        result = self.player.__lt__(self.other_player)
        expected = "Test is a better player than Test2"

        self.assertEqual(expected, result)

    def test__str__method(self):
        self.player.points = 50.5684
        self.player.wins = ["T1", "T2", "T3"]

        result = self.player.__str__()
        expected = f"Tennis Player: Test\n" \
               f"Age: 30\n" \
               f"Points: 50.6\n" \
               f"Tournaments won: T1, T2, T3"

        self.assertEqual(expected, result)

        self.player.points = 50
        self.player.wins = []

        result = self.player.__str__()
        expected = f"Tennis Player: Test\n" \
                   f"Age: 30\n" \
                   f"Points: 50.0\n" \
                   f"Tournaments won: "

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()