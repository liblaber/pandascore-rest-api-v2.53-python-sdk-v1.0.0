from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_event_payload import LoLEventPayload
from .lo_l_event_type import LoLEventType


@JsonMap({"type_": "type"})
class LoLGameEvent(BaseModel):
    """LoLGameEvent

    :param game_id: LoL game ID
    :type game_id: int
    :param ingame_timestamp: ingame_timestamp
    :type ingame_timestamp: int
    :param is_first: Whether event is first of its kind to happen
    :type is_first: bool
    :param match_id: match_id
    :type match_id: int
    :param payload: payload
    :type payload: LoLEventPayload
    :param tournament_id: tournament_id
    :type tournament_id: int
    :param type_: type_
    :type type_: LoLEventType
    """

    def __init__(
        self,
        game_id: int,
        ingame_timestamp: int,
        is_first: bool,
        match_id: int,
        payload: LoLEventPayload,
        tournament_id: int,
        type_: LoLEventType,
    ):
        self.game_id = game_id
        self.ingame_timestamp = ingame_timestamp
        self.is_first = is_first
        self.match_id = match_id
        self.payload = self._define_object(payload, LoLEventPayload)
        self.tournament_id = tournament_id
        self.type_ = self._enum_matching(type_, LoLEventType.list(), "type_")
