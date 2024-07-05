from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class OwPlayerGameAverages(BaseModel):
    """OwPlayerGameAverages

    :param damage_done: damage_done
    :type damage_done: float
    :param deaths: deaths
    :type deaths: float
    :param destructions: destructions
    :type destructions: float
    :param eliminations: eliminations
    :type eliminations: float
    :param healing_done: healing_done
    :type healing_done: float
    :param kills: kills
    :type kills: float
    :param resurrections: resurrections
    :type resurrections: float
    :param ultimates: ultimates
    :type ultimates: float
    """

    def __init__(
        self,
        damage_done: float,
        deaths: float,
        destructions: float,
        eliminations: float,
        healing_done: float,
        kills: float,
        resurrections: float,
        ultimates: float,
    ):
        self.damage_done = damage_done
        self.deaths = deaths
        self.destructions = destructions
        self.eliminations = eliminations
        self.healing_done = healing_done
        self.kills = kills
        self.resurrections = resurrections
        self.ultimates = ultimates
