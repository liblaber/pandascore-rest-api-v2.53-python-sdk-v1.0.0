# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class MatchPlayerResult(BaseModel):
    """MatchPlayerResult

    :param player_id: ID of the player
    :type player_id: int
    :param score: score
    :type score: int
    """

    def __init__(self, player_id: int, score: int):
        """MatchPlayerResult

        :param player_id: ID of the player
        :type player_id: int
        :param score: score
        :type score: int
        """
        self.player_id = self._define_number("player_id", player_id, ge=1)
        self.score = self._define_number("score", score, ge=0)
