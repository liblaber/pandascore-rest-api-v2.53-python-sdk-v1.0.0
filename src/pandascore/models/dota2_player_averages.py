from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class Dota2PlayerAverages(BaseModel):
    """Dota2PlayerAverages

    :param assists: assists
    :type assists: float
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
    :param gold_per_minute: gold_per_minute
    :type gold_per_minute: float
    :param gold_percentage: Percentage of gold (per min) the player had compared to the total gold of the team
    :type gold_percentage: float
    :param heal: heal
    :type heal: float
    :param hero_damage: hero_damage
    :type hero_damage: float
    :param hero_damage_percentage: Percentage of damage to heroes the player had compared to the total damage of the team
    :type hero_damage_percentage: float
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
    :param observer_wards_destroyed: observer_wards_destroyed
    :type observer_wards_destroyed: float
    :param observer_wards_placed: observer_wards_placed
    :type observer_wards_placed: float
    :param observer_wards_purchased: observer_wards_purchased
    :type observer_wards_purchased: float
    :param sentry_wards_destroyed: sentry_wards_destroyed
    :type sentry_wards_destroyed: float
    :param sentry_wards_placed: sentry_wards_placed
    :type sentry_wards_placed: float
    :param sentry_wards_purchased: sentry_wards_purchased
    :type sentry_wards_purchased: float
    :param tower_damage: tower_damage
    :type tower_damage: float
    :param tower_kills: tower_kills
    :type tower_kills: float
    :param wards_placed: wards_placed
    :type wards_placed: float
    :param xp_per_minute: xp_per_minute
    :type xp_per_minute: float
    """

    def __init__(
        self,
        assists: float,
        camps_stacked: float,
        creeps_stacked: float,
        damage_taken: float,
        deaths: float,
        denies: float,
        gold_per_minute: float,
        gold_percentage: float,
        heal: float,
        hero_damage: float,
        hero_damage_percentage: float,
        kills: float,
        lane_creep: float,
        last_hits: float,
        net_worth: float,
        neutral_creep: float,
        observer_wards_destroyed: float,
        observer_wards_placed: float,
        observer_wards_purchased: float,
        sentry_wards_destroyed: float,
        sentry_wards_placed: float,
        sentry_wards_purchased: float,
        tower_damage: float,
        tower_kills: float,
        wards_placed: float,
        xp_per_minute: float,
    ):
        self.assists = assists
        self.camps_stacked = camps_stacked
        self.creeps_stacked = creeps_stacked
        self.damage_taken = damage_taken
        self.deaths = deaths
        self.denies = denies
        self.gold_per_minute = gold_per_minute
        self.gold_percentage = gold_percentage
        self.heal = heal
        self.hero_damage = hero_damage
        self.hero_damage_percentage = hero_damage_percentage
        self.kills = kills
        self.lane_creep = lane_creep
        self.last_hits = last_hits
        self.net_worth = net_worth
        self.neutral_creep = neutral_creep
        self.observer_wards_destroyed = observer_wards_destroyed
        self.observer_wards_placed = observer_wards_placed
        self.observer_wards_purchased = observer_wards_purchased
        self.sentry_wards_destroyed = sentry_wards_destroyed
        self.sentry_wards_placed = sentry_wards_placed
        self.sentry_wards_purchased = sentry_wards_purchased
        self.tower_damage = tower_damage
        self.tower_kills = tower_kills
        self.wards_placed = wards_placed
        self.xp_per_minute = xp_per_minute
