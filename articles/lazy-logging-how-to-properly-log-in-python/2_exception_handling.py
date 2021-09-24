import logging
from typing import Dict

log = logging.getLogger(__name__)


class Player:
    def __init__(self, id_: str, name: str, rating: float):
        self.id = id_
        self.name = name
        self.rating = rating

    def __str__(self) -> str:
        return f"{self.name!r} with rating {self.rating:.2f}"


class PlayersDatabase:
    def __init__(self) -> None:
        self.players: Dict[str, Player] = {}

    def add_player(self, player: Player) -> None:
        if self.players.get(player.id):
            raise self.DBError(f"Player with ID {player.id!r} already exists")
        self.players[player.id] = player
        # log.debug(f"Added player to the database: {player}")  # Eager logging
        log.debug("Added player to the database: %s", player)  # Lazy logging

    class DBError(Exception):
        pass


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    db = PlayersDatabase()
    db.add_player(Player(id_="id_1", name="Robert Lewandowski", rating=9.6))
    db.add_player(
        Player(id_="id_2", name="Cristiano Ronaldo", rating=None),  # type: ignore
    )

    print("Continuing the program...")
