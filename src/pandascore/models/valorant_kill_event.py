from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .valorant_kill_event_details import ValorantKillEventDetails
from .valorant_event_type import ValorantEventType


@JsonMap({"type_": "type"})
class ValorantKillEvent(BaseModel):
    """ValorantKillEvent

    :param kill: kill
    :type kill: ValorantKillEventDetails
    :param number: number
    :type number: int
    :param timestamp: Time elapsed since the beginning of round, in seconds
    :type timestamp: int
    :param type_: type_
    :type type_: ValorantEventType
    """

    def __init__(
        self,
        kill: ValorantKillEventDetails,
        number: int,
        timestamp: int,
        type_: ValorantEventType,
    ):
        self.kill = self._define_object(kill, ValorantKillEventDetails)
        self.number = number
        self.timestamp = timestamp
        self.type_ = self._enum_matching(type_, ValorantEventType.list(), "type_")
