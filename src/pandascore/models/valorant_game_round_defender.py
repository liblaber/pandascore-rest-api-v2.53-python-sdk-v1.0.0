from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class ValorantGameRoundDefender(BaseModel):
    """ValorantGameRoundDefender

    :param score: Defenders score at the beginning of the round
    :type score: int
    :param team_id: ID of the defenders team
    :type team_id: int
    """

    def __init__(self, score: int, team_id: int):
        self.score = score
        self.team_id = team_id
