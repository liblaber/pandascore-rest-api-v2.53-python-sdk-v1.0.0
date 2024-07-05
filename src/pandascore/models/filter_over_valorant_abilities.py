from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .valorant_ability_type import ValorantAbilityType


@JsonMap({"id_": "id"})
class FilterOverValorantAbilities(BaseModel):
    """FilterOverValorantAbilities

    :param ability_type: ability_type, defaults to None
    :type ability_type: List[ValorantAbilityType], optional
    :param creds: creds, defaults to None
    :type creds: List[float], optional
    :param id_: id_, defaults to None
    :type id_: List[int], optional
    :param name: name, defaults to None
    :type name: List[str], optional
    :param videogame_version: Filter by the names of videogame versions, all versions using `filter[videogame_version]=all`, or by the latest version using `filter[videogame_version]=latest`, defaults to None
    :type videogame_version: any, optional
    """

    def __init__(
        self,
        ability_type: List[ValorantAbilityType] = None,
        creds: List[float] = None,
        id_: List[int] = None,
        name: List[str] = None,
        videogame_version: any = None,
    ):
        if ability_type is not None:
            self.ability_type = self._define_list(ability_type, ValorantAbilityType)
        if creds is not None:
            self.creds = creds
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if videogame_version is not None:
            self.videogame_version = videogame_version
