from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_champion import LoLChampion
from .lo_l_used_item import LoLUsedItem


@JsonMap({})
class LoLFavoriteChampion(BaseModel):
    """A player's most used champion

    :param champion: champion
    :type champion: LoLChampion
    :param games_count: Number of games
    :type games_count: int
    :param games_lost: Number of games lost by the player on the given champion
    :type games_lost: int
    :param games_won: Number of games won by the player on the given champion
    :type games_won: int
    :param most_used_items: most_used_items
    :type most_used_items: List[LoLUsedItem]
    """

    def __init__(
        self,
        champion: LoLChampion,
        games_count: int,
        games_lost: int,
        games_won: int,
        most_used_items: List[LoLUsedItem],
    ):
        self.champion = self._define_object(champion, LoLChampion)
        self.games_count = games_count
        self.games_lost = games_lost
        self.games_won = games_won
        self.most_used_items = self._define_list(most_used_items, LoLUsedItem)
