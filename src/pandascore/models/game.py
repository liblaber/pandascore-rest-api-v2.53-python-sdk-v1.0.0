from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel
from .game_id import GameId, GameIdGuard
from .game_status import GameStatus
from .game_winner import GameWinner


class GameWinnerType1(Enum):
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
        return list(map(lambda x: x.value, GameWinnerType1._member_map_.values()))


@JsonMap({"id_": "id"})
class Game(BaseModel):
    """Game

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
    :param id_: ID of the game. <br/>IDs are video game-specific, ie. a Valorant game and an Overwatch game can have the same game ID.
    :type id_: GameId
    :param length: Duration of the game in seconds. <br/>`null` when the game status is not `finished`
    :type length: int
    :param match_id: match_id
    :type match_id: int
    :param position: Game position in the match. Starts at 1
    :type position: int
    :param status: The game status
    :type status: GameStatus
    :param winner: winner
    :type winner: GameWinner
    :param winner_type: winner_type
    :type winner_type: GameWinnerType1
    """

    def __init__(
        self,
        begin_at: str,
        complete: bool,
        detailed_stats: bool,
        end_at: str,
        finished: bool,
        forfeit: bool,
        id_: GameId,
        length: int,
        match_id: int,
        position: int,
        status: GameStatus,
        winner: GameWinner,
        winner_type: GameWinnerType1,
    ):
        self.begin_at = begin_at
        self.complete = complete
        self.detailed_stats = detailed_stats
        self.end_at = end_at
        self.finished = finished
        self.forfeit = forfeit
        self.id_ = GameIdGuard.return_one_of(id_)
        self.length = length
        self.match_id = match_id
        self.position = position
        self.status = self._enum_matching(status, GameStatus.list(), "status")
        self.winner = self._define_object(winner, GameWinner)
        self.winner_type = self._enum_matching(
            winner_type, GameWinnerType1.list(), "winner_type"
        )
