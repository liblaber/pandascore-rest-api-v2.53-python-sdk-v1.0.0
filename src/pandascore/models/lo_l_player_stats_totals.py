# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .lo_l_player_total_kill_counters import LoLPlayerTotalKillCounters
from .lo_l_kills_series import LoLKillsSeries


@JsonMap({})
class LoLPlayerStatsTotals(BaseModel):
    """LoLPlayerStatsTotals

    :param assists: assists
    :type assists: int
    :param deaths: deaths
    :type deaths: int
    :param games_lost: Number of games
    :type games_lost: int
    :param games_played: Number of games
    :type games_played: int
    :param games_won: Number of games
    :type games_won: int
    :param kill_counters: kill_counters
    :type kill_counters: LoLPlayerTotalKillCounters
    :param kills: kills
    :type kills: int
    :param kills_series: kills_series
    :type kills_series: LoLKillsSeries
    :param matches_lost: matches_lost
    :type matches_lost: int
    :param matches_played: matches_played
    :type matches_played: int
    :param matches_won: matches_won
    :type matches_won: int
    :param wards_placed: wards_placed
    :type wards_placed: int
    """

    def __init__(
        self,
        assists: int,
        deaths: int,
        games_lost: int,
        games_played: int,
        games_won: int,
        kill_counters: LoLPlayerTotalKillCounters,
        kills: int,
        kills_series: LoLKillsSeries,
        matches_lost: int,
        matches_played: int,
        matches_won: int,
        wards_placed: int,
    ):
        self.assists = assists
        self.deaths = deaths
        self.games_lost = games_lost
        self.games_played = games_played
        self.games_won = games_won
        self.kill_counters = self._define_object(
            kill_counters, LoLPlayerTotalKillCounters
        )
        self.kills = kills
        self.kills_series = self._define_object(kills_series, LoLKillsSeries)
        self.matches_lost = matches_lost
        self.matches_played = matches_played
        self.matches_won = matches_won
        self.wards_placed = wards_placed
