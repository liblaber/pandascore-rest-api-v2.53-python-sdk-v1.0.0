from __future__ import annotations
from typing import Union
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel
from .game import Game
from .base_league import BaseLeague
from .match_live import MatchLive
from .match_type import MatchType
from .opponent import Opponent
from .match_result import MatchResult, MatchResultGuard
from .match_team_result import MatchTeamResult
from .match_player_result import MatchPlayerResult
from .base_serie import BaseSerie
from .match_status import MatchStatus
from .stream import Stream
from .base_tournament import BaseTournament
from .match_winner_type import MatchWinnerType


@JsonMap({"id_": "id"})
class Winner1_4(BaseModel):
    """Winner1_4

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
class Winner2_4(BaseModel):
    """Winner2_4

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


class Dota2GameMatchWinnerGuard(OneOfBaseModel):
    class_list = {"Winner1_4": Winner1_4, "Winner2_4": Winner2_4}


Dota2GameMatchWinner = Union[Winner1_4, Winner2_4]


class Dota2GameMatchWinnerIdGuard(OneOfBaseModel):
    class_list = {"int": int, "int": int}


Dota2GameMatchWinnerId = Union[int, int]


@JsonMap({"id_": "id"})
class Dota2GameMatch(BaseModel):
    """Dota2GameMatch

    :param begin_at: begin_at
    :type begin_at: str
    :param detailed_stats: Whether the match offers full stats
    :type detailed_stats: bool
    :param draw: Whether result of the match is a draw
    :type draw: bool
    :param end_at: end_at
    :type end_at: str
    :param forfeit: Whether match was forfeited
    :type forfeit: bool
    :param game_advantage: ID of the opponent with a game advantage
    :type game_advantage: int
    :param games: games
    :type games: List[Game]
    :param id_: id_
    :type id_: int
    :param league: league
    :type league: BaseLeague
    :param league_id: league_id
    :type league_id: int
    :param live: live
    :type live: MatchLive
    :param match_type: match_type
    :type match_type: MatchType
    :param modified_at: modified_at
    :type modified_at: str
    :param name: name
    :type name: str
    :param number_of_games: Number of games
    :type number_of_games: int
    :param opponents: opponents
    :type opponents: List[Opponent]
    :param original_scheduled_at: original_scheduled_at
    :type original_scheduled_at: str
    :param rescheduled: Whether match has been rescheduled
    :type rescheduled: bool
    :param results: results
    :type results: List[MatchResult]
    :param scheduled_at: scheduled_at
    :type scheduled_at: str
    :param serie: serie
    :type serie: BaseSerie
    :param serie_id: serie_id
    :type serie_id: int
    :param slug: slug
    :type slug: str
    :param status: status
    :type status: MatchStatus
    :param streams_list: streams_list
    :type streams_list: List[Stream]
    :param tournament: tournament
    :type tournament: BaseTournament
    :param tournament_id: tournament_id
    :type tournament_id: int
    :param winner: winner
    :type winner: Dota2GameMatchWinner
    :param winner_id: winner_id
    :type winner_id: Dota2GameMatchWinnerId
    :param winner_type: winner_type
    :type winner_type: MatchWinnerType
    """

    def __init__(
        self,
        begin_at: str,
        detailed_stats: bool,
        draw: bool,
        end_at: str,
        forfeit: bool,
        game_advantage: int,
        games: List[Game],
        id_: int,
        league: BaseLeague,
        league_id: int,
        live: MatchLive,
        match_type: MatchType,
        modified_at: str,
        name: str,
        number_of_games: int,
        opponents: List[Opponent],
        original_scheduled_at: str,
        rescheduled: bool,
        results: List[MatchResult],
        scheduled_at: str,
        serie: BaseSerie,
        serie_id: int,
        slug: str,
        status: MatchStatus,
        streams_list: List[Stream],
        tournament: BaseTournament,
        tournament_id: int,
        winner: Dota2GameMatchWinner,
        winner_id: Dota2GameMatchWinnerId,
        winner_type: MatchWinnerType,
    ):
        self.begin_at = begin_at
        self.detailed_stats = detailed_stats
        self.draw = draw
        self.end_at = end_at
        self.forfeit = forfeit
        self.game_advantage = game_advantage
        self.games = self._define_list(games, Game)
        self.id_ = id_
        self.league = self._define_object(league, BaseLeague)
        self.league_id = league_id
        self.live = self._define_object(live, MatchLive)
        self.match_type = self._enum_matching(
            match_type, MatchType.list(), "match_type"
        )
        self.modified_at = modified_at
        self.name = name
        self.number_of_games = number_of_games
        self.opponents = self._define_list(opponents, Opponent)
        self.original_scheduled_at = original_scheduled_at
        self.rescheduled = rescheduled
        self.results = self._define_list(results, MatchResult)
        self.scheduled_at = scheduled_at
        self.serie = self._define_object(serie, BaseSerie)
        self.serie_id = serie_id
        self.slug = self._pattern_matching(slug, "^[ a-zA-Z0-9_-]+$", "slug")
        self.status = self._enum_matching(status, MatchStatus.list(), "status")
        self.streams_list = self._define_list(streams_list, Stream)
        self.tournament = self._define_object(tournament, BaseTournament)
        self.tournament_id = tournament_id
        self.winner = Dota2GameMatchWinnerGuard.return_one_of(winner)
        self.winner_id = Dota2GameMatchWinnerIdGuard.return_one_of(winner_id)
        self.winner_type = self._enum_matching(
            winner_type, MatchWinnerType.list(), "winner_type"
        )
