from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."

        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name

        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        try:
            current_player = next(filter(lambda p: p.name == player_name, self.players))
        except StopIteration:
            return f"Player {player_name} is not in the guild."

        self.players.remove(current_player)
        current_player.guild = "Unaffiliated"

        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        players_info = '\n'.join([current_player.player_info() for current_player in self.players])

        return f"Guild: {self.name}\n" \
               f"{players_info}"
