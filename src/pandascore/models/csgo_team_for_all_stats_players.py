from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .csgo_player_for_all_stats_players import CsgoPlayerForAllStatsPlayers


@JsonMap({"id_": "id"})
class CsgoTeamForAllStatsPlayers(BaseModel):
    """CsgoTeamForAllStatsPlayers

    :param id_: id_
    :type id_: int
    :param name: The name of the team.
    :type name: str
    :param players: players
    :type players: List[CsgoPlayerForAllStatsPlayers]
    :param slug: slug
    :type slug: str
    """

    def __init__(
        self,
        id_: int,
        name: str,
        players: List[CsgoPlayerForAllStatsPlayers],
        slug: str,
    ):
        self.id_ = id_
        self.name = name
        self.players = self._define_list(players, CsgoPlayerForAllStatsPlayers)
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
