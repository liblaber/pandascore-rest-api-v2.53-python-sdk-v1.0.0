from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .full_game_match import FullGameMatch
from .lo_l_game_player import LoLGamePlayer
from .game_status import GameStatus
from .lo_l_game_team import LoLGameTeam
from .game_winner import GameWinner


class LoLGameWinnerType(Enum):
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
        return list(map(lambda x: x.value, LoLGameWinnerType._member_map_.values()))


@JsonMap({"id_": "id"})
class LoLGame(BaseModel):
    """LoLGame

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
    :param match: A match
    :type match: FullGameMatch
    :param match_id: match_id
    :type match_id: int
    :param players: players
    :type players: List[LoLGamePlayer]
    :param position: Game position in the match. Starts at 1
    :type position: int
    :param status: The game status
    :type status: GameStatus
    :param teams: teams
    :type teams: List[LoLGameTeam]
    :param winner: winner
    :type winner: GameWinner
    :param winner_type: winner_type
    :type winner_type: LoLGameWinnerType
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
        match: FullGameMatch,
        match_id: int,
        players: List[LoLGamePlayer],
        position: int,
        status: GameStatus,
        teams: List[LoLGameTeam],
        winner: GameWinner,
        winner_type: LoLGameWinnerType,
    ):
        self.begin_at = begin_at
        self.complete = complete
        self.detailed_stats = detailed_stats
        self.end_at = end_at
        self.finished = finished
        self.forfeit = forfeit
        self.id_ = id_
        self.length = length
        self.match = self._define_object(match, FullGameMatch)
        self.match_id = match_id
        self.players = self._define_list(players, LoLGamePlayer)
        self.position = position
        self.status = self._enum_matching(status, GameStatus.list(), "status")
        self.teams = self._define_list(teams, LoLGameTeam)
        self.winner = self._define_object(winner, GameWinner)
        self.winner_type = self._enum_matching(
            winner_type, LoLGameWinnerType.list(), "winner_type"
        )
