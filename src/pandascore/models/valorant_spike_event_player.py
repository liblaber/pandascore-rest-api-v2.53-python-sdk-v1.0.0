from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .valorant_event_player import ValorantEventPlayer


@JsonMap({})
class ValorantSpikeEventPlayer(BaseModel):
    """ValorantSpikeEventPlayer

    :param player: player
    :type player: ValorantEventPlayer
    """

    def __init__(self, player: ValorantEventPlayer):
        self.player = self._define_object(player, ValorantEventPlayer)
