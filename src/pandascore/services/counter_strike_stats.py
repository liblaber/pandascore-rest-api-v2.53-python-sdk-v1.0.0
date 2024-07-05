from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.videogame_title_id_or_slug import VideogameTitleIdOrSlug
from ..models.utils.cast_models import cast_models
from ..models.tournament_id_or_slug import TournamentIdOrSlug
from ..models.team_id_or_slug import TeamIdOrSlug
from ..models.serie_id_or_slug import SerieIdOrSlug
from ..models.player_id_or_slug import PlayerIdOrSlug
from ..models.match_id_or_slug import MatchIdOrSlug
from ..models.csgo_stats_for_team_by_tournament import CsgoStatsForTeamByTournament
from ..models.csgo_stats_for_team_by_serie import CsgoStatsForTeamBySerie
from ..models.csgo_stats_for_team_by_match import CsgoStatsForTeamByMatch
from ..models.csgo_stats_for_team import CsgoStatsForTeam
from ..models.csgo_stats_for_player_by_tournament import CsgoStatsForPlayerByTournament
from ..models.csgo_stats_for_player_by_serie import CsgoStatsForPlayerBySerie
from ..models.csgo_stats_for_player_by_match import CsgoStatsForPlayerByMatch
from ..models.csgo_stats_for_player import CsgoStatsForPlayer
from ..models.csgo_stats_for_all_players_by_match import CsgoStatsForAllPlayersByMatch


class CounterStrikeStatsService(BaseService):

    @cast_models
    def get_csgo_matches_match_id_or_slug_players_stats(
        self, match_id_or_slug: MatchIdOrSlug
    ) -> CsgoStatsForAllPlayersByMatch:
        """Get detailed statistics of Counter-Strike players for the given match

        :param match_id_or_slug: A match ID or slug
        :type match_id_or_slug: MatchIdOrSlug
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of all Counter-Strike players by match
        :rtype: CsgoStatsForAllPlayersByMatch
        """

        Validator(MatchIdOrSlug).validate(match_id_or_slug)

        serialized_request = (
            Serializer(
                f"{self.base_url}/csgo/matches/{{match_id_or_slug}}/players/stats",
                self.get_default_headers(),
            )
            .add_path("match_id_or_slug", match_id_or_slug)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return CsgoStatsForAllPlayersByMatch._unmap(response)

    @cast_models
    def get_csgo_matches_match_id_or_slug_players_player_id_or_slug_stats(
        self, match_id_or_slug: MatchIdOrSlug, player_id_or_slug: PlayerIdOrSlug
    ) -> CsgoStatsForPlayerByMatch:
        """Get detailed statistics of a given Counter-Strike player for the given match

        :param match_id_or_slug: A match ID or slug
        :type match_id_or_slug: MatchIdOrSlug
        :param player_id_or_slug: A player ID or slug
        :type player_id_or_slug: PlayerIdOrSlug
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a Counter-Strike player by match
        :rtype: CsgoStatsForPlayerByMatch
        """

        Validator(MatchIdOrSlug).validate(match_id_or_slug)
        Validator(PlayerIdOrSlug).validate(player_id_or_slug)

        serialized_request = (
            Serializer(
                f"{self.base_url}/csgo/matches/{{match_id_or_slug}}/players/{{player_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("match_id_or_slug", match_id_or_slug)
            .add_path("player_id_or_slug", player_id_or_slug)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return CsgoStatsForPlayerByMatch._unmap(response)

    @cast_models
    def get_csgo_matches_match_id_or_slug_teams_team_id_or_slug_stats(
        self, match_id_or_slug: MatchIdOrSlug, team_id_or_slug: TeamIdOrSlug
    ) -> CsgoStatsForTeamByMatch:
        """Get detailed statistics of a given Counter-Strike team for the given match

        :param match_id_or_slug: A match ID or slug
        :type match_id_or_slug: MatchIdOrSlug
        :param team_id_or_slug: A team ID or slug
        :type team_id_or_slug: TeamIdOrSlug
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a Counter-Strike team by match
        :rtype: CsgoStatsForTeamByMatch
        """

        Validator(MatchIdOrSlug).validate(match_id_or_slug)
        Validator(TeamIdOrSlug).validate(team_id_or_slug)

        serialized_request = (
            Serializer(
                f"{self.base_url}/csgo/matches/{{match_id_or_slug}}/teams/{{team_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("match_id_or_slug", match_id_or_slug)
            .add_path("team_id_or_slug", team_id_or_slug)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return CsgoStatsForTeamByMatch._unmap(response)

    @cast_models
    def get_csgo_players_player_id_or_slug_stats(
        self,
        player_id_or_slug: PlayerIdOrSlug,
        videogame_title: VideogameTitleIdOrSlug = None,
        from_: str = None,
        to: str = None,
    ) -> CsgoStatsForPlayer:
        """Get detailed statistics of a given Counter-Strike player

        :param player_id_or_slug: A player ID or slug
        :type player_id_or_slug: PlayerIdOrSlug
        :param videogame_title: videogame_title, defaults to None
        :type videogame_title: VideogameTitleIdOrSlug, optional
        :param from_: Filter out 'from' date, defaults to None
        :type from_: str, optional
        :param to: Filter out 'to' date, defaults to None
        :type to: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a Counter-Strike player
        :rtype: CsgoStatsForPlayer
        """

        Validator(PlayerIdOrSlug).validate(player_id_or_slug)
        Validator(VideogameTitleIdOrSlug).is_optional().validate(videogame_title)
        Validator(str).is_optional().validate(from_)
        Validator(str).is_optional().validate(to)

        serialized_request = (
            Serializer(
                f"{self.base_url}/csgo/players/{{player_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("player_id_or_slug", player_id_or_slug)
            .add_query("videogame_title", videogame_title)
            .add_query("from", from_)
            .add_query("to", to)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return CsgoStatsForPlayer._unmap(response)

    @cast_models
    def get_csgo_series_serie_id_or_slug_players_player_id_or_slug_stats(
        self, serie_id_or_slug: SerieIdOrSlug, player_id_or_slug: PlayerIdOrSlug
    ) -> CsgoStatsForPlayerBySerie:
        """Get detailed statistics of a given Counter-Strike player for the given serie

        :param serie_id_or_slug: A serie ID or slug
        :type serie_id_or_slug: SerieIdOrSlug
        :param player_id_or_slug: A player ID or slug
        :type player_id_or_slug: PlayerIdOrSlug
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a Counter-Strike player by serie
        :rtype: CsgoStatsForPlayerBySerie
        """

        Validator(SerieIdOrSlug).validate(serie_id_or_slug)
        Validator(PlayerIdOrSlug).validate(player_id_or_slug)

        serialized_request = (
            Serializer(
                f"{self.base_url}/csgo/series/{{serie_id_or_slug}}/players/{{player_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("serie_id_or_slug", serie_id_or_slug)
            .add_path("player_id_or_slug", player_id_or_slug)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return CsgoStatsForPlayerBySerie._unmap(response)

    @cast_models
    def get_csgo_series_serie_id_or_slug_teams_team_id_or_slug_stats(
        self, serie_id_or_slug: SerieIdOrSlug, team_id_or_slug: TeamIdOrSlug
    ) -> CsgoStatsForTeamBySerie:
        """Get detailed statistics of a given Counter-Strike team for the given serie

        :param serie_id_or_slug: A serie ID or slug
        :type serie_id_or_slug: SerieIdOrSlug
        :param team_id_or_slug: A team ID or slug
        :type team_id_or_slug: TeamIdOrSlug
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a Counter-Strike team by serie
        :rtype: CsgoStatsForTeamBySerie
        """

        Validator(SerieIdOrSlug).validate(serie_id_or_slug)
        Validator(TeamIdOrSlug).validate(team_id_or_slug)

        serialized_request = (
            Serializer(
                f"{self.base_url}/csgo/series/{{serie_id_or_slug}}/teams/{{team_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("serie_id_or_slug", serie_id_or_slug)
            .add_path("team_id_or_slug", team_id_or_slug)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return CsgoStatsForTeamBySerie._unmap(response)

    @cast_models
    def get_csgo_teams_team_id_or_slug_stats(
        self,
        team_id_or_slug: TeamIdOrSlug,
        videogame_title: VideogameTitleIdOrSlug = None,
        from_: str = None,
        to: str = None,
    ) -> CsgoStatsForTeam:
        """Get detailed statistics of a given Counter-Strike team

        :param team_id_or_slug: A team ID or slug
        :type team_id_or_slug: TeamIdOrSlug
        :param videogame_title: videogame_title, defaults to None
        :type videogame_title: VideogameTitleIdOrSlug, optional
        :param from_: Filter out 'from' date, defaults to None
        :type from_: str, optional
        :param to: Filter out 'to' date, defaults to None
        :type to: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a Counter-Strike team
        :rtype: CsgoStatsForTeam
        """

        Validator(TeamIdOrSlug).validate(team_id_or_slug)
        Validator(VideogameTitleIdOrSlug).is_optional().validate(videogame_title)
        Validator(str).is_optional().validate(from_)
        Validator(str).is_optional().validate(to)

        serialized_request = (
            Serializer(
                f"{self.base_url}/csgo/teams/{{team_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("team_id_or_slug", team_id_or_slug)
            .add_query("videogame_title", videogame_title)
            .add_query("from", from_)
            .add_query("to", to)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return CsgoStatsForTeam._unmap(response)

    @cast_models
    def get_csgo_tournaments_tournament_id_or_slug_players_player_id_or_slug_stats(
        self,
        tournament_id_or_slug: TournamentIdOrSlug,
        player_id_or_slug: PlayerIdOrSlug,
    ) -> CsgoStatsForPlayerByTournament:
        """Get detailed statistics of a given Counter-Strike player for the given tournament

        :param tournament_id_or_slug: A tournament ID or slug
        :type tournament_id_or_slug: TournamentIdOrSlug
        :param player_id_or_slug: A player ID or slug
        :type player_id_or_slug: PlayerIdOrSlug
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a Counter-Strike player by tournament
        :rtype: CsgoStatsForPlayerByTournament
        """

        Validator(TournamentIdOrSlug).validate(tournament_id_or_slug)
        Validator(PlayerIdOrSlug).validate(player_id_or_slug)

        serialized_request = (
            Serializer(
                f"{self.base_url}/csgo/tournaments/{{tournament_id_or_slug}}/players/{{player_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("tournament_id_or_slug", tournament_id_or_slug)
            .add_path("player_id_or_slug", player_id_or_slug)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return CsgoStatsForPlayerByTournament._unmap(response)

    @cast_models
    def get_csgo_tournaments_tournament_id_or_slug_teams_team_id_or_slug_stats(
        self, tournament_id_or_slug: TournamentIdOrSlug, team_id_or_slug: TeamIdOrSlug
    ) -> CsgoStatsForTeamByTournament:
        """Get detailed statistics of a given Counter-Strike team for the given tournament

        :param tournament_id_or_slug: A tournament ID or slug
        :type tournament_id_or_slug: TournamentIdOrSlug
        :param team_id_or_slug: A team ID or slug
        :type team_id_or_slug: TeamIdOrSlug
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a Counter-Strike team by tournament
        :rtype: CsgoStatsForTeamByTournament
        """

        Validator(TournamentIdOrSlug).validate(tournament_id_or_slug)
        Validator(TeamIdOrSlug).validate(team_id_or_slug)

        serialized_request = (
            Serializer(
                f"{self.base_url}/csgo/tournaments/{{tournament_id_or_slug}}/teams/{{team_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("tournament_id_or_slug", tournament_id_or_slug)
            .add_path("team_id_or_slug", team_id_or_slug)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return CsgoStatsForTeamByTournament._unmap(response)
