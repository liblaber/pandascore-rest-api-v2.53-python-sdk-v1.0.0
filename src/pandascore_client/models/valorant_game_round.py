# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .valorant_game_round_attacker import ValorantGameRoundAttacker
from .valorant_game_round_defender import ValorantGameRoundDefender
from .valorant_game_round_outcome import ValorantGameRoundOutcome
from .valorant_game_round_winner import ValorantGameRoundWinner


@JsonMap({})
class ValorantGameRound(BaseModel):
    """ValorantGameRound

    :param attackers: attackers
    :type attackers: ValorantGameRoundAttacker
    :param defenders: defenders
    :type defenders: ValorantGameRoundDefender
    :param number: The round number, starting at 1
    :type number: float
    :param outcome: How was the round finished. <br/>`spike_exploded`: spike exploded <br/>`defenders_eliminated`: attackers killed all defenders <br/>`spike_defused`: spike defused <br/>`attack_timeout`: attackers failed to plant the spike in time <br/>`attackers_eliminated`: defenders killed all attackers
    :type outcome: ValorantGameRoundOutcome
    :param winner_team: winner_team
    :type winner_team: ValorantGameRoundWinner
    """

    def __init__(
        self,
        attackers: ValorantGameRoundAttacker,
        defenders: ValorantGameRoundDefender,
        number: float,
        outcome: ValorantGameRoundOutcome,
        winner_team: ValorantGameRoundWinner,
    ):
        """ValorantGameRound

        :param attackers: attackers
        :type attackers: ValorantGameRoundAttacker
        :param defenders: defenders
        :type defenders: ValorantGameRoundDefender
        :param number: The round number, starting at 1
        :type number: float
        :param outcome: How was the round finished. <br/>`spike_exploded`: spike exploded <br/>`defenders_eliminated`: attackers killed all defenders <br/>`spike_defused`: spike defused <br/>`attack_timeout`: attackers failed to plant the spike in time <br/>`attackers_eliminated`: defenders killed all attackers
        :type outcome: ValorantGameRoundOutcome
        :param winner_team: winner_team
        :type winner_team: ValorantGameRoundWinner
        """
        self.attackers = self._define_object(attackers, ValorantGameRoundAttacker)
        self.defenders = self._define_object(defenders, ValorantGameRoundDefender)
        self.number = self._define_number("number", number, ge=0)
        self.outcome = self._enum_matching(
            outcome, ValorantGameRoundOutcome.list(), "outcome"
        )
        self.winner_team = self._define_object(winner_team, ValorantGameRoundWinner)
