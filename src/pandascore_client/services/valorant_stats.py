# This file was generated by liblab | https://liblab.com/

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.videogame_version_or_all import VideogameVersionOrAll
from ..models.valorant_stats_for_team_by_tournament import (
    ValorantStatsForTeamByTournament,
)
from ..models.valorant_stats_for_team_by_serie import ValorantStatsForTeamBySerie
from ..models.valorant_stats_for_team_by_match import ValorantStatsForTeamByMatch
from ..models.valorant_stats_for_team import ValorantStatsForTeam
from ..models.valorant_stats_for_players_by_match import ValorantStatsForPlayersByMatch
from ..models.valorant_stats_for_player_by_tournament import (
    ValorantStatsForPlayerByTournament,
)
from ..models.valorant_stats_for_player_by_serie import ValorantStatsForPlayerBySerie
from ..models.valorant_stats_for_player import ValorantStatsForPlayer
from ..models.utils.cast_models import cast_models
from ..models.tournament_id_or_slug import TournamentIdOrSlug
from ..models.team_id_or_slug import TeamIdOrSlug
from ..models.serie_id_or_slug import SerieIdOrSlug
from ..models.player_id_or_slug import PlayerIdOrSlug
from ..models.match_id_or_slug import MatchIdOrSlug


class ValorantStatsService(BaseService):

    @cast_models
    def get_valorant_matches_match_id_or_slug_players_stats(
        self, match_id_or_slug: MatchIdOrSlug
    ) -> ValorantStatsForPlayersByMatch:
        """Get the aggregated statistics for all players in a Valorant match

        :param match_id_or_slug: A match ID or slug
        :type match_id_or_slug: MatchIdOrSlug
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of all Valorant players by match
        :rtype: ValorantStatsForPlayersByMatch
        """

        Validator(MatchIdOrSlug).validate(match_id_or_slug)

        serialized_request = (
            Serializer(
                f"{self.base_url}/valorant/matches/{{match_id_or_slug}}/players/stats",
                self.get_default_headers(),
            )
            .add_path("match_id_or_slug", match_id_or_slug)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return ValorantStatsForPlayersByMatch._unmap(response)

    @cast_models
    def get_valorant_matches_match_id_or_slug_teams_team_id_or_slug_stats(
        self, match_id_or_slug: MatchIdOrSlug, team_id_or_slug: TeamIdOrSlug
    ) -> ValorantStatsForTeamByMatch:
        """Get the aggregated team statistics for a Valorant match

        :param match_id_or_slug: A match ID or slug
        :type match_id_or_slug: MatchIdOrSlug
        :param team_id_or_slug: A team ID or slug
        :type team_id_or_slug: TeamIdOrSlug
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a Valorant team by match
        :rtype: ValorantStatsForTeamByMatch
        """

        Validator(MatchIdOrSlug).validate(match_id_or_slug)
        Validator(TeamIdOrSlug).validate(team_id_or_slug)

        serialized_request = (
            Serializer(
                f"{self.base_url}/valorant/matches/{{match_id_or_slug}}/teams/{{team_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("match_id_or_slug", match_id_or_slug)
            .add_path("team_id_or_slug", team_id_or_slug)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return ValorantStatsForTeamByMatch._unmap(response)

    @cast_models
    def get_valorant_players_player_id_or_slug_stats(
        self,
        player_id_or_slug: PlayerIdOrSlug,
        videogame_version: VideogameVersionOrAll = None,
        from_: str = None,
        to: str = None,
    ) -> ValorantStatsForPlayer:
        """Get a Valorant player stats by ID or slug

        :param player_id_or_slug: A player ID or slug
        :type player_id_or_slug: PlayerIdOrSlug
        :param videogame_version: videogame_version, defaults to None
        :type videogame_version: VideogameVersionOrAll, optional
        :param from_: Filter out 'from' date, defaults to None
        :type from_: str, optional
        :param to: Filter out 'to' date, defaults to None
        :type to: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a Valorant player
        :rtype: ValorantStatsForPlayer
        """

        Validator(PlayerIdOrSlug).validate(player_id_or_slug)
        Validator(VideogameVersionOrAll).is_optional().validate(videogame_version)
        Validator(str).is_optional().validate(from_)
        Validator(str).is_optional().validate(to)

        serialized_request = (
            Serializer(
                f"{self.base_url}/valorant/players/{{player_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("player_id_or_slug", player_id_or_slug)
            .add_query("videogame_version", videogame_version)
            .add_query("from", from_)
            .add_query("to", to)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return ValorantStatsForPlayer._unmap(response)

    @cast_models
    def get_valorant_series_serie_id_or_slug_players_player_id_or_slug_stats(
        self,
        serie_id_or_slug: SerieIdOrSlug,
        player_id_or_slug: PlayerIdOrSlug,
        videogame_version: VideogameVersionOrAll = None,
    ) -> ValorantStatsForPlayerBySerie:
        """Get the aggregated player statistics for a Valorant series

        :param serie_id_or_slug: A serie ID or slug
        :type serie_id_or_slug: SerieIdOrSlug
        :param player_id_or_slug: A player ID or slug
        :type player_id_or_slug: PlayerIdOrSlug
        :param videogame_version: videogame_version, defaults to None
        :type videogame_version: VideogameVersionOrAll, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a Valorant player by serie
        :rtype: ValorantStatsForPlayerBySerie
        """

        Validator(SerieIdOrSlug).validate(serie_id_or_slug)
        Validator(PlayerIdOrSlug).validate(player_id_or_slug)
        Validator(VideogameVersionOrAll).is_optional().validate(videogame_version)

        serialized_request = (
            Serializer(
                f"{self.base_url}/valorant/series/{{serie_id_or_slug}}/players/{{player_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("serie_id_or_slug", serie_id_or_slug)
            .add_path("player_id_or_slug", player_id_or_slug)
            .add_query("videogame_version", videogame_version)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return ValorantStatsForPlayerBySerie._unmap(response)

    @cast_models
    def get_valorant_series_serie_id_or_slug_teams_team_id_or_slug_stats(
        self,
        serie_id_or_slug: SerieIdOrSlug,
        team_id_or_slug: TeamIdOrSlug,
        videogame_version: VideogameVersionOrAll = None,
    ) -> ValorantStatsForTeamBySerie:
        """Get the aggregated team statistics for a Valorant series

        :param serie_id_or_slug: A serie ID or slug
        :type serie_id_or_slug: SerieIdOrSlug
        :param team_id_or_slug: A team ID or slug
        :type team_id_or_slug: TeamIdOrSlug
        :param videogame_version: videogame_version, defaults to None
        :type videogame_version: VideogameVersionOrAll, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a Valorant team by serie
        :rtype: ValorantStatsForTeamBySerie
        """

        Validator(SerieIdOrSlug).validate(serie_id_or_slug)
        Validator(TeamIdOrSlug).validate(team_id_or_slug)
        Validator(VideogameVersionOrAll).is_optional().validate(videogame_version)

        serialized_request = (
            Serializer(
                f"{self.base_url}/valorant/series/{{serie_id_or_slug}}/teams/{{team_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("serie_id_or_slug", serie_id_or_slug)
            .add_path("team_id_or_slug", team_id_or_slug)
            .add_query("videogame_version", videogame_version)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return ValorantStatsForTeamBySerie._unmap(response)

    @cast_models
    def get_valorant_teams_team_id_or_slug_stats(
        self,
        team_id_or_slug: TeamIdOrSlug,
        videogame_version: VideogameVersionOrAll = None,
        from_: str = None,
        to: str = None,
    ) -> ValorantStatsForTeam:
        """Get a Valorant team stats by ID or slug

        :param team_id_or_slug: A team ID or slug
        :type team_id_or_slug: TeamIdOrSlug
        :param videogame_version: videogame_version, defaults to None
        :type videogame_version: VideogameVersionOrAll, optional
        :param from_: Filter out 'from' date, defaults to None
        :type from_: str, optional
        :param to: Filter out 'to' date, defaults to None
        :type to: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a Valorant team
        :rtype: ValorantStatsForTeam
        """

        Validator(TeamIdOrSlug).validate(team_id_or_slug)
        Validator(VideogameVersionOrAll).is_optional().validate(videogame_version)
        Validator(str).is_optional().validate(from_)
        Validator(str).is_optional().validate(to)

        serialized_request = (
            Serializer(
                f"{self.base_url}/valorant/teams/{{team_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("team_id_or_slug", team_id_or_slug)
            .add_query("videogame_version", videogame_version)
            .add_query("from", from_)
            .add_query("to", to)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return ValorantStatsForTeam._unmap(response)

    @cast_models
    def get_valorant_tournaments_tournament_id_or_slug_players_player_id_or_slug_stats(
        self,
        tournament_id_or_slug: TournamentIdOrSlug,
        player_id_or_slug: PlayerIdOrSlug,
        videogame_version: VideogameVersionOrAll = None,
    ) -> ValorantStatsForPlayerByTournament:
        """Get the aggregated player statistics for a Valorant tournament

        :param tournament_id_or_slug: A tournament ID or slug
        :type tournament_id_or_slug: TournamentIdOrSlug
        :param player_id_or_slug: A player ID or slug
        :type player_id_or_slug: PlayerIdOrSlug
        :param videogame_version: videogame_version, defaults to None
        :type videogame_version: VideogameVersionOrAll, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a Valorant player by tournament
        :rtype: ValorantStatsForPlayerByTournament
        """

        Validator(TournamentIdOrSlug).validate(tournament_id_or_slug)
        Validator(PlayerIdOrSlug).validate(player_id_or_slug)
        Validator(VideogameVersionOrAll).is_optional().validate(videogame_version)

        serialized_request = (
            Serializer(
                f"{self.base_url}/valorant/tournaments/{{tournament_id_or_slug}}/players/{{player_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("tournament_id_or_slug", tournament_id_or_slug)
            .add_path("player_id_or_slug", player_id_or_slug)
            .add_query("videogame_version", videogame_version)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return ValorantStatsForPlayerByTournament._unmap(response)

    @cast_models
    def get_valorant_tournaments_tournament_id_or_slug_teams_team_id_or_slug_stats(
        self,
        tournament_id_or_slug: TournamentIdOrSlug,
        team_id_or_slug: TeamIdOrSlug,
        videogame_version: VideogameVersionOrAll = None,
    ) -> ValorantStatsForTeamByTournament:
        """Get the aggregated team statistics for a Valorant tournament

        :param tournament_id_or_slug: A tournament ID or slug
        :type tournament_id_or_slug: TournamentIdOrSlug
        :param team_id_or_slug: A team ID or slug
        :type team_id_or_slug: TeamIdOrSlug
        :param videogame_version: videogame_version, defaults to None
        :type videogame_version: VideogameVersionOrAll, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of a Valorant team by tournament
        :rtype: ValorantStatsForTeamByTournament
        """

        Validator(TournamentIdOrSlug).validate(tournament_id_or_slug)
        Validator(TeamIdOrSlug).validate(team_id_or_slug)
        Validator(VideogameVersionOrAll).is_optional().validate(videogame_version)

        serialized_request = (
            Serializer(
                f"{self.base_url}/valorant/tournaments/{{tournament_id_or_slug}}/teams/{{team_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("tournament_id_or_slug", tournament_id_or_slug)
            .add_path("team_id_or_slug", team_id_or_slug)
            .add_query("videogame_version", videogame_version)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return ValorantStatsForTeamByTournament._unmap(response)
