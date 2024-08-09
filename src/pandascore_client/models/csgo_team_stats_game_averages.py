# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class CsgoTeamStatsGameAverages(BaseModel):
    """CsgoTeamStatsGameAverages

    :param adr: Player's average damage per round
    :type adr: float
    :param assists: Average number of kill assists
    :type assists: float
    :param deaths: Average number of deaths
    :type deaths: float
    :param first_kills_diff: Average of first kill difference
    :type first_kills_diff: float
    :param flash_assists: Average number of flash assists
    :type flash_assists: float
    :param headshots: Average number of headshots
    :type headshots: float
    :param k_d_diff: Average kills deaths difference
    :type k_d_diff: float
    :param kast: Average percentage of rounds in which the player either had a kill, assist, survived or was traded
    :type kast: float
    :param kills: Average number of kills
    :type kills: float
    """

    def __init__(
        self,
        adr: float,
        assists: float,
        deaths: float,
        first_kills_diff: float,
        flash_assists: float,
        headshots: float,
        k_d_diff: float,
        kast: float,
        kills: float,
    ):
        """CsgoTeamStatsGameAverages

        :param adr: Player's average damage per round
        :type adr: float
        :param assists: Average number of kill assists
        :type assists: float
        :param deaths: Average number of deaths
        :type deaths: float
        :param first_kills_diff: Average of first kill difference
        :type first_kills_diff: float
        :param flash_assists: Average number of flash assists
        :type flash_assists: float
        :param headshots: Average number of headshots
        :type headshots: float
        :param k_d_diff: Average kills deaths difference
        :type k_d_diff: float
        :param kast: Average percentage of rounds in which the player either had a kill, assist, survived or was traded
        :type kast: float
        :param kills: Average number of kills
        :type kills: float
        """
        self.adr = self._define_number("adr", adr, nullable=True, ge=0)
        self.assists = self._define_number("assists", assists, nullable=True, ge=0)
        self.deaths = self._define_number("deaths", deaths, nullable=True, ge=0)
        self.first_kills_diff = self._define_number(
            "first_kills_diff", first_kills_diff, nullable=True
        )
        self.flash_assists = self._define_number(
            "flash_assists", flash_assists, nullable=True, ge=0
        )
        self.headshots = self._define_number(
            "headshots", headshots, nullable=True, ge=0
        )
        self.k_d_diff = self._define_number("k_d_diff", k_d_diff, nullable=True)
        self.kast = self._define_number("kast", kast, nullable=True, ge=0)
        self.kills = self._define_number("kills", kills, nullable=True, ge=0)