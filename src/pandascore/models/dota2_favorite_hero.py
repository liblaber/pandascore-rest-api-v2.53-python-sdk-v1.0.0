from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .dota2_hero import Dota2Hero
from .dota2_used_item import Dota2UsedItem


@JsonMap({})
class Dota2FavoriteHero(BaseModel):
    """Player's favorite heroes

    :param games_count: Number of games
    :type games_count: int
    :param games_lost: Number of games lost by the player on the given hero
    :type games_lost: int
    :param games_won: Number of games won by the player on the given hero
    :type games_won: int
    :param hero: hero
    :type hero: Dota2Hero
    :param most_used_items: most_used_items
    :type most_used_items: List[Dota2UsedItem]
    """

    def __init__(
        self,
        games_count: int,
        games_lost: int,
        games_won: int,
        hero: Dota2Hero,
        most_used_items: List[Dota2UsedItem],
    ):
        self.games_count = games_count
        self.games_lost = games_lost
        self.games_won = games_won
        self.hero = self._define_object(hero, Dota2Hero)
        self.most_used_items = self._define_list(most_used_items, Dota2UsedItem)
