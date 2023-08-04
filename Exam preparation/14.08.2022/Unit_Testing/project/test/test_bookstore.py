import unittest

from project.bookstore import Bookstore


class TestsBookstore(unittest.TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(100)
        self.bookstore_with_books = Bookstore(200)
        self.bookstore_with_books.availability_in_store_by_book_titles = {
            "book1": 10,
            "book2": 1,
            "book3": 5,
        }

    def test_initialize_bookstore(self):
        self.assertEqual(100, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore._Bookstore__total_sold_books)

    def test_total_sold_books(self):
        self.assertEqual(0, self.bookstore.total_sold_books)

        self.bookstore._Bookstore__total_sold_books = 10
        self.assertEqual(10, self.bookstore.total_sold_books)

    def test_books_limit_lower_or_equal_to_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0

        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = -10

        self.assertEqual("Books limit of -10 is not valid", str(ve.exception))

    def test__len__method(self):
        self.assertEqual(16, self.bookstore_with_books.__len__())
        self.assertEqual(0, self.bookstore.__len__())

    def test_receive_book_no_more_space_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("book", 101)

        self.assertTrue(101 > self.bookstore.books_limit)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_non_existing_book_successful(self):
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.__len__())
        result = self.bookstore.receive_book("book", 10)
        expected = "10 copies of book are available in the bookstore."

        self.assertEqual(10, self.bookstore.availability_in_store_by_book_titles["book"])
        self.assertEqual(expected, result)

    def test_receive_book_existing_book_successful_update(self):
        self.bookstore.receive_book("book", 10)
        #self.assertEqual(10, self.bookstore.availability_in_store_by_book_titles["book"])

        result = self.bookstore.receive_book("book", 10)
        expected = "20 copies of book are available in the bookstore."

        #self.assertEqual(20, len(self.bookstore))
        self.assertEqual(20, self.bookstore.availability_in_store_by_book_titles["book"])
        self.assertEqual(expected, result)

    def test_sell_book_non_existing_book_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("book", 10)

        self.assertEqual("Book book doesn't exist!", str(ex.exception))

    def test_sell_book_with_not_enough_copies_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore_with_books.sell_book("book1", 50)

        self.assertEqual(10, self.bookstore_with_books.availability_in_store_by_book_titles["book1"])
        self.assertEqual("book1 has not enough copies to sell. Left: 10", str(ex.exception))

    def test_sell_book_successful(self):
        result = self.bookstore_with_books.sell_book("book1", 1)

        self.assertEqual(1, self.bookstore_with_books.total_sold_books)
        self.assertEqual("Sold 1 copies of book1", result)
        self.assertEqual(9, self.bookstore_with_books.availability_in_store_by_book_titles["book1"])
        #self.assertEqual(15, len(self.bookstore_with_books))

        result2 = self.bookstore_with_books.sell_book("book1", 2)
        #self.assertEqual("Sold 2 copies of book1", result2)
        self.assertEqual(3, self.bookstore_with_books.total_sold_books)
        self.assertEqual(7, self.bookstore_with_books.availability_in_store_by_book_titles["book1"])


    def test__str__method(self):
        self.bookstore_with_books.sell_book("book1", 2)
        result = self.bookstore_with_books.__str__()
        expected = ("Total sold books: 2\n"
                    "Current availability: 14\n"
                    " - book1: 8 copies\n"
                    " - book2: 1 copies\n"
                    " - book3: 5 copies")

        self.assertEqual(expected, result)

# this test was missing!
        self.bookstore.receive_book("book", 1)
        self.bookstore.sell_book("book", 1)

        result2 = self.bookstore.__str__()
        expected2 = ("Total sold books: 1\n"
                     "Current availability: 0\n"
                     " - book: 0 copies")

        self.assertEqual(expected2, result2)

if __name__ == "__main__":
    unittest.main()
