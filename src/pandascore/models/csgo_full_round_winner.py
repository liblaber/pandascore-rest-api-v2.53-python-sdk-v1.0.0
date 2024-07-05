from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .csgo_round_side import CsgoRoundSide


@JsonMap({})
class CsgoFullRoundWinner(BaseModel):
    """CsgoFullRoundWinner

    :param side: side
    :type side: CsgoRoundSide
    :param team_id: team_id
    :type team_id: int
    :param team_name: The name of the team.
    :type team_name: str
    """

    def __init__(self, side: CsgoRoundSide, team_id: int, team_name: str):
        self.side = self._enum_matching(side, CsgoRoundSide.list(), "side")
        self.team_id = team_id
        self.team_name = team_name
