import unittest

from project.shopping_cart import ShoppingCart


class TestsShoppingCart(unittest.TestCase):
    def setUp(self) -> None:
        self.cart = ShoppingCart("Billa", 100)

    def test_initialize_shopping_cart(self):
        self.assertEqual("Billa", self.cart.shop_name)
        self.assertEqual(100, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_shop_name_with_lowercase_first_letter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "billa"

        expected = "Shop must contain only letters and must start with capital letter!"

        self.assertEqual(expected, str(ve.exception))

    def test_shop_name_with_name_containing_other_symbols_than_letters(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "Billa1"

        expected = "Shop must contain only letters and must start with capital letter!"

        self.assertEqual(expected, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "B*"

        expected = "Shop must contain only letters and must start with capital letter!"

        self.assertEqual(expected, str(ve.exception))

    def test_add_to_cart_product_price_greater_or_equal_to_100_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("bread", 100)

        self.assertEqual("Product bread cost too much!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("bread", 200)

        self.assertEqual("Product bread cost too much!", str(ve.exception))

    def test_add_to_cart_successful(self):
        result = self.cart.add_to_cart("bread", 2)

        self.assertEqual({"bread": 2}, self.cart.products)
        self.assertEqual("bread product was successfully added to the cart!", result)

    def test_remove_from_cart_successful(self):
        self.cart.products = {"bread": 2, "milk": 1.5}

        result = self.cart.remove_from_cart("bread")

        self.assertEqual({"milk": 1.5}, self.cart.products)
        self.assertEqual("Product bread was successfully removed from the cart!", result)

    def test_remove_from_cart_non_existing_product_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart("Bread")

        self.assertEqual("No product with name Bread in the cart!", str(ve.exception))

    def test__add__method(self):
        self.cart.products = {"bread": 2, "milk": 1.5}
        other_cart = ShoppingCart("Lidl", 200)
        other_cart.products = {"cheese": 2.5, "eggs": 3}

        resulting_cart = self.cart.__add__(other_cart)

        self.assertEqual("BillaLidl", resulting_cart.shop_name)
        self.assertEqual(300, resulting_cart.budget)
        self.assertEqual({"bread": 2, "milk": 1.5, "cheese": 2.5, "eggs": 3}, resulting_cart.products)


    def test_buy_products_total_sum_greater_than_budget_raises_value_error(self):
        self.cart.products = {"bread": 2, "milk": 1.5}
        self.cart.budget = 2

        self.assertEqual(3.5, sum(self.cart.products.values()))

        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()

        expected = "Not enough money to buy the products! Over budget with 1.50lv!"
        self.assertEqual(expected, str(ve.exception))

    def test_buy_products_successful(self):
        self.cart.products = {"bread": 2, "milk": 1.5}
        result = self.cart.buy_products()

        self.assertEqual("Products were successfully bought! Total cost: 3.50lv.", result)


if __name__ == "__main__":
    unittest.main()
