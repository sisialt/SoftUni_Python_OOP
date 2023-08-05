import unittest

from project.team import Team


class TestsTeam(unittest.TestCase):
    def setUp(self) -> None:
        self.team = Team("One")
        self.team_with_members = Team("Two")
        self.team_with_members.members = {"Peter": 30, "Lena": 20}

    def test_initialize_team(self):
        self.assertEqual("One", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_with_other_symbols_than_letters_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "rbveb1"

        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.team.name = "*2a"

        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_add_member_one_member_to_add(self):
        result = self.team.add_member(Peter=30)

        self.assertEqual("Successfully added: Peter", result)
        self.assertEqual(30, self.team.members["Peter"])

    def test_add_member_more_members_to_add(self):
        self.team.members = {"Joe": 40}
        result = self.team.add_member(Peter=30, Tina=25, Kati=20, Joe=20)

        self.assertEqual("Successfully added: Peter, Tina, Kati", result)
        self.assertEqual(30, self.team.members["Peter"])
        self.assertEqual({"Joe": 40, "Peter": 30, "Tina": 25, "Kati": 20}, self.team.members)

    def test_remove_member_successful(self):
        result = self.team_with_members.remove_member("Peter")

        self.assertEqual({"Lena": 20}, self.team_with_members.members)
        self.assertEqual("Member Peter removed", result)

    def test_remove_member_non_existing_member(self):
        result = self.team_with_members.remove_member("Jo")

        self.assertEqual("Member with name Jo does not exist", result)
        self.assertEqual({"Peter": 30, "Lena": 20}, self.team_with_members.members)

    def test__gt__method(self):
        result = self.team.__gt__(self.team_with_members)
        result2 = self.team_with_members.__gt__(self.team)
        self.assertEqual(False, result)  # missing
        self.assertEqual(True, result2)  # missing
        # self.assertFalse(result)
        # self.assertTrue(result2)

    def test__len__method(self):
        result = self.team_with_members.__len__()  # missing
        self.assertEqual(0, len(self.team.members))
        self.assertEqual(2, result)  # missing

    def test__add__method(self):
        result = self.team.__add__(self.team_with_members)

        self.assertEqual({"Peter": 30, "Lena": 20}, result.members)
        self.assertEqual("OneTwo", result.name)

        self.team.add_member(Lea=10)
        result = self.team.__add__(self.team_with_members)

        self.assertEqual({"Lea": 10, "Peter": 30, "Lena": 20}, result.members)

    def test__str__method(self):
        result = self.team_with_members.__str__()
        expected = ("Team name: Two\n"
                    "Member: Peter - 30-years old\n"
                    "Member: Lena - 20-years old")

        self.assertEqual(expected, result)

        self.team_with_members.add_member(Lea=30)

        result = self.team_with_members.__str__()
        expected = ("Team name: Two\n"
                    "Member: Lea - 30-years old\n"
                    "Member: Peter - 30-years old\n"
                    "Member: Lena - 20-years old")

        self.assertEqual(expected, result)

    def test__str__method_empty_members(self):
        result = self.team.__str__()
        expected = "Team name: One"

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
