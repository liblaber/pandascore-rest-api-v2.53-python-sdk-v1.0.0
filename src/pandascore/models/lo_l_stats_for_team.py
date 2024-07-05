from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_team_last_game import LoLTeamLastGame
from .lo_l_banned_champion import LoLBannedChampion
from .lo_l_picked_champion import LoLPickedChampion
from .base_player import BasePlayer
from .lo_l_team_by_serie_stat import LoLTeamBySerieStat
from .lo_l_total_team_stat import LoLTotalTeamStat


@JsonMap({"id_": "id"})
class LoLStatsForTeam(BaseModel):
    """Aggregated statistics for a team grouped by serie

    :param acronym: acronym
    :type acronym: str
    :param id_: id_
    :type id_: int
    :param image_url: URL of the team logo
    :type image_url: str
    :param last_games: last_games
    :type last_games: List[LoLTeamLastGame]
    :param location: The team's organization location
    :type location: str
    :param modified_at: modified_at
    :type modified_at: str
    :param most_banned: most_banned
    :type most_banned: List[LoLBannedChampion]
    :param most_banned_against: most_banned_against
    :type most_banned_against: List[LoLBannedChampion]
    :param most_picked: most_picked
    :type most_picked: List[LoLPickedChampion]
    :param name: The name of the team.
    :type name: str
    :param players: players
    :type players: List[BasePlayer]
    :param slug: slug
    :type slug: str
    :param stats: stats
    :type stats: List[LoLTeamBySerieStat]
    :param total_stats: Total Team's statistics
    :type total_stats: LoLTotalTeamStat
    """

    def __init__(
        self,
        acronym: str,
        id_: int,
        image_url: str,
        last_games: List[LoLTeamLastGame],
        location: str,
        modified_at: str,
        most_banned: List[LoLBannedChampion],
        most_banned_against: List[LoLBannedChampion],
        most_picked: List[LoLPickedChampion],
        name: str,
        players: List[BasePlayer],
        slug: str,
        stats: List[LoLTeamBySerieStat],
        total_stats: LoLTotalTeamStat,
    ):
        self.acronym = acronym
        self.id_ = id_
        self.image_url = image_url
        self.last_games = self._define_list(last_games, LoLTeamLastGame)
        self.location = location
        self.modified_at = modified_at
        self.most_banned = self._define_list(most_banned, LoLBannedChampion)
        self.most_banned_against = self._define_list(
            most_banned_against, LoLBannedChampion
        )
        self.most_picked = self._define_list(most_picked, LoLPickedChampion)
        self.name = name
        self.players = self._define_list(players, BasePlayer)
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
        self.stats = self._define_list(stats, LoLTeamBySerieStat)
        self.total_stats = self._define_object(total_stats, LoLTotalTeamStat)
