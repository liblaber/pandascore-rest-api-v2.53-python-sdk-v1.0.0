from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .game_status import GameStatus


@JsonMap({})
class SearchOverValorantGames(BaseModel):
    """SearchOverValorantGames

    :param status: The game status, defaults to None
    :type status: GameStatus, optional
    """

    def __init__(self, status: GameStatus = None):
        if status is not None:
            self.status = self._enum_matching(status, GameStatus.list(), "status")
