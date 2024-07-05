from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel


class LoLMatchPlayerRole(Enum):
    """An enumeration representing different categories.

    :cvar ADC: "adc"
    :vartype ADC: str
    :cvar JUN: "jun"
    :vartype JUN: str
    :cvar MID: "mid"
    :vartype MID: str
    :cvar SUP: "sup"
    :vartype SUP: str
    :cvar TOP: "top"
    :vartype TOP: str
    """

    ADC = "adc"
    JUN = "jun"
    MID = "mid"
    SUP = "sup"
    TOP = "top"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, LoLMatchPlayerRole._member_map_.values()))


@JsonMap({})
class LoLMatchPlayer(BaseModel):
    """Player's data for a LoL Match

    :param assists: assists
    :type assists: int
    :param deaths: deaths
    :type deaths: int
    :param first_name: First name of the player. `null` if unknown
    :type first_name: str
    :param image_url: URL to the photo of the player. `null` if not available.
    :type image_url: str
    :param kills: kills
    :type kills: int
    :param last_name: Last name of the player. `null` if unknown
    :type last_name: str
    :param name: Professional name of the player
    :type name: str
    :param nationality: Country code matching the nationality of the player according to the ISO 3166-1 standard (Alpha-2 code). <br/>In addition to the standard, the `XK` code is used for Kosovo. <br/>`null` if unknown
    :type nationality: str
    :param number_of_games: Number of games
    :type number_of_games: int
    :param player_id: ID of the player
    :type player_id: int
    :param role: role
    :type role: LoLMatchPlayerRole
    :param slug: Unique, human-readable identifier for the player. <br/>`id` and `slug` can be used interchangeably throughout the API.
    :type slug: str
    """

    def __init__(
        self,
        assists: int,
        deaths: int,
        first_name: str,
        image_url: str,
        kills: int,
        last_name: str,
        name: str,
        nationality: str,
        number_of_games: int,
        player_id: int,
        role: LoLMatchPlayerRole,
        slug: str,
    ):
        self.assists = assists
        self.deaths = deaths
        self.first_name = first_name
        self.image_url = image_url
        self.kills = kills
        self.last_name = last_name
        self.name = name
        self.nationality = nationality
        self.number_of_games = number_of_games
        self.player_id = player_id
        self.role = self._enum_matching(role, LoLMatchPlayerRole.list(), "role")
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
