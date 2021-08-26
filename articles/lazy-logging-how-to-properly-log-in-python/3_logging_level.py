import logging
import random
import time
from typing import Dict

log = logging.getLogger(__name__)


class Player:
    def __init__(self, id_: str, name: str, rating: float):
        self.id = id_
        self.name = name
        self.rating = rating

    @property
    def rating_prediction(self) -> float:
        print("Counting rating prediction...")  # noqa: T001
        time.sleep(3)  # Imitate time-consuming operation
        return random.uniform(8, 10)  # nosec

    def __str__(self) -> str:
        return (
            f"{self.name!r} with rating {self.rating:.2f} "
            f"and rating prediction {self.rating_prediction:.2f}"
        )


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
    logging.basicConfig(level=logging.WARNING)

    db = PlayersDatabase()
    db.add_player(Player(id_="id_3", name="Neymar", rating=8.3))
