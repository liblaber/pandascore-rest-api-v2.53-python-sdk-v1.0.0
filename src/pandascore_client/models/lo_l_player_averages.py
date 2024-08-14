# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .lo_l_average_kill_counters import LoLAverageKillCounters
from .lo_l_average_magic_damage import LoLAverageMagicDamage
from .lo_l_average_physical_damage import LoLAveragePhysicalDamage
from .lo_l_average_total_damage import LoLAverageTotalDamage
from .lo_l_average_true_damage import LoLAverageTrueDamage


@JsonMap({})
class LoLPlayerAverages(BaseModel):
    """LoLPlayerAverages

    :param assists: assists
    :type assists: float
    :param cs_at_14: cs_at_14
    :type cs_at_14: float
    :param cs_diff_at_14: Player CS difference compared to their lane opponent at the 14th minute in-game
    :type cs_diff_at_14: float
    :param deaths: deaths
    :type deaths: float
    :param gold_earned: gold_earned
    :type gold_earned: float
    :param gold_percentage: Percentage of gold the player had compared to the total gold of the team
    :type gold_percentage: float
    :param gold_spent: gold_spent
    :type gold_spent: float
    :param kill_counters: kill_counters
    :type kill_counters: LoLAverageKillCounters
    :param kills: kills
    :type kills: float
    :param magic_damage: magic_damage
    :type magic_damage: LoLAverageMagicDamage
    :param minions_killed: minions_killed
    :type minions_killed: float
    :param physical_damage: physical_damage
    :type physical_damage: LoLAveragePhysicalDamage
    :param total_damage: total_damage
    :type total_damage: LoLAverageTotalDamage
    :param total_heal: total_heal
    :type total_heal: float
    :param total_time_crowd_control_dealt: total_time_crowd_control_dealt
    :type total_time_crowd_control_dealt: float
    :param total_units_healed: total_units_healed
    :type total_units_healed: float
    :param true_damage: true_damage
    :type true_damage: LoLAverageTrueDamage
    :param vision_wards_bought_in_game: vision_wards_bought_in_game
    :type vision_wards_bought_in_game: float
    :param wards_placed: wards_placed
    :type wards_placed: float
    """

    def __init__(
        self,
        assists: float,
        cs_at_14: float,
        cs_diff_at_14: float,
        deaths: float,
        gold_earned: float,
        gold_percentage: float,
        gold_spent: float,
        kill_counters: LoLAverageKillCounters,
        kills: float,
        magic_damage: LoLAverageMagicDamage,
        minions_killed: float,
        physical_damage: LoLAveragePhysicalDamage,
        total_damage: LoLAverageTotalDamage,
        total_heal: float,
        total_time_crowd_control_dealt: float,
        total_units_healed: float,
        true_damage: LoLAverageTrueDamage,
        vision_wards_bought_in_game: float,
        wards_placed: float,
    ):
        """LoLPlayerAverages

        :param assists: assists
        :type assists: float
        :param cs_at_14: cs_at_14
        :type cs_at_14: float
        :param cs_diff_at_14: Player CS difference compared to their lane opponent at the 14th minute in-game
        :type cs_diff_at_14: float
        :param deaths: deaths
        :type deaths: float
        :param gold_earned: gold_earned
        :type gold_earned: float
        :param gold_percentage: Percentage of gold the player had compared to the total gold of the team
        :type gold_percentage: float
        :param gold_spent: gold_spent
        :type gold_spent: float
        :param kill_counters: kill_counters
        :type kill_counters: LoLAverageKillCounters
        :param kills: kills
        :type kills: float
        :param magic_damage: magic_damage
        :type magic_damage: LoLAverageMagicDamage
        :param minions_killed: minions_killed
        :type minions_killed: float
        :param physical_damage: physical_damage
        :type physical_damage: LoLAveragePhysicalDamage
        :param total_damage: total_damage
        :type total_damage: LoLAverageTotalDamage
        :param total_heal: total_heal
        :type total_heal: float
        :param total_time_crowd_control_dealt: total_time_crowd_control_dealt
        :type total_time_crowd_control_dealt: float
        :param total_units_healed: total_units_healed
        :type total_units_healed: float
        :param true_damage: true_damage
        :type true_damage: LoLAverageTrueDamage
        :param vision_wards_bought_in_game: vision_wards_bought_in_game
        :type vision_wards_bought_in_game: float
        :param wards_placed: wards_placed
        :type wards_placed: float
        """
        self.assists = self._define_number("assists", assists, nullable=True, ge=0)
        self.cs_at_14 = self._define_number("cs_at_14", cs_at_14, nullable=True, ge=0)
        self.cs_diff_at_14 = self._define_number(
            "cs_diff_at_14", cs_diff_at_14, nullable=True
        )
        self.deaths = self._define_number("deaths", deaths, nullable=True, ge=0)
        self.gold_earned = self._define_number(
            "gold_earned", gold_earned, nullable=True, ge=0
        )
        self.gold_percentage = self._define_number(
            "gold_percentage", gold_percentage, nullable=True, ge=0, le=100
        )
        self.gold_spent = self._define_number(
            "gold_spent", gold_spent, nullable=True, ge=0
        )
        self.kill_counters = self._define_object(kill_counters, LoLAverageKillCounters)
        self.kills = self._define_number("kills", kills, nullable=True, ge=0)
        self.magic_damage = self._define_object(magic_damage, LoLAverageMagicDamage)
        self.minions_killed = self._define_number(
            "minions_killed", minions_killed, nullable=True, ge=0
        )
        self.physical_damage = self._define_object(
            physical_damage, LoLAveragePhysicalDamage
        )
        self.total_damage = self._define_object(total_damage, LoLAverageTotalDamage)
        self.total_heal = self._define_number(
            "total_heal", total_heal, nullable=True, ge=0
        )
        self.total_time_crowd_control_dealt = self._define_number(
            "total_time_crowd_control_dealt",
            total_time_crowd_control_dealt,
            nullable=True,
            ge=0,
        )
        self.total_units_healed = self._define_number(
            "total_units_healed", total_units_healed, nullable=True, ge=0
        )
        self.true_damage = self._define_object(true_damage, LoLAverageTrueDamage)
        self.vision_wards_bought_in_game = self._define_number(
            "vision_wards_bought_in_game",
            vision_wards_bought_in_game,
            nullable=True,
            ge=0,
        )
        self.wards_placed = self._define_number(
            "wards_placed", wards_placed, nullable=True, ge=0
        )
