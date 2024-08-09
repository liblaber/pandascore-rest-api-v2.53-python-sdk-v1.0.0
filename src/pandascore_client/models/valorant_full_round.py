# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .valorant_full_round_attacker_team import ValorantFullRoundAttackerTeam
from .valorant_full_round_defender_team import ValorantFullRoundDefenderTeam
from .valorant_game_round_outcome import ValorantGameRoundOutcome
from .valorant_game_round_winner import ValorantGameRoundWinner


@JsonMap({})
class ValorantFullRound(BaseModel):
    """ValorantFullRound

    :param attackers: attackers
    :type attackers: ValorantFullRoundAttackerTeam
    :param defenders: defenders
    :type defenders: ValorantFullRoundDefenderTeam
    :param number: number
    :type number: int
    :param outcome: How was the round finished. <br/>`spike_exploded`: spike exploded <br/>`defenders_eliminated`: attackers killed all defenders <br/>`spike_defused`: spike defused <br/>`attack_timeout`: attackers failed to plant the spike in time <br/>`attackers_eliminated`: defenders killed all attackers
    :type outcome: ValorantGameRoundOutcome
    :param winner_team: winner_team
    :type winner_team: ValorantGameRoundWinner
    """

    def __init__(
        self,
        attackers: ValorantFullRoundAttackerTeam,
        defenders: ValorantFullRoundDefenderTeam,
        number: int,
        outcome: ValorantGameRoundOutcome,
        winner_team: ValorantGameRoundWinner,
    ):
        """ValorantFullRound

        :param attackers: attackers
        :type attackers: ValorantFullRoundAttackerTeam
        :param defenders: defenders
        :type defenders: ValorantFullRoundDefenderTeam
        :param number: number
        :type number: int
        :param outcome: How was the round finished. <br/>`spike_exploded`: spike exploded <br/>`defenders_eliminated`: attackers killed all defenders <br/>`spike_defused`: spike defused <br/>`attack_timeout`: attackers failed to plant the spike in time <br/>`attackers_eliminated`: defenders killed all attackers
        :type outcome: ValorantGameRoundOutcome
        :param winner_team: winner_team
        :type winner_team: ValorantGameRoundWinner
        """
        self.attackers = self._define_object(attackers, ValorantFullRoundAttackerTeam)
        self.defenders = self._define_object(defenders, ValorantFullRoundDefenderTeam)
        self.number = self._define_number("number", number, ge=1)
        self.outcome = self._enum_matching(
            outcome, ValorantGameRoundOutcome.list(), "outcome"
        )
        self.winner_team = self._define_object(winner_team, ValorantGameRoundWinner)