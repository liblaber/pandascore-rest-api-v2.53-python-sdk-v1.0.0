from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class LoLKillCounters(BaseModel):
    """LoLKillCounters

    :param inhibitors: Number of inhibitors killed by the player
    :type inhibitors: int
    :param neutral_minions: Creep Score awarded for killing neutral minions. <br/> <br/>NB: This can be different than the actual number of neutral minions killed.
    :type neutral_minions: int
    :param neutral_minions_enemy_jungle: Creep Score awarded for killing neutral minions in the player's enemy jungle. <br/> <br/>NB: This can be different than the actual number of neutral minions killed.
    :type neutral_minions_enemy_jungle: int
    :param neutral_minions_team_jungle: Creep Score awarded for killing neutral minions in the player's team jungle. <br/> <br/>NB: This can be different than the actual number of neutral minions killed.
    :type neutral_minions_team_jungle: int
    :param players: Number of players killed
    :type players: int
    :param turrets: Number of turrets killed
    :type turrets: int
    :param wards: Number of wards killed by the player
    :type wards: int
    """

    def __init__(
        self,
        inhibitors: int,
        neutral_minions: int,
        neutral_minions_enemy_jungle: int,
        neutral_minions_team_jungle: int,
        players: int,
        turrets: int,
        wards: int,
    ):
        self.inhibitors = inhibitors
        self.neutral_minions = neutral_minions
        self.neutral_minions_enemy_jungle = neutral_minions_enemy_jungle
        self.neutral_minions_team_jungle = neutral_minions_team_jungle
        self.players = players
        self.turrets = turrets
        self.wards = wards
