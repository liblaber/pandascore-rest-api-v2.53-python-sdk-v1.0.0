from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .valorant_agent_stats import ValorantAgentStats
from .valorant_player_clutch_wins import ValorantPlayerClutchWins
from .valorant_game_player import ValorantGamePlayer
from .base_player import BasePlayer
from .valorant_player_streaks import ValorantPlayerStreaks
from .tournament import Tournament


@JsonMap({})
class ValorantStatsForPlayerByTournament(BaseModel):
    """ValorantStatsForPlayerByTournament

    :param agents: Agents picks, wins, and losses stats for this map
    :type agents: List[ValorantAgentStats]
    :param assists: Number of player's assists
    :type assists: int
    :param average_damage_per_round: Average damage per round (ADR) of the player
    :type average_damage_per_round: float
    :param clutch_wins: Round wins when the player was the last team member alive
    :type clutch_wins: ValorantPlayerClutchWins
    :param deaths: Number of player's death
    :type deaths: int
    :param defused_spikes: Number of spikes defused by the player
    :type defused_spikes: int
    :param first_deaths: Number of rounds where the player died first
    :type first_deaths: int
    :param first_kill_percentage: First kill percentage of the player
    :type first_kill_percentage: float
    :param first_kills: Number of rounds where the player did the first kill
    :type first_kills: int
    :param headshot_percentage: Percentage of headshots within the player's shots
    :type headshot_percentage: float
    :param kills: Number of player's kills
    :type kills: int
    :param last_games: last_games
    :type last_games: List[ValorantGamePlayer]
    :param planted_spikes: Number of spikes planted by the player
    :type planted_spikes: int
    :param player: player
    :type player: BasePlayer
    :param streaks: Streaks done by the player (in a given round)
    :type streaks: ValorantPlayerStreaks
    :param total_games: Amount of games played by the player
    :type total_games: int
    :param tournament: tournament
    :type tournament: Tournament
    """

    def __init__(
        self,
        agents: List[ValorantAgentStats],
        assists: int,
        average_damage_per_round: float,
        clutch_wins: ValorantPlayerClutchWins,
        deaths: int,
        defused_spikes: int,
        first_deaths: int,
        first_kill_percentage: float,
        first_kills: int,
        headshot_percentage: float,
        kills: int,
        last_games: List[ValorantGamePlayer],
        planted_spikes: int,
        player: BasePlayer,
        streaks: ValorantPlayerStreaks,
        total_games: int,
        tournament: Tournament,
    ):
        self.agents = self._define_list(agents, ValorantAgentStats)
        self.assists = assists
        self.average_damage_per_round = average_damage_per_round
        self.clutch_wins = self._define_object(clutch_wins, ValorantPlayerClutchWins)
        self.deaths = deaths
        self.defused_spikes = defused_spikes
        self.first_deaths = first_deaths
        self.first_kill_percentage = first_kill_percentage
        self.first_kills = first_kills
        self.headshot_percentage = headshot_percentage
        self.kills = kills
        self.last_games = self._define_list(last_games, ValorantGamePlayer)
        self.planted_spikes = planted_spikes
        self.player = self._define_object(player, BasePlayer)
        self.streaks = self._define_object(streaks, ValorantPlayerStreaks)
        self.total_games = total_games
        self.tournament = self._define_object(tournament, Tournament)
