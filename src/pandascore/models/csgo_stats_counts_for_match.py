from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class CsgoStatsCountsForMatch(BaseModel):
    """CsgoStatsCountsForMatch

    :param assists: Player's number of kill assists for a game
    :type assists: int
    :param deaths: Player's number of deaths
    :type deaths: int
    :param first_kills_diff: First kill difference
    :type first_kills_diff: int
    :param flash_assists: Player's number of flash assists for a game
    :type flash_assists: float
    :param games_draw: Number of games
    :type games_draw: int
    :param games_lost: Number of games
    :type games_lost: int
    :param games_played: Number of games
    :type games_played: int
    :param games_won: Number of games
    :type games_won: int
    :param headshots: Player's number of headshots
    :type headshots: int
    :param k_d_diff: Player's kills deaths difference for a game
    :type k_d_diff: int
    :param kills: Player's number of kills
    :type kills: int
    :param rounds_played: Number of rounds played
    :type rounds_played: int
    """

    def __init__(
        self,
        assists: int,
        deaths: int,
        first_kills_diff: int,
        flash_assists: float,
        games_draw: int,
        games_lost: int,
        games_played: int,
        games_won: int,
        headshots: int,
        k_d_diff: int,
        kills: int,
        rounds_played: int,
    ):
        self.assists = assists
        self.deaths = deaths
        self.first_kills_diff = first_kills_diff
        self.flash_assists = flash_assists
        self.games_draw = games_draw
        self.games_lost = games_lost
        self.games_played = games_played
        self.games_won = games_won
        self.headshots = headshots
        self.k_d_diff = k_d_diff
        self.kills = kills
        self.rounds_played = rounds_played
