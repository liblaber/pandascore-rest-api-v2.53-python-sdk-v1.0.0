from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .valorant_ability_type import ValorantAbilityType


@JsonMap({})
class SearchOverValorantAbilities(BaseModel):
    """SearchOverValorantAbilities

    :param ability_type: Ability type, defaults to None
    :type ability_type: ValorantAbilityType, optional
    :param name: Name of the ability, defaults to None
    :type name: str, optional
    """

    def __init__(self, ability_type: ValorantAbilityType = None, name: str = None):
        if ability_type is not None:
            self.ability_type = self._enum_matching(
                ability_type, ValorantAbilityType.list(), "ability_type"
            )
        if name is not None:
            self.name = name
