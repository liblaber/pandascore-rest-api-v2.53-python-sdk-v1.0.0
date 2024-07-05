from __future__ import annotations
from enum import Enum
from typing import Union
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel
from .base_league import BaseLeague
from .base_match import BaseMatch
from .base_serie import BaseSerie
from .base_team import BaseTeam
from .videogame_id import VideogameId


class ShortTournamentTier(Enum):
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
        return list(map(lambda x: x.value, ShortTournamentTier._member_map_.values()))


@JsonMap({"id_": "id"})
class ShortTournamentVideogameTitle(BaseModel):
    """ShortTournamentVideogameTitle

    :param id_: id_
    :type id_: int
    :param name: name
    :type name: str
    :param slug: slug
    :type slug: str
    :param videogame_id: A videogame ID
    :type videogame_id: VideogameId
    """

    def __init__(self, id_: int, name: str, slug: str, videogame_id: VideogameId):
        self.id_ = id_
        self.name = name
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
        self.videogame_id = self._enum_matching(
            videogame_id, VideogameId.list(), "videogame_id"
        )


class ShortTournamentWinnerIdGuard(OneOfBaseModel):
    class_list = {"int": int, "int": int}


ShortTournamentWinnerId = Union[int, int]


class ShortTournamentWinnerType(Enum):
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
            map(lambda x: x.value, ShortTournamentWinnerType._member_map_.values())
        )


@JsonMap({"id_": "id"})
class ShortTournament(BaseModel):
    """ShortTournament

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
    :param league: league
    :type league: BaseLeague
    :param league_id: league_id
    :type league_id: int
    :param live_supported: Whether live is supported
    :type live_supported: bool
    :param matches: matches
    :type matches: List[BaseMatch]
    :param modified_at: modified_at
    :type modified_at: str
    :param name: name
    :type name: str
    :param prizepool: prizepool
    :type prizepool: str
    :param serie: serie
    :type serie: BaseSerie
    :param serie_id: serie_id
    :type serie_id: int
    :param slug: slug
    :type slug: str
    :param teams: teams
    :type teams: List[BaseTeam]
    :param tier: The tier of the tournament, ranging from 'S' to 'Unranked'. Ranking 'S' > 'A' > 'B' > 'C' > 'D' > 'Unranked'
    :type tier: ShortTournamentTier
    :param videogame: videogame
    :type videogame: dict
    :param videogame_title: videogame_title
    :type videogame_title: ShortTournamentVideogameTitle
    :param winner_id: winner_id
    :type winner_id: ShortTournamentWinnerId
    :param winner_type: winner_type
    :type winner_type: ShortTournamentWinnerType
    """

    def __init__(
        self,
        begin_at: str,
        detailed_stats: bool,
        end_at: str,
        has_bracket: bool,
        id_: int,
        league: BaseLeague,
        league_id: int,
        live_supported: bool,
        matches: List[BaseMatch],
        modified_at: str,
        name: str,
        prizepool: str,
        serie: BaseSerie,
        serie_id: int,
        slug: str,
        teams: List[BaseTeam],
        tier: ShortTournamentTier,
        videogame: dict,
        videogame_title: ShortTournamentVideogameTitle,
        winner_id: ShortTournamentWinnerId,
        winner_type: ShortTournamentWinnerType,
    ):
        self.begin_at = begin_at
        self.detailed_stats = detailed_stats
        self.end_at = end_at
        self.has_bracket = has_bracket
        self.id_ = id_
        self.league = self._define_object(league, BaseLeague)
        self.league_id = league_id
        self.live_supported = live_supported
        self.matches = self._define_list(matches, BaseMatch)
        self.modified_at = modified_at
        self.name = name
        self.prizepool = prizepool
        self.serie = self._define_object(serie, BaseSerie)
        self.serie_id = serie_id
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
        self.teams = self._define_list(teams, BaseTeam)
        self.tier = self._enum_matching(tier, ShortTournamentTier.list(), "tier")
        self.videogame = videogame
        self.videogame_title = self._define_object(
            videogame_title, ShortTournamentVideogameTitle
        )
        self.winner_id = ShortTournamentWinnerIdGuard.return_one_of(winner_id)
        self.winner_type = self._enum_matching(
            winner_type, ShortTournamentWinnerType.list(), "winner_type"
        )
