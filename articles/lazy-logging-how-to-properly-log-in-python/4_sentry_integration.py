import logging
from typing import Dict, Optional

import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration

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
        log.debug("Added player to the database: %s", player)

    def get_player(self, player_id: str) -> Optional[Player]:
        player = self.players.get(player_id)
        if not player:
            # log.warning(
            #     f"Player with ID {player_id!r} has not been found"
            # )  # Eager logging
            log.warning(
                "Player with ID %r has not been found", player_id
            )  # Lazy logging
            return None
        log.debug("Retrieved player from the database: %s", player)
        return player

    class DBError(Exception):
        pass


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    sentry_logging = LoggingIntegration(level=logging.INFO, event_level=logging.WARNING)
    sentry_sdk.init("<SENTRY_DSN>", integrations=[sentry_logging])

    db = PlayersDatabase()
    db.add_player(Player(id_="id_4", name="Lionel Messi", rating=9.5))

    player_id_4 = db.get_player("id_4")

    player_id_5 = db.get_player("id_5")
    player_id_6 = db.get_player("id_6")
    player_id_7 = db.get_player("id_7")
