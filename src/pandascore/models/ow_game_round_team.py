from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .ow_game_round_player import OwGameRoundPlayer
from .base_team import BaseTeam


@JsonMap({})
class OwGameRoundTeam(BaseModel):
    """OwGameRoundTeam

    :param players: players
    :type players: List[OwGameRoundPlayer]
    :param team: team
    :type team: BaseTeam
    """

    def __init__(self, players: List[OwGameRoundPlayer], team: BaseTeam):
        self.players = self._define_list(players, OwGameRoundPlayer)
        self.team = self._define_object(team, BaseTeam)
