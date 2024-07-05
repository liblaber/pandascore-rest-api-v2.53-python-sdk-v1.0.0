from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


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
        self.flat_armor_mod = flat_armor_mod
        self.flat_crit_chance_mod = flat_crit_chance_mod
        self.flat_hp_pool_mod = flat_hp_pool_mod
        self.flat_hp_regen_mod = flat_hp_regen_mod
        self.flat_magic_damage_mod = flat_magic_damage_mod
        self.flat_movement_speed_mod = flat_movement_speed_mod
        self.flat_mp_pool_mod = flat_mp_pool_mod
        self.flat_mp_regen_mod = flat_mp_regen_mod
        self.flat_physical_damage_mod = flat_physical_damage_mod
        self.flat_spell_block_mod = flat_spell_block_mod
        self.gold_base = gold_base
        self.gold_purchasable = gold_purchasable
        self.gold_sell = gold_sell
        self.gold_total = gold_total
        self.id_ = id_
        self.image_url = image_url
        self.is_trinket = is_trinket
        self.name = name
        self.percent_attack_speed_mod = percent_attack_speed_mod
        self.percent_life_steal_mod = percent_life_steal_mod
        self.percent_movement_speed_mod = percent_movement_speed_mod
        self.videogame_versions = videogame_versions
