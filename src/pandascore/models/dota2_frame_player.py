from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .dota2_frame_hero import Dota2FrameHero


@JsonMap({"id_": "id"})
class Dota2FramePlayer(BaseModel):
    """Dota2FramePlayer

    :param gold: Total gold of the player
    :type gold: int
    :param hero: hero
    :type hero: Dota2FrameHero
    :param id_: ID of the player
    :type id_: int
    :param name: Professional name of the player
    :type name: str
    :param xp: Total experience of the player
    :type xp: int
    """

    def __init__(self, gold: int, hero: Dota2FrameHero, id_: int, name: str, xp: int):
        self.gold = gold
        self.hero = self._define_object(hero, Dota2FrameHero)
        self.id_ = id_
        self.name = name
        self.xp = xp
