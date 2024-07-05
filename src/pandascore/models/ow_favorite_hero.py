from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .ow_hero import OwHero


@JsonMap({})
class OwFavoriteHero(BaseModel):
    """OwFavoriteHero

    :param games_count: Number of games
    :type games_count: int
    :param hero: hero
    :type hero: OwHero
    """

    def __init__(self, games_count: int, hero: OwHero):
        self.games_count = games_count
        self.hero = self._define_object(hero, OwHero)
