from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players: list[Player] = []
        self.supplies: list[Supply] = []

    def add_player(self, *args):
        result = []
        for player in args:
            if player not in self.players:
                self.players.append(player)
                result.append(player.name)

        return f"Successfully added: {', '.join(result)}"

    def add_supply(self, *args):
        self.supplies.extend([s for s in args])

    def sustain(self, player_name: str, sustenance_type: str):
        valid_sustenance_types = ["Drink", "Food"]
        if sustenance_type not in valid_sustenance_types:
            return

        try:
            player = [p for p in self.players if p.name == player_name][0]
        except IndexError:
            return

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        supplies = [[i, s] for i, s in enumerate(self.supplies) if s.__class__.__name__ == sustenance_type]
        if not supplies:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")
        supply = supplies[-1]

        player.stamina = min(100, player.stamina + supply[1].energy)

        self.supplies.pop(supply[0])

        return f"{player_name} sustained successfully with {supply[1].name}."

    # @staticmethod
    # def start_attack(first_attacker, second_attacker):
    #     second_attacker.stamina -= first_attacker.stamina / 2
    #
    #     if second_attacker.stamina <= 0:
    #         second_attacker.stamina = 0
    #         return first_attacker.name

    def duel(self, first_player_name: str, second_player_name: str):
        result = []

        first_player = [p for p in self.players if p.name == first_player_name][0]
        second_player = [p for p in self.players if p.name == second_player_name][0]

        for p in [first_player, second_player]:
            if p.stamina <= 0:
                result.append(f"Player {p.name} does not have enough stamina.")

        if result:
            return '\n'.join(result)

        sorted_players = sorted([
            next(filter(lambda p: p.name == first_player_name, self.players)),
            next(filter(lambda p: p.name == second_player_name, self.players)),
        ], key=lambda p: p.stamina)

        first_player_damage = sorted_players[0].stamina / 2
        sorted_players[1].stamina = max(sorted_players[1].stamina - first_player_damage, 0)

        second_player_damage = sorted_players[1].stamina / 2
        sorted_players[0].stamina = max(sorted_players[0].stamina - second_player_damage, 0)

        winner = sorted(sorted_players, key=lambda p: -p.stamina)[0]

        return f"Winner: {winner.name}"

        # if first_player.stamina < second_player.stamina:
        #     winner_name = self.start_attack(first_player, second_player)
        #     if not winner_name:
        #         winner_name = self.start_attack(second_player, first_player)
        #
        # else:
        #     winner_name = self.start_attack(second_player, first_player)
        #     if not winner_name:
        #         winner_name = self.start_attack(first_player, second_player)
        #
        # if not winner_name:
        #     if first_player.stamina > second_player.stamina:
        #         winner_name = first_player_name
        #     else:
        #         winner_name = second_player_name
        #
        # return f"Winner: {winner_name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(0, player.stamina - player.age * 2)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []
        for player in self.players:
            result.append(str(player))

        for supply in self.supplies:
            result.append(supply.details())

        result = '\n'.join(result)
        return result


# forgot to validate types, valid_sustenance_types (line 23)