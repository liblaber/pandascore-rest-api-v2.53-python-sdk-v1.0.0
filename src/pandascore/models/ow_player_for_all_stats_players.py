from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .ow_player_stats_for_all_players_by_match import OwPlayerStatsForAllPlayersByMatch


@JsonMap({"id_": "id"})
class OwPlayerForAllStatsPlayers(BaseModel):
    """OwPlayerForAllStatsPlayers

    :param first_name: First name of the player. `null` if unknown
    :type first_name: str
    :param id_: ID of the player
    :type id_: int
    :param last_name: Last name of the player. `null` if unknown
    :type last_name: str
    :param name: Professional name of the player
    :type name: str
    :param stats: Statistics for all players for a match
    :type stats: OwPlayerStatsForAllPlayersByMatch
    """

    def __init__(
        self,
        first_name: str,
        id_: int,
        last_name: str,
        name: str,
        stats: OwPlayerStatsForAllPlayersByMatch,
    ):
        self.first_name = first_name
        self.id_ = id_
        self.last_name = last_name
        self.name = name
        self.stats = self._define_object(stats, OwPlayerStatsForAllPlayersByMatch)
