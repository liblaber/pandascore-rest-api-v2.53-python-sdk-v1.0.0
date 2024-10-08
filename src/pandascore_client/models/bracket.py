# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import Union
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.one_of_base_model import OneOfBaseModel
from .game import Game
from .match_live import MatchLive
from .match_type import MatchType
from .opponent import Opponent
from .previous_match import PreviousMatch
from .match_result import MatchResult, MatchResultGuard
from .match_team_result import MatchTeamResult
from .match_player_result import MatchPlayerResult
from .match_status import MatchStatus
from .stream import Stream
from .match_winner_type import MatchWinnerType


class BracketWinnerIdGuard(OneOfBaseModel):
    class_list = {"int": int, "int": int}


BracketWinnerId = Union[int, int]


@JsonMap({"id_": "id"})
class Bracket(BaseModel):
    """Bracket

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
    :param previous_matches: previous_matches
    :type previous_matches: List[PreviousMatch]
    :param results: results
    :type results: List[MatchResult]
    :param scheduled_at: scheduled_at
    :type scheduled_at: str
    :param slug: slug
    :type slug: str
    :param status: status
    :type status: MatchStatus
    :param streams_list: streams_list
    :type streams_list: List[Stream]
    :param tournament_id: tournament_id
    :type tournament_id: int
    :param winner_id: winner_id
    :type winner_id: BracketWinnerId
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
        live: MatchLive,
        match_type: MatchType,
        modified_at: str,
        name: str,
        number_of_games: int,
        opponents: List[Opponent],
        original_scheduled_at: str,
        previous_matches: List[PreviousMatch],
        results: List[MatchResult],
        scheduled_at: str,
        slug: str,
        status: MatchStatus,
        streams_list: List[Stream],
        tournament_id: int,
        winner_id: BracketWinnerId,
        winner_type: MatchWinnerType,
    ):
        """Bracket

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
        :param previous_matches: previous_matches
        :type previous_matches: List[PreviousMatch]
        :param results: results
        :type results: List[MatchResult]
        :param scheduled_at: scheduled_at
        :type scheduled_at: str
        :param slug: slug
        :type slug: str
        :param status: status
        :type status: MatchStatus
        :param streams_list: streams_list
        :type streams_list: List[Stream]
        :param tournament_id: tournament_id
        :type tournament_id: int
        :param winner_id: winner_id
        :type winner_id: BracketWinnerId
        :param winner_type: winner_type
        :type winner_type: MatchWinnerType
        """
        self.begin_at = self._define_str(
            "begin_at", begin_at, nullable=True, min_length=1
        )
        self.detailed_stats = detailed_stats
        self.draw = draw
        self.end_at = self._define_str("end_at", end_at, nullable=True, min_length=1)
        self.forfeit = forfeit
        self.game_advantage = self._define_number(
            "game_advantage", game_advantage, nullable=True, ge=1
        )
        self.games = self._define_list(games, Game)
        self.id_ = self._define_number("id_", id_, ge=1)
        self.live = self._define_object(live, MatchLive)
        self.match_type = self._enum_matching(
            match_type, MatchType.list(), "match_type"
        )
        self.modified_at = self._define_str("modified_at", modified_at, min_length=1)
        self.name = name
        self.number_of_games = self._define_number(
            "number_of_games", number_of_games, ge=0
        )
        self.opponents = self._define_list(opponents, Opponent)
        self.original_scheduled_at = self._define_str(
            "original_scheduled_at", original_scheduled_at, nullable=True, min_length=1
        )
        self.previous_matches = self._define_list(previous_matches, PreviousMatch)
        self.results = self._define_list(results, MatchResult)
        self.scheduled_at = self._define_str(
            "scheduled_at", scheduled_at, nullable=True, min_length=1
        )
        self.slug = self._define_str(
            "slug", slug, nullable=True, pattern="^[ a-zA-Z0-9_-]+$", min_length=1
        )
        self.status = self._enum_matching(status, MatchStatus.list(), "status")
        self.streams_list = self._define_list(streams_list, Stream)
        self.tournament_id = self._define_number("tournament_id", tournament_id, ge=1)
        self.winner_id = BracketWinnerIdGuard.return_one_of(winner_id)
        self.winner_type = self._enum_matching(
            winner_type, MatchWinnerType.list(), "winner_type"
        )
