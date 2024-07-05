from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class LoLPickedChampion(BaseModel):
    """A team's picked champion

    :param count: count
    :type count: int
    :param games_lost: Number of games lost by the team on the given champion
    :type games_lost: int
    :param games_won: Number of games won by the team on the given champion
    :type games_won: int
    :param name: name
    :type name: str
    """

    def __init__(self, count: int, games_lost: int, games_won: int, name: str):
        self.count = count
        self.games_lost = games_lost
        self.games_won = games_won
        self.name = name
