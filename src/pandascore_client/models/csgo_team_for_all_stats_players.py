# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
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
        self.id_ = self._define_number("id_", id_, ge=1)
        self.name = name
        self.players = self._define_list(players, CsgoPlayerForAllStatsPlayers)
        self.slug = self._define_str(
            "slug", slug, pattern="^[a-z0-9_-]+$", min_length=1
        )
