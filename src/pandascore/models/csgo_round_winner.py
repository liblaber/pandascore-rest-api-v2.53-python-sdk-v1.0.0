from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .csgo_round_side import CsgoRoundSide


@JsonMap({"id_": "id"})
class CsgoRoundWinner(BaseModel):
    """CsgoRoundWinner

    :param id_: id_
    :type id_: int
    :param side: side
    :type side: CsgoRoundSide
    """

    def __init__(self, id_: int, side: CsgoRoundSide):
        self.id_ = id_
        self.side = self._enum_matching(side, CsgoRoundSide.list(), "side")
