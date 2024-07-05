from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class LoLTeamStatsTotals(BaseModel):
    """LoLTeamStatsTotals

    :param assists: assists
    :type assists: int
    :param baron_kills: baron_kills
    :type baron_kills: int
    :param blue_games_lost: Number of games
    :type blue_games_lost: int
    :param blue_games_won: Number of games
    :type blue_games_won: int
    :param chemtech_drake_kills: chemtech_drake_kills
    :type chemtech_drake_kills: int
    :param deaths: deaths
    :type deaths: int
    :param dragon_kills: dragon_kills
    :type dragon_kills: int
    :param elder_drake_kills: elder_drake_kills
    :type elder_drake_kills: int
    :param games_lost: Number of games
    :type games_lost: int
    :param games_played: Number of games
    :type games_played: int
    :param games_won: Number of games
    :type games_won: int
    :param herald_kill: herald_kill
    :type herald_kill: int
    :param hextech_drake_kills: hextech_drake_kills
    :type hextech_drake_kills: int
    :param infernal_drake_kills: infernal_drake_kills
    :type infernal_drake_kills: int
    :param inhibitor_kills: inhibitor_kills
    :type inhibitor_kills: int
    :param kills: kills
    :type kills: int
    :param matches_lost: matches_lost
    :type matches_lost: int
    :param matches_played: matches_played
    :type matches_played: int
    :param matches_won: matches_won
    :type matches_won: int
    :param mountain_drake_kills: mountain_drake_kills
    :type mountain_drake_kills: int
    :param ocean_drake_kills: ocean_drake_kills
    :type ocean_drake_kills: int
    :param red_games_lost: Number of games
    :type red_games_lost: int
    :param red_games_won: Number of games
    :type red_games_won: int
    :param tower_kills: tower_kills
    :type tower_kills: int
    :param voidgrub_kills: The number of voidgrubs killed by a team.
    :type voidgrub_kills: int
    :param wards_placed: wards_placed
    :type wards_placed: int
    """

    def __init__(
        self,
        assists: int,
        baron_kills: int,
        blue_games_lost: int,
        blue_games_won: int,
        chemtech_drake_kills: int,
        deaths: int,
        dragon_kills: int,
        elder_drake_kills: int,
        games_lost: int,
        games_played: int,
        games_won: int,
        herald_kill: int,
        hextech_drake_kills: int,
        infernal_drake_kills: int,
        inhibitor_kills: int,
        kills: int,
        matches_lost: int,
        matches_played: int,
        matches_won: int,
        mountain_drake_kills: int,
        ocean_drake_kills: int,
        red_games_lost: int,
        red_games_won: int,
        tower_kills: int,
        voidgrub_kills: int,
        wards_placed: int,
    ):
        self.assists = assists
        self.baron_kills = baron_kills
        self.blue_games_lost = blue_games_lost
        self.blue_games_won = blue_games_won
        self.chemtech_drake_kills = chemtech_drake_kills
        self.deaths = deaths
        self.dragon_kills = dragon_kills
        self.elder_drake_kills = elder_drake_kills
        self.games_lost = games_lost
        self.games_played = games_played
        self.games_won = games_won
        self.herald_kill = herald_kill
        self.hextech_drake_kills = hextech_drake_kills
        self.infernal_drake_kills = infernal_drake_kills
        self.inhibitor_kills = inhibitor_kills
        self.kills = kills
        self.matches_lost = matches_lost
        self.matches_played = matches_played
        self.matches_won = matches_won
        self.mountain_drake_kills = mountain_drake_kills
        self.ocean_drake_kills = ocean_drake_kills
        self.red_games_lost = red_games_lost
        self.red_games_won = red_games_won
        self.tower_kills = tower_kills
        self.voidgrub_kills = voidgrub_kills
        self.wards_placed = wards_placed
