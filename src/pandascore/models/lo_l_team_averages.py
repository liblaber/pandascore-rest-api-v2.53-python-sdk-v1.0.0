from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_team_ratios import LoLTeamRatios


@JsonMap({})
class LoLTeamAverages(BaseModel):
    """LoLTeamAverages

    :param assists: assists
    :type assists: float
    :param baron_kills: baron_kills
    :type baron_kills: float
    :param deaths: deaths
    :type deaths: float
    :param dragon_kills: dragon_kills
    :type dragon_kills: float
    :param game_length: Duration of the game in seconds. <br/>`null` when the game status is not `finished`
    :type game_length: int
    :param gold_earned: gold_earned
    :type gold_earned: float
    :param herald_kill: herald_kill
    :type herald_kill: float
    :param inhibitor_kills: inhibitor_kills
    :type inhibitor_kills: float
    :param kills: kills
    :type kills: float
    :param ratios: ratios
    :type ratios: LoLTeamRatios
    :param total_minions_killed: total_minions_killed
    :type total_minions_killed: float
    :param tower_kills: tower_kills
    :type tower_kills: float
    :param voidgrub_kills: The number of voidgrubs killed by a team.
    :type voidgrub_kills: float
    :param wards_placed: wards_placed
    :type wards_placed: float
    """

    def __init__(
        self,
        assists: float,
        baron_kills: float,
        deaths: float,
        dragon_kills: float,
        game_length: int,
        gold_earned: float,
        herald_kill: float,
        inhibitor_kills: float,
        kills: float,
        ratios: LoLTeamRatios,
        total_minions_killed: float,
        tower_kills: float,
        voidgrub_kills: float,
        wards_placed: float,
    ):
        self.assists = assists
        self.baron_kills = baron_kills
        self.deaths = deaths
        self.dragon_kills = dragon_kills
        self.game_length = game_length
        self.gold_earned = gold_earned
        self.herald_kill = herald_kill
        self.inhibitor_kills = inhibitor_kills
        self.kills = kills
        self.ratios = self._define_object(ratios, LoLTeamRatios)
        self.total_minions_killed = total_minions_killed
        self.tower_kills = tower_kills
        self.voidgrub_kills = voidgrub_kills
        self.wards_placed = wards_placed
