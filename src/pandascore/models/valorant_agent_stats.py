from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .valorant_player_clutch_wins import ValorantPlayerClutchWins
from .valorant_player_streaks import ValorantPlayerStreaks


@JsonMap({"id_": "id"})
class ValorantAgentStats(BaseModel):
    """ValorantAgentStats

    :param assists: Number of player's assists
    :type assists: int
    :param clutch_wins: Round wins when the player was the last team member alive
    :type clutch_wins: ValorantPlayerClutchWins
    :param deaths: Number of player's death
    :type deaths: int
    :param defused_spikes: Number of spikes defused by the player
    :type defused_spikes: int
    :param first_deaths: Number of rounds where the player died first
    :type first_deaths: int
    :param first_kills: Number of rounds where the player did the first kill
    :type first_kills: int
    :param headshot_percentage: Percentage of headshots within the player's shots
    :type headshot_percentage: float
    :param id_: ID of the agent
    :type id_: int
    :param kills: Number of player's kills
    :type kills: int
    :param losses: Number of games lost with this agent
    :type losses: int
    :param name: Name of the agent
    :type name: str
    :param picks: Number of times the agent was picked
    :type picks: int
    :param planted_spikes: Number of spikes planted by the player
    :type planted_spikes: int
    :param portrait_url: URL to a portrait image of the agent
    :type portrait_url: str
    :param rounds_played: Number of rounds played
    :type rounds_played: int
    :param streaks: Streaks done by the player (in a given round)
    :type streaks: ValorantPlayerStreaks
    :param videogame_versions: Array of of video game versions (ie. patches) for this resource
    :type videogame_versions: List[str]
    :param wins: Number of games won with this agent
    :type wins: int
    """

    def __init__(
        self,
        assists: int,
        clutch_wins: ValorantPlayerClutchWins,
        deaths: int,
        defused_spikes: int,
        first_deaths: int,
        first_kills: int,
        headshot_percentage: float,
        id_: int,
        kills: int,
        losses: int,
        name: str,
        picks: int,
        planted_spikes: int,
        portrait_url: str,
        rounds_played: int,
        streaks: ValorantPlayerStreaks,
        videogame_versions: List[str],
        wins: int,
    ):
        self.assists = assists
        self.clutch_wins = self._define_object(clutch_wins, ValorantPlayerClutchWins)
        self.deaths = deaths
        self.defused_spikes = defused_spikes
        self.first_deaths = first_deaths
        self.first_kills = first_kills
        self.headshot_percentage = headshot_percentage
        self.id_ = id_
        self.kills = kills
        self.losses = losses
        self.name = name
        self.picks = picks
        self.planted_spikes = planted_spikes
        self.portrait_url = portrait_url
        self.rounds_played = rounds_played
        self.streaks = self._define_object(streaks, ValorantPlayerStreaks)
        self.videogame_versions = videogame_versions
        self.wins = wins
