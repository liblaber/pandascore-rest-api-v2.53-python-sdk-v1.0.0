from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .dota2_team_ratios import Dota2TeamRatios


@JsonMap({})
class Dota2TeamAverages(BaseModel):
    """Dota2TeamAverages

    :param assists: assists
    :type assists: float
    :param barracks: barracks
    :type barracks: float
    :param camps_stacked: The average number of camps stacked by the team
    :type camps_stacked: float
    :param creeps_stacked: creeps_stacked
    :type creeps_stacked: float
    :param damage_taken: The average damage taken by the team
    :type damage_taken: float
    :param deaths: deaths
    :type deaths: float
    :param denies: Average number of denies per game
    :type denies: float
    :param game_length: Duration of the game in seconds. <br/>`null` when the game status is not `finished`
    :type game_length: int
    :param gold_per_min: gold_per_min
    :type gold_per_min: float
    :param gold_spent: The average of the team's gold spent
    :type gold_spent: float
    :param heal: heal
    :type heal: float
    :param hero_damage: hero_damage
    :type hero_damage: float
    :param kills: kills
    :type kills: float
    :param lane_creep: lane_creep
    :type lane_creep: float
    :param last_hits: last_hits
    :type last_hits: float
    :param net_worth: net_worth
    :type net_worth: float
    :param neutral_creep: neutral_creep
    :type neutral_creep: float
    :param observer_used: observer_used
    :type observer_used: float
    :param observer_wards_destroyed: observer_wards_destroyed
    :type observer_wards_destroyed: float
    :param observer_wards_purchased: observer_wards_purchased
    :type observer_wards_purchased: float
    :param ratios: ratios
    :type ratios: Dota2TeamRatios
    :param roshan_kills: The average number of Roshans killed by the team
    :type roshan_kills: float
    :param sentry_used: sentry_used
    :type sentry_used: float
    :param sentry_wards_destroyed: sentry_wards_destroyed
    :type sentry_wards_destroyed: float
    :param sentry_wards_purchased: sentry_wards_purchased
    :type sentry_wards_purchased: float
    :param tower_damage: tower_damage
    :type tower_damage: float
    :param tower_kills: tower_kills
    :type tower_kills: float
    :param xp_per_min: xp_per_min
    :type xp_per_min: float
    """

    def __init__(
        self,
        assists: float,
        barracks: float,
        camps_stacked: float,
        creeps_stacked: float,
        damage_taken: float,
        deaths: float,
        denies: float,
        game_length: int,
        gold_per_min: float,
        gold_spent: float,
        heal: float,
        hero_damage: float,
        kills: float,
        lane_creep: float,
        last_hits: float,
        net_worth: float,
        neutral_creep: float,
        observer_used: float,
        observer_wards_destroyed: float,
        observer_wards_purchased: float,
        ratios: Dota2TeamRatios,
        roshan_kills: float,
        sentry_used: float,
        sentry_wards_destroyed: float,
        sentry_wards_purchased: float,
        tower_damage: float,
        tower_kills: float,
        xp_per_min: float,
    ):
        self.assists = assists
        self.barracks = barracks
        self.camps_stacked = camps_stacked
        self.creeps_stacked = creeps_stacked
        self.damage_taken = damage_taken
        self.deaths = deaths
        self.denies = denies
        self.game_length = game_length
        self.gold_per_min = gold_per_min
        self.gold_spent = gold_spent
        self.heal = heal
        self.hero_damage = hero_damage
        self.kills = kills
        self.lane_creep = lane_creep
        self.last_hits = last_hits
        self.net_worth = net_worth
        self.neutral_creep = neutral_creep
        self.observer_used = observer_used
        self.observer_wards_destroyed = observer_wards_destroyed
        self.observer_wards_purchased = observer_wards_purchased
        self.ratios = self._define_object(ratios, Dota2TeamRatios)
        self.roshan_kills = roshan_kills
        self.sentry_used = sentry_used
        self.sentry_wards_destroyed = sentry_wards_destroyed
        self.sentry_wards_purchased = sentry_wards_purchased
        self.tower_damage = tower_damage
        self.tower_kills = tower_kills
        self.xp_per_min = xp_per_min
