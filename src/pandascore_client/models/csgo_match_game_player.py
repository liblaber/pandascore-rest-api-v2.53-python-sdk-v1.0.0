# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class CsgoMatchGamePlayer(BaseModel):
    """Player's data for a Game in a CSGO Match

    :param adr: Player's average damage per round
    :type adr: float
    :param assists: Player's number of kill assists for a game
    :type assists: int
    :param deaths: Player's number of deaths
    :type deaths: int
    :param flash_assists: Player's number of flash assists for a game
    :type flash_assists: float
    :param headshots: Player's number of headshots
    :type headshots: int
    :param k_d_diff: Player's kills deaths difference for a game
    :type k_d_diff: int
    :param kast: Percentage of rounds in which the player either had a kill, assist, survived or was traded
    :type kast: float
    :param kills: Player's number of kills
    :type kills: int
    :param player_id: ID of the player
    :type player_id: int
    """

    def __init__(
        self,
        adr: float,
        assists: int,
        deaths: int,
        flash_assists: float,
        headshots: int,
        k_d_diff: int,
        kast: float,
        kills: int,
        player_id: int,
    ):
        """Player's data for a Game in a CSGO Match

        :param adr: Player's average damage per round
        :type adr: float
        :param assists: Player's number of kill assists for a game
        :type assists: int
        :param deaths: Player's number of deaths
        :type deaths: int
        :param flash_assists: Player's number of flash assists for a game
        :type flash_assists: float
        :param headshots: Player's number of headshots
        :type headshots: int
        :param k_d_diff: Player's kills deaths difference for a game
        :type k_d_diff: int
        :param kast: Percentage of rounds in which the player either had a kill, assist, survived or was traded
        :type kast: float
        :param kills: Player's number of kills
        :type kills: int
        :param player_id: ID of the player
        :type player_id: int
        """
        self.adr = self._define_number("adr", adr, nullable=True, ge=0)
        self.assists = self._define_number("assists", assists, nullable=True, ge=0)
        self.deaths = self._define_number("deaths", deaths, nullable=True, ge=0)
        self.flash_assists = self._define_number(
            "flash_assists", flash_assists, nullable=True, ge=0
        )
        self.headshots = self._define_number(
            "headshots", headshots, nullable=True, ge=0
        )
        self.k_d_diff = self._define_number("k_d_diff", k_d_diff, nullable=True)
        self.kast = self._define_number("kast", kast, nullable=True, ge=0)
        self.kills = self._define_number("kills", kills, nullable=True, ge=0)
        self.player_id = self._define_number("player_id", player_id, ge=1)
