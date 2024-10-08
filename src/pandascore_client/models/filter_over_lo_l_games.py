# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .game_status import GameStatus
from .opponent_type import OpponentType


@JsonMap({"id_": "id"})
class FilterOverLoLGames(BaseModel):
    """FilterOverLoLGames

    :param begin_at: begin_at, defaults to None
    :type begin_at: List[str], optional
    :param complete: Whether When `true`, the game statistics are complete and will not be updated again, defaults to None
    :type complete: bool, optional
    :param detailed_stats: Whether historical data is available for the game, defaults to None
    :type detailed_stats: bool, optional
    :param end_at: end_at, defaults to None
    :type end_at: List[str], optional
    :param finished: Whether the game is finished, defaults to None
    :type finished: bool, optional
    :param forfeit: Whether the game has been forfeited, defaults to None
    :type forfeit: bool, optional
    :param id_: id_, defaults to None
    :type id_: List[int], optional
    :param length: length, defaults to None
    :type length: List[int], optional
    :param match_id: match_id, defaults to None
    :type match_id: List[int], optional
    :param position: position, defaults to None
    :type position: List[int], optional
    :param status: status, defaults to None
    :type status: List[GameStatus], optional
    :param winner_type: winner_type, defaults to None
    :type winner_type: List[OpponentType], optional
    """

    def __init__(
        self,
        begin_at: List[str] = None,
        complete: bool = None,
        detailed_stats: bool = None,
        end_at: List[str] = None,
        finished: bool = None,
        forfeit: bool = None,
        id_: List[int] = None,
        length: List[int] = None,
        match_id: List[int] = None,
        position: List[int] = None,
        status: List[GameStatus] = None,
        winner_type: List[OpponentType] = None,
    ):
        """FilterOverLoLGames

        :param begin_at: begin_at, defaults to None
        :type begin_at: List[str], optional
        :param complete: Whether When `true`, the game statistics are complete and will not be updated again, defaults to None
        :type complete: bool, optional
        :param detailed_stats: Whether historical data is available for the game, defaults to None
        :type detailed_stats: bool, optional
        :param end_at: end_at, defaults to None
        :type end_at: List[str], optional
        :param finished: Whether the game is finished, defaults to None
        :type finished: bool, optional
        :param forfeit: Whether the game has been forfeited, defaults to None
        :type forfeit: bool, optional
        :param id_: id_, defaults to None
        :type id_: List[int], optional
        :param length: length, defaults to None
        :type length: List[int], optional
        :param match_id: match_id, defaults to None
        :type match_id: List[int], optional
        :param position: position, defaults to None
        :type position: List[int], optional
        :param status: status, defaults to None
        :type status: List[GameStatus], optional
        :param winner_type: winner_type, defaults to None
        :type winner_type: List[OpponentType], optional
        """
        if begin_at is not None:
            self.begin_at = begin_at
        if complete is not None:
            self.complete = complete
        if detailed_stats is not None:
            self.detailed_stats = detailed_stats
        if end_at is not None:
            self.end_at = end_at
        if finished is not None:
            self.finished = finished
        if forfeit is not None:
            self.forfeit = forfeit
        if id_ is not None:
            self.id_ = id_
        if length is not None:
            self.length = length
        if match_id is not None:
            self.match_id = match_id
        if position is not None:
            self.position = position
        if status is not None:
            self.status = self._define_list(status, GameStatus)
        if winner_type is not None:
            self.winner_type = self._define_list(winner_type, OpponentType)
