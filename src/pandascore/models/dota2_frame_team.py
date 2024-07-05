from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .dota2_frame_player import Dota2FramePlayer


@JsonMap({"id_": "id"})
class Dota2FrameTeam(BaseModel):
    """Dota2FrameTeam

    :param gold_advantage: Gold advantage of the team (negative if deficit)
    :type gold_advantage: float
    :param id_: id_
    :type id_: int
    :param name: The name of the team.
    :type name: str
    :param players: The players of the team
    :type players: List[Dota2FramePlayer]
    :param xp_advantage: Experience advantage of the team (negative if deficit)
    :type xp_advantage: float
    """

    def __init__(
        self,
        gold_advantage: float,
        id_: int,
        name: str,
        players: List[Dota2FramePlayer],
        xp_advantage: float,
    ):
        self.gold_advantage = gold_advantage
        self.id_ = id_
        self.name = name
        self.players = self._define_list(players, Dota2FramePlayer)
        self.xp_advantage = xp_advantage
