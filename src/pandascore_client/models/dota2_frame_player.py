# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
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
        self.gold = self._define_number("gold", gold, ge=0)
        self.hero = self._define_object(hero, Dota2FrameHero)
        self.id_ = self._define_number("id_", id_, ge=1)
        self.name = name
        self.xp = self._define_number("xp", xp, ge=0)
