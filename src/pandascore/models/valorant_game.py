from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .full_game_match import FullGameMatch
from .valorant_game_round import ValorantGameRound
from .game_status import GameStatus
from .valorant_game_team import ValorantGameTeam
from .game_winner import GameWinner


@JsonMap({"id_": "id"})
class ValorantGameMap(BaseModel):
    """An object that represents a Valorant map

    :param id_: ID of the map
    :type id_: int
    :param image_url: URL to an image of the map
    :type image_url: str
    :param name: Name of the map
    :type name: str
    :param slug: Human-readable identifier of the map
    :type slug: str
    :param videogame_versions: Array of of video game versions (ie. patches) for this resource
    :type videogame_versions: List[str]
    """

    def __init__(
        self,
        id_: int,
        image_url: str,
        name: str,
        slug: str,
        videogame_versions: List[str],
    ):
        self.id_ = id_
        self.image_url = image_url
        self.name = name
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
        self.videogame_versions = videogame_versions


@JsonMap({"id_": "id"})
class ValorantGame(BaseModel):
    """ValorantGame

    :param begin_at: The game begin time, UTC. <br/>`null` when the game status is `not_started`
    :type begin_at: str
    :param complete: Whether When `true`, the game statistics are complete and will not be updated again
    :type complete: bool
    :param detailed_stats: Whether historical data is available for the game
    :type detailed_stats: bool
    :param end_at: The game end time, UTC. <br/>`null` when the game status is not `finished`
    :type end_at: str
    :param finished: Whether the game is finished
    :type finished: bool
    :param forfeit: Whether the game has been forfeited
    :type forfeit: bool
    :param id_: id_
    :type id_: int
    :param length: Duration of the game in seconds. <br/>`null` when the game status is not `finished`
    :type length: int
    :param map: An object that represents a Valorant map
    :type map: ValorantGameMap
    :param match: A match
    :type match: FullGameMatch
    :param position: Game position in the match. Starts at 1
    :type position: int
    :param rounds: Summary of rounds
    :type rounds: List[ValorantGameRound]
    :param status: The game status
    :type status: GameStatus
    :param teams: teams
    :type teams: List[ValorantGameTeam]
    :param winner: winner
    :type winner: GameWinner
    """

    def __init__(
        self,
        begin_at: str,
        complete: bool,
        detailed_stats: bool,
        end_at: str,
        finished: bool,
        forfeit: bool,
        id_: int,
        length: int,
        map: ValorantGameMap,
        match: FullGameMatch,
        position: int,
        rounds: List[ValorantGameRound],
        status: GameStatus,
        teams: List[ValorantGameTeam],
        winner: GameWinner,
    ):
        self.begin_at = begin_at
        self.complete = complete
        self.detailed_stats = detailed_stats
        self.end_at = end_at
        self.finished = finished
        self.forfeit = forfeit
        self.id_ = id_
        self.length = length
        self.map = self._define_object(map, ValorantGameMap)
        self.match = self._define_object(match, FullGameMatch)
        self.position = position
        self.rounds = self._define_list(rounds, ValorantGameRound)
        self.status = self._enum_matching(status, GameStatus.list(), "status")
        self.teams = self._define_list(teams, ValorantGameTeam)
        self.winner = self._define_object(winner, GameWinner)
