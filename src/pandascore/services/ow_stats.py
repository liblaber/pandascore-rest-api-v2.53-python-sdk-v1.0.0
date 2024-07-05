from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.tournament_id_or_slug import TournamentIdOrSlug
from ..models.serie_id_or_slug import SerieIdOrSlug
from ..models.player_id_or_slug import PlayerIdOrSlug
from ..models.ow_stats_for_player_by_tournament import OwStatsForPlayerByTournament
from ..models.ow_stats_for_player_by_serie import OwStatsForPlayerBySerie
from ..models.ow_stats_for_player_by_match import OwStatsForPlayerByMatch
from ..models.ow_stats_for_player_by_game import OwStatsForPlayerByGame
from ..models.ow_stats_for_player import OwStatsForPlayer
from ..models.ow_stats_for_all_players_by_match import OwStatsForAllPlayersByMatch
from ..models.match_id_or_slug import MatchIdOrSlug


class OwStatsService(BaseService):

    @cast_models
    def get_ow_games_ow_game_id_players_player_id_or_slug_stats(
        self, ow_game_id: int, player_id_or_slug: PlayerIdOrSlug
    ) -> OwStatsForPlayerByGame:
        """Get detailed statistics of a given Overwatch given player for the given game

        :param ow_game_id: An Overwatch game ID
        :type ow_game_id: int
        :param player_id_or_slug: A player ID or slug
        :type player_id_or_slug: PlayerIdOrSlug
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of an Overwatch player by game
        :rtype: OwStatsForPlayerByGame
        """

        Validator(int).min(1).validate(ow_game_id)
        Validator(PlayerIdOrSlug).validate(player_id_or_slug)

        serialized_request = (
            Serializer(
                f"{self.base_url}/ow/games/{{ow_game_id}}/players/{{player_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("ow_game_id", ow_game_id)
            .add_path("player_id_or_slug", player_id_or_slug)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return OwStatsForPlayerByGame._unmap(response)

    @cast_models
    def get_ow_matches_match_id_or_slug_players_stats(
        self, match_id_or_slug: MatchIdOrSlug
    ) -> OwStatsForAllPlayersByMatch:
        """Get detailed statistics of Overwatch players for the given match

        :param match_id_or_slug: A match ID or slug
        :type match_id_or_slug: MatchIdOrSlug
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of all Overwatch players by match
        :rtype: OwStatsForAllPlayersByMatch
        """

        Validator(MatchIdOrSlug).validate(match_id_or_slug)

        serialized_request = (
            Serializer(
                f"{self.base_url}/ow/matches/{{match_id_or_slug}}/players/stats",
                self.get_default_headers(),
            )
            .add_path("match_id_or_slug", match_id_or_slug)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return OwStatsForAllPlayersByMatch._unmap(response)

    @cast_models
    def get_ow_matches_match_id_or_slug_players_player_id_or_slug_stats(
        self, match_id_or_slug: MatchIdOrSlug, player_id_or_slug: PlayerIdOrSlug
    ) -> OwStatsForPlayerByMatch:
        """Get detailed statistics of a given Overwatch given player for the given match

        :param match_id_or_slug: A match ID or slug
        :type match_id_or_slug: MatchIdOrSlug
        :param player_id_or_slug: A player ID or slug
        :type player_id_or_slug: PlayerIdOrSlug
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of an Overwatch player by match
        :rtype: OwStatsForPlayerByMatch
        """

        Validator(MatchIdOrSlug).validate(match_id_or_slug)
        Validator(PlayerIdOrSlug).validate(player_id_or_slug)

        serialized_request = (
            Serializer(
                f"{self.base_url}/ow/matches/{{match_id_or_slug}}/players/{{player_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("match_id_or_slug", match_id_or_slug)
            .add_path("player_id_or_slug", player_id_or_slug)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return OwStatsForPlayerByMatch._unmap(response)

    @cast_models
    def get_ow_players_player_id_or_slug_stats(
        self, player_id_or_slug: PlayerIdOrSlug, from_: str = None, to: str = None
    ) -> OwStatsForPlayer:
        """Get detailed statistics of a given Overwatch player

        :param player_id_or_slug: A player ID or slug
        :type player_id_or_slug: PlayerIdOrSlug
        :param from_: Filter out 'from' date, defaults to None
        :type from_: str, optional
        :param to: Filter out 'to' date, defaults to None
        :type to: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of an Overwatch player
        :rtype: OwStatsForPlayer
        """

        Validator(PlayerIdOrSlug).validate(player_id_or_slug)
        Validator(str).is_optional().validate(from_)
        Validator(str).is_optional().validate(to)

        serialized_request = (
            Serializer(
                f"{self.base_url}/ow/players/{{player_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("player_id_or_slug", player_id_or_slug)
            .add_query("from", from_)
            .add_query("to", to)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return OwStatsForPlayer._unmap(response)

    @cast_models
    def get_ow_series_serie_id_or_slug_players_player_id_or_slug_stats(
        self, serie_id_or_slug: SerieIdOrSlug, player_id_or_slug: PlayerIdOrSlug
    ) -> OwStatsForPlayerBySerie:
        """Get detailed statistics of a given Overwatch given player for the given serie

        :param serie_id_or_slug: A serie ID or slug
        :type serie_id_or_slug: SerieIdOrSlug
        :param player_id_or_slug: A player ID or slug
        :type player_id_or_slug: PlayerIdOrSlug
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of an Overwatch player by serie
        :rtype: OwStatsForPlayerBySerie
        """

        Validator(SerieIdOrSlug).validate(serie_id_or_slug)
        Validator(PlayerIdOrSlug).validate(player_id_or_slug)

        serialized_request = (
            Serializer(
                f"{self.base_url}/ow/series/{{serie_id_or_slug}}/players/{{player_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("serie_id_or_slug", serie_id_or_slug)
            .add_path("player_id_or_slug", player_id_or_slug)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return OwStatsForPlayerBySerie._unmap(response)

    @cast_models
    def get_ow_tournaments_tournament_id_or_slug_players_player_id_or_slug_stats(
        self,
        tournament_id_or_slug: TournamentIdOrSlug,
        player_id_or_slug: PlayerIdOrSlug,
    ) -> OwStatsForPlayerByTournament:
        """Get detailed statistics of a given Overwatch player for the given tournament

        :param tournament_id_or_slug: A tournament ID or slug
        :type tournament_id_or_slug: TournamentIdOrSlug
        :param player_id_or_slug: A player ID or slug
        :type player_id_or_slug: PlayerIdOrSlug
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Statistics of an Overwatch player by tournament
        :rtype: OwStatsForPlayerByTournament
        """

        Validator(TournamentIdOrSlug).validate(tournament_id_or_slug)
        Validator(PlayerIdOrSlug).validate(player_id_or_slug)

        serialized_request = (
            Serializer(
                f"{self.base_url}/ow/tournaments/{{tournament_id_or_slug}}/players/{{player_id_or_slug}}/stats",
                self.get_default_headers(),
            )
            .add_path("tournament_id_or_slug", tournament_id_or_slug)
            .add_path("player_id_or_slug", player_id_or_slug)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return OwStatsForPlayerByTournament._unmap(response)
