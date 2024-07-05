from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .csgo_outcome import CsgoOutcome
from .csgo_side import CsgoSide


@JsonMap({})
class CsgoRound(BaseModel):
    """CsgoRound

    :param ct: ct
    :type ct: int
    :param outcome: outcome
    :type outcome: CsgoOutcome
    :param round: round
    :type round: int
    :param terrorists: terrorists
    :type terrorists: int
    :param winner_side: winner_side
    :type winner_side: CsgoSide
    :param winner_team: winner_team
    :type winner_team: int
    """

    def __init__(
        self,
        ct: int,
        outcome: CsgoOutcome,
        round: int,
        terrorists: int,
        winner_side: CsgoSide,
        winner_team: int,
    ):
        self.ct = ct
        self.outcome = self._enum_matching(outcome, CsgoOutcome.list(), "outcome")
        self.round = round
        self.terrorists = terrorists
        self.winner_side = self._enum_matching(
            winner_side, CsgoSide.list(), "winner_side"
        )
        self.winner_team = winner_team
