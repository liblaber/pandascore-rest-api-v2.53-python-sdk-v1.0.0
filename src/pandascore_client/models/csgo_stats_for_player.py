# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .csgo_game_player import CsgoGamePlayer
from .csgo_player_stats import CsgoPlayerStats
from .base_team import BaseTeam


@JsonMap({"id_": "id"})
class CsgoStatsForPlayerCurrentTeam(BaseModel):
    """CsgoStatsForPlayerCurrentTeam

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
        """CsgoStatsForPlayerCurrentTeam

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
        self.acronym = self._define_str("acronym", acronym, nullable=True)
        self.id_ = self._define_number("id_", id_, ge=1)
        self.image_url = self._define_str("image_url", image_url, nullable=True)
        self.location = self._define_str("location", location, nullable=True)
        self.modified_at = self._define_str("modified_at", modified_at, min_length=1)
        self.name = name
        self.slug = self._define_str(
            "slug", slug, nullable=True, pattern="^[a-z0-9_-]+$", min_length=1
        )


@JsonMap({"id_": "id"})
class CsgoStatsForPlayer(BaseModel):
    """Player's aggregated statistics

    :param active: Whether player is active
    :type active: bool
    :param age: Age of the player, `null` if unknown. When `birthday` is `null`, `age` is an approxiamation. Read more about [players' age](/docs/about-players-age) <br/>**Note**: This field is only present for users running the Historical plan or above.
    :type age: float
    :param birthday: Birth day of the player, `YYYY-MM-DD` format. `null` if unknown. <br/>**Note**: This field is only present for users running the Historical plan or above.
    :type birthday: str
    :param current_team: current_team
    :type current_team: CsgoStatsForPlayerCurrentTeam
    :param current_videogame: current_videogame
    :type current_videogame: dict
    :param first_name: First name of the player. `null` if unknown
    :type first_name: str
    :param id_: ID of the player
    :type id_: int
    :param image_url: URL to the photo of the player. `null` if not available.
    :type image_url: str
    :param last_games: last_games
    :type last_games: List[CsgoGamePlayer]
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
    :param stats: Statistics for all matches
    :type stats: CsgoPlayerStats
    :param teams: teams
    :type teams: List[BaseTeam]
    """

    def __init__(
        self,
        active: bool,
        age: float,
        birthday: str,
        current_team: CsgoStatsForPlayerCurrentTeam,
        current_videogame: dict,
        first_name: str,
        id_: int,
        image_url: str,
        last_games: List[CsgoGamePlayer],
        last_name: str,
        modified_at: str,
        name: str,
        nationality: str,
        role: str,
        slug: str,
        stats: CsgoPlayerStats,
        teams: List[BaseTeam],
    ):
        """Player's aggregated statistics

        :param active: Whether player is active
        :type active: bool
        :param age: Age of the player, `null` if unknown. When `birthday` is `null`, `age` is an approxiamation. Read more about [players' age](/docs/about-players-age) <br/>**Note**: This field is only present for users running the Historical plan or above.
        :type age: float
        :param birthday: Birth day of the player, `YYYY-MM-DD` format. `null` if unknown. <br/>**Note**: This field is only present for users running the Historical plan or above.
        :type birthday: str
        :param current_team: current_team
        :type current_team: CsgoStatsForPlayerCurrentTeam
        :param current_videogame: current_videogame
        :type current_videogame: dict
        :param first_name: First name of the player. `null` if unknown
        :type first_name: str
        :param id_: ID of the player
        :type id_: int
        :param image_url: URL to the photo of the player. `null` if not available.
        :type image_url: str
        :param last_games: last_games
        :type last_games: List[CsgoGamePlayer]
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
        :param stats: Statistics for all matches
        :type stats: CsgoPlayerStats
        :param teams: teams
        :type teams: List[BaseTeam]
        """
        self.active = active
        self.age = self._define_number("age", age, nullable=True, ge=0)
        self.birthday = self._define_str("birthday", birthday, nullable=True)
        self.current_team = self._define_object(
            current_team, CsgoStatsForPlayerCurrentTeam
        )
        self.current_videogame = current_videogame
        self.first_name = self._define_str("first_name", first_name, nullable=True)
        self.id_ = self._define_number("id_", id_, ge=1)
        self.image_url = self._define_str("image_url", image_url, nullable=True)
        self.last_games = self._define_list(last_games, CsgoGamePlayer)
        self.last_name = self._define_str("last_name", last_name, nullable=True)
        self.modified_at = self._define_str("modified_at", modified_at, min_length=1)
        self.name = name
        self.nationality = self._define_str("nationality", nationality, nullable=True)
        self.role = self._define_str("role", role, nullable=True)
        self.slug = self._define_str(
            "slug", slug, nullable=True, pattern="^[a-z0-9_-]+$", min_length=1
        )
        self.stats = self._define_object(stats, CsgoPlayerStats)
        self.teams = self._define_list(teams, BaseTeam)
