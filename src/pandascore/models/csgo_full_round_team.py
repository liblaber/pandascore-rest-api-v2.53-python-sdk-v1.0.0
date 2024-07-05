from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .csgo_full_round_team_player import CsgoFullRoundTeamPlayer


@JsonMap({})
class CsgoFullRoundTeam(BaseModel):
    """CsgoFullRoundTeam

    :param players: players
    :type players: List[CsgoFullRoundTeamPlayer]
    :param round_score: The round score for the team.
    :type round_score: int
    :param team_id: team_id
    :type team_id: int
    :param team_name: The name of the team.
    :type team_name: str
    """

    def __init__(
        self,
        players: List[CsgoFullRoundTeamPlayer],
        round_score: int,
        team_id: int,
        team_name: str,
    ):
        self.players = self._define_list(players, CsgoFullRoundTeamPlayer)
        self.round_score = round_score
        self.team_id = team_id
        self.team_name = team_name
