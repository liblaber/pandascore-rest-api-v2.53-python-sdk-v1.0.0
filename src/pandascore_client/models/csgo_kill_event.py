# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
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
        self.ingame_timestamp = self._define_number(
            "ingame_timestamp", ingame_timestamp, ge=0
        )
        self.kill = self._define_object(kill, CsgoKillEventDetails)
        self.round_number = self._define_number("round_number", round_number, ge=1)
        self.type_ = self._enum_matching(type_, CsgoEventType.list(), "type_")
