from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .csgo_round_start_event_details import CsgoRoundStartEventDetails
from .csgo_event_type import CsgoEventType


@JsonMap({"type_": "type"})
class CsgoRoundStartEvent(BaseModel):
    """CsgoRoundStartEvent

    :param ingame_timestamp: Time elapsed since the beginning of the game, in milliseconds
    :type ingame_timestamp: int
    :param round_number: round_number
    :type round_number: int
    :param round_start: round_start
    :type round_start: CsgoRoundStartEventDetails
    :param type_: type_
    :type type_: CsgoEventType
    """

    def __init__(
        self,
        ingame_timestamp: int,
        round_number: int,
        round_start: CsgoRoundStartEventDetails,
        type_: CsgoEventType,
    ):
        self.ingame_timestamp = ingame_timestamp
        self.round_number = round_number
        self.round_start = self._define_object(round_start, CsgoRoundStartEventDetails)
        self.type_ = self._enum_matching(type_, CsgoEventType.list(), "type_")
