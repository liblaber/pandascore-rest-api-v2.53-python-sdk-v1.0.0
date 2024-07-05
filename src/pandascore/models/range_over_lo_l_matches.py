from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .match_type import MatchType
from .match_status import MatchStatus
from .opponent_id import OpponentId, OpponentIdGuard
from .match_winner_type import MatchWinnerType


@JsonMap({"id_": "id"})
class RangeOverLoLMatches(BaseModel):
    """RangeOverLoLMatches

    :param begin_at: begin_at, defaults to None
    :type begin_at: List[str], optional
    :param detailed_stats: detailed_stats, defaults to None
    :type detailed_stats: List[bool], optional
    :param draw: draw, defaults to None
    :type draw: List[bool], optional
    :param end_at: end_at, defaults to None
    :type end_at: List[str], optional
    :param forfeit: forfeit, defaults to None
    :type forfeit: List[bool], optional
    :param id_: id_, defaults to None
    :type id_: List[int], optional
    :param match_type: match_type, defaults to None
    :type match_type: List[MatchType], optional
    :param modified_at: modified_at, defaults to None
    :type modified_at: List[str], optional
    :param name: name, defaults to None
    :type name: List[str], optional
    :param number_of_games: number_of_games, defaults to None
    :type number_of_games: List[int], optional
    :param scheduled_at: scheduled_at, defaults to None
    :type scheduled_at: List[str], optional
    :param slug: slug, defaults to None
    :type slug: List[str], optional
    :param status: status, defaults to None
    :type status: List[MatchStatus], optional
    :param tournament_id: tournament_id, defaults to None
    :type tournament_id: List[int], optional
    :param winner_id: winner_id, defaults to None
    :type winner_id: List[OpponentId], optional
    :param winner_type: winner_type, defaults to None
    :type winner_type: List[MatchWinnerType], optional
    """

    def __init__(
        self,
        begin_at: List[str] = None,
        detailed_stats: List[bool] = None,
        draw: List[bool] = None,
        end_at: List[str] = None,
        forfeit: List[bool] = None,
        id_: List[int] = None,
        match_type: List[MatchType] = None,
        modified_at: List[str] = None,
        name: List[str] = None,
        number_of_games: List[int] = None,
        scheduled_at: List[str] = None,
        slug: List[str] = None,
        status: List[MatchStatus] = None,
        tournament_id: List[int] = None,
        winner_id: List[OpponentId] = None,
        winner_type: List[MatchWinnerType] = None,
    ):
        if begin_at is not None:
            self.begin_at = begin_at
        if detailed_stats is not None:
            self.detailed_stats = detailed_stats
        if draw is not None:
            self.draw = draw
        if end_at is not None:
            self.end_at = end_at
        if forfeit is not None:
            self.forfeit = forfeit
        if id_ is not None:
            self.id_ = id_
        if match_type is not None:
            self.match_type = self._define_list(match_type, MatchType)
        if modified_at is not None:
            self.modified_at = modified_at
        if name is not None:
            self.name = name
        if number_of_games is not None:
            self.number_of_games = number_of_games
        if scheduled_at is not None:
            self.scheduled_at = scheduled_at
        if slug is not None:
            self.slug = slug
        if status is not None:
            self.status = self._define_list(status, MatchStatus)
        if tournament_id is not None:
            self.tournament_id = tournament_id
        if winner_id is not None:
            self.winner_id = self._define_list(winner_id, OpponentId)
        if winner_type is not None:
            self.winner_type = self._define_list(winner_type, MatchWinnerType)
