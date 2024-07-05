from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .game_status import GameStatus


@JsonMap({"id_": "id"})
class RangeOverCsgoGames(BaseModel):
    """RangeOverCsgoGames

    :param begin_at: begin_at, defaults to None
    :type begin_at: List[str], optional
    :param complete: complete, defaults to None
    :type complete: List[bool], optional
    :param detailed_stats: detailed_stats, defaults to None
    :type detailed_stats: List[bool], optional
    :param end_at: end_at, defaults to None
    :type end_at: List[str], optional
    :param finished: finished, defaults to None
    :type finished: List[bool], optional
    :param forfeit: forfeit, defaults to None
    :type forfeit: List[bool], optional
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
    """

    def __init__(
        self,
        begin_at: List[str] = None,
        complete: List[bool] = None,
        detailed_stats: List[bool] = None,
        end_at: List[str] = None,
        finished: List[bool] = None,
        forfeit: List[bool] = None,
        id_: List[int] = None,
        length: List[int] = None,
        match_id: List[int] = None,
        position: List[int] = None,
        status: List[GameStatus] = None,
    ):
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
