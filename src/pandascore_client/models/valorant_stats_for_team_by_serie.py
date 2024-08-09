# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .valorant_team_clutch_wins import ValorantTeamClutchWins
from .base_valorant_game import BaseValorantGame
from .valorant_team_map_stats import ValorantTeamMapStats
from .serie import Serie
from .valorant_team_streaks import ValorantTeamStreaks
from .base_valorant_team import BaseValorantTeam


@JsonMap({})
class ValorantStatsForTeamBySerie(BaseModel):
    """ValorantStatsForTeamBySerie

    :param assists: Number of team's assists
    :type assists: int
    :param clutch_wins: Rounds wins with a single team member alive
    :type clutch_wins: ValorantTeamClutchWins
    :param deaths: Number of team's death
    :type deaths: int
    :param defused_spikes: Number of spikes defused by a team member
    :type defused_spikes: int
    :param first_deaths: Number of rounds where a team member died first
    :type first_deaths: int
    :param first_kills: Number of rounds where a team member did the first kill
    :type first_kills: int
    :param games_draw: Number of games
    :type games_draw: int
    :param games_lost: Number of games
    :type games_lost: int
    :param games_played: Number of games
    :type games_played: int
    :param games_won: Number of games
    :type games_won: int
    :param headshot_percentage: Percentage of headshots within the player's shots
    :type headshot_percentage: float
    :param kills: Number of team's kills
    :type kills: int
    :param kills_per_death: Ratio of team's kills per deaths
    :type kills_per_death: float
    :param last_games: last_games
    :type last_games: List[BaseValorantGame]
    :param maps: maps
    :type maps: List[ValorantTeamMapStats]
    :param matches_draw: matches_draw
    :type matches_draw: int
    :param matches_lost: matches_lost
    :type matches_lost: int
    :param matches_played: matches_played
    :type matches_played: int
    :param matches_won: matches_won
    :type matches_won: int
    :param pistol_round_losses: Number of pistol rounds lost by the team
    :type pistol_round_losses: int
    :param pistol_round_total_played: Number of pistol rounds played by the team
    :type pistol_round_total_played: int
    :param pistol_round_wins: Number of pistol rounds won by the team
    :type pistol_round_wins: int
    :param planted_spikes: Number of spikes planted by a team member
    :type planted_spikes: int
    :param serie: A serie, an occurrence of a league event
    :type serie: Serie
    :param streaks: Streaks done by a team member (in a given round)
    :type streaks: ValorantTeamStreaks
    :param team: team
    :type team: BaseValorantTeam
    """

    def __init__(
        self,
        assists: int,
        clutch_wins: ValorantTeamClutchWins,
        deaths: int,
        defused_spikes: int,
        first_deaths: int,
        first_kills: int,
        games_draw: int,
        games_lost: int,
        games_played: int,
        games_won: int,
        headshot_percentage: float,
        kills: int,
        kills_per_death: float,
        last_games: List[BaseValorantGame],
        maps: List[ValorantTeamMapStats],
        matches_draw: int,
        matches_lost: int,
        matches_played: int,
        matches_won: int,
        pistol_round_losses: int,
        pistol_round_total_played: int,
        pistol_round_wins: int,
        planted_spikes: int,
        serie: Serie,
        streaks: ValorantTeamStreaks,
        team: BaseValorantTeam,
    ):
        """ValorantStatsForTeamBySerie

        :param assists: Number of team's assists
        :type assists: int
        :param clutch_wins: Rounds wins with a single team member alive
        :type clutch_wins: ValorantTeamClutchWins
        :param deaths: Number of team's death
        :type deaths: int
        :param defused_spikes: Number of spikes defused by a team member
        :type defused_spikes: int
        :param first_deaths: Number of rounds where a team member died first
        :type first_deaths: int
        :param first_kills: Number of rounds where a team member did the first kill
        :type first_kills: int
        :param games_draw: Number of games
        :type games_draw: int
        :param games_lost: Number of games
        :type games_lost: int
        :param games_played: Number of games
        :type games_played: int
        :param games_won: Number of games
        :type games_won: int
        :param headshot_percentage: Percentage of headshots within the player's shots
        :type headshot_percentage: float
        :param kills: Number of team's kills
        :type kills: int
        :param kills_per_death: Ratio of team's kills per deaths
        :type kills_per_death: float
        :param last_games: last_games
        :type last_games: List[BaseValorantGame]
        :param maps: maps
        :type maps: List[ValorantTeamMapStats]
        :param matches_draw: matches_draw
        :type matches_draw: int
        :param matches_lost: matches_lost
        :type matches_lost: int
        :param matches_played: matches_played
        :type matches_played: int
        :param matches_won: matches_won
        :type matches_won: int
        :param pistol_round_losses: Number of pistol rounds lost by the team
        :type pistol_round_losses: int
        :param pistol_round_total_played: Number of pistol rounds played by the team
        :type pistol_round_total_played: int
        :param pistol_round_wins: Number of pistol rounds won by the team
        :type pistol_round_wins: int
        :param planted_spikes: Number of spikes planted by a team member
        :type planted_spikes: int
        :param serie: A serie, an occurrence of a league event
        :type serie: Serie
        :param streaks: Streaks done by a team member (in a given round)
        :type streaks: ValorantTeamStreaks
        :param team: team
        :type team: BaseValorantTeam
        """
        self.assists = self._define_number("assists", assists, nullable=True, ge=0)
        self.clutch_wins = self._define_object(clutch_wins, ValorantTeamClutchWins)
        self.deaths = self._define_number("deaths", deaths, nullable=True, ge=0)
        self.defused_spikes = self._define_number(
            "defused_spikes", defused_spikes, nullable=True, ge=0
        )
        self.first_deaths = self._define_number(
            "first_deaths", first_deaths, nullable=True, ge=0
        )
        self.first_kills = self._define_number(
            "first_kills", first_kills, nullable=True, ge=0
        )
        self.games_draw = self._define_number("games_draw", games_draw, ge=0)
        self.games_lost = self._define_number("games_lost", games_lost, ge=0)
        self.games_played = self._define_number("games_played", games_played, ge=0)
        self.games_won = self._define_number("games_won", games_won, ge=0)
        self.headshot_percentage = self._define_number(
            "headshot_percentage", headshot_percentage, nullable=True, ge=0, le=100
        )
        self.kills = self._define_number("kills", kills, nullable=True, ge=0)
        self.kills_per_death = self._define_number(
            "kills_per_death", kills_per_death, nullable=True, ge=0
        )
        self.last_games = self._define_list(last_games, BaseValorantGame)
        self.maps = self._define_list(maps, ValorantTeamMapStats)
        self.matches_draw = self._define_number("matches_draw", matches_draw, ge=0)
        self.matches_lost = self._define_number("matches_lost", matches_lost, ge=0)
        self.matches_played = self._define_number(
            "matches_played", matches_played, ge=0
        )
        self.matches_won = self._define_number("matches_won", matches_won, ge=0)
        self.pistol_round_losses = self._define_number(
            "pistol_round_losses", pistol_round_losses, ge=0
        )
        self.pistol_round_total_played = self._define_number(
            "pistol_round_total_played", pistol_round_total_played, ge=0
        )
        self.pistol_round_wins = self._define_number(
            "pistol_round_wins", pistol_round_wins, ge=0
        )
        self.planted_spikes = self._define_number(
            "planted_spikes", planted_spikes, nullable=True, ge=0
        )
        self.serie = self._define_object(serie, Serie)
        self.streaks = self._define_object(streaks, ValorantTeamStreaks)
        self.team = self._define_object(team, BaseValorantTeam)