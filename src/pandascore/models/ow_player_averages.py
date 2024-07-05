from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class OwPlayerAverages(BaseModel):
    """OwPlayerAverages

    :param average_time_to_charge_ultimate: average_time_to_charge_ultimate
    :type average_time_to_charge_ultimate: float
    :param deaths_count: deaths_count
    :type deaths_count: float
    :param deaths_per_10_minutes: deaths_per_10_minutes
    :type deaths_per_10_minutes: float
    :param destructions_count: destructions_count
    :type destructions_count: float
    :param destructions_per_10_minutes: destructions_per_10_minutes
    :type destructions_per_10_minutes: float
    :param kills_count: kills_count
    :type kills_count: float
    :param kills_per_10_minutes: kills_per_10_minutes
    :type kills_per_10_minutes: float
    :param map_draw: map_draw
    :type map_draw: float
    :param map_lost: map_lost
    :type map_lost: float
    :param map_won: map_won
    :type map_won: float
    :param resurrections_count: resurrections_count
    :type resurrections_count: float
    :param resurrections_per_10_minutes: resurrections_per_10_minutes
    :type resurrections_per_10_minutes: float
    :param ultimates_count: ultimates_count
    :type ultimates_count: float
    :param ultimates_per_10_minutes: ultimates_per_10_minutes
    :type ultimates_per_10_minutes: float
    """

    def __init__(
        self,
        average_time_to_charge_ultimate: float,
        deaths_count: float,
        deaths_per_10_minutes: float,
        destructions_count: float,
        destructions_per_10_minutes: float,
        kills_count: float,
        kills_per_10_minutes: float,
        map_draw: float,
        map_lost: float,
        map_won: float,
        resurrections_count: float,
        resurrections_per_10_minutes: float,
        ultimates_count: float,
        ultimates_per_10_minutes: float,
    ):
        self.average_time_to_charge_ultimate = average_time_to_charge_ultimate
        self.deaths_count = deaths_count
        self.deaths_per_10_minutes = deaths_per_10_minutes
        self.destructions_count = destructions_count
        self.destructions_per_10_minutes = destructions_per_10_minutes
        self.kills_count = kills_count
        self.kills_per_10_minutes = kills_per_10_minutes
        self.map_draw = map_draw
        self.map_lost = map_lost
        self.map_won = map_won
        self.resurrections_count = resurrections_count
        self.resurrections_per_10_minutes = resurrections_per_10_minutes
        self.ultimates_count = ultimates_count
        self.ultimates_per_10_minutes = ultimates_per_10_minutes
