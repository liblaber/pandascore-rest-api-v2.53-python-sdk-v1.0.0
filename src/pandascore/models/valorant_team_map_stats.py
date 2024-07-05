from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .valorant_agent_stats import ValorantAgentStats
from .valorant_team_clutch_wins import ValorantTeamClutchWins
from .valorant_team_streaks import ValorantTeamStreaks


@JsonMap({"id_": "id"})
class ValorantTeamMapStats(BaseModel):
    """ValorantTeamMapStats

    :param agents: Agents picks, wins, and losses stats for this map
    :type agents: List[ValorantAgentStats]
    :param assists: Number of team's assists
    :type assists: int
    :param average_rounds: Average number of rounds played by the team on this map
    :type average_rounds: float
    :param clutch_wins: Rounds wins with a single team member alive
    :type clutch_wins: ValorantTeamClutchWins
    :param deaths: Number of team's death
    :type deaths: int
    :param defused_spikes: Number of spikes defused by a team member
    :type defused_spikes: int
    :param draws: Number of team draws on this map
    :type draws: int
    :param first_deaths: Number of rounds where a team member died first
    :type first_deaths: int
    :param first_kills: Number of rounds where a team member did the first kill
    :type first_kills: int
    :param headshot_percentage: Percentage of headshots within the player's shots
    :type headshot_percentage: float
    :param id_: ID of the map
    :type id_: int
    :param image_url: URL to an image of the map
    :type image_url: str
    :param kills: Number of team's kills
    :type kills: int
    :param kills_per_death: Ratio of team's kills per deaths
    :type kills_per_death: float
    :param losses: Number of team losses on this map
    :type losses: int
    :param name: Name of the map
    :type name: str
    :param pistol_round_losses: Number of pistol rounds lost by the team
    :type pistol_round_losses: int
    :param pistol_round_total_played: Number of pistol rounds played by the team
    :type pistol_round_total_played: int
    :param pistol_round_wins: Number of pistol rounds won by the team
    :type pistol_round_wins: int
    :param planted_spikes: Number of spikes planted by a team member
    :type planted_spikes: int
    :param slug: Human-readable identifier of the map
    :type slug: str
    :param streaks: Streaks done by a team member (in a given round)
    :type streaks: ValorantTeamStreaks
    :param total_played: Number of times the team played on this map
    :type total_played: int
    :param videogame_versions: Array of of video game versions (ie. patches) for this resource
    :type videogame_versions: List[str]
    :param wins: Number of team wins on this map
    :type wins: int
    """

    def __init__(
        self,
        agents: List[ValorantAgentStats],
        assists: int,
        average_rounds: float,
        clutch_wins: ValorantTeamClutchWins,
        deaths: int,
        defused_spikes: int,
        draws: int,
        first_deaths: int,
        first_kills: int,
        headshot_percentage: float,
        id_: int,
        image_url: str,
        kills: int,
        kills_per_death: float,
        losses: int,
        name: str,
        pistol_round_losses: int,
        pistol_round_total_played: int,
        pistol_round_wins: int,
        planted_spikes: int,
        slug: str,
        streaks: ValorantTeamStreaks,
        total_played: int,
        videogame_versions: List[str],
        wins: int,
    ):
        self.agents = self._define_list(agents, ValorantAgentStats)
        self.assists = assists
        self.average_rounds = average_rounds
        self.clutch_wins = self._define_object(clutch_wins, ValorantTeamClutchWins)
        self.deaths = deaths
        self.defused_spikes = defused_spikes
        self.draws = draws
        self.first_deaths = first_deaths
        self.first_kills = first_kills
        self.headshot_percentage = headshot_percentage
        self.id_ = id_
        self.image_url = image_url
        self.kills = kills
        self.kills_per_death = kills_per_death
        self.losses = losses
        self.name = name
        self.pistol_round_losses = pistol_round_losses
        self.pistol_round_total_played = pistol_round_total_played
        self.pistol_round_wins = pistol_round_wins
        self.planted_spikes = planted_spikes
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
        self.streaks = self._define_object(streaks, ValorantTeamStreaks)
        self.total_played = total_played
        self.videogame_versions = videogame_versions
        self.wins = wins
