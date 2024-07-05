from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class LoLKillsSeries(BaseModel):
    """LoLKillsSeries

    :param double_kills: double_kills
    :type double_kills: int
    :param penta_kills: penta_kills
    :type penta_kills: int
    :param quadra_kills: quadra_kills
    :type quadra_kills: int
    :param triple_kills: triple_kills
    :type triple_kills: int
    """

    def __init__(
        self, double_kills: int, penta_kills: int, quadra_kills: int, triple_kills: int
    ):
        self.double_kills = double_kills
        self.penta_kills = penta_kills
        self.quadra_kills = quadra_kills
        self.triple_kills = triple_kills
