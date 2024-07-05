from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .base_valorant_agent import BaseValorantAgent
from .valorant_player_shield import ValorantPlayerShield
from .base_valorant_weapon import BaseValorantWeapon


@JsonMap({"id_": "id"})
class ValorantFullRoundPlayer(BaseModel):
    """ValorantFullRoundPlayer

    :param agent: agent
    :type agent: BaseValorantAgent
    :param assists: Number of player's assists
    :type assists: int
    :param combat_score: Combat score of the player in the round
    :type combat_score: int
    :param eco_beg_prep: Player economy at the beginning of the preperation phase
    :type eco_beg_prep: int
    :param eco_end_prep: Player economy at the end of the preperation phase
    :type eco_end_prep: int
    :param id_: ID of the player
    :type id_: int
    :param kills: Number of player's kills
    :type kills: int
    :param name: Professional name of the player
    :type name: str
    :param shield_type: shield_type
    :type shield_type: ValorantPlayerShield
    :param weapon: weapon
    :type weapon: BaseValorantWeapon
    """

    def __init__(
        self,
        agent: BaseValorantAgent,
        assists: int,
        combat_score: int,
        eco_beg_prep: int,
        eco_end_prep: int,
        id_: int,
        kills: int,
        name: str,
        shield_type: ValorantPlayerShield,
        weapon: BaseValorantWeapon,
    ):
        self.agent = self._define_object(agent, BaseValorantAgent)
        self.assists = assists
        self.combat_score = combat_score
        self.eco_beg_prep = eco_beg_prep
        self.eco_end_prep = eco_end_prep
        self.id_ = id_
        self.kills = kills
        self.name = name
        self.shield_type = self._enum_matching(
            shield_type, ValorantPlayerShield.list(), "shield_type"
        )
        self.weapon = self._define_object(weapon, BaseValorantWeapon)
