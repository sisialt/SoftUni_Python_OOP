from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    expenses_per_race = 250000

    def __init__(self, budget: int):
        super().__init__(budget)
        # self.earned_money = 0

    # @property
    # def earned_money(self):
    #     return self.__earned_money
    #
    # @earned_money.setter
    # def earned_money(self, value):
    #     if value == 1:
    #         self.__earned_money = 1500000
    #     elif value == 2:
    #         self.__earned_money = 800000
    #     elif value == 8:
    #         self.__earned_money = 20000
    #     elif value == 10:
    #         self.__earned_money = 10000

    def calculate_revenue_after_race(self, race_pos: int):
        if race_pos == 1:
            earned_money = 1500000 + 20000
        elif race_pos == 2:
            earned_money = 800000 + 20000
        elif race_pos == 8:
            earned_money = 20000
        elif race_pos <= 10:
            earned_money = 10000
        else:
            earned_money = 0

        revenue = earned_money - RedBullTeam.expenses_per_race

        self.budget += revenue

        return f"The revenue after the race is { revenue }$. Current budget {self.budget}$"

# from typing import Dict
# from project.formula_teams.formula_team import FormulaTeam
#
#
# class RedBullTeam(FormulaTeam):
#
#     @property
#     def sponsors(self) -> Dict[str, Dict[int, int]]:
#         return {
#             "Oracle": {
#                 1: 1_500_000,
#                 2: 800_000,
#             },
#             "Honda": {
#                 8: 20_000,
#                 10: 10_000,
#             },
#         }
#
#     @property
#     def expenses(self) -> int:
#         return 250_000