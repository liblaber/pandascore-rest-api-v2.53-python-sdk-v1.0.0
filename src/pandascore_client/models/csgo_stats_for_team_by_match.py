# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .base_csgo_game import BaseCsgoGame
from .base_player import BasePlayer
from .csgo_team_stats_by_match import CsgoTeamStatsByMatch


@JsonMap({"id_": "id"})
class CsgoStatsForTeamByMatch(BaseModel):
    """Team's aggregated statistics for a match

    :param acronym: acronym
    :type acronym: str
    :param current_videogame: current_videogame
    :type current_videogame: dict
    :param id_: id_
    :type id_: int
    :param image_url: URL of the team logo
    :type image_url: str
    :param last_games: last_games
    :type last_games: List[BaseCsgoGame]
    :param location: The team's organization location
    :type location: str
    :param modified_at: modified_at
    :type modified_at: str
    :param name: The name of the team.
    :type name: str
    :param players: players
    :type players: List[BasePlayer]
    :param slug: slug
    :type slug: str
    :param stats: Statistics for a match
    :type stats: CsgoTeamStatsByMatch
    """

    def __init__(
        self,
        acronym: str,
        current_videogame: dict,
        id_: int,
        image_url: str,
        last_games: List[BaseCsgoGame],
        location: str,
        modified_at: str,
        name: str,
        players: List[BasePlayer],
        slug: str,
        stats: CsgoTeamStatsByMatch,
    ):
        """Team's aggregated statistics for a match

        :param acronym: acronym
        :type acronym: str
        :param current_videogame: current_videogame
        :type current_videogame: dict
        :param id_: id_
        :type id_: int
        :param image_url: URL of the team logo
        :type image_url: str
        :param last_games: last_games
        :type last_games: List[BaseCsgoGame]
        :param location: The team's organization location
        :type location: str
        :param modified_at: modified_at
        :type modified_at: str
        :param name: The name of the team.
        :type name: str
        :param players: players
        :type players: List[BasePlayer]
        :param slug: slug
        :type slug: str
        :param stats: Statistics for a match
        :type stats: CsgoTeamStatsByMatch
        """
        self.acronym = self._define_str("acronym", acronym, nullable=True)
        self.current_videogame = current_videogame
        self.id_ = self._define_number("id_", id_, ge=1)
        self.image_url = self._define_str("image_url", image_url, nullable=True)
        self.last_games = self._define_list(last_games, BaseCsgoGame)
        self.location = self._define_str("location", location, nullable=True)
        self.modified_at = self._define_str("modified_at", modified_at, min_length=1)
        self.name = name
        self.players = self._define_list(players, BasePlayer)
        self.slug = self._define_str(
            "slug", slug, nullable=True, pattern="^[a-z0-9_-]+$", min_length=1
        )
        self.stats = self._define_object(stats, CsgoTeamStatsByMatch)