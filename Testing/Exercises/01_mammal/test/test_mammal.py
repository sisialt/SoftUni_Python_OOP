import unittest

from project.mammal import Mammal


class MammalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Mam", "type", "some sound")

    def test_initialize_mammal(self):
        mammal = Mammal("Mam", "type", "some sound")

        self.assertEqual("Mam", mammal.name)
        self.assertEqual("type", mammal.type)
        self.assertEqual("some sound", mammal.sound)
        self.assertEqual("animals", mammal.get_kingdom())
        self.assertEqual("animals", mammal._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual("Mam makes some sound", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual("Mam is of type type", self.mammal.info())


if __name__ == "__main__":
    unittest.main()

# from project.mammal import Mammal was missing
