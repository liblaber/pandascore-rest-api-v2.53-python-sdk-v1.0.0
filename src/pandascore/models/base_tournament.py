from enum import Enum
from typing import Union
from .utils.json_map import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel


class BaseTournamentTier(Enum):
    """An enumeration representing different categories.

    :cvar A: "a"
    :vartype A: str
    :cvar B: "b"
    :vartype B: str
    :cvar C: "c"
    :vartype C: str
    :cvar D: "d"
    :vartype D: str
    :cvar S: "s"
    :vartype S: str
    :cvar UNRANKED: "unranked"
    :vartype UNRANKED: str
    """

    A = "a"
    B = "b"
    C = "c"
    D = "d"
    S = "s"
    UNRANKED = "unranked"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, BaseTournamentTier._member_map_.values()))


class BaseTournamentWinnerIdGuard(OneOfBaseModel):
    class_list = {"int": int, "int": int}


BaseTournamentWinnerId = Union[int, int]


class BaseTournamentWinnerType(Enum):
    """An enumeration representing different categories.

    :cvar PLAYER: "Player"
    :vartype PLAYER: str
    :cvar TEAM: "Team"
    :vartype TEAM: str
    """

    PLAYER = "Player"
    TEAM = "Team"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, BaseTournamentWinnerType._member_map_.values())
        )


@JsonMap({"id_": "id"})
class BaseTournament(BaseModel):
    """BaseTournament

    :param begin_at: begin_at
    :type begin_at: str
    :param detailed_stats: Whether the tournament is expected to have detailed statistics available
    :type detailed_stats: bool
    :param end_at: end_at
    :type end_at: str
    :param has_bracket: Whether the tournament has a bracket
    :type has_bracket: bool
    :param id_: id_
    :type id_: int
    :param league_id: league_id
    :type league_id: int
    :param live_supported: Whether live is supported
    :type live_supported: bool
    :param modified_at: modified_at
    :type modified_at: str
    :param name: name
    :type name: str
    :param prizepool: prizepool
    :type prizepool: str
    :param serie_id: serie_id
    :type serie_id: int
    :param slug: slug
    :type slug: str
    :param tier: The tier of the tournament, ranging from 'S' to 'Unranked'. Ranking 'S' > 'A' > 'B' > 'C' > 'D' > 'Unranked'
    :type tier: BaseTournamentTier
    :param winner_id: winner_id
    :type winner_id: BaseTournamentWinnerId
    :param winner_type: winner_type
    :type winner_type: BaseTournamentWinnerType
    """

    def __init__(
        self,
        begin_at: str,
        detailed_stats: bool,
        end_at: str,
        has_bracket: bool,
        id_: int,
        league_id: int,
        live_supported: bool,
        modified_at: str,
        name: str,
        prizepool: str,
        serie_id: int,
        slug: str,
        tier: BaseTournamentTier,
        winner_id: BaseTournamentWinnerId,
        winner_type: BaseTournamentWinnerType,
    ):
        self.begin_at = begin_at
        self.detailed_stats = detailed_stats
        self.end_at = end_at
        self.has_bracket = has_bracket
        self.id_ = id_
        self.league_id = league_id
        self.live_supported = live_supported
        self.modified_at = modified_at
        self.name = name
        self.prizepool = prizepool
        self.serie_id = serie_id
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
        self.tier = self._enum_matching(tier, BaseTournamentTier.list(), "tier")
        self.winner_id = BaseTournamentWinnerIdGuard.return_one_of(winner_id)
        self.winner_type = self._enum_matching(
            winner_type, BaseTournamentWinnerType.list(), "winner_type"
        )
