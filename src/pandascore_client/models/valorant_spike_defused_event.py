# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .valorant_spike_event_player import ValorantSpikeEventPlayer
from .valorant_event_type import ValorantEventType


@JsonMap({"type_": "type"})
class ValorantSpikeDefusedEvent(BaseModel):
    """ValorantSpikeDefusedEvent

    :param number: number
    :type number: int
    :param spike_defused: spike_defused
    :type spike_defused: ValorantSpikeEventPlayer
    :param timestamp: Time elapsed since the beginning of round, in seconds
    :type timestamp: int
    :param type_: type_
    :type type_: ValorantEventType
    """

    def __init__(
        self,
        number: int,
        spike_defused: ValorantSpikeEventPlayer,
        timestamp: int,
        type_: ValorantEventType,
    ):
        """ValorantSpikeDefusedEvent

        :param number: number
        :type number: int
        :param spike_defused: spike_defused
        :type spike_defused: ValorantSpikeEventPlayer
        :param timestamp: Time elapsed since the beginning of round, in seconds
        :type timestamp: int
        :param type_: type_
        :type type_: ValorantEventType
        """
        self.number = self._define_number("number", number, ge=1)
        self.spike_defused = self._define_object(
            spike_defused, ValorantSpikeEventPlayer
        )
        self.timestamp = self._define_number("timestamp", timestamp, ge=0)
        self.type_ = self._enum_matching(type_, ValorantEventType.list(), "type_")
