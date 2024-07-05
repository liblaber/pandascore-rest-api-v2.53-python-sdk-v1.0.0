from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .csgo_full_round_team import CsgoFullRoundTeam
from .csgo_full_round_map import CsgoFullRoundMap
from .csgo_outcome import CsgoOutcome
from .csgo_full_round_winner import CsgoFullRoundWinner


@JsonMap({})
class CsgoFullRound(BaseModel):
    """CsgoFullRound

    :param counter_terrorists: counter_terrorists
    :type counter_terrorists: CsgoFullRoundTeam
    :param map: The location selected during the picks and bans phase for the game.
    :type map: CsgoFullRoundMap
    :param number: number
    :type number: int
    :param outcome: outcome
    :type outcome: CsgoOutcome
    :param terrorists: terrorists
    :type terrorists: CsgoFullRoundTeam
    :param winner_team: winner_team
    :type winner_team: CsgoFullRoundWinner
    """

    def __init__(
        self,
        counter_terrorists: CsgoFullRoundTeam,
        map: CsgoFullRoundMap,
        number: int,
        outcome: CsgoOutcome,
        terrorists: CsgoFullRoundTeam,
        winner_team: CsgoFullRoundWinner,
    ):
        self.counter_terrorists = self._define_object(
            counter_terrorists, CsgoFullRoundTeam
        )
        self.map = self._define_object(map, CsgoFullRoundMap)
        self.number = number
        self.outcome = self._enum_matching(outcome, CsgoOutcome.list(), "outcome")
        self.terrorists = self._define_object(terrorists, CsgoFullRoundTeam)
        self.winner_team = self._define_object(winner_team, CsgoFullRoundWinner)
