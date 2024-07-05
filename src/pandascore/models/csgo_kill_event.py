from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .csgo_kill_event_details import CsgoKillEventDetails
from .csgo_event_type import CsgoEventType


@JsonMap({"type_": "type"})
class CsgoKillEvent(BaseModel):
    """CsgoKillEvent

    :param ingame_timestamp: Time elapsed since the beginning of the game, in milliseconds
    :type ingame_timestamp: int
    :param kill: kill
    :type kill: CsgoKillEventDetails
    :param round_number: round_number
    :type round_number: int
    :param type_: type_
    :type type_: CsgoEventType
    """

    def __init__(
        self,
        ingame_timestamp: int,
        kill: CsgoKillEventDetails,
        round_number: int,
        type_: CsgoEventType,
    ):
        self.ingame_timestamp = ingame_timestamp
        self.kill = self._define_object(kill, CsgoKillEventDetails)
        self.round_number = round_number
        self.type_ = self._enum_matching(type_, CsgoEventType.list(), "type_")
