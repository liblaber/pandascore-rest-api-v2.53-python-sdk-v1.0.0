from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .valorant_ability_type import ValorantAbilityType


@JsonMap({"id_": "id"})
class RangeOverValorantAbilities(BaseModel):
    """RangeOverValorantAbilities

    :param ability_type: ability_type, defaults to None
    :type ability_type: List[ValorantAbilityType], optional
    :param creds: creds, defaults to None
    :type creds: List[float], optional
    :param id_: id_, defaults to None
    :type id_: List[int], optional
    :param name: name, defaults to None
    :type name: List[str], optional
    """

    def __init__(
        self,
        ability_type: List[ValorantAbilityType] = None,
        creds: List[float] = None,
        id_: List[int] = None,
        name: List[str] = None,
    ):
        if ability_type is not None:
            self.ability_type = self._define_list(ability_type, ValorantAbilityType)
        if creds is not None:
            self.creds = creds
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
