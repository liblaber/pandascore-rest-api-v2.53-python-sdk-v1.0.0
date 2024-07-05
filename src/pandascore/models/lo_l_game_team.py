from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_team_color import LoLTeamColor
from .base_team import BaseTeam


@JsonMap({})
class LoLGameTeam(BaseModel):
    """Team's data for a Game

    :param bans: bans
    :type bans: List[int]
    :param baron_kills: baron_kills
    :type baron_kills: int
    :param chemtech_drake_kills: chemtech_drake_kills
    :type chemtech_drake_kills: int
    :param cloud_drake_kills: cloud_drake_kills
    :type cloud_drake_kills: int
    :param color: color
    :type color: LoLTeamColor
    :param dragon_kills: dragon_kills
    :type dragon_kills: int
    :param elder_drake_kills: elder_drake_kills
    :type elder_drake_kills: int
    :param first_baron: Whether team got first baron Nashor
    :type first_baron: bool
    :param first_blood: Whether team got first blood
    :type first_blood: bool
    :param first_dragon: Whether team got first dragon
    :type first_dragon: bool
    :param first_herald: Whether team got first herald
    :type first_herald: bool
    :param first_inhibitor: Whether team got first inhibitor
    :type first_inhibitor: bool
    :param first_tower: Whether team got first tower
    :type first_tower: bool
    :param first_voidgrub: Whether team killed the first voidgrub
    :type first_voidgrub: bool
    :param gold_earned: gold_earned
    :type gold_earned: int
    :param herald_kills: herald_kills
    :type herald_kills: int
    :param hextech_drake_kills: hextech_drake_kills
    :type hextech_drake_kills: int
    :param infernal_drake_kills: infernal_drake_kills
    :type infernal_drake_kills: int
    :param inhibitor_kills: inhibitor_kills
    :type inhibitor_kills: int
    :param kills: kills
    :type kills: int
    :param mountain_drake_kills: mountain_drake_kills
    :type mountain_drake_kills: int
    :param ocean_drake_kills: ocean_drake_kills
    :type ocean_drake_kills: int
    :param player_ids: player_ids
    :type player_ids: List[int]
    :param team: team
    :type team: BaseTeam
    :param tower_kills: tower_kills
    :type tower_kills: int
    :param voidgrub_kills: The number of voidgrubs killed by a team.
    :type voidgrub_kills: int
    """

    def __init__(
        self,
        bans: List[int],
        baron_kills: int,
        chemtech_drake_kills: int,
        cloud_drake_kills: int,
        color: LoLTeamColor,
        dragon_kills: int,
        elder_drake_kills: int,
        first_baron: bool,
        first_blood: bool,
        first_dragon: bool,
        first_herald: bool,
        first_inhibitor: bool,
        first_tower: bool,
        first_voidgrub: bool,
        gold_earned: int,
        herald_kills: int,
        hextech_drake_kills: int,
        infernal_drake_kills: int,
        inhibitor_kills: int,
        kills: int,
        mountain_drake_kills: int,
        ocean_drake_kills: int,
        player_ids: List[int],
        team: BaseTeam,
        tower_kills: int,
        voidgrub_kills: int,
    ):
        self.bans = bans
        self.baron_kills = baron_kills
        self.chemtech_drake_kills = chemtech_drake_kills
        self.cloud_drake_kills = cloud_drake_kills
        self.color = self._enum_matching(color, LoLTeamColor.list(), "color")
        self.dragon_kills = dragon_kills
        self.elder_drake_kills = elder_drake_kills
        self.first_baron = first_baron
        self.first_blood = first_blood
        self.first_dragon = first_dragon
        self.first_herald = first_herald
        self.first_inhibitor = first_inhibitor
        self.first_tower = first_tower
        self.first_voidgrub = first_voidgrub
        self.gold_earned = gold_earned
        self.herald_kills = herald_kills
        self.hextech_drake_kills = hextech_drake_kills
        self.infernal_drake_kills = infernal_drake_kills
        self.inhibitor_kills = inhibitor_kills
        self.kills = kills
        self.mountain_drake_kills = mountain_drake_kills
        self.ocean_drake_kills = ocean_drake_kills
        self.player_ids = player_ids
        self.team = self._define_object(team, BaseTeam)
        self.tower_kills = tower_kills
        self.voidgrub_kills = voidgrub_kills
