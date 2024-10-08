# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
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
        """CsgoRoundPlayer

        :param id_: ID of the player
        :type id_: int
        :param name: Professional name of the player
        :type name: str
        :param team_side: team_side
        :type team_side: CsgoRoundSide
        """
        self.id_ = self._define_number("id_", id_, ge=1)
        self.name = name
        self.team_side = self._enum_matching(
            team_side, CsgoRoundSide.list(), "team_side"
        )
