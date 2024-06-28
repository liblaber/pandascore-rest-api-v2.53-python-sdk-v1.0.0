# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import Union
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel
from .match_type import MatchType
from .match_status import MatchStatus
from .videogame_id_or_slug import VideogameIdOrSlug, VideogameIdOrSlugGuard
from .videogame_id import VideogameId
from .videogame_slug import VideogameSlug
from .opponent_id import OpponentId, OpponentIdGuard
from .match_winner_type import MatchWinnerType
from .team_id_or_slug import TeamIdOrSlug, TeamIdOrSlugGuard
from .player_id_or_slug import PlayerIdOrSlug, PlayerIdOrSlugGuard


class FilterOverMatchesOpponentIdGuard(OneOfBaseModel):
    class_list = {"int": int, "str": str, "int": int, "str": str}


FilterOverMatchesOpponentId = Union[int, str, int, str]


class FilterOverMatchesVideogameTitleGuard(OneOfBaseModel):
    class_list = {"int": int, "str": str}


FilterOverMatchesVideogameTitle = Union[int, str]


class FilterOverMatchesVideogameVersionGuard(OneOfBaseModel):
    class_list = {"str": str, "any": any, "any": any}


FilterOverMatchesVideogameVersion = Union[str, any, any]


@JsonMap({"id_": "id"})
class FilterOverMatches(BaseModel):
    """FilterOverMatches

    :param begin_at: begin_at, defaults to None
    :type begin_at: List[str], optional
    :param detailed_stats: Whether the match offers full stats, defaults to None
    :type detailed_stats: bool, optional
    :param draw: Whether result of the match is a draw, defaults to None
    :type draw: bool, optional
    :param end_at: end_at, defaults to None
    :type end_at: List[str], optional
    :param finished: finished, defaults to None
    :type finished: bool, optional
    :param forfeit: Whether match was forfeited, defaults to None
    :type forfeit: bool, optional
    :param future: `true` for future matches only, `false` for past matches only. <br/>Filtering is done on the `begin_at` value, so  matches with `running` status will not appear if `true`., defaults to None
    :type future: bool, optional
    :param id_: id_, defaults to None
    :type id_: List[int], optional
    :param league_id: league_id, defaults to None
    :type league_id: List[int], optional
    :param match_type: match_type, defaults to None
    :type match_type: List[MatchType], optional
    :param modified_at: modified_at, defaults to None
    :type modified_at: List[str], optional
    :param name: name, defaults to None
    :type name: List[str], optional
    :param not_started: not_started, defaults to None
    :type not_started: bool, optional
    :param number_of_games: number_of_games, defaults to None
    :type number_of_games: List[int], optional
    :param opponent_id: A Team or a Player (id or slug). You can use`filter[winner_type]=Team` or `filter[winner_type]=Player` to focus on teams or players., defaults to None
    :type opponent_id: List[FilterOverMatchesOpponentId], optional
    :param opponents_filled: Whether a match has opponents filled i.e. opponents are not TBD., defaults to None
    :type opponents_filled: bool, optional
    :param past: past, defaults to None
    :type past: bool, optional
    :param running: running, defaults to None
    :type running: bool, optional
    :param scheduled_at: scheduled_at, defaults to None
    :type scheduled_at: List[str], optional
    :param serie_id: serie_id, defaults to None
    :type serie_id: List[int], optional
    :param slug: slug, defaults to None
    :type slug: List[str], optional
    :param status: status, defaults to None
    :type status: List[MatchStatus], optional
    :param tournament_id: tournament_id, defaults to None
    :type tournament_id: List[int], optional
    :param unscheduled: unscheduled, defaults to None
    :type unscheduled: bool, optional
    :param videogame: videogame, defaults to None
    :type videogame: List[VideogameIdOrSlug], optional
    :param videogame_title: A videogame title id or slug. <br/>Only for `/csgo/*`, `/codmw/*`, `/fifa/*` and `/ow/*` endpoints <br/>, defaults to None
    :type videogame_title: List[FilterOverMatchesVideogameTitle], optional
    :param videogame_version: Filter by the names of videogame versions, all versions using `filter[videogame_version]=all`, or by the latest version using `filter[videogame_version]=latest` <br/>Only for `valorant/*` and `/lol/*` endpoints. <br/>, defaults to None
    :type videogame_version: List[FilterOverMatchesVideogameVersion], optional
    :param winner_id: winner_id, defaults to None
    :type winner_id: List[OpponentId], optional
    :param winner_type: winner_type, defaults to None
    :type winner_type: List[MatchWinnerType], optional
    """

    def __init__(
        self,
        begin_at: List[str] = None,
        detailed_stats: bool = None,
        draw: bool = None,
        end_at: List[str] = None,
        finished: bool = None,
        forfeit: bool = None,
        future: bool = None,
        id_: List[int] = None,
        league_id: List[int] = None,
        match_type: List[MatchType] = None,
        modified_at: List[str] = None,
        name: List[str] = None,
        not_started: bool = None,
        number_of_games: List[int] = None,
        opponent_id: List[FilterOverMatchesOpponentId] = None,
        opponents_filled: bool = None,
        past: bool = None,
        running: bool = None,
        scheduled_at: List[str] = None,
        serie_id: List[int] = None,
        slug: List[str] = None,
        status: List[MatchStatus] = None,
        tournament_id: List[int] = None,
        unscheduled: bool = None,
        videogame: List[VideogameIdOrSlug] = None,
        videogame_title: List[FilterOverMatchesVideogameTitle] = None,
        videogame_version: List[FilterOverMatchesVideogameVersion] = None,
        winner_id: List[OpponentId] = None,
        winner_type: List[MatchWinnerType] = None,
    ):
        if begin_at is not None:
            self.begin_at = begin_at
        if detailed_stats is not None:
            self.detailed_stats = detailed_stats
        if draw is not None:
            self.draw = draw
        if end_at is not None:
            self.end_at = end_at
        if finished is not None:
            self.finished = finished
        if forfeit is not None:
            self.forfeit = forfeit
        if future is not None:
            self.future = future
        if id_ is not None:
            self.id_ = id_
        if league_id is not None:
            self.league_id = league_id
        if match_type is not None:
            self.match_type = self._define_list(match_type, MatchType)
        if modified_at is not None:
            self.modified_at = modified_at
        if name is not None:
            self.name = name
        if not_started is not None:
            self.not_started = not_started
        if number_of_games is not None:
            self.number_of_games = number_of_games
        if opponent_id is not None:
            self.opponent_id = self._define_list(
                opponent_id, FilterOverMatchesOpponentId
            )
        if opponents_filled is not None:
            self.opponents_filled = opponents_filled
        if past is not None:
            self.past = past
        if running is not None:
            self.running = running
        if scheduled_at is not None:
            self.scheduled_at = scheduled_at
        if serie_id is not None:
            self.serie_id = serie_id
        if slug is not None:
            self.slug = slug
        if status is not None:
            self.status = self._define_list(status, MatchStatus)
        if tournament_id is not None:
            self.tournament_id = tournament_id
        if unscheduled is not None:
            self.unscheduled = unscheduled
        if videogame is not None:
            self.videogame = self._define_list(videogame, VideogameIdOrSlug)
        if videogame_title is not None:
            self.videogame_title = self._define_list(
                videogame_title, FilterOverMatchesVideogameTitle
            )
        if videogame_version is not None:
            self.videogame_version = self._define_list(
                videogame_version, FilterOverMatchesVideogameVersion
            )
        if winner_id is not None:
            self.winner_id = self._define_list(winner_id, OpponentId)
        if winner_type is not None:
            self.winner_type = self._define_list(winner_type, MatchWinnerType)
