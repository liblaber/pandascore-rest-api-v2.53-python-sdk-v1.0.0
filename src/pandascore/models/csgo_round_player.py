from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .csgo_round_side import CsgoRoundSide


@JsonMap({"id_": "id"})
class CsgoRoundPlayer(BaseModel):
    """CsgoRoundPlayer

    :param id_: ID of the player
    :type id_: int
    :param name: Professional name of the player
    :type name: str
    :param team_side: team_side
    :type team_side: CsgoRoundSide
    """

    def __init__(self, id_: int, name: str, team_side: CsgoRoundSide):
        self.id_ = id_
        self.name = name
        self.team_side = self._enum_matching(
            team_side, CsgoRoundSide.list(), "team_side"
        )
