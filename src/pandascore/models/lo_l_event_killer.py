from __future__ import annotations
from typing import Union
from .base import OneOfBaseModel
from .lo_l_event_drake import LoLEventDrake
from .lo_l_event_herald import LoLEventHerald
from .lo_l_event_minion import LoLEventMinion
from .lo_l_event_nashor import LoLEventNashor
from .lo_l_event_player import LoLEventPlayer
from .lo_l_event_tower import LoLEventTower
from .lo_l_event_neutral_minion import LoLEventNeutralMinion
from .lo_l_event_voidgrub import LoLEventVoidgrub
from .lo_l_event_unknown import LoLEventUnknown


class LoLEventKillerGuard(OneOfBaseModel):
    class_list = {
        "LoLEventDrake": LoLEventDrake,
        "LoLEventHerald": LoLEventHerald,
        "LoLEventMinion": LoLEventMinion,
        "LoLEventNashor": LoLEventNashor,
        "LoLEventPlayer": LoLEventPlayer,
        "LoLEventTower": LoLEventTower,
        "LoLEventNeutralMinion": LoLEventNeutralMinion,
        "LoLEventVoidgrub": LoLEventVoidgrub,
        "LoLEventUnknown": LoLEventUnknown,
    }


LoLEventKiller = Union[
    LoLEventDrake,
    LoLEventHerald,
    LoLEventMinion,
    LoLEventNashor,
    LoLEventPlayer,
    LoLEventTower,
    LoLEventNeutralMinion,
    LoLEventVoidgrub,
    LoLEventUnknown,
]
