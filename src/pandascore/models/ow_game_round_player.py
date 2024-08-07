from __future__ import annotations
from typing import Union
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel
from .ow_game_round_player_hero import OwGameRoundPlayerHero
from .base_player import BasePlayer


@JsonMap({"id_": "id"})
class Opponent1_5(BaseModel):
    """Opponent1_5

    :param active: Whether player is active
    :type active: bool
    :param age: Age of the player, `null` if unknown. When `birthday` is `null`, `age` is an approxiamation. Read more about [players' age](/docs/about-players-age) <br/>**Note**: This field is only present for users running the Historical plan or above.
    :type age: float
    :param birthday: Birth day of the player, `YYYY-MM-DD` format. `null` if unknown. <br/>**Note**: This field is only present for users running the Historical plan or above.
    :type birthday: str
    :param first_name: First name of the player. `null` if unknown
    :type first_name: str
    :param id_: ID of the player
    :type id_: int
    :param image_url: URL to the photo of the player. `null` if not available.
    :type image_url: str
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
    """

    def __init__(
        self,
        active: bool,
        age: float,
        birthday: str,
        first_name: str,
        id_: int,
        image_url: str,
        last_name: str,
        modified_at: str,
        name: str,
        nationality: str,
        role: str,
        slug: str,
    ):
        self.active = active
        self.age = age
        self.birthday = birthday
        self.first_name = first_name
        self.id_ = id_
        self.image_url = image_url
        self.last_name = last_name
        self.modified_at = modified_at
        self.name = name
        self.nationality = nationality
        self.role = role
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")


@JsonMap({"id_": "id"})
class Opponent2_5(BaseModel):
    """Opponent2_5

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


class OwGameRoundPlayerOpponentGuard(OneOfBaseModel):
    class_list = {"Opponent1_5": Opponent1_5, "Opponent2_5": Opponent2_5}


OwGameRoundPlayerOpponent = Union[Opponent1_5, Opponent2_5]


@JsonMap({})
class OwGameRoundPlayer(BaseModel):
    """OwGameRoundPlayer

    :param deaths: deaths
    :type deaths: int
    :param destructions: destructions
    :type destructions: int
    :param heroes: heroes
    :type heroes: List[OwGameRoundPlayerHero]
    :param kills: kills
    :type kills: int
    :param opponent: opponent
    :type opponent: OwGameRoundPlayerOpponent
    :param player: player
    :type player: BasePlayer
    :param player_id: ID of the player
    :type player_id: int
    :param resurrections: resurrections
    :type resurrections: int
    :param ultimate: ultimate
    :type ultimate: int
    """

    def __init__(
        self,
        deaths: int,
        destructions: int,
        heroes: List[OwGameRoundPlayerHero],
        kills: int,
        opponent: OwGameRoundPlayerOpponent,
        player: BasePlayer,
        player_id: int,
        resurrections: int,
        ultimate: int,
    ):
        self.deaths = deaths
        self.destructions = destructions
        self.heroes = self._define_list(heroes, OwGameRoundPlayerHero)
        self.kills = kills
        self.opponent = OwGameRoundPlayerOpponentGuard.return_one_of(opponent)
        self.player = self._define_object(player, BasePlayer)
        self.player_id = player_id
        self.resurrections = resurrections
        self.ultimate = ultimate
