from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .csgo_rounds_score import CsgoRoundsScore


@JsonMap({})
class CsgoRoundStartEventDetails(BaseModel):
    """CsgoRoundStartEventDetails

    :param counter_terrorists: counter_terrorists
    :type counter_terrorists: CsgoRoundsScore
    :param terrorists: terrorists
    :type terrorists: CsgoRoundsScore
    """

    def __init__(
        self, counter_terrorists: CsgoRoundsScore, terrorists: CsgoRoundsScore
    ):
        self.counter_terrorists = self._define_object(
            counter_terrorists, CsgoRoundsScore
        )
        self.terrorists = self._define_object(terrorists, CsgoRoundsScore)
