from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.tournament_id_or_slug import TournamentIdOrSlug
from ..models.team_id_or_slug import TeamIdOrSlug
from ..models.serie_id_or_slug import SerieIdOrSlug
from ..models.player_id_or_slug import PlayerIdOrSlug
from ..models.match_id_or_slug import MatchIdOrSlug
from ..models.get_dota2_players_player_id_or_slug_stats_side import (
    GetDota2PlayersPlayerIdOrSlugStatsSide,
)
from ..models.dota2_stats_for_team_by_tournament import Dota2StatsForTeamByTournament
from ..models.dota2_stats_for_team_by_serie import Dota2StatsForTeamBySerie
from ..models.dota2_stats_for_team import Dota2StatsForTeam
from ..models.dota2_stats_for_player_by_tournament import (
    Dota2StatsForPlayerByTournament,
)
from ..models.dota2_stats_for_player_by_serie import Dota2StatsForPlayerBySerie
from ..models.dota2_stats_for_player import Dota2StatsForPlayer
from ..models.dota2_stats_for_all_players_by_match import Dota2StatsForAllPlayersByMatch


class Dota2StatsService(BaseService):

    @cast_models
    def get_dota2_matches_match_id_or_slug_players_stats(
        self, match_id_or_slug: MatchIdOrSlug
    ) -> Dota2StatsForAllPlayersByMatch:
        """Get detailed statistics of Dota2 players for the given match

        :param match_id_or_slug: A match ID or slug
        :type match_id_or_slug: MatchIdOrSlug
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of all Dota2 players by match
        :rtype: Dota2StatsForAllPlayersByMatch
        """

        Validator(MatchIdOrSlug).validate(match_id_or_slug)

        serialized_request = (
            Serializer(
                f"{self.base_url}/dota2/matches/{{match_id_or_slug}}/players/stats",
                self.get_default_headers(),
            )
            .add_path("match_id_or_slug", match_id_or_slug)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return Dota2StatsForAllPlayersByMatch._unmap(response)

    @cast_models
    def get_dota2_players_player_id_or_slug_stats(
        self,
        player_id_or_slug: PlayerIdOrSlug,
        games_count: int = None,
        side: GetDota2PlayersPlayerIdOrSlugStatsSide = None,
        from_: str = None,
        to: str = None,
    ) -> Dota2StatsForPlayer:
        """Get detailed statistics of a given Dota2 player

        :param player_id_or_slug: A player ID or slug
        :type player_id_or_slug: PlayerIdOrSlug
        :param games_count: The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/>, defaults to None
        :type games_count: int, optional
        :param side: side, defaults to None
        :type side: GetDota2PlayersPlayerIdOrSlugStatsSide, optional
        :param from_: Filter out 'from' date, defaults to None
        :type from_: str, optional
        :param to: Filter out 'to' date, defaults to None
        :type to: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a Dota2 player
        :rtype: Dota2StatsForPlayer
        """

        Validator(PlayerIdOrSlug).validate(player_id_or_slug)
        Validator(int).is_optional().validate(games_count)
        Validator(GetDota2PlayersPlayerIdOrSlugStatsSide).is_optional().validate(side)
        Validator(str).is_optional().validate(from_)
        Validator(str).is_optional().validate(to)

        serialized_request = (
            Serializer(
                f"{self.base_url}/dota2/players/{{player_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("player_id_or_slug", player_id_or_slug)
            .add_query("games_count", games_count)
            .add_query("side", side)
            .add_query("from", from_)
            .add_query("to", to)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return Dota2StatsForPlayer._unmap(response)

    @cast_models
    def get_dota2_series_serie_id_or_slug_players_player_id_or_slug_stats(
        self,
        serie_id_or_slug: SerieIdOrSlug,
        player_id_or_slug: PlayerIdOrSlug,
        games_count: int = None,
        side: GetDota2PlayersPlayerIdOrSlugStatsSide = None,
    ) -> Dota2StatsForPlayerBySerie:
        """Get detailed statistics of a given Dota2 player for the given serie

        :param serie_id_or_slug: A serie ID or slug
        :type serie_id_or_slug: SerieIdOrSlug
        :param player_id_or_slug: A player ID or slug
        :type player_id_or_slug: PlayerIdOrSlug
        :param games_count: The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/>, defaults to None
        :type games_count: int, optional
        :param side: side, defaults to None
        :type side: GetDota2PlayersPlayerIdOrSlugStatsSide, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a Dota2 player by serie
        :rtype: Dota2StatsForPlayerBySerie
        """

        Validator(SerieIdOrSlug).validate(serie_id_or_slug)
        Validator(PlayerIdOrSlug).validate(player_id_or_slug)
        Validator(int).is_optional().validate(games_count)
        Validator(GetDota2PlayersPlayerIdOrSlugStatsSide).is_optional().validate(side)

        serialized_request = (
            Serializer(
                f"{self.base_url}/dota2/series/{{serie_id_or_slug}}/players/{{player_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("serie_id_or_slug", serie_id_or_slug)
            .add_path("player_id_or_slug", player_id_or_slug)
            .add_query("games_count", games_count)
            .add_query("side", side)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return Dota2StatsForPlayerBySerie._unmap(response)

    @cast_models
    def get_dota2_series_serie_id_or_slug_teams_team_id_or_slug_stats(
        self,
        serie_id_or_slug: SerieIdOrSlug,
        team_id_or_slug: TeamIdOrSlug,
        games_count: int = None,
        side: GetDota2PlayersPlayerIdOrSlugStatsSide = None,
    ) -> Dota2StatsForTeamBySerie:
        """Get detailed statistics of a given Dota2 team for the given serie

        :param serie_id_or_slug: A serie ID or slug
        :type serie_id_or_slug: SerieIdOrSlug
        :param team_id_or_slug: A team ID or slug
        :type team_id_or_slug: TeamIdOrSlug
        :param games_count: The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/>, defaults to None
        :type games_count: int, optional
        :param side: side, defaults to None
        :type side: GetDota2PlayersPlayerIdOrSlugStatsSide, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a Dota2 team by serie
        :rtype: Dota2StatsForTeamBySerie
        """

        Validator(SerieIdOrSlug).validate(serie_id_or_slug)
        Validator(TeamIdOrSlug).validate(team_id_or_slug)
        Validator(int).is_optional().validate(games_count)
        Validator(GetDota2PlayersPlayerIdOrSlugStatsSide).is_optional().validate(side)

        serialized_request = (
            Serializer(
                f"{self.base_url}/dota2/series/{{serie_id_or_slug}}/teams/{{team_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("serie_id_or_slug", serie_id_or_slug)
            .add_path("team_id_or_slug", team_id_or_slug)
            .add_query("games_count", games_count)
            .add_query("side", side)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return Dota2StatsForTeamBySerie._unmap(response)

    @cast_models
    def get_dota2_teams_team_id_or_slug_stats(
        self,
        team_id_or_slug: TeamIdOrSlug,
        games_count: int = None,
        side: GetDota2PlayersPlayerIdOrSlugStatsSide = None,
        from_: str = None,
        to: str = None,
    ) -> Dota2StatsForTeam:
        """Get detailed statistics of a given Dota2 team

        :param team_id_or_slug: A team ID or slug
        :type team_id_or_slug: TeamIdOrSlug
        :param games_count: The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/>, defaults to None
        :type games_count: int, optional
        :param side: side, defaults to None
        :type side: GetDota2PlayersPlayerIdOrSlugStatsSide, optional
        :param from_: Filter out 'from' date, defaults to None
        :type from_: str, optional
        :param to: Filter out 'to' date, defaults to None
        :type to: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a Dota2 team
        :rtype: Dota2StatsForTeam
        """

        Validator(TeamIdOrSlug).validate(team_id_or_slug)
        Validator(int).is_optional().validate(games_count)
        Validator(GetDota2PlayersPlayerIdOrSlugStatsSide).is_optional().validate(side)
        Validator(str).is_optional().validate(from_)
        Validator(str).is_optional().validate(to)

        serialized_request = (
            Serializer(
                f"{self.base_url}/dota2/teams/{{team_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("team_id_or_slug", team_id_or_slug)
            .add_query("games_count", games_count)
            .add_query("side", side)
            .add_query("from", from_)
            .add_query("to", to)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return Dota2StatsForTeam._unmap(response)

    @cast_models
    def get_dota2_tournaments_tournament_id_or_slug_players_player_id_or_slug_stats(
        self,
        tournament_id_or_slug: TournamentIdOrSlug,
        player_id_or_slug: PlayerIdOrSlug,
        games_count: int = None,
        side: GetDota2PlayersPlayerIdOrSlugStatsSide = None,
    ) -> Dota2StatsForPlayerByTournament:
        """Get detailed statistics of a given Dota2 player for the given tournament

        :param tournament_id_or_slug: A tournament ID or slug
        :type tournament_id_or_slug: TournamentIdOrSlug
        :param player_id_or_slug: A player ID or slug
        :type player_id_or_slug: PlayerIdOrSlug
        :param games_count: The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/>, defaults to None
        :type games_count: int, optional
        :param side: side, defaults to None
        :type side: GetDota2PlayersPlayerIdOrSlugStatsSide, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a Dota2 player by tournament
        :rtype: Dota2StatsForPlayerByTournament
        """

        Validator(TournamentIdOrSlug).validate(tournament_id_or_slug)
        Validator(PlayerIdOrSlug).validate(player_id_or_slug)
        Validator(int).is_optional().validate(games_count)
        Validator(GetDota2PlayersPlayerIdOrSlugStatsSide).is_optional().validate(side)

        serialized_request = (
            Serializer(
                f"{self.base_url}/dota2/tournaments/{{tournament_id_or_slug}}/players/{{player_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("tournament_id_or_slug", tournament_id_or_slug)
            .add_path("player_id_or_slug", player_id_or_slug)
            .add_query("games_count", games_count)
            .add_query("side", side)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return Dota2StatsForPlayerByTournament._unmap(response)

    @cast_models
    def get_dota2_tournaments_tournament_id_or_slug_teams_team_id_or_slug_stats(
        self,
        tournament_id_or_slug: TournamentIdOrSlug,
        team_id_or_slug: TeamIdOrSlug,
        games_count: int = None,
        side: GetDota2PlayersPlayerIdOrSlugStatsSide = None,
    ) -> Dota2StatsForTeamByTournament:
        """Get detailed statistics of a given Dota2 team for the given tournament

        :param tournament_id_or_slug: A tournament ID or slug
        :type tournament_id_or_slug: TournamentIdOrSlug
        :param team_id_or_slug: A team ID or slug
        :type team_id_or_slug: TeamIdOrSlug
        :param games_count: The amount of games used for the statistics. <br/> <br/>For example if `?games_count=5`, it would show the statistics for the most recent 5 games played <br/>, defaults to None
        :type games_count: int, optional
        :param side: side, defaults to None
        :type side: GetDota2PlayersPlayerIdOrSlugStatsSide, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a Dota2 team by tournament
        :rtype: Dota2StatsForTeamByTournament
        """

        Validator(TournamentIdOrSlug).validate(tournament_id_or_slug)
        Validator(TeamIdOrSlug).validate(team_id_or_slug)
        Validator(int).is_optional().validate(games_count)
        Validator(GetDota2PlayersPlayerIdOrSlugStatsSide).is_optional().validate(side)

        serialized_request = (
            Serializer(
                f"{self.base_url}/dota2/tournaments/{{tournament_id_or_slug}}/teams/{{team_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("tournament_id_or_slug", tournament_id_or_slug)
            .add_path("team_id_or_slug", team_id_or_slug)
            .add_query("games_count", games_count)
            .add_query("side", side)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return Dota2StatsForTeamByTournament._unmap(response)
