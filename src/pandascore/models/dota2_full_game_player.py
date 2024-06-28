# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from typing import Union
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel
from .dota2_per_hero_ability import Dota2PerHeroAbility
from .dota2_item import Dota2Item
from .base_player import BasePlayer


class Dota2FullGamePlayerFaction(Enum):
    """An enumeration representing different categories.

    :cvar DIRE: "dire"
    :vartype DIRE: str
    :cvar RADIANT: "radiant"
    :vartype RADIANT: str
    """

    DIRE = "dire"
    RADIANT = "radiant"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, Dota2FullGamePlayerFaction._member_map_.values())
        )


@JsonMap({"id_": "id"})
class Dota2FullGamePlayerHero(BaseModel):
    """Dota2FullGamePlayerHero

    :param id_: id_
    :type id_: int
    :param image_url: image_url
    :type image_url: str
    :param localized_name: localized_name
    :type localized_name: str
    :param name: name
    :type name: str
    """

    def __init__(self, id_: int, image_url: str, localized_name: str, name: str):
        self.id_ = id_
        self.image_url = image_url
        self.localized_name = localized_name
        self.name = self._pattern_matching(name, "^[a-z0-9_-]+$", "name")


@JsonMap({"id_": "id"})
class Opponent1_1(BaseModel):
    """Opponent1_1

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
class Opponent2_1(BaseModel):
    """Opponent2_1

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


class Dota2FullGamePlayerOpponentGuard(OneOfBaseModel):
    class_list = {"Opponent1_1": Opponent1_1, "Opponent2_1": Opponent2_1}


Dota2FullGamePlayerOpponent = Union[Opponent1_1, Opponent2_1]


@JsonMap({"id_": "id"})
class Dota2FullGamePlayerTeam(BaseModel):
    """Dota2FullGamePlayerTeam

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


@JsonMap({})
class Dota2FullGamePlayer(BaseModel):
    """Player's data for a game

    :param abilities: abilities
    :type abilities: List[Dota2PerHeroAbility]
    :param assists: Player's number of assists for a game
    :type assists: int
    :param camps_stacked: camps_stacked
    :type camps_stacked: int
    :param creeps_stacked: creeps_stacked
    :type creeps_stacked: int
    :param damage_taken: damage_taken
    :type damage_taken: int
    :param deaths: deaths
    :type deaths: int
    :param denies: Number of denies performed by a player
    :type denies: int
    :param faction: faction
    :type faction: Dota2FullGamePlayerFaction
    :param game_id: game_id
    :type game_id: int
    :param gold_per_min: gold_per_min
    :type gold_per_min: int
    :param gold_percentage: Percentage of gold (per min) the player had compared to the total gold of the team
    :type gold_percentage: float
    :param gold_remaining: gold_remaining
    :type gold_remaining: int
    :param gold_spent: gold_spent
    :type gold_spent: int
    :param heal: Healing (in HP) performed by the player
    :type heal: int
    :param hero: hero
    :type hero: Dota2FullGamePlayerHero
    :param hero_damage: hero_damage
    :type hero_damage: int
    :param hero_damage_percentage: hero_damage_percentage
    :type hero_damage_percentage: float
    :param hero_level: hero_level
    :type hero_level: int
    :param items: items
    :type items: List[Dota2Item]
    :param kills: kills
    :type kills: int
    :param lane_creep: lane_creep
    :type lane_creep: int
    :param last_hits: last_hits
    :type last_hits: int
    :param net_worth: Net worth of the player
    :type net_worth: int
    :param neutral_creep: neutral_creep
    :type neutral_creep: int
    :param observer_used: observer_used
    :type observer_used: int
    :param observer_wards_destroyed: observer_wards_destroyed
    :type observer_wards_destroyed: int
    :param observer_wards_purchased: observer_wards_purchased
    :type observer_wards_purchased: int
    :param opponent: opponent
    :type opponent: Dota2FullGamePlayerOpponent
    :param player: player
    :type player: BasePlayer
    :param role: Position of the player (1, 2, 3, 4, 5)
    :type role: int
    :param sentry_used: sentry_used
    :type sentry_used: int
    :param sentry_wards_destroyed: sentry_wards_destroyed
    :type sentry_wards_destroyed: int
    :param sentry_wards_purchased: sentry_wards_purchased
    :type sentry_wards_purchased: int
    :param team: team
    :type team: Dota2FullGamePlayerTeam
    :param team_id: team_id
    :type team_id: int
    :param tower_damage: tower_damage
    :type tower_damage: int
    :param tower_kills: tower_kills
    :type tower_kills: int
    :param xp_per_min: xp_per_min
    :type xp_per_min: int
    """

    def __init__(
        self,
        abilities: List[Dota2PerHeroAbility],
        assists: int,
        camps_stacked: int,
        creeps_stacked: int,
        damage_taken: int,
        deaths: int,
        denies: int,
        faction: Dota2FullGamePlayerFaction,
        game_id: int,
        gold_per_min: int,
        gold_percentage: float,
        gold_remaining: int,
        gold_spent: int,
        heal: int,
        hero: Dota2FullGamePlayerHero,
        hero_damage: int,
        hero_damage_percentage: float,
        hero_level: int,
        items: List[Dota2Item],
        kills: int,
        lane_creep: int,
        last_hits: int,
        net_worth: int,
        neutral_creep: int,
        observer_used: int,
        observer_wards_destroyed: int,
        observer_wards_purchased: int,
        opponent: Dota2FullGamePlayerOpponent,
        player: BasePlayer,
        role: int,
        sentry_used: int,
        sentry_wards_destroyed: int,
        sentry_wards_purchased: int,
        team: Dota2FullGamePlayerTeam,
        team_id: int,
        tower_damage: int,
        tower_kills: int,
        xp_per_min: int,
    ):
        self.abilities = self._define_list(abilities, Dota2PerHeroAbility)
        self.assists = assists
        self.camps_stacked = camps_stacked
        self.creeps_stacked = creeps_stacked
        self.damage_taken = damage_taken
        self.deaths = deaths
        self.denies = denies
        self.faction = self._enum_matching(
            faction, Dota2FullGamePlayerFaction.list(), "faction"
        )
        self.game_id = game_id
        self.gold_per_min = gold_per_min
        self.gold_percentage = gold_percentage
        self.gold_remaining = gold_remaining
        self.gold_spent = gold_spent
        self.heal = heal
        self.hero = self._define_object(hero, Dota2FullGamePlayerHero)
        self.hero_damage = hero_damage
        self.hero_damage_percentage = hero_damage_percentage
        self.hero_level = hero_level
        self.items = self._define_list(items, Dota2Item)
        self.kills = kills
        self.lane_creep = lane_creep
        self.last_hits = last_hits
        self.net_worth = net_worth
        self.neutral_creep = neutral_creep
        self.observer_used = observer_used
        self.observer_wards_destroyed = observer_wards_destroyed
        self.observer_wards_purchased = observer_wards_purchased
        self.opponent = Dota2FullGamePlayerOpponentGuard.return_one_of(opponent)
        self.player = self._define_object(player, BasePlayer)
        self.role = role
        self.sentry_used = sentry_used
        self.sentry_wards_destroyed = sentry_wards_destroyed
        self.sentry_wards_purchased = sentry_wards_purchased
        self.team = self._define_object(team, Dota2FullGamePlayerTeam)
        self.team_id = team_id
        self.tower_damage = tower_damage
        self.tower_kills = tower_kills
        self.xp_per_min = xp_per_min