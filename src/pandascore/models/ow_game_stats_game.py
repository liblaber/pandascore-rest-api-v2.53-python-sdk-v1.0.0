from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .gameless_full_game_match import GamelessFullGameMatch
from .ow_game_round import OwGameRound
from .game_status import GameStatus
from .game_winner import GameWinner
from .ow_map_game_mode import OwMapGameMode


@JsonMap({"id_": "id"})
class OwGameStatsGameMap(BaseModel):
    """OwGameStatsGameMap

    :param game_mode: game_mode
    :type game_mode: OwMapGameMode
    :param id_: id_
    :type id_: int
    :param image_url: image_url
    :type image_url: str
    :param name: name
    :type name: str
    :param slug: slug
    :type slug: str
    :param thumbnail_url: thumbnail_url
    :type thumbnail_url: str
    """

    def __init__(
        self,
        game_mode: OwMapGameMode,
        id_: int,
        image_url: str,
        name: str,
        slug: str,
        thumbnail_url: str,
    ):
        self.game_mode = self._enum_matching(
            game_mode, OwMapGameMode.list(), "game_mode"
        )
        self.id_ = id_
        self.image_url = image_url
        self.name = name
        self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
        self.thumbnail_url = thumbnail_url


class OwGameStatsGameWinnerType(Enum):
    """An enumeration representing different categories.

    :cvar PLAYER: "Player"
    :vartype PLAYER: str
    :cvar TEAM: "Team"
    :vartype TEAM: str
    """

    PLAYER = "Player"
    TEAM = "Team"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, OwGameStatsGameWinnerType._member_map_.values())
        )


@JsonMap({"id_": "id"})
class OwGameStatsGame(BaseModel):
    """A game

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
    :param map: map
    :type map: OwGameStatsGameMap
    :param match: A match
    :type match: GamelessFullGameMatch
    :param match_id: match_id
    :type match_id: int
    :param position: Game position in the match. Starts at 1
    :type position: int
    :param rounds: rounds
    :type rounds: List[OwGameRound]
    :param status: The game status
    :type status: GameStatus
    :param winner: winner
    :type winner: GameWinner
    :param winner_type: winner_type
    :type winner_type: OwGameStatsGameWinnerType
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
        map: OwGameStatsGameMap,
        match: GamelessFullGameMatch,
        match_id: int,
        position: int,
        rounds: List[OwGameRound],
        status: GameStatus,
        winner: GameWinner,
        winner_type: OwGameStatsGameWinnerType,
    ):
        self.begin_at = begin_at
        self.complete = complete
        self.detailed_stats = detailed_stats
        self.end_at = end_at
        self.finished = finished
        self.forfeit = forfeit
        self.id_ = id_
        self.length = length
        self.map = self._define_object(map, OwGameStatsGameMap)
        self.match = self._define_object(match, GamelessFullGameMatch)
        self.match_id = match_id
        self.position = position
        self.rounds = self._define_list(rounds, OwGameRound)
        self.status = self._enum_matching(status, GameStatus.list(), "status")
        self.winner = self._define_object(winner, GameWinner)
        self.winner_type = self._enum_matching(
            winner_type, OwGameStatsGameWinnerType.list(), "winner_type"
        )
