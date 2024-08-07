from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .dota2_favorite_hero import Dota2FavoriteHero
from .dota2_game_player import Dota2GamePlayer
from .dota2_player_by_serie_stat import Dota2PlayerBySerieStat
from .base_team import BaseTeam
from .dota2_total_player_stat import Dota2TotalPlayerStat


@JsonMap({"id_": "id"})
class Dota2StatsForPlayerCurrentTeam(BaseModel):
    """Dota2StatsForPlayerCurrentTeam

    :param acronym: acronym
    :type acronym: str
    :param id_: id_
    :type id_: int
    :param image_url: URL of the team logo
    :type image_url: str
    :param location: The team's organization location
    :type location: str
    :param modified_at: modified_at
    :type modified_at: str
    :param name: The name of the team.
    :type name: str
    :param slug: slug
    :type slug: str
    """

    def __init__(
        self,
        acronym: str,
        id_: int,
        image_url: str,
        location: str,
        modified_at: str,
        name: str,
        slug: str,
    ):
        self.acronym = acronym
        self.id_ = id_
        self.image_url = image_url
        self.location = location
        self.modified_at = modified_at
        self.name = name
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")


@JsonMap({"id_": "id"})
class Dota2StatsForPlayer(BaseModel):
    """Aggregated statistics for a player grouped by serie

    :param active: Whether player is active
    :type active: bool
    :param age: Age of the player, `null` if unknown. When `birthday` is `null`, `age` is an approxiamation. Read more about [players' age](/docs/about-players-age) <br/>**Note**: This field is only present for users running the Historical plan or above.
    :type age: float
    :param birthday: Birth day of the player, `YYYY-MM-DD` format. `null` if unknown. <br/>**Note**: This field is only present for users running the Historical plan or above.
    :type birthday: str
    :param current_team: current_team
    :type current_team: Dota2StatsForPlayerCurrentTeam
    :param current_videogame: current_videogame
    :type current_videogame: dict
    :param favorite_heroes: favorite_heroes
    :type favorite_heroes: List[Dota2FavoriteHero]
    :param first_name: First name of the player. `null` if unknown
    :type first_name: str
    :param id_: ID of the player
    :type id_: int
    :param image_url: URL to the photo of the player. `null` if not available.
    :type image_url: str
    :param last_games: last_games
    :type last_games: List[Dota2GamePlayer]
    :param last_name: Last name of the player. `null` if unknown
    :type last_name: str
    :param modified_at: modified_at
    :type modified_at: str
    :param name: Professional name of the player
    :type name: str
    :param nationality: Country code matching the nationality of the player according to the ISO 3166-1 standard (Alpha-2 code). <br/>In addition to the standard, the `XK` code is used for Kosovo. <br/>`null` if unknown
    :type nationality: str
    :param role: Role/position of the player. Field value varies depending on the video game.`null` if unknown. <br/>**Note**: role is only available for DotA 2, League of Legends, and Overwatch players. <br/>`null` for other video games.
    :type role: str
    :param slug: Unique, human-readable identifier for the player. <br/>`id` and `slug` can be used interchangeably throughout the API.
    :type slug: str
    :param stats: stats
    :type stats: List[Dota2PlayerBySerieStat]
    :param teams: teams
    :type teams: List[BaseTeam]
    :param total_stats: Total Player's statistics
    :type total_stats: Dota2TotalPlayerStat
    """

    def __init__(
        self,
        active: bool,
        age: float,
        birthday: str,
        current_team: Dota2StatsForPlayerCurrentTeam,
        current_videogame: dict,
        favorite_heroes: List[Dota2FavoriteHero],
        first_name: str,
        id_: int,
        image_url: str,
        last_games: List[Dota2GamePlayer],
        last_name: str,
        modified_at: str,
        name: str,
        nationality: str,
        role: str,
        slug: str,
        stats: List[Dota2PlayerBySerieStat],
        teams: List[BaseTeam],
        total_stats: Dota2TotalPlayerStat,
    ):
        self.active = active
        self.age = age
        self.birthday = birthday
        self.current_team = self._define_object(
            current_team, Dota2StatsForPlayerCurrentTeam
        )
        self.current_videogame = current_videogame
        self.favorite_heroes = self._define_list(favorite_heroes, Dota2FavoriteHero)
        self.first_name = first_name
        self.id_ = id_
        self.image_url = image_url
        self.last_games = self._define_list(last_games, Dota2GamePlayer)
        self.last_name = last_name
        self.modified_at = modified_at
        self.name = name
        self.nationality = nationality
        self.role = role
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
        self.stats = self._define_list(stats, Dota2PlayerBySerieStat)
        self.teams = self._define_list(teams, BaseTeam)
        self.total_stats = self._define_object(total_stats, Dota2TotalPlayerStat)
