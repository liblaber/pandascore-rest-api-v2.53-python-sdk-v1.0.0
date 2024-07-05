from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .csgo_round_player import CsgoRoundPlayer
from .csgo_round_side import CsgoRoundSide


@JsonMap({"id_": "id"})
class Killer(BaseModel):
    """Killer

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


@JsonMap({})
class CsgoKillEventDetails(BaseModel):
    """CsgoKillEventDetails

    :param killer: killer
    :type killer: Killer
    :param victim: victim
    :type victim: CsgoRoundPlayer
    """

    def __init__(self, killer: Killer, victim: CsgoRoundPlayer):
        self.killer = self._define_object(killer, Killer)
        self.victim = self._define_object(victim, CsgoRoundPlayer)
