from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .valorant_spike_event_player import ValorantSpikeEventPlayer
from .valorant_event_type import ValorantEventType


@JsonMap({"type_": "type"})
class ValorantSpikePlantedEvent(BaseModel):
    """ValorantSpikePlantedEvent

    :param number: number
    :type number: int
    :param spike_planted: spike_planted
    :type spike_planted: ValorantSpikeEventPlayer
    :param timestamp: Time elapsed since the beginning of round, in seconds
    :type timestamp: int
    :param type_: type_
    :type type_: ValorantEventType
    """

    def __init__(
        self,
        number: int,
        spike_planted: ValorantSpikeEventPlayer,
        timestamp: int,
        type_: ValorantEventType,
    ):
        self.number = number
        self.spike_planted = self._define_object(
            spike_planted, ValorantSpikeEventPlayer
        )
        self.timestamp = timestamp
        self.type_ = self._enum_matching(type_, ValorantEventType.list(), "type_")
