# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .lo_l_match_game_player import LoLMatchGamePlayer
from .game_status import GameStatus
from .game_winner import GameWinner


class LoLMatchGameWinnerType(Enum):
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
            map(lambda x: x.value, LoLMatchGameWinnerType._member_map_.values())
        )


@JsonMap({"id_": "id"})
class LoLMatchGame(BaseModel):
    """LoLMatchGame

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
    :param id_: LoL game ID
    :type id_: int
    :param length: Duration of the game in seconds. <br/>`null` when the game status is not `finished`
    :type length: int
    :param match_id: match_id
    :type match_id: int
    :param players: players
    :type players: List[LoLMatchGamePlayer]
    :param position: Game position in the match. Starts at 1
    :type position: int
    :param status: The game status
    :type status: GameStatus
    :param winner: winner
    :type winner: GameWinner
    :param winner_type: winner_type
    :type winner_type: LoLMatchGameWinnerType
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
        match_id: int,
        players: List[LoLMatchGamePlayer],
        position: int,
        status: GameStatus,
        winner: GameWinner,
        winner_type: LoLMatchGameWinnerType,
    ):
        """LoLMatchGame

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
        :param id_: LoL game ID
        :type id_: int
        :param length: Duration of the game in seconds. <br/>`null` when the game status is not `finished`
        :type length: int
        :param match_id: match_id
        :type match_id: int
        :param players: players
        :type players: List[LoLMatchGamePlayer]
        :param position: Game position in the match. Starts at 1
        :type position: int
        :param status: The game status
        :type status: GameStatus
        :param winner: winner
        :type winner: GameWinner
        :param winner_type: winner_type
        :type winner_type: LoLMatchGameWinnerType
        """
        self.begin_at = self._define_str(
            "begin_at", begin_at, nullable=True, min_length=1
        )
        self.complete = complete
        self.detailed_stats = detailed_stats
        self.end_at = self._define_str("end_at", end_at, nullable=True, min_length=1)
        self.finished = finished
        self.forfeit = forfeit
        self.id_ = self._define_number("id_", id_, ge=1)
        self.length = self._define_number("length", length, nullable=True, ge=0)
        self.match_id = self._define_number("match_id", match_id, ge=1)
        self.players = self._define_list(players, LoLMatchGamePlayer)
        self.position = self._define_number("position", position, ge=1)
        self.status = self._enum_matching(status, GameStatus.list(), "status")
        self.winner = self._define_object(winner, GameWinner)
        self.winner_type = self._enum_matching(
            winner_type, LoLMatchGameWinnerType.list(), "winner_type"
        )