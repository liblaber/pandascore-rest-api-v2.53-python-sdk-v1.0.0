from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class CsgoTeamMapStats(BaseModel):
    """Statistics for a map

    :param ct_pistol_round_total_played: Number of pistol rounds played as Counter-Terrorists on this map
    :type ct_pistol_round_total_played: int
    :param ct_pistol_round_wins: Number of pistol rounds won as Counter-Terrorists on this map
    :type ct_pistol_round_wins: int
    :param ct_round_total_played: Number of rounds played as Counter-Terrorists on this map
    :type ct_round_total_played: int
    :param ct_round_wins: Number of rounds won as Counter-Terrorists on this map
    :type ct_round_wins: int
    :param id_: The ID of the map.
    :type id_: int
    :param image_url: A URL to the image of the map.
    :type image_url: str
    :param losses: Number of team losses on this map
    :type losses: int
    :param name: The name of the map.
    :type name: str
    :param pistol_round_total_played: Number of pistol rounds played on this map
    :type pistol_round_total_played: int
    :param round_total_played: Number of rounds played on this map
    :type round_total_played: int
    :param slug: Human-readable identifier of the map
    :type slug: str
    :param t_pistol_round_total_played: Number of pistol rounds played as Terrorists on this map
    :type t_pistol_round_total_played: int
    :param t_pistol_round_wins: Number of pistol rounds won as Terrorists on this map
    :type t_pistol_round_wins: int
    :param t_round_total_played: Number of rounds played as Terrorists on this map
    :type t_round_total_played: int
    :param t_round_wins: Number of rounds won as Terrorists on this map
    :type t_round_wins: int
    :param total_played: Number of times the team played on this map
    :type total_played: int
    :param wins: Number of team wins on this map
    :type wins: int
    """

    def __init__(
        self,
        ct_pistol_round_total_played: int,
        ct_pistol_round_wins: int,
        ct_round_total_played: int,
        ct_round_wins: int,
        id_: int,
        image_url: str,
        losses: int,
        name: str,
        pistol_round_total_played: int,
        round_total_played: int,
        slug: str,
        t_pistol_round_total_played: int,
        t_pistol_round_wins: int,
        t_round_total_played: int,
        t_round_wins: int,
        total_played: int,
        wins: int,
    ):
        self.ct_pistol_round_total_played = ct_pistol_round_total_played
        self.ct_pistol_round_wins = ct_pistol_round_wins
        self.ct_round_total_played = ct_round_total_played
        self.ct_round_wins = ct_round_wins
        self.id_ = id_
        self.image_url = image_url
        self.losses = losses
        self.name = name
        self.pistol_round_total_played = pistol_round_total_played
        self.round_total_played = round_total_played
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
        self.t_pistol_round_total_played = t_pistol_round_total_played
        self.t_pistol_round_wins = t_pistol_round_wins
        self.t_round_total_played = t_round_total_played
        self.t_round_wins = t_round_wins
        self.total_played = total_played
        self.wins = wins
