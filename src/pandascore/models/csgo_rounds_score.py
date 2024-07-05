from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class CsgoRoundsScore(BaseModel):
    """CsgoRoundsScore

    :param score: The round score for the team.
    :type score: int
    :param team_id: team_id
    :type team_id: int
    """

    def __init__(self, score: int, team_id: int):
        self.score = score
        self.team_id = team_id
