from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class OwPlayerTotals(BaseModel):
    """OwPlayerTotals

    :param average_time_to_charge_ultimate: average_time_to_charge_ultimate
    :type average_time_to_charge_ultimate: float
    :param damage_done: damage_done
    :type damage_done: float
    :param deaths: deaths
    :type deaths: float
    :param destructions: destructions
    :type destructions: float
    :param eliminations: eliminations
    :type eliminations: int
    :param healing_done: healing_done
    :type healing_done: float
    :param kills: kills
    :type kills: float
    :param map_draw: map_draw
    :type map_draw: float
    :param map_lost: map_lost
    :type map_lost: float
    :param map_won: map_won
    :type map_won: float
    :param resurrections: resurrections
    :type resurrections: float
    :param time_played: Time in seconds
    :type time_played: int
    :param ultimates: ultimates
    :type ultimates: float
    """

    def __init__(
        self,
        average_time_to_charge_ultimate: float,
        damage_done: float,
        deaths: float,
        destructions: float,
        eliminations: int,
        healing_done: float,
        kills: float,
        map_draw: float,
        map_lost: float,
        map_won: float,
        resurrections: float,
        time_played: int,
        ultimates: float,
    ):
        self.average_time_to_charge_ultimate = average_time_to_charge_ultimate
        self.damage_done = damage_done
        self.deaths = deaths
        self.destructions = destructions
        self.eliminations = eliminations
        self.healing_done = healing_done
        self.kills = kills
        self.map_draw = map_draw
        self.map_lost = map_lost
        self.map_won = map_won
        self.resurrections = resurrections
        self.time_played = time_played
        self.ultimates = ultimates
