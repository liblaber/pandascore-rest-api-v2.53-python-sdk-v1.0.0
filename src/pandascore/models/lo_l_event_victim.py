from __future__ import annotations
from typing import Union
from .base import OneOfBaseModel
from .lo_l_event_drake import LoLEventDrake
from .lo_l_event_herald import LoLEventHerald
from .lo_l_event_nashor import LoLEventNashor
from .lo_l_event_player import LoLEventPlayer
from .lo_l_event_tower import LoLEventTower
from .lo_l_event_inhibitor import LoLEventInhibitor
from .lo_l_event_voidgrub import LoLEventVoidgrub
from .lo_l_event_unknown import LoLEventUnknown


class LoLEventVictimGuard(OneOfBaseModel):
    class_list = {
        "LoLEventDrake": LoLEventDrake,
        "LoLEventHerald": LoLEventHerald,
        "LoLEventNashor": LoLEventNashor,
        "LoLEventPlayer": LoLEventPlayer,
        "LoLEventTower": LoLEventTower,
        "LoLEventInhibitor": LoLEventInhibitor,
        "LoLEventVoidgrub": LoLEventVoidgrub,
        "LoLEventUnknown": LoLEventUnknown,
    }


LoLEventVictim = Union[
    LoLEventDrake,
    LoLEventHerald,
    LoLEventNashor,
    LoLEventPlayer,
    LoLEventTower,
    LoLEventInhibitor,
    LoLEventVoidgrub,
    LoLEventUnknown,
]
