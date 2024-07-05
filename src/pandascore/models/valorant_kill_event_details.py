from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .valorant_event_killer import ValorantEventKiller
from .valorant_event_victim import ValorantEventVictim


@JsonMap({})
class ValorantKillEventDetails(BaseModel):
    """ValorantKillEventDetails

    :param bomb_kill: Whether the kill was caused by the bomb
    :type bomb_kill: bool
    :param killer: killer
    :type killer: ValorantEventKiller
    :param victim: victim
    :type victim: ValorantEventVictim
    """

    def __init__(
        self, bomb_kill: bool, killer: ValorantEventKiller, victim: ValorantEventVictim
    ):
        self.bomb_kill = bomb_kill
        self.killer = self._define_object(killer, ValorantEventKiller)
        self.victim = self._define_object(victim, ValorantEventVictim)
