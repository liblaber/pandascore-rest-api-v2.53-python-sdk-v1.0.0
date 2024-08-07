from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .base_dota2_game import BaseDota2Game
from .dota2_banned_hero import Dota2BannedHero
from .dota2_picked_hero import Dota2PickedHero
from .base_player import BasePlayer
from .dota2_team_by_tournament_stat import Dota2TeamByTournamentStat


@JsonMap({"id_": "id"})
class Dota2StatsForTeamByTournament(BaseModel):
    """Team's aggregated statistics for a tournament

    :param acronym: acronym
    :type acronym: str
    :param id_: id_
    :type id_: int
    :param image_url: URL of the team logo
    :type image_url: str
    :param last_games: last_games
    :type last_games: List[BaseDota2Game]
    :param location: The team's organization location
    :type location: str
    :param modified_at: modified_at
    :type modified_at: str
    :param most_banned: most_banned
    :type most_banned: List[Dota2BannedHero]
    :param most_banned_against: most_banned_against
    :type most_banned_against: List[Dota2BannedHero]
    :param most_picked: most_picked
    :type most_picked: List[Dota2PickedHero]
    :param name: The name of the team.
    :type name: str
    :param players: players
    :type players: List[BasePlayer]
    :param slug: slug
    :type slug: str
    :param stats: Team's statistics for a tournament
    :type stats: Dota2TeamByTournamentStat
    :param videogame: videogame
    :type videogame: dict
    """

    def __init__(
        self,
        acronym: str,
        id_: int,
        image_url: str,
        last_games: List[BaseDota2Game],
        location: str,
        modified_at: str,
        most_banned: List[Dota2BannedHero],
        most_banned_against: List[Dota2BannedHero],
        most_picked: List[Dota2PickedHero],
        name: str,
        players: List[BasePlayer],
        slug: str,
        stats: Dota2TeamByTournamentStat,
        videogame: dict,
    ):
        self.acronym = acronym
        self.id_ = id_
        self.image_url = image_url
        self.last_games = self._define_list(last_games, BaseDota2Game)
        self.location = location
        self.modified_at = modified_at
        self.most_banned = self._define_list(most_banned, Dota2BannedHero)
        self.most_banned_against = self._define_list(
            most_banned_against, Dota2BannedHero
        )
        self.most_picked = self._define_list(most_picked, Dota2PickedHero)
        self.name = name
        self.players = self._define_list(players, BasePlayer)
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
        self.stats = self._define_object(stats, Dota2TeamByTournamentStat)
        self.videogame = videogame
