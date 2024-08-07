from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class CsgoStatsRoundAverages(BaseModel):
    """CsgoStatsRoundAverages

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
    :param kills: Average number of kills
    :type kills: float
    """

    def __init__(
        self,
        assists: float,
        deaths: float,
        first_kills_diff: float,
        flash_assists: float,
        headshots: float,
        k_d_diff: float,
        kills: float,
    ):
        self.assists = assists
        self.deaths = deaths
        self.first_kills_diff = first_kills_diff
        self.flash_assists = flash_assists
        self.headshots = headshots
        self.k_d_diff = k_d_diff
        self.kills = kills
