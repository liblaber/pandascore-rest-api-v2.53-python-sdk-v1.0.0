# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class Dota2PickedHero(BaseModel):
    """Dota2PickedHero

    :param count: count
    :type count: int
    :param games_lost: Number of games lost by the team
    :type games_lost: int
    :param games_won: Number of games won by the team
    :type games_won: int
    :param name: name
    :type name: str
    """

    def __init__(self, count: int, games_lost: int, games_won: int, name: str):
        """Dota2PickedHero

        :param count: count
        :type count: int
        :param games_lost: Number of games lost by the team
        :type games_lost: int
        :param games_won: Number of games won by the team
        :type games_won: int
        :param name: name
        :type name: str
        """
        self.count = self._define_number("count", count, ge=0)
        self.games_lost = self._define_number("games_lost", games_lost, ge=0)
        self.games_won = self._define_number("games_won", games_won, ge=0)
        self.name = self._define_str(
            "name", name, pattern="^[a-z0-9_-]+$", min_length=1
        )
