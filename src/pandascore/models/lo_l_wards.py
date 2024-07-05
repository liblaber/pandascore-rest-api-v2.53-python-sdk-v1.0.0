from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class LoLWards(BaseModel):
    """LoLWards

    :param placed: placed
    :type placed: int
    :param sight_wards_bought_in_game: sight_wards_bought_in_game
    :type sight_wards_bought_in_game: int
    :param vision_wards_bought_in_game: vision_wards_bought_in_game
    :type vision_wards_bought_in_game: int
    """

    def __init__(
        self,
        placed: int,
        sight_wards_bought_in_game: int,
        vision_wards_bought_in_game: int,
    ):
        self.placed = placed
        self.sight_wards_bought_in_game = sight_wards_bought_in_game
        self.vision_wards_bought_in_game = vision_wards_bought_in_game
