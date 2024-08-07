from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class Dota2TeamStatsTotals(BaseModel):
    """Dota2TeamStatsTotals

    :param assists: assists
    :type assists: int
    :param deaths: deaths
    :type deaths: int
    :param dire_games_lost: Number of games
    :type dire_games_lost: int
    :param dire_games_won: Number of games
    :type dire_games_won: int
    :param games_lost: Number of games
    :type games_lost: int
    :param games_played: Number of games
    :type games_played: int
    :param games_won: Number of games
    :type games_won: int
    :param kills: kills
    :type kills: int
    :param matches_draw: matches_draw
    :type matches_draw: int
    :param matches_lost: matches_lost
    :type matches_lost: int
    :param matches_played: matches_played
    :type matches_played: int
    :param matches_won: matches_won
    :type matches_won: int
    :param observer_wards_destroyed: observer_wards_destroyed
    :type observer_wards_destroyed: int
    :param observer_wards_placed: observer_wards_placed
    :type observer_wards_placed: int
    :param radiant_games_lost: Number of games
    :type radiant_games_lost: int
    :param radiant_games_won: Number of games
    :type radiant_games_won: int
    :param roshan_kills: The total number of Roshans killed by the team
    :type roshan_kills: int
    :param sentry_wards_destroyed: sentry_wards_destroyed
    :type sentry_wards_destroyed: int
    :param sentry_wards_placed: sentry_wards_placed
    :type sentry_wards_placed: int
    :param tower_kills: tower_kills
    :type tower_kills: int
    """

    def __init__(
        self,
        assists: int,
        deaths: int,
        dire_games_lost: int,
        dire_games_won: int,
        games_lost: int,
        games_played: int,
        games_won: int,
        kills: int,
        matches_draw: int,
        matches_lost: int,
        matches_played: int,
        matches_won: int,
        observer_wards_destroyed: int,
        observer_wards_placed: int,
        radiant_games_lost: int,
        radiant_games_won: int,
        roshan_kills: int,
        sentry_wards_destroyed: int,
        sentry_wards_placed: int,
        tower_kills: int,
    ):
        self.assists = assists
        self.deaths = deaths
        self.dire_games_lost = dire_games_lost
        self.dire_games_won = dire_games_won
        self.games_lost = games_lost
        self.games_played = games_played
        self.games_won = games_won
        self.kills = kills
        self.matches_draw = matches_draw
        self.matches_lost = matches_lost
        self.matches_played = matches_played
        self.matches_won = matches_won
        self.observer_wards_destroyed = observer_wards_destroyed
        self.observer_wards_placed = observer_wards_placed
        self.radiant_games_lost = radiant_games_lost
        self.radiant_games_won = radiant_games_won
        self.roshan_kills = roshan_kills
        self.sentry_wards_destroyed = sentry_wards_destroyed
        self.sentry_wards_placed = sentry_wards_placed
        self.tower_kills = tower_kills
