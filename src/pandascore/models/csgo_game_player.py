from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .base_opponent import BaseOpponent, BaseOpponentGuard
from .base_player import BasePlayer
from .base_team import BaseTeam


@JsonMap({})
class CsgoGamePlayer(BaseModel):
    """Player's data for a game

    :param adr: Player's average damage per round
    :type adr: float
    :param assists: Player's number of kill assists for a game
    :type assists: int
    :param deaths: Player's number of deaths
    :type deaths: int
    :param first_kills_diff: First kill difference
    :type first_kills_diff: int
    :param flash_assists: Player's number of flash assists for a game
    :type flash_assists: float
    :param game_id: Counter-Strike game ID
    :type game_id: int
    :param headshots: Player's number of headshots
    :type headshots: int
    :param k_d_diff: Player's kills deaths difference for a game
    :type k_d_diff: int
    :param kast: Percentage of rounds in which the player either had a kill, assist, survived or was traded
    :type kast: float
    :param kills: Player's number of kills
    :type kills: int
    :param opponent: opponent
    :type opponent: BaseOpponent
    :param player: player
    :type player: BasePlayer
    :param rating: rating
    :type rating: float
    :param team: team
    :type team: BaseTeam
    """

    def __init__(
        self,
        adr: float,
        assists: int,
        deaths: int,
        first_kills_diff: int,
        flash_assists: float,
        game_id: int,
        headshots: int,
        k_d_diff: int,
        kast: float,
        kills: int,
        opponent: BaseOpponent,
        player: BasePlayer,
        rating: float,
        team: BaseTeam,
    ):
        self.adr = adr
        self.assists = assists
        self.deaths = deaths
        self.first_kills_diff = first_kills_diff
        self.flash_assists = flash_assists
        self.game_id = game_id
        self.headshots = headshots
        self.k_d_diff = k_d_diff
        self.kast = kast
        self.kills = kills
        self.opponent = BaseOpponentGuard.return_one_of(opponent)
        self.player = self._define_object(player, BasePlayer)
        self.rating = rating
        self.team = self._define_object(team, BaseTeam)
