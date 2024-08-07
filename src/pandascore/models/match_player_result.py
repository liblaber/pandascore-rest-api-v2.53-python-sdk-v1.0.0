from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class MatchPlayerResult(BaseModel):
    """MatchPlayerResult

    :param player_id: ID of the player
    :type player_id: int
    :param score: score
    :type score: int
    """

    def __init__(self, player_id: int, score: int):
        self.player_id = player_id
        self.score = score
