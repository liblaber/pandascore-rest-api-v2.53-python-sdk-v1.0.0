from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .csgo_outcome import CsgoOutcome
from .csgo_round_winner import CsgoRoundWinner


@JsonMap({})
class CsgoRoundEndEventDetails(BaseModel):
    """CsgoRoundEndEventDetails

    :param outcome: outcome
    :type outcome: CsgoOutcome
    :param winner_team: winner_team
    :type winner_team: CsgoRoundWinner
    """

    def __init__(self, outcome: CsgoOutcome, winner_team: CsgoRoundWinner):
        self.outcome = self._enum_matching(outcome, CsgoOutcome.list(), "outcome")
        self.winner_team = self._define_object(winner_team, CsgoRoundWinner)
