from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.videogame_version_or_all import VideogameVersionOrAll
from ..models.utils.cast_models import cast_models
from ..models.tournament_id_or_slug import TournamentIdOrSlug
from ..models.team_id_or_slug import TeamIdOrSlug
from ..models.serie_id_or_slug import SerieIdOrSlug
from ..models.player_id_or_slug import PlayerIdOrSlug
from ..models.page import Page
from ..models.match_id_or_slug import MatchIdOrSlug
from ..models.lo_l_stats_for_team_by_tournament import LoLStatsForTeamByTournament
from ..models.lo_l_stats_for_team_by_serie import LoLStatsForTeamBySerie
from ..models.lo_l_stats_for_team import LoLStatsForTeam
from ..models.lo_l_stats_for_player_by_tournament import LoLStatsForPlayerByTournament
from ..models.lo_l_stats_for_player_by_serie import LoLStatsForPlayerBySerie
from ..models.lo_l_stats_for_player import LoLStatsForPlayer
from ..models.lo_l_stats_for_all_players_by_match import LoLStatsForAllPlayersByMatch
from ..models.get_lol_players_player_id_or_slug_stats_side import (
    GetLolPlayersPlayerIdOrSlugStatsSide,
)


class LoLStatsService(BaseService):

    @cast_models
    def get_lol_matches_match_id_or_slug_players_stats(
        self, match_id_or_slug: MatchIdOrSlug
    ) -> LoLStatsForAllPlayersByMatch:
        """Get detailed statistics of League-of-Legends players for the given match

        :param match_id_or_slug: A match ID or slug
        :type match_id_or_slug: MatchIdOrSlug
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of all Lol players by match
        :rtype: LoLStatsForAllPlayersByMatch
        """

        Validator(MatchIdOrSlug).validate(match_id_or_slug)

        serialized_request = (
            Serializer(
                f"{self.base_url}/lol/matches/{{match_id_or_slug}}/players/stats",
                self.get_default_headers(),
            )
            .add_path("match_id_or_slug", match_id_or_slug)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return LoLStatsForAllPlayersByMatch._unmap(response)

    @cast_models
    def get_lol_players_player_id_or_slug_stats(
        self,
        player_id_or_slug: PlayerIdOrSlug,
        games_count: int = None,
        side: GetLolPlayersPlayerIdOrSlugStatsSide = None,
        videogame_version: VideogameVersionOrAll = None,
        from_: str = None,
        to: str = None,
    ) -> LoLStatsForPlayer:
        """Get detailed statistics of a given League-of-Legends player

        :param player_id_or_slug: A player ID or slug
        :type player_id_or_slug: PlayerIdOrSlug
        :param games_count: The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/>, defaults to None
        :type games_count: int, optional
        :param side: side, defaults to None
        :type side: GetLolPlayersPlayerIdOrSlugStatsSide, optional
        :param videogame_version: videogame_version, defaults to None
        :type videogame_version: VideogameVersionOrAll, optional
        :param from_: Filter out 'from' date, defaults to None
        :type from_: str, optional
        :param to: Filter out 'to' date, defaults to None
        :type to: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a League-of-Legends player
        :rtype: LoLStatsForPlayer
        """

        Validator(PlayerIdOrSlug).validate(player_id_or_slug)
        Validator(int).is_optional().validate(games_count)
        Validator(GetLolPlayersPlayerIdOrSlugStatsSide).is_optional().validate(side)
        Validator(VideogameVersionOrAll).is_optional().validate(videogame_version)
        Validator(str).is_optional().validate(from_)
        Validator(str).is_optional().validate(to)

        serialized_request = (
            Serializer(
                f"{self.base_url}/lol/players/{{player_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("player_id_or_slug", player_id_or_slug)
            .add_query("games_count", games_count)
            .add_query("side", side)
            .add_query("videogame_version", videogame_version)
            .add_query("from", from_)
            .add_query("to", to)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return LoLStatsForPlayer._unmap(response)

    @cast_models
    def get_lol_series_serie_id_or_slug_players_player_id_or_slug_stats(
        self,
        serie_id_or_slug: SerieIdOrSlug,
        player_id_or_slug: PlayerIdOrSlug,
        games_count: int = None,
        side: GetLolPlayersPlayerIdOrSlugStatsSide = None,
        videogame_version: VideogameVersionOrAll = None,
    ) -> LoLStatsForPlayerBySerie:
        """Get detailed statistics of a given League-of-Legends player for the given serie

        :param serie_id_or_slug: A serie ID or slug
        :type serie_id_or_slug: SerieIdOrSlug
        :param player_id_or_slug: A player ID or slug
        :type player_id_or_slug: PlayerIdOrSlug
        :param games_count: The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/>, defaults to None
        :type games_count: int, optional
        :param side: side, defaults to None
        :type side: GetLolPlayersPlayerIdOrSlugStatsSide, optional
        :param videogame_version: videogame_version, defaults to None
        :type videogame_version: VideogameVersionOrAll, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a League-of-Legends player by serie
        :rtype: LoLStatsForPlayerBySerie
        """

        Validator(SerieIdOrSlug).validate(serie_id_or_slug)
        Validator(PlayerIdOrSlug).validate(player_id_or_slug)
        Validator(int).is_optional().validate(games_count)
        Validator(GetLolPlayersPlayerIdOrSlugStatsSide).is_optional().validate(side)
        Validator(VideogameVersionOrAll).is_optional().validate(videogame_version)

        serialized_request = (
            Serializer(
                f"{self.base_url}/lol/series/{{serie_id_or_slug}}/players/{{player_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("serie_id_or_slug", serie_id_or_slug)
            .add_path("player_id_or_slug", player_id_or_slug)
            .add_query("games_count", games_count)
            .add_query("side", side)
            .add_query("videogame_version", videogame_version)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return LoLStatsForPlayerBySerie._unmap(response)

    @cast_models
    def get_lol_series_serie_id_or_slug_teams_stats(
        self,
        serie_id_or_slug: SerieIdOrSlug,
        games_count: int = None,
        side: GetLolPlayersPlayerIdOrSlugStatsSide = None,
        videogame_version: VideogameVersionOrAll = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[LoLStatsForTeamBySerie]:
        """Get detailed statistics of the LoL teams for the given series

        :param serie_id_or_slug: A serie ID or slug
        :type serie_id_or_slug: SerieIdOrSlug
        :param games_count: The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/>, defaults to None
        :type games_count: int, optional
        :param side: side, defaults to None
        :type side: GetLolPlayersPlayerIdOrSlugStatsSide, optional
        :param videogame_version: videogame_version, defaults to None
        :type videogame_version: VideogameVersionOrAll, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of League-of-Legends teams by serie
        :rtype: List[LoLStatsForTeamBySerie]
        """

        Validator(SerieIdOrSlug).validate(serie_id_or_slug)
        Validator(int).is_optional().validate(games_count)
        Validator(GetLolPlayersPlayerIdOrSlugStatsSide).is_optional().validate(side)
        Validator(VideogameVersionOrAll).is_optional().validate(videogame_version)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/lol/series/{{serie_id_or_slug}}/teams/stats",
                self.get_default_headers(),
            )
            .add_path("serie_id_or_slug", serie_id_or_slug)
            .add_query("games_count", games_count)
            .add_query("side", side)
            .add_query("videogame_version", videogame_version)
            .add_query("page", page)
            .add_query("per_page", per_page)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return [LoLStatsForTeamBySerie._unmap(item) for item in response]

    @cast_models
    def get_lol_series_serie_id_or_slug_teams_team_id_or_slug_stats(
        self,
        serie_id_or_slug: SerieIdOrSlug,
        team_id_or_slug: TeamIdOrSlug,
        games_count: int = None,
        side: GetLolPlayersPlayerIdOrSlugStatsSide = None,
        videogame_version: VideogameVersionOrAll = None,
    ) -> LoLStatsForTeamBySerie:
        """Get detailed statistics of a given League-of-Legends team for the given serie

        :param serie_id_or_slug: A serie ID or slug
        :type serie_id_or_slug: SerieIdOrSlug
        :param team_id_or_slug: A team ID or slug
        :type team_id_or_slug: TeamIdOrSlug
        :param games_count: The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/>, defaults to None
        :type games_count: int, optional
        :param side: side, defaults to None
        :type side: GetLolPlayersPlayerIdOrSlugStatsSide, optional
        :param videogame_version: videogame_version, defaults to None
        :type videogame_version: VideogameVersionOrAll, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a League-of-Legends team by serie
        :rtype: LoLStatsForTeamBySerie
        """

        Validator(SerieIdOrSlug).validate(serie_id_or_slug)
        Validator(TeamIdOrSlug).validate(team_id_or_slug)
        Validator(int).is_optional().validate(games_count)
        Validator(GetLolPlayersPlayerIdOrSlugStatsSide).is_optional().validate(side)
        Validator(VideogameVersionOrAll).is_optional().validate(videogame_version)

        serialized_request = (
            Serializer(
                f"{self.base_url}/lol/series/{{serie_id_or_slug}}/teams/{{team_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("serie_id_or_slug", serie_id_or_slug)
            .add_path("team_id_or_slug", team_id_or_slug)
            .add_query("games_count", games_count)
            .add_query("side", side)
            .add_query("videogame_version", videogame_version)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return LoLStatsForTeamBySerie._unmap(response)

    @cast_models
    def get_lol_teams_team_id_or_slug_stats(
        self,
        team_id_or_slug: TeamIdOrSlug,
        games_count: int = None,
        side: GetLolPlayersPlayerIdOrSlugStatsSide = None,
        videogame_version: VideogameVersionOrAll = None,
        from_: str = None,
        to: str = None,
    ) -> LoLStatsForTeam:
        """Get detailed statistics of a given League-of-Legends team

        :param team_id_or_slug: A team ID or slug
        :type team_id_or_slug: TeamIdOrSlug
        :param games_count: The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/>, defaults to None
        :type games_count: int, optional
        :param side: side, defaults to None
        :type side: GetLolPlayersPlayerIdOrSlugStatsSide, optional
        :param videogame_version: videogame_version, defaults to None
        :type videogame_version: VideogameVersionOrAll, optional
        :param from_: Filter out 'from' date, defaults to None
        :type from_: str, optional
        :param to: Filter out 'to' date, defaults to None
        :type to: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a League-of-Legends team
        :rtype: LoLStatsForTeam
        """

        Validator(TeamIdOrSlug).validate(team_id_or_slug)
        Validator(int).is_optional().validate(games_count)
        Validator(GetLolPlayersPlayerIdOrSlugStatsSide).is_optional().validate(side)
        Validator(VideogameVersionOrAll).is_optional().validate(videogame_version)
        Validator(str).is_optional().validate(from_)
        Validator(str).is_optional().validate(to)

        serialized_request = (
            Serializer(
                f"{self.base_url}/lol/teams/{{team_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("team_id_or_slug", team_id_or_slug)
            .add_query("games_count", games_count)
            .add_query("side", side)
            .add_query("videogame_version", videogame_version)
            .add_query("from", from_)
            .add_query("to", to)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return LoLStatsForTeam._unmap(response)

    @cast_models
    def get_lol_tournaments_tournament_id_or_slug_players_player_id_or_slug_stats(
        self,
        tournament_id_or_slug: TournamentIdOrSlug,
        player_id_or_slug: PlayerIdOrSlug,
        games_count: int = None,
        side: GetLolPlayersPlayerIdOrSlugStatsSide = None,
        videogame_version: VideogameVersionOrAll = None,
    ) -> LoLStatsForPlayerByTournament:
        """Get detailed statistics of a given League-of-Legends player for the given tournament

        :param tournament_id_or_slug: A tournament ID or slug
        :type tournament_id_or_slug: TournamentIdOrSlug
        :param player_id_or_slug: A player ID or slug
        :type player_id_or_slug: PlayerIdOrSlug
        :param games_count: The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/>, defaults to None
        :type games_count: int, optional
        :param side: side, defaults to None
        :type side: GetLolPlayersPlayerIdOrSlugStatsSide, optional
        :param videogame_version: videogame_version, defaults to None
        :type videogame_version: VideogameVersionOrAll, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a League-of-Legends player by tournament
        :rtype: LoLStatsForPlayerByTournament
        """

        Validator(TournamentIdOrSlug).validate(tournament_id_or_slug)
        Validator(PlayerIdOrSlug).validate(player_id_or_slug)
        Validator(int).is_optional().validate(games_count)
        Validator(GetLolPlayersPlayerIdOrSlugStatsSide).is_optional().validate(side)
        Validator(VideogameVersionOrAll).is_optional().validate(videogame_version)

        serialized_request = (
            Serializer(
                f"{self.base_url}/lol/tournaments/{{tournament_id_or_slug}}/players/{{player_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("tournament_id_or_slug", tournament_id_or_slug)
            .add_path("player_id_or_slug", player_id_or_slug)
            .add_query("games_count", games_count)
            .add_query("side", side)
            .add_query("videogame_version", videogame_version)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return LoLStatsForPlayerByTournament._unmap(response)

    @cast_models
    def get_lol_tournaments_tournament_id_or_slug_teams_team_id_or_slug_stats(
        self,
        tournament_id_or_slug: TournamentIdOrSlug,
        team_id_or_slug: TeamIdOrSlug,
        games_count: int = None,
        side: GetLolPlayersPlayerIdOrSlugStatsSide = None,
        videogame_version: VideogameVersionOrAll = None,
    ) -> LoLStatsForTeamByTournament:
        """Get detailed statistics of a given League-of-Legends team for the given tournament

        :param tournament_id_or_slug: A tournament ID or slug
        :type tournament_id_or_slug: TournamentIdOrSlug
        :param team_id_or_slug: A team ID or slug
        :type team_id_or_slug: TeamIdOrSlug
        :param games_count: The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/>, defaults to None
        :type games_count: int, optional
        :param side: side, defaults to None
        :type side: GetLolPlayersPlayerIdOrSlugStatsSide, optional
        :param videogame_version: videogame_version, defaults to None
        :type videogame_version: VideogameVersionOrAll, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a League-of-Legends team by tournament
        :rtype: LoLStatsForTeamByTournament
        """

        Validator(TournamentIdOrSlug).validate(tournament_id_or_slug)
        Validator(TeamIdOrSlug).validate(team_id_or_slug)
        Validator(int).is_optional().validate(games_count)
        Validator(GetLolPlayersPlayerIdOrSlugStatsSide).is_optional().validate(side)
        Validator(VideogameVersionOrAll).is_optional().validate(videogame_version)

        serialized_request = (
            Serializer(
                f"{self.base_url}/lol/tournaments/{{tournament_id_or_slug}}/teams/{{team_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("tournament_id_or_slug", tournament_id_or_slug)
            .add_path("team_id_or_slug", team_id_or_slug)
            .add_query("games_count", games_count)
            .add_query("side", side)
            .add_query("videogame_version", videogame_version)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return LoLStatsForTeamByTournament._unmap(response)
