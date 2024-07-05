from __future__ import annotations
from enum import Enum
from typing import Union
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel
from .lo_l_flags import LoLFlags
from .base_lo_l_item import BaseLoLItem
from .lo_l_kill_counters import LoLKillCounters
from .lo_l_kills_series import LoLKillsSeries
from .lo_l_magic_damage import LoLMagicDamage
from .lo_l_mastery import LoLMastery
from .lo_l_physical_damage import LoLPhysicalDamage
from .base_player import BasePlayer
from .lo_l_rune import LoLRune
from .lo_l_player_runes_reforged import LoLPlayerRunesReforged
from .lo_l_spell import LoLSpell
from .base_team import BaseTeam
from .lo_l_total_damage import LoLTotalDamage
from .lo_l_true_damage import LoLTrueDamage
from .lo_l_wards import LoLWards


@JsonMap({"id_": "id"})
class LoLGamePlayerChampion(BaseModel):
    """LoLGamePlayerChampion

    :param id_: id_
    :type id_: int
    :param image_url: image_url
    :type image_url: str
    :param name: name
    :type name: str
    """

    def __init__(self, id_: int, image_url: str, name: str):
        self.id_ = id_
        self.image_url = image_url
        self.name = name


@JsonMap({"id_": "id"})
class Opponent1_3(BaseModel):
    """Opponent1_3

    :param active: Whether player is active
    :type active: bool
    :param age: Age of the player, `null` if unknown. When `birthday` is `null`, `age` is an approxiamation. Read more about [players' age](/docs/about-players-age) <br/>**Note**: This field is only present for users running the Historical plan or above.
    :type age: float
    :param birthday: Birth day of the player, `YYYY-MM-DD` format. `null` if unknown. <br/>**Note**: This field is only present for users running the Historical plan or above.
    :type birthday: str
    :param first_name: First name of the player. `null` if unknown
    :type first_name: str
    :param id_: ID of the player
    :type id_: int
    :param image_url: URL to the photo of the player. `null` if not available.
    :type image_url: str
    :param last_name: Last name of the player. `null` if unknown
    :type last_name: str
    :param modified_at: modified_at
    :type modified_at: str
    :param name: Professional name of the player
    :type name: str
    :param nationality: Country code matching the nationality of the player according to the ISO 3166-1 standard (Alpha-2 code). <br/>In addition to the standard, the `XK` code is used for Kosovo. <br/>`null` if unknown
    :type nationality: str
    :param role: Role/position of the player. Field value varies depending on the video game.`null` if unknown. <br/>**Note**: role is only available for DotA 2, League of Legends, and Overwatch players. <br/>`null` for other video games.
    :type role: str
    :param slug: Unique, human-readable identifier for the player. <br/>`id` and `slug` can be used interchangeably throughout the API.
    :type slug: str
    """

    def __init__(
        self,
        active: bool,
        age: float,
        birthday: str,
        first_name: str,
        id_: int,
        image_url: str,
        last_name: str,
        modified_at: str,
        name: str,
        nationality: str,
        role: str,
        slug: str,
    ):
        self.active = active
        self.age = age
        self.birthday = birthday
        self.first_name = first_name
        self.id_ = id_
        self.image_url = image_url
        self.last_name = last_name
        self.modified_at = modified_at
        self.name = name
        self.nationality = nationality
        self.role = role
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")


@JsonMap({"id_": "id"})
class Opponent2_3(BaseModel):
    """Opponent2_3

    :param acronym: acronym
    :type acronym: str
    :param id_: id_
    :type id_: int
    :param image_url: URL of the team logo
    :type image_url: str
    :param location: The team's organization location
    :type location: str
    :param modified_at: modified_at
    :type modified_at: str
    :param name: The name of the team.
    :type name: str
    :param slug: slug
    :type slug: str
    """

    def __init__(
        self,
        acronym: str,
        id_: int,
        image_url: str,
        location: str,
        modified_at: str,
        name: str,
        slug: str,
    ):
        self.acronym = acronym
        self.id_ = id_
        self.image_url = image_url
        self.location = location
        self.modified_at = modified_at
        self.name = name
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")


class LoLGamePlayerOpponentGuard(OneOfBaseModel):
    class_list = {"Opponent1_3": Opponent1_3, "Opponent2_3": Opponent2_3}


LoLGamePlayerOpponent = Union[Opponent1_3, Opponent2_3]


class LoLGamePlayerRole(Enum):
    """An enumeration representing different categories.

    :cvar ADC: "adc"
    :vartype ADC: str
    :cvar JUN: "jun"
    :vartype JUN: str
    :cvar MID: "mid"
    :vartype MID: str
    :cvar SUP: "sup"
    :vartype SUP: str
    :cvar TOP: "top"
    :vartype TOP: str
    """

    ADC = "adc"
    JUN = "jun"
    MID = "mid"
    SUP = "sup"
    TOP = "top"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, LoLGamePlayerRole._member_map_.values()))


@JsonMap({})
class LoLGamePlayer(BaseModel):
    """Player's data for a Game

    :param assists: assists
    :type assists: int
    :param champion: champion
    :type champion: LoLGamePlayerChampion
    :param creep_score: The player's Creep Score (CS.) <br/> <br/>NB: Creep Score can be different that the number of minions killed because neutral monsters can give more score.
    :type creep_score: int
    :param cs_at_14: The player's Creep Score (CS.) at 14minutes
    :type cs_at_14: int
    :param cs_diff_at_14: Player CS difference compared to their lane opponent at the 14th minute in-game
    :type cs_diff_at_14: float
    :param deaths: deaths
    :type deaths: int
    :param flags: flags
    :type flags: LoLFlags
    :param game_id: LoL game ID
    :type game_id: int
    :param gold_earned: gold_earned
    :type gold_earned: int
    :param gold_percentage: Percentage of gold the player had compared to the total gold of the team
    :type gold_percentage: float
    :param gold_spent: gold_spent
    :type gold_spent: int
    :param items: items
    :type items: List[BaseLoLItem]
    :param kills: kills
    :type kills: int
    :param kills_counters: kills_counters
    :type kills_counters: LoLKillCounters
    :param kills_series: kills_series
    :type kills_series: LoLKillsSeries
    :param largest_critical_strike: largest_critical_strike
    :type largest_critical_strike: int
    :param largest_killing_spree: largest_killing_spree
    :type largest_killing_spree: int
    :param largest_multi_kill: largest_multi_kill
    :type largest_multi_kill: int
    :param level: level
    :type level: int
    :param magic_damage: magic_damage
    :type magic_damage: LoLMagicDamage
    :param masteries: masteries
    :type masteries: List[LoLMastery]
    :param minions_killed: The player's Creep Score (CS.)
    :type minions_killed: int
    :param opponent: opponent
    :type opponent: LoLGamePlayerOpponent
    :param physical_damage: physical_damage
    :type physical_damage: LoLPhysicalDamage
    :param player: player
    :type player: BasePlayer
    :param player_id: ID of the player
    :type player_id: int
    :param role: role
    :type role: LoLGamePlayerRole
    :param runes: runes
    :type runes: List[LoLRune]
    :param runes_reforged: runes_reforged
    :type runes_reforged: LoLPlayerRunesReforged
    :param spells: spells
    :type spells: List[LoLSpell]
    :param team: team
    :type team: BaseTeam
    :param total_damage: total_damage
    :type total_damage: LoLTotalDamage
    :param total_heal: total_heal
    :type total_heal: int
    :param total_time_crowd_control_dealt: total_time_crowd_control_dealt
    :type total_time_crowd_control_dealt: int
    :param total_units_healed: total_units_healed
    :type total_units_healed: int
    :param true_damage: true_damage
    :type true_damage: LoLTrueDamage
    :param wards: wards
    :type wards: LoLWards
    :param wards_placed: wards_placed
    :type wards_placed: int
    """

    def __init__(
        self,
        assists: int,
        champion: LoLGamePlayerChampion,
        creep_score: int,
        cs_at_14: int,
        cs_diff_at_14: float,
        deaths: int,
        flags: LoLFlags,
        game_id: int,
        gold_earned: int,
        gold_percentage: float,
        gold_spent: int,
        items: List[BaseLoLItem],
        kills: int,
        kills_counters: LoLKillCounters,
        kills_series: LoLKillsSeries,
        largest_critical_strike: int,
        largest_killing_spree: int,
        largest_multi_kill: int,
        level: int,
        magic_damage: LoLMagicDamage,
        masteries: List[LoLMastery],
        minions_killed: int,
        opponent: LoLGamePlayerOpponent,
        physical_damage: LoLPhysicalDamage,
        player: BasePlayer,
        player_id: int,
        role: LoLGamePlayerRole,
        runes: List[LoLRune],
        runes_reforged: LoLPlayerRunesReforged,
        spells: List[LoLSpell],
        team: BaseTeam,
        total_damage: LoLTotalDamage,
        total_heal: int,
        total_time_crowd_control_dealt: int,
        total_units_healed: int,
        true_damage: LoLTrueDamage,
        wards: LoLWards,
        wards_placed: int,
    ):
        self.assists = assists
        self.champion = self._define_object(champion, LoLGamePlayerChampion)
        self.creep_score = creep_score
        self.cs_at_14 = cs_at_14
        self.cs_diff_at_14 = cs_diff_at_14
        self.deaths = deaths
        self.flags = self._define_object(flags, LoLFlags)
        self.game_id = game_id
        self.gold_earned = gold_earned
        self.gold_percentage = gold_percentage
        self.gold_spent = gold_spent
        self.items = self._define_list(items, BaseLoLItem)
        self.kills = kills
        self.kills_counters = self._define_object(kills_counters, LoLKillCounters)
        self.kills_series = self._define_object(kills_series, LoLKillsSeries)
        self.largest_critical_strike = largest_critical_strike
        self.largest_killing_spree = largest_killing_spree
        self.largest_multi_kill = largest_multi_kill
        self.level = level
        self.magic_damage = self._define_object(magic_damage, LoLMagicDamage)
        self.masteries = self._define_list(masteries, LoLMastery)
        self.minions_killed = minions_killed
        self.opponent = LoLGamePlayerOpponentGuard.return_one_of(opponent)
        self.physical_damage = self._define_object(physical_damage, LoLPhysicalDamage)
        self.player = self._define_object(player, BasePlayer)
        self.player_id = player_id
        self.role = self._enum_matching(role, LoLGamePlayerRole.list(), "role")
        self.runes = self._define_list(runes, LoLRune)
        self.runes_reforged = self._define_object(
            runes_reforged, LoLPlayerRunesReforged
        )
        self.spells = self._define_list(spells, LoLSpell)
        self.team = self._define_object(team, BaseTeam)
        self.total_damage = self._define_object(total_damage, LoLTotalDamage)
        self.total_heal = total_heal
        self.total_time_crowd_control_dealt = total_time_crowd_control_dealt
        self.total_units_healed = total_units_healed
        self.true_damage = self._define_object(true_damage, LoLTrueDamage)
        self.wards = self._define_object(wards, LoLWards)
        self.wards_placed = wards_placed
