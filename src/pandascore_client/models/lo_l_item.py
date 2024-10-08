# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class LoLItem(BaseModel):
    """LoLItem

    :param flat_armor_mod: flat_armor_mod
    :type flat_armor_mod: int
    :param flat_crit_chance_mod: flat_crit_chance_mod
    :type flat_crit_chance_mod: int
    :param flat_hp_pool_mod: flat_hp_pool_mod
    :type flat_hp_pool_mod: int
    :param flat_hp_regen_mod: flat_hp_regen_mod
    :type flat_hp_regen_mod: int
    :param flat_magic_damage_mod: flat_magic_damage_mod
    :type flat_magic_damage_mod: int
    :param flat_movement_speed_mod: flat_movement_speed_mod
    :type flat_movement_speed_mod: int
    :param flat_mp_pool_mod: flat_mp_pool_mod
    :type flat_mp_pool_mod: int
    :param flat_mp_regen_mod: flat_mp_regen_mod
    :type flat_mp_regen_mod: int
    :param flat_physical_damage_mod: flat_physical_damage_mod
    :type flat_physical_damage_mod: int
    :param flat_spell_block_mod: flat_spell_block_mod
    :type flat_spell_block_mod: int
    :param gold_base: gold_base
    :type gold_base: int
    :param gold_purchasable: Whether gold can be bought
    :type gold_purchasable: bool
    :param gold_sell: gold_sell
    :type gold_sell: int
    :param gold_total: gold_total
    :type gold_total: int
    :param id_: id_
    :type id_: int
    :param image_url: image_url
    :type image_url: str
    :param is_trinket: Whether item is a trinket
    :type is_trinket: bool
    :param name: name
    :type name: str
    :param percent_attack_speed_mod: percent_attack_speed_mod
    :type percent_attack_speed_mod: int
    :param percent_life_steal_mod: percent_life_steal_mod
    :type percent_life_steal_mod: int
    :param percent_movement_speed_mod: percent_movement_speed_mod
    :type percent_movement_speed_mod: int
    :param videogame_versions: Array of of video game versions (ie. patches) for this resource
    :type videogame_versions: List[str]
    """

    def __init__(
        self,
        flat_armor_mod: int,
        flat_crit_chance_mod: int,
        flat_hp_pool_mod: int,
        flat_hp_regen_mod: int,
        flat_magic_damage_mod: int,
        flat_movement_speed_mod: int,
        flat_mp_pool_mod: int,
        flat_mp_regen_mod: int,
        flat_physical_damage_mod: int,
        flat_spell_block_mod: int,
        gold_base: int,
        gold_purchasable: bool,
        gold_sell: int,
        gold_total: int,
        id_: int,
        image_url: str,
        is_trinket: bool,
        name: str,
        percent_attack_speed_mod: int,
        percent_life_steal_mod: int,
        percent_movement_speed_mod: int,
        videogame_versions: List[str],
    ):
        """LoLItem

        :param flat_armor_mod: flat_armor_mod
        :type flat_armor_mod: int
        :param flat_crit_chance_mod: flat_crit_chance_mod
        :type flat_crit_chance_mod: int
        :param flat_hp_pool_mod: flat_hp_pool_mod
        :type flat_hp_pool_mod: int
        :param flat_hp_regen_mod: flat_hp_regen_mod
        :type flat_hp_regen_mod: int
        :param flat_magic_damage_mod: flat_magic_damage_mod
        :type flat_magic_damage_mod: int
        :param flat_movement_speed_mod: flat_movement_speed_mod
        :type flat_movement_speed_mod: int
        :param flat_mp_pool_mod: flat_mp_pool_mod
        :type flat_mp_pool_mod: int
        :param flat_mp_regen_mod: flat_mp_regen_mod
        :type flat_mp_regen_mod: int
        :param flat_physical_damage_mod: flat_physical_damage_mod
        :type flat_physical_damage_mod: int
        :param flat_spell_block_mod: flat_spell_block_mod
        :type flat_spell_block_mod: int
        :param gold_base: gold_base
        :type gold_base: int
        :param gold_purchasable: Whether gold can be bought
        :type gold_purchasable: bool
        :param gold_sell: gold_sell
        :type gold_sell: int
        :param gold_total: gold_total
        :type gold_total: int
        :param id_: id_
        :type id_: int
        :param image_url: image_url
        :type image_url: str
        :param is_trinket: Whether item is a trinket
        :type is_trinket: bool
        :param name: name
        :type name: str
        :param percent_attack_speed_mod: percent_attack_speed_mod
        :type percent_attack_speed_mod: int
        :param percent_life_steal_mod: percent_life_steal_mod
        :type percent_life_steal_mod: int
        :param percent_movement_speed_mod: percent_movement_speed_mod
        :type percent_movement_speed_mod: int
        :param videogame_versions: Array of of video game versions (ie. patches) for this resource
        :type videogame_versions: List[str]
        """
        self.flat_armor_mod = self._define_number(
            "flat_armor_mod", flat_armor_mod, nullable=True, ge=0
        )
        self.flat_crit_chance_mod = self._define_number(
            "flat_crit_chance_mod", flat_crit_chance_mod, nullable=True, ge=0
        )
        self.flat_hp_pool_mod = self._define_number(
            "flat_hp_pool_mod", flat_hp_pool_mod, nullable=True, ge=0
        )
        self.flat_hp_regen_mod = self._define_number(
            "flat_hp_regen_mod", flat_hp_regen_mod, nullable=True, ge=0
        )
        self.flat_magic_damage_mod = self._define_number(
            "flat_magic_damage_mod", flat_magic_damage_mod, nullable=True, ge=0
        )
        self.flat_movement_speed_mod = self._define_number(
            "flat_movement_speed_mod", flat_movement_speed_mod, nullable=True, ge=0
        )
        self.flat_mp_pool_mod = self._define_number(
            "flat_mp_pool_mod", flat_mp_pool_mod, nullable=True, ge=0
        )
        self.flat_mp_regen_mod = self._define_number(
            "flat_mp_regen_mod", flat_mp_regen_mod, nullable=True, ge=0
        )
        self.flat_physical_damage_mod = self._define_number(
            "flat_physical_damage_mod", flat_physical_damage_mod, nullable=True, ge=0
        )
        self.flat_spell_block_mod = self._define_number(
            "flat_spell_block_mod", flat_spell_block_mod, nullable=True, ge=0
        )
        self.gold_base = self._define_number(
            "gold_base", gold_base, nullable=True, ge=0
        )
        self.gold_purchasable = gold_purchasable
        self.gold_sell = self._define_number(
            "gold_sell", gold_sell, nullable=True, ge=0
        )
        self.gold_total = self._define_number(
            "gold_total", gold_total, nullable=True, ge=0
        )
        self.id_ = self._define_number("id_", id_, ge=1)
        self.image_url = self._define_str("image_url", image_url, nullable=True)
        self.is_trinket = is_trinket
        self.name = name
        self.percent_attack_speed_mod = self._define_number(
            "percent_attack_speed_mod", percent_attack_speed_mod, nullable=True, ge=0
        )
        self.percent_life_steal_mod = self._define_number(
            "percent_life_steal_mod", percent_life_steal_mod, nullable=True, ge=0
        )
        self.percent_movement_speed_mod = self._define_number(
            "percent_movement_speed_mod",
            percent_movement_speed_mod,
            nullable=True,
            ge=0,
        )
        self.videogame_versions = videogame_versions
