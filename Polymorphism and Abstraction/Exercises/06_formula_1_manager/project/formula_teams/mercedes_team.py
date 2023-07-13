from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    expenses_per_race = 200000

    def calculate_revenue_after_race(self, race_pos: int):
        if race_pos == 1:
            earned_money = 1000000 + 100000
        elif race_pos <= 3:
            earned_money = 500000 + 100000
        elif race_pos == 5:
            earned_money = 100000
        elif race_pos <= 7:
            earned_money = 50000
        else:
            earned_money = 0

        revenue = earned_money - MercedesTeam.expenses_per_race

        self.budget += revenue

        return f"The revenue after the race is { revenue }$. Current budget {self.budget}$"

# from typing import Dict
# from project.formula_teams.formula_team import FormulaTeam
#
#
# class MercedesTeam(FormulaTeam):
#
#     @property
#     def sponsors(self) -> Dict[str, Dict[int, int]]:
#         return {
#             "Petronas": {
#                 1: 1_000_000,
#                 3: 500_000,
#             },
#             "TeamViewer": {
#                 5: 100_000,
#                 7: 50_000,
#             },
#         }
#
#     @property
#     def expenses(self) -> int:
#         return 200_000