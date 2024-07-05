from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .dota2_full_game_player import Dota2FullGamePlayer
from .game_status import GameStatus
from .dota2_game_team import Dota2GameTeam
from .game_winner import GameWinner


class BaseDota2GameWinnerType(Enum):
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
            map(lambda x: x.value, BaseDota2GameWinnerType._member_map_.values())
        )


@JsonMap({"id_": "id"})
class BaseDota2Game(BaseModel):
    """BaseDota2Game

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
    :param first_blood: first_blood
    :type first_blood: int
    :param forfeit: Whether the game has been forfeited
    :type forfeit: bool
    :param id_: id_
    :type id_: int
    :param length: Duration of the game in seconds. <br/>`null` when the game status is not `finished`
    :type length: int
    :param match_id: match_id
    :type match_id: int
    :param players: players
    :type players: List[Dota2FullGamePlayer]
    :param position: Game position in the match. Starts at 1
    :type position: int
    :param status: The game status
    :type status: GameStatus
    :param teams: teams
    :type teams: List[Dota2GameTeam]
    :param winner: winner
    :type winner: GameWinner
    :param winner_type: winner_type
    :type winner_type: BaseDota2GameWinnerType
    """

    def __init__(
        self,
        begin_at: str,
        complete: bool,
        detailed_stats: bool,
        end_at: str,
        finished: bool,
        first_blood: int,
        forfeit: bool,
        id_: int,
        length: int,
        match_id: int,
        players: List[Dota2FullGamePlayer],
        position: int,
        status: GameStatus,
        teams: List[Dota2GameTeam],
        winner: GameWinner,
        winner_type: BaseDota2GameWinnerType,
    ):
        self.begin_at = begin_at
        self.complete = complete
        self.detailed_stats = detailed_stats
        self.end_at = end_at
        self.finished = finished
        self.first_blood = first_blood
        self.forfeit = forfeit
        self.id_ = id_
        self.length = length
        self.match_id = match_id
        self.players = self._define_list(players, Dota2FullGamePlayer)
        self.position = position
        self.status = self._enum_matching(status, GameStatus.list(), "status")
        self.teams = self._define_list(teams, Dota2GameTeam)
        self.winner = self._define_object(winner, GameWinner)
        self.winner_type = self._enum_matching(
            winner_type, BaseDota2GameWinnerType.list(), "winner_type"
        )
