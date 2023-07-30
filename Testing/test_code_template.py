import unittest

from project.name import Name


class NameTests(unittest.TestCase):
    def setUp(self) -> None:
        self.my_name = Name(0)

    def test_initialize_name(self):
        pass


if __name__ == "__main__":
    unittest.main()
