from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class LoLTeamRatios(BaseModel):
    """LoLTeamRatios

    :param first_baron: first_baron
    :type first_baron: float
    :param first_blood: first_blood
    :type first_blood: float
    :param first_dragon: first_dragon
    :type first_dragon: float
    :param first_herald: first_herald
    :type first_herald: float
    :param first_inhibitor: first_inhibitor
    :type first_inhibitor: float
    :param first_tower: first_tower
    :type first_tower: float
    :param first_voidgrub: Whether the team killed the first voidgrub.
    :type first_voidgrub: float
    :param win: win
    :type win: float
    """

    def __init__(
        self,
        first_baron: float,
        first_blood: float,
        first_dragon: float,
        first_herald: float,
        first_inhibitor: float,
        first_tower: float,
        first_voidgrub: float,
        win: float,
    ):
        self.first_baron = first_baron
        self.first_blood = first_blood
        self.first_dragon = first_dragon
        self.first_herald = first_herald
        self.first_inhibitor = first_inhibitor
        self.first_tower = first_tower
        self.first_voidgrub = first_voidgrub
        self.win = win
