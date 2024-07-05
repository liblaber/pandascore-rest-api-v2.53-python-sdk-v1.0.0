from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .valorant_team_side import ValorantTeamSide


@JsonMap({"id_": "id"})
class ValorantGameRoundWinner(BaseModel):
    """ValorantGameRoundWinner

    :param id_: ID of the team that won the round
    :type id_: int
    :param side: Team side in the round
    :type side: ValorantTeamSide
    """

    def __init__(self, id_: int, side: ValorantTeamSide):
        self.id_ = id_
        self.side = self._enum_matching(side, ValorantTeamSide.list(), "side")
