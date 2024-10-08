# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class FilterOverLoLItems(BaseModel):
    """FilterOverLoLItems

    :param flat_armor_mod: flat_armor_mod, defaults to None
    :type flat_armor_mod: List[int], optional
    :param flat_crit_chance_mod: flat_crit_chance_mod, defaults to None
    :type flat_crit_chance_mod: List[int], optional
    :param flat_hp_pool_mod: flat_hp_pool_mod, defaults to None
    :type flat_hp_pool_mod: List[int], optional
    :param flat_hp_regen_mod: flat_hp_regen_mod, defaults to None
    :type flat_hp_regen_mod: List[int], optional
    :param flat_magic_damage_mod: flat_magic_damage_mod, defaults to None
    :type flat_magic_damage_mod: List[int], optional
    :param flat_movement_speed_mod: flat_movement_speed_mod, defaults to None
    :type flat_movement_speed_mod: List[int], optional
    :param flat_mp_pool_mod: flat_mp_pool_mod, defaults to None
    :type flat_mp_pool_mod: List[int], optional
    :param flat_mp_regen_mod: flat_mp_regen_mod, defaults to None
    :type flat_mp_regen_mod: List[int], optional
    :param flat_physical_damage_mod: flat_physical_damage_mod, defaults to None
    :type flat_physical_damage_mod: List[int], optional
    :param flat_spell_block_mod: flat_spell_block_mod, defaults to None
    :type flat_spell_block_mod: List[int], optional
    :param gold_base: gold_base, defaults to None
    :type gold_base: List[int], optional
    :param gold_purchasable: Whether gold can be bought, defaults to None
    :type gold_purchasable: bool, optional
    :param gold_sell: gold_sell, defaults to None
    :type gold_sell: List[int], optional
    :param gold_total: gold_total, defaults to None
    :type gold_total: List[int], optional
    :param id_: id_, defaults to None
    :type id_: List[int], optional
    :param name: name, defaults to None
    :type name: List[str], optional
    :param percent_attack_speed_mod: percent_attack_speed_mod, defaults to None
    :type percent_attack_speed_mod: List[int], optional
    :param percent_life_steal_mod: percent_life_steal_mod, defaults to None
    :type percent_life_steal_mod: List[int], optional
    :param percent_movement_speed_mod: percent_movement_speed_mod, defaults to None
    :type percent_movement_speed_mod: List[int], optional
    :param trinket: Whether item is a trinket, defaults to None
    :type trinket: bool, optional
    :param videogame_version: Filter by the names of videogame versions, all versions using `filter[videogame_version]=all`, or by the latest version using `filter[videogame_version]=latest`, defaults to None
    :type videogame_version: any, optional
    """

    def __init__(
        self,
        flat_armor_mod: List[int] = None,
        flat_crit_chance_mod: List[int] = None,
        flat_hp_pool_mod: List[int] = None,
        flat_hp_regen_mod: List[int] = None,
        flat_magic_damage_mod: List[int] = None,
        flat_movement_speed_mod: List[int] = None,
        flat_mp_pool_mod: List[int] = None,
        flat_mp_regen_mod: List[int] = None,
        flat_physical_damage_mod: List[int] = None,
        flat_spell_block_mod: List[int] = None,
        gold_base: List[int] = None,
        gold_purchasable: bool = None,
        gold_sell: List[int] = None,
        gold_total: List[int] = None,
        id_: List[int] = None,
        name: List[str] = None,
        percent_attack_speed_mod: List[int] = None,
        percent_life_steal_mod: List[int] = None,
        percent_movement_speed_mod: List[int] = None,
        trinket: bool = None,
        videogame_version: any = None,
    ):
        """FilterOverLoLItems

        :param flat_armor_mod: flat_armor_mod, defaults to None
        :type flat_armor_mod: List[int], optional
        :param flat_crit_chance_mod: flat_crit_chance_mod, defaults to None
        :type flat_crit_chance_mod: List[int], optional
        :param flat_hp_pool_mod: flat_hp_pool_mod, defaults to None
        :type flat_hp_pool_mod: List[int], optional
        :param flat_hp_regen_mod: flat_hp_regen_mod, defaults to None
        :type flat_hp_regen_mod: List[int], optional
        :param flat_magic_damage_mod: flat_magic_damage_mod, defaults to None
        :type flat_magic_damage_mod: List[int], optional
        :param flat_movement_speed_mod: flat_movement_speed_mod, defaults to None
        :type flat_movement_speed_mod: List[int], optional
        :param flat_mp_pool_mod: flat_mp_pool_mod, defaults to None
        :type flat_mp_pool_mod: List[int], optional
        :param flat_mp_regen_mod: flat_mp_regen_mod, defaults to None
        :type flat_mp_regen_mod: List[int], optional
        :param flat_physical_damage_mod: flat_physical_damage_mod, defaults to None
        :type flat_physical_damage_mod: List[int], optional
        :param flat_spell_block_mod: flat_spell_block_mod, defaults to None
        :type flat_spell_block_mod: List[int], optional
        :param gold_base: gold_base, defaults to None
        :type gold_base: List[int], optional
        :param gold_purchasable: Whether gold can be bought, defaults to None
        :type gold_purchasable: bool, optional
        :param gold_sell: gold_sell, defaults to None
        :type gold_sell: List[int], optional
        :param gold_total: gold_total, defaults to None
        :type gold_total: List[int], optional
        :param id_: id_, defaults to None
        :type id_: List[int], optional
        :param name: name, defaults to None
        :type name: List[str], optional
        :param percent_attack_speed_mod: percent_attack_speed_mod, defaults to None
        :type percent_attack_speed_mod: List[int], optional
        :param percent_life_steal_mod: percent_life_steal_mod, defaults to None
        :type percent_life_steal_mod: List[int], optional
        :param percent_movement_speed_mod: percent_movement_speed_mod, defaults to None
        :type percent_movement_speed_mod: List[int], optional
        :param trinket: Whether item is a trinket, defaults to None
        :type trinket: bool, optional
        :param videogame_version: Filter by the names of videogame versions, all versions using `filter[videogame_version]=all`, or by the latest version using `filter[videogame_version]=latest`, defaults to None
        :type videogame_version: any, optional
        """
        if flat_armor_mod is not None:
            self.flat_armor_mod = flat_armor_mod
        if flat_crit_chance_mod is not None:
            self.flat_crit_chance_mod = flat_crit_chance_mod
        if flat_hp_pool_mod is not None:
            self.flat_hp_pool_mod = flat_hp_pool_mod
        if flat_hp_regen_mod is not None:
            self.flat_hp_regen_mod = flat_hp_regen_mod
        if flat_magic_damage_mod is not None:
            self.flat_magic_damage_mod = flat_magic_damage_mod
        if flat_movement_speed_mod is not None:
            self.flat_movement_speed_mod = flat_movement_speed_mod
        if flat_mp_pool_mod is not None:
            self.flat_mp_pool_mod = flat_mp_pool_mod
        if flat_mp_regen_mod is not None:
            self.flat_mp_regen_mod = flat_mp_regen_mod
        if flat_physical_damage_mod is not None:
            self.flat_physical_damage_mod = flat_physical_damage_mod
        if flat_spell_block_mod is not None:
            self.flat_spell_block_mod = flat_spell_block_mod
        if gold_base is not None:
            self.gold_base = gold_base
        if gold_purchasable is not None:
            self.gold_purchasable = gold_purchasable
        if gold_sell is not None:
            self.gold_sell = gold_sell
        if gold_total is not None:
            self.gold_total = gold_total
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if percent_attack_speed_mod is not None:
            self.percent_attack_speed_mod = percent_attack_speed_mod
        if percent_life_steal_mod is not None:
            self.percent_life_steal_mod = percent_life_steal_mod
        if percent_movement_speed_mod is not None:
            self.percent_movement_speed_mod = percent_movement_speed_mod
        if trinket is not None:
            self.trinket = trinket
        if videogame_version is not None:
            self.videogame_version = videogame_version
