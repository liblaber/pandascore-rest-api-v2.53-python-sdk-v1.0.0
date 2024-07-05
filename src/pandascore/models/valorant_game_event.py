from __future__ import annotations
from typing import Union
from .base import OneOfBaseModel
from .valorant_kill_event import ValorantKillEvent
from .valorant_spike_planted_event import ValorantSpikePlantedEvent
from .valorant_spike_defused_event import ValorantSpikeDefusedEvent


class ValorantGameEventGuard(OneOfBaseModel):
    class_list = {
        "ValorantKillEvent": ValorantKillEvent,
        "ValorantSpikePlantedEvent": ValorantSpikePlantedEvent,
        "ValorantSpikeDefusedEvent": ValorantSpikeDefusedEvent,
    }


ValorantGameEvent = Union[
    ValorantKillEvent, ValorantSpikePlantedEvent, ValorantSpikeDefusedEvent
]
