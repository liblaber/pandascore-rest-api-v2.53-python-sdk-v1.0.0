from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .base_lo_l_champion import BaseLoLChampion
from .base_lo_l_spell import BaseLoLSpell


@JsonMap({"id_": "id"})
class LoLPlayersRoleDetail(BaseModel):
    """LoLPlayersRoleDetail

    :param assists: assists
    :type assists: int
    :param champion: champion
    :type champion: BaseLoLChampion
    :param cs: The player's Creep Score (CS.) <br/> <br/>NB: Creep Score can be different that the number of minions killed because neutral monsters can give more score.
    :type cs: int
    :param deaths: deaths
    :type deaths: int
    :param id_: ID of the player
    :type id_: int
    :param kills: kills
    :type kills: int
    :param level: level
    :type level: int
    :param name: Professional name of the player
    :type name: str
    :param summoner_spells: summoner_spells
    :type summoner_spells: List[BaseLoLSpell]
    """

    def __init__(
        self,
        assists: int,
        champion: BaseLoLChampion,
        cs: int,
        deaths: int,
        id_: int,
        kills: int,
        level: int,
        name: str,
        summoner_spells: List[BaseLoLSpell],
    ):
        self.assists = assists
        self.champion = self._define_object(champion, BaseLoLChampion)
        self.cs = cs
        self.deaths = deaths
        self.id_ = id_
        self.kills = kills
        self.level = level
        self.name = name
        self.summoner_spells = self._define_list(summoner_spells, BaseLoLSpell)
