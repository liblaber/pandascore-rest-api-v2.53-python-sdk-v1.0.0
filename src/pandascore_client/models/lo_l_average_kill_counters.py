# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


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
        self.inhibitors = self._define_number(
            "inhibitors", inhibitors, nullable=True, ge=0
        )
        self.neutral_minions = self._define_number(
            "neutral_minions", neutral_minions, nullable=True, ge=0
        )
        self.neutral_minions_enemy_jungle = self._define_number(
            "neutral_minions_enemy_jungle",
            neutral_minions_enemy_jungle,
            nullable=True,
            ge=0,
        )
        self.neutral_minions_team_jungle = self._define_number(
            "neutral_minions_team_jungle",
            neutral_minions_team_jungle,
            nullable=True,
            ge=0,
        )
        self.players = self._define_number("players", players, nullable=True, ge=0)
        self.turrets = self._define_number("turrets", turrets, nullable=True, ge=0)
        self.wards = self._define_number("wards", wards, nullable=True, ge=0)
