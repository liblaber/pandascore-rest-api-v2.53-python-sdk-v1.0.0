from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class LoLAverageKillCounters(BaseModel):
    """LoLAverageKillCounters

    :param inhibitors: inhibitors
    :type inhibitors: float
    :param neutral_minions: neutral_minions
    :type neutral_minions: float
    :param neutral_minions_enemy_jungle: neutral_minions_enemy_jungle
    :type neutral_minions_enemy_jungle: float
    :param neutral_minions_team_jungle: neutral_minions_team_jungle
    :type neutral_minions_team_jungle: float
    :param players: players
    :type players: float
    :param turrets: turrets
    :type turrets: float
    :param wards: wards
    :type wards: float
    """

    def __init__(
        self,
        inhibitors: float,
        neutral_minions: float,
        neutral_minions_enemy_jungle: float,
        neutral_minions_team_jungle: float,
        players: float,
        turrets: float,
        wards: float,
    ):
        self.inhibitors = inhibitors
        self.neutral_minions = neutral_minions
        self.neutral_minions_enemy_jungle = neutral_minions_enemy_jungle
        self.neutral_minions_team_jungle = neutral_minions_team_jungle
        self.players = players
        self.turrets = turrets
        self.wards = wards
