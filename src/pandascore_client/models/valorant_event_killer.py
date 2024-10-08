# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .base_valorant_agent import BaseValorantAgent
from .valorant_team_side import ValorantTeamSide


@JsonMap({"id_": "id"})
class Ability(BaseModel):
    """Ability

    :param id_: ID of the ability
    :type id_: int
    :param image_url: URL to an image of the ability
    :type image_url: str
    :param name: Name of the ability
    :type name: str
    """

    def __init__(self, id_: int, image_url: str, name: str):
        """Ability

        :param id_: ID of the ability
        :type id_: int
        :param image_url: URL to an image of the ability
        :type image_url: str
        :param name: Name of the ability
        :type name: str
        """
        self.id_ = self._define_number("id_", id_, ge=1)
        self.image_url = self._define_str("image_url", image_url, nullable=True)
        self.name = name


@JsonMap({"id_": "id"})
class Weapon(BaseModel):
    """Weapon

    :param id_: ID of the weapon
    :type id_: int
    :param image_url: URL to an image of the weapon
    :type image_url: str
    :param name: Name of the weapon
    :type name: str
    """

    def __init__(self, id_: int, image_url: str, name: str):
        """Weapon

        :param id_: ID of the weapon
        :type id_: int
        :param image_url: URL to an image of the weapon
        :type image_url: str
        :param name: Name of the weapon
        :type name: str
        """
        self.id_ = self._define_number("id_", id_, ge=1)
        self.image_url = image_url
        self.name = name


@JsonMap({"id_": "id"})
class ValorantEventKiller(BaseModel):
    """ValorantEventKiller

    :param ability: ability
    :type ability: Ability
    :param agent: agent
    :type agent: BaseValorantAgent
    :param id_: ID of the player
    :type id_: int
    :param name: Professional name of the player
    :type name: str
    :param team_side: Team side in the round
    :type team_side: ValorantTeamSide
    :param weapon: weapon
    :type weapon: Weapon
    """

    def __init__(
        self,
        ability: Ability,
        agent: BaseValorantAgent,
        id_: int,
        name: str,
        team_side: ValorantTeamSide,
        weapon: Weapon,
    ):
        """ValorantEventKiller

        :param ability: ability
        :type ability: Ability
        :param agent: agent
        :type agent: BaseValorantAgent
        :param id_: ID of the player
        :type id_: int
        :param name: Professional name of the player
        :type name: str
        :param team_side: Team side in the round
        :type team_side: ValorantTeamSide
        :param weapon: weapon
        :type weapon: Weapon
        """
        self.ability = self._define_object(ability, Ability)
        self.agent = self._define_object(agent, BaseValorantAgent)
        self.id_ = self._define_number("id_", id_, ge=1)
        self.name = name
        self.team_side = self._enum_matching(
            team_side, ValorantTeamSide.list(), "team_side"
        )
        self.weapon = self._define_object(weapon, Weapon)
