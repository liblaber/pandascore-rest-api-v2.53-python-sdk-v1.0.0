from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .valorant_short_agent import ValorantShortAgent
from .valorant_player_clutch_wins import ValorantPlayerClutchWins
from .valorant_player_streaks import ValorantPlayerStreaks


@JsonMap({"id_": "id"})
class ValorantGamePlayer(BaseModel):
    """ValorantGamePlayer

    :param active: Whether player is active
    :type active: bool
    :param age: Age of the player, `null` if unknown. When `birthday` is `null`, `age` is an approxiamation. Read more about [players' age](/docs/about-players-age) <br/>**Note**: This field is only present for users running the Historical plan or above.
    :type age: float
    :param agent: agent
    :type agent: ValorantShortAgent
    :param assists: Number of player's assists
    :type assists: int
    :param average_combat_score: Average combat score (ACS) of the player
    :type average_combat_score: int
    :param average_damage_per_round: Average damage per round (ADR) of the player
    :type average_damage_per_round: float
    :param average_economy_score: Average economy score (ECS) of the player
    :type average_economy_score: float
    :param birthday: Birth day of the player, `YYYY-MM-DD` format. `null` if unknown. <br/>**Note**: This field is only present for users running the Historical plan or above.
    :type birthday: str
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
    :param first_name: First name of the player. `null` if unknown
    :type first_name: str
    :param headshot_percentage: Percentage of headshots within the player's shots
    :type headshot_percentage: float
    :param id_: ID of the player
    :type id_: int
    :param image_url: URL to the photo of the player. `null` if not available.
    :type image_url: str
    :param kill_death_difference: Difference between the player's number of kills and number of death (kills - deaths)
    :type kill_death_difference: float
    :param kills: Number of player's kills
    :type kills: int
    :param kills_per_death: Ratio of player's kills per deaths (kills / deaths)
    :type kills_per_death: float
    :param last_name: Last name of the player. `null` if unknown
    :type last_name: str
    :param modified_at: modified_at
    :type modified_at: str
    :param name: Professional name of the player
    :type name: str
    :param nationality: Country code matching the nationality of the player according to the ISO 3166-1 standard (Alpha-2 code). <br/>In addition to the standard, the `XK` code is used for Kosovo. <br/>`null` if unknown
    :type nationality: str
    :param planted_spikes: Number of spikes planted by the player
    :type planted_spikes: int
    :param role: Role/position of the player. Field value varies depending on the video game.`null` if unknown. <br/>**Note**: role is only available for DotA 2, League of Legends, and Overwatch players. <br/>`null` for other video games.
    :type role: str
    :param slug: Unique, human-readable identifier for the player. <br/>`id` and `slug` can be used interchangeably throughout the API.
    :type slug: str
    :param streaks: Streaks done by the player (in a given round)
    :type streaks: ValorantPlayerStreaks
    """

    def __init__(
        self,
        active: bool,
        age: float,
        agent: ValorantShortAgent,
        assists: int,
        average_combat_score: int,
        average_damage_per_round: float,
        average_economy_score: float,
        birthday: str,
        clutch_wins: ValorantPlayerClutchWins,
        deaths: int,
        defused_spikes: int,
        first_deaths: int,
        first_kills: int,
        first_name: str,
        headshot_percentage: float,
        id_: int,
        image_url: str,
        kill_death_difference: float,
        kills: int,
        kills_per_death: float,
        last_name: str,
        modified_at: str,
        name: str,
        nationality: str,
        planted_spikes: int,
        role: str,
        slug: str,
        streaks: ValorantPlayerStreaks,
    ):
        self.active = active
        self.age = age
        self.agent = self._define_object(agent, ValorantShortAgent)
        self.assists = assists
        self.average_combat_score = average_combat_score
        self.average_damage_per_round = average_damage_per_round
        self.average_economy_score = average_economy_score
        self.birthday = birthday
        self.clutch_wins = self._define_object(clutch_wins, ValorantPlayerClutchWins)
        self.deaths = deaths
        self.defused_spikes = defused_spikes
        self.first_deaths = first_deaths
        self.first_kills = first_kills
        self.first_name = first_name
        self.headshot_percentage = headshot_percentage
        self.id_ = id_
        self.image_url = image_url
        self.kill_death_difference = kill_death_difference
        self.kills = kills
        self.kills_per_death = kills_per_death
        self.last_name = last_name
        self.modified_at = modified_at
        self.name = name
        self.nationality = nationality
        self.planted_spikes = planted_spikes
        self.role = role
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
        self.streaks = self._define_object(streaks, ValorantPlayerStreaks)
