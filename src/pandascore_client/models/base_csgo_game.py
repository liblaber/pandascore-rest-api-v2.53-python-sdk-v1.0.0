# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .csgo_game_player import CsgoGamePlayer
from .csgo_round import CsgoRound
from .csgo_rounds_score import CsgoRoundsScore
from .game_status import GameStatus
from .base_team import BaseTeam
from .game_winner import GameWinner


@JsonMap({"id_": "id"})
class BaseCsgoGameMap(BaseModel):
    """BaseCsgoGameMap

    :param id_: The ID of the map.
    :type id_: int
    :param image_url: A URL to the image of the map.
    :type image_url: str
    :param name: The name of the map.
    :type name: str
    :param slug: Human-readable identifier of the map
    :type slug: str
    """

    def __init__(self, id_: int, image_url: str, name: str, slug: str):
        """BaseCsgoGameMap

        :param id_: The ID of the map.
        :type id_: int
        :param image_url: A URL to the image of the map.
        :type image_url: str
        :param name: The name of the map.
        :type name: str
        :param slug: Human-readable identifier of the map
        :type slug: str
        """
        self.id_ = self._define_number("id_", id_, ge=1)
        self.image_url = self._define_str("image_url", image_url, nullable=True)
        self.name = name
        self.slug = self._define_str(
            "slug", slug, pattern="^[a-z0-9_-]+$", min_length=1
        )


class BaseCsgoGameWinnerType(Enum):
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
            map(lambda x: x.value, BaseCsgoGameWinnerType._member_map_.values())
        )


@JsonMap({"id_": "id"})
class BaseCsgoGame(BaseModel):
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
    :param id_: Counter-Strike game ID
    :type id_: int
    :param length: Duration of the game in seconds. <br/>`null` when the game status is not `finished`
    :type length: int
    :param map: map
    :type map: BaseCsgoGameMap
    :param match_id: match_id
    :type match_id: int
    :param players: players
    :type players: List[CsgoGamePlayer]
    :param position: Game position in the match. Starts at 1
    :type position: int
    :param rounds: rounds
    :type rounds: List[CsgoRound]
    :param rounds_score: rounds_score
    :type rounds_score: List[CsgoRoundsScore]
    :param status: The game status
    :type status: GameStatus
    :param teams: teams
    :type teams: List[BaseTeam]
    :param winner: winner
    :type winner: GameWinner
    :param winner_type: winner_type
    :type winner_type: BaseCsgoGameWinnerType
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
        map: BaseCsgoGameMap,
        match_id: int,
        players: List[CsgoGamePlayer],
        position: int,
        rounds: List[CsgoRound],
        rounds_score: List[CsgoRoundsScore],
        status: GameStatus,
        teams: List[BaseTeam],
        winner: GameWinner,
        winner_type: BaseCsgoGameWinnerType,
    ):
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
        :param id_: Counter-Strike game ID
        :type id_: int
        :param length: Duration of the game in seconds. <br/>`null` when the game status is not `finished`
        :type length: int
        :param map: map
        :type map: BaseCsgoGameMap
        :param match_id: match_id
        :type match_id: int
        :param players: players
        :type players: List[CsgoGamePlayer]
        :param position: Game position in the match. Starts at 1
        :type position: int
        :param rounds: rounds
        :type rounds: List[CsgoRound]
        :param rounds_score: rounds_score
        :type rounds_score: List[CsgoRoundsScore]
        :param status: The game status
        :type status: GameStatus
        :param teams: teams
        :type teams: List[BaseTeam]
        :param winner: winner
        :type winner: GameWinner
        :param winner_type: winner_type
        :type winner_type: BaseCsgoGameWinnerType
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
        self.map = self._define_object(map, BaseCsgoGameMap)
        self.match_id = self._define_number("match_id", match_id, ge=1)
        self.players = self._define_list(players, CsgoGamePlayer)
        self.position = self._define_number("position", position, ge=1)
        self.rounds = self._define_list(rounds, CsgoRound)
        self.rounds_score = self._define_list(rounds_score, CsgoRoundsScore)
        self.status = self._enum_matching(status, GameStatus.list(), "status")
        self.teams = self._define_list(teams, BaseTeam)
        self.winner = self._define_object(winner, GameWinner)
        self.winner_type = self._enum_matching(
            winner_type, BaseCsgoGameWinnerType.list(), "winner_type"
        )