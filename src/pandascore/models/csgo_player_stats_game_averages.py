from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class CsgoPlayerStatsGameAverages(BaseModel):
    """CsgoPlayerStatsGameAverages

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
    :param hltv_game_rating: Average rating
    :type hltv_game_rating: float
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
        hltv_game_rating: float,
        k_d_diff: float,
        kast: float,
        kills: float,
    ):
        self.adr = adr
        self.assists = assists
        self.deaths = deaths
        self.first_kills_diff = first_kills_diff
        self.flash_assists = flash_assists
        self.headshots = headshots
        self.hltv_game_rating = hltv_game_rating
        self.k_d_diff = k_d_diff
        self.kast = kast
        self.kills = kills
