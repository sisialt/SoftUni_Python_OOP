import unittest

from project.library import Library


class TestsLibrary(unittest.TestCase):
    def setUp(self) -> None:
        self.library = Library("One")
        self.library_with_books = Library("Two")
        self.library_with_books.books_by_authors = {
            "A.A.": ["Title"],
            "B.B.": ["Title1", "Title2", "Title3"],
        }
        self.library_with_books.readers = {
            "Jo": [{"A.A.": "Title"}],
            "Lea": [{"B.B.": "Title2"}],
        }

    def test_initialize_library(self):
        self.assertEqual("One", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_empty_string_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ""

        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_book_non_existing_author_non_existing_title_successful(self):
        self.library.add_book("C.C.", "TitleC")

        self.assertEqual({"C.C.": ["TitleC"]}, self.library.books_by_authors)

    def test_add_book_existing_author_existing_title(self):
        self.library_with_books.add_book("B.B.", "Title2")

        expected = {
            "A.A.": ["Title"],
            "B.B.": ["Title1", "Title2", "Title3"]
        }

        self.assertEqual(expected, self.library_with_books.books_by_authors)

    def test_add_book_existing_author_non_existing_title_successful(self):
        self.library_with_books.add_book("B.B.", "Title4")

        expected = {
            "A.A.": ["Title"],
            "B.B.": ["Title1", "Title2", "Title3", "Title4"]
        }

        self.assertEqual(expected, self.library_with_books.books_by_authors)

    def test_add_reader_non_existing_reader_successful(self):
        self.library.add_reader("R")

        self.assertEqual({"R": []}, self.library.readers)

    def test_add_reader_existing_reader(self):
        result = self.library_with_books.add_reader("Jo")

        expected = {
            "Jo": [{"A.A.": "Title"}],
            "Lea": [{"B.B.": "Title2"}],
        }

        self.assertEqual(expected, self.library_with_books.readers)
        self.assertEqual("Jo is already registered in the Two library.", result)

    def test_rent_book_non_existing_reader(self):
        result = self.library.rent_book("S", "S.S.", "TitleS")

        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)
        self.assertEqual("S is not registered in the One Library.", result)

    def test_rent_book_non_existing_author(self):
        result = self.library_with_books.rent_book("Jo", "Q.Q.", "TitleQ")

        self.assertEqual({
            "A.A.": ["Title"],
            "B.B.": ["Title1", "Title2", "Title3"],
        }, self.library_with_books.books_by_authors)

        self.assertEqual({
            "Jo": [{"A.A.": "Title"}],
            "Lea": [{"B.B.": "Title2"}],
        }, self.library_with_books.readers)

        self.assertEqual("Two Library does not have any Q.Q.'s books.", result)

    def test_rent_book_non_existing_title(self):
        result = self.library_with_books.rent_book("Jo", "A.A.", "Title100")
        self.assertEqual({
            "A.A.": ["Title"],
            "B.B.": ["Title1", "Title2", "Title3"],
        }, self.library_with_books.books_by_authors)

        self.assertEqual({
            "Jo": [{"A.A.": "Title"}],
            "Lea": [{"B.B.": "Title2"}],
        }, self.library_with_books.readers)
        self.assertEqual("""Two Library does not have A.A.'s "Title100".""", result)

    def test_rent_book_successful(self):
        result = self.library_with_books.rent_book("Jo", "B.B.", "Title3")

        expected = [{"A.A.": "Title"}, {"B.B.": "Title3"}]

        self.assertEqual(["Title1", "Title2"], self.library_with_books.books_by_authors["B.B."])
        self.assertEqual(expected, self.library_with_books.readers["Jo"])
        #self.assertEqual(None, result)


if __name__ == "__main__":
    unittest.main()
