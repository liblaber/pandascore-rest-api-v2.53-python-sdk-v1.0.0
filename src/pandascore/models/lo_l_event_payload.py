from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_event_player import LoLEventPlayer
from .lo_l_event_killer import LoLEventKiller, LoLEventKillerGuard
from .lo_l_event_drake import LoLEventDrake
from .lo_l_event_herald import LoLEventHerald
from .lo_l_event_minion import LoLEventMinion
from .lo_l_event_nashor import LoLEventNashor
from .lo_l_event_tower import LoLEventTower
from .lo_l_event_neutral_minion import LoLEventNeutralMinion
from .lo_l_event_voidgrub import LoLEventVoidgrub
from .lo_l_event_unknown import LoLEventUnknown
from .lo_l_event_victim import LoLEventVictim, LoLEventVictimGuard
from .lo_l_event_inhibitor import LoLEventInhibitor


@JsonMap({})
class LoLEventPayload(BaseModel):
    """LoLEventPayload

    :param assists: assists
    :type assists: List[LoLEventPlayer]
    :param killer: killer
    :type killer: LoLEventKiller
    :param victim: victim
    :type victim: LoLEventVictim
    """

    def __init__(
        self,
        assists: List[LoLEventPlayer],
        killer: LoLEventKiller,
        victim: LoLEventVictim,
    ):
        self.assists = self._define_list(assists, LoLEventPlayer)
        self.killer = LoLEventKillerGuard.return_one_of(killer)
        self.victim = LoLEventVictimGuard.return_one_of(victim)
