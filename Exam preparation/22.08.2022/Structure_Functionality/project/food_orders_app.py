from typing import List

from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    VALID_MEAL_TYPES = {"Starter": Starter, "MainDish": MainDish, "Dessert": Dessert}
    receipt_id = 0

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def __find_client_by_phone_number(self, number):
        c = [c for c in self.clients_list if c.phone_number == number]
        if c:
            return c[0]

    def __is_menu_ready(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def register_client(self, client_phone_number: str):
        client = self.__find_client_by_phone_number(client_phone_number)
        if client:
            raise Exception("The client has already been registered!")

        client = Client(client_phone_number)
        self.clients_list.append(client)

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):  # marker
        for m in meals:
            if m.__class__.__name__ in self.VALID_MEAL_TYPES:
                self.menu.append(m)

    def show_menu(self):
        self.__is_menu_ready()

        return "\n".join([m.details() for m in self.menu])

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        self.__is_menu_ready()

        client = self.__find_client_by_phone_number(client_phone_number)
        if not client:
            self.register_client(client_phone_number)

        meals_to_order = []
        bill = 0

        for meal_name, quantity in meal_names_and_quantities.items():
            meal_with_same_name = [m for m in self.menu if m.name == meal_name]

            if not meal_with_same_name:
                raise Exception(f"{meal_name} is not on the menu!")

            meal = meal_with_same_name[0]

            if meal.quantity < quantity:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!") # it was m.__class__.__name__

            new_order = FoodOrdersApp.VALID_MEAL_TYPES[meal.__class__.__name__](meal_name, meal.price, quantity)
            meals_to_order.append(new_order)
            bill += meal.price * quantity

        client.shopping_cart.extend(meals_to_order)
        client.bill += bill

        for meal in client.shopping_cart:
            meal_in_menu = [m for m in self.menu if m.name == meal.name][0]
            meal_in_menu.quantity -= meal.quantity

        return (f"Client {client_phone_number} successfully ordered "
                    f"{', '.join([m.name for m in client.shopping_cart])} "
                    f"for {client.bill:.2f}lv.")

    def cancel_order(self, client_phone_number: str):
        client = self.__find_client_by_phone_number(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal in client.shopping_cart:
            meal_in_menu = [m for m in self.menu if meal.name == m.name][0]
            meal_in_menu.quantity += meal.quantity

        client.shopping_cart = []
        client.bill = 0

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__find_client_by_phone_number(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        total_paid_money = client.bill

        client.shopping_cart = []
        client.bill = 0
        FoodOrdersApp.receipt_id += 1

        return (f"Receipt #{FoodOrdersApp.receipt_id} "
                f"with total amount of {total_paid_money:.2f} "
                f"was successfully paid for {client_phone_number}.")

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."