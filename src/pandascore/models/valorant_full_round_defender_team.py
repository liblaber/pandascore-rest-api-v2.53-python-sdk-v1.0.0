from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .valorant_full_round_player import ValorantFullRoundPlayer


@JsonMap({})
class ValorantFullRoundDefenderTeam(BaseModel):
    """ValorantFullRoundDefenderTeam

    :param players: players
    :type players: List[ValorantFullRoundPlayer]
    :param score: Defenders score at the beginning of the round
    :type score: int
    :param team_id: ID of the defenders team
    :type team_id: int
    """

    def __init__(
        self, players: List[ValorantFullRoundPlayer], score: int, team_id: int
    ):
        self.players = self._define_list(players, ValorantFullRoundPlayer)
        self.score = score
        self.team_id = team_id
