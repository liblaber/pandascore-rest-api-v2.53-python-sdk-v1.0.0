from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.team_id_or_slug import TeamIdOrSlug
from ..models.search_over_lo_l_team_last_games import SearchOverLoLTeamLastGames
from ..models.search_over_lo_l_games import SearchOverLoLGames
from ..models.range_over_lo_l_team_last_games import RangeOverLoLTeamLastGames
from ..models.range_over_lo_l_games import RangeOverLoLGames
from ..models.page import Page
from ..models.match_id_or_slug import MatchIdOrSlug
from ..models.lo_l_team_last_game import LoLTeamLastGame
from ..models.lo_l_game_frame import LoLGameFrame
from ..models.lo_l_game_event import LoLGameEvent
from ..models.lo_l_game import LoLGame
from ..models.filter_over_lo_l_team_last_games import FilterOverLoLTeamLastGames
from ..models.filter_over_lo_l_games import FilterOverLoLGames


class LoLGamesService(BaseService):

    @cast_models
    def get_lol_games_lol_game_id(self, lol_game_id: int) -> LoLGame:
        """Get a single League of Legends game by ID

        :param lol_game_id: A LoL game ID
        :type lol_game_id: int
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A League-of-Legends game
        :rtype: LoLGame
        """

        Validator(int).min(1).validate(lol_game_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/lol/games/{{lol_game_id}}", self.get_default_headers()
            )
            .add_path("lol_game_id", lol_game_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return LoLGame._unmap(response)

    @cast_models
    def get_lol_games_lol_game_id_events(
        self, lol_game_id: int, page: Page = None, per_page: int = None
    ) -> List[LoLGameEvent]:
        """List events for a given League of Legends game

        :param lol_game_id: A LoL game ID
        :type lol_game_id: int
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of League-of-Legends game events
        :rtype: List[LoLGameEvent]
        """

        Validator(int).min(1).validate(lol_game_id)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/lol/games/{{lol_game_id}}/events",
                self.get_default_headers(),
            )
            .add_path("lol_game_id", lol_game_id)
            .add_query("page", page)
            .add_query("per_page", per_page)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return [LoLGameEvent._unmap(item) for item in response]

    @cast_models
    def get_lol_games_lol_game_id_frames(
        self, lol_game_id: int, page: Page = None, per_page: int = None
    ) -> List[LoLGameFrame]:
        """List frames for a given League of Legends game

        :param lol_game_id: A LoL game ID
        :type lol_game_id: int
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of League-of-Legends game frames
        :rtype: List[LoLGameFrame]
        """

        Validator(int).min(1).validate(lol_game_id)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/lol/games/{{lol_game_id}}/frames",
                self.get_default_headers(),
            )
            .add_path("lol_game_id", lol_game_id)
            .add_query("page", page)
            .add_query("per_page", per_page)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return [LoLGameFrame._unmap(item) for item in response]

    @cast_models
    def get_lol_matches_match_id_or_slug_games(
        self,
        match_id_or_slug: MatchIdOrSlug,
        filter: FilterOverLoLGames = None,
        range: RangeOverLoLGames = None,
        sort: List[any] = None,
        search: SearchOverLoLGames = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[LoLGame]:
        """List games for a given League of Legends match

        :param match_id_or_slug: A match ID or slug
        :type match_id_or_slug: MatchIdOrSlug
        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverLoLGames, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverLoLGames, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverLoLGames, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of League-of-Legends games
        :rtype: List[LoLGame]
        """

        Validator(MatchIdOrSlug).validate(match_id_or_slug)
        Validator(FilterOverLoLGames).is_optional().validate(filter)
        Validator(RangeOverLoLGames).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverLoLGames).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/lol/matches/{{match_id_or_slug}}/games",
                self.get_default_headers(),
            )
            .add_path("match_id_or_slug", match_id_or_slug)
            .add_query("filter", filter, style="deepObject")
            .add_query("range", range, style="deepObject")
            .add_query("sort", sort)
            .add_query("search", search, style="deepObject")
            .add_query("page", page)
            .add_query("per_page", per_page)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return [LoLGame._unmap(item) for item in response]

    @cast_models
    def get_lol_teams_team_id_or_slug_games(
        self,
        team_id_or_slug: TeamIdOrSlug,
        filter: FilterOverLoLTeamLastGames = None,
        range: RangeOverLoLTeamLastGames = None,
        sort: List[any] = None,
        search: SearchOverLoLTeamLastGames = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[LoLTeamLastGame]:
        """List finished games for a given League of Legends team

        :param team_id_or_slug: A team ID or slug
        :type team_id_or_slug: TeamIdOrSlug
        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverLoLTeamLastGames, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverLoLTeamLastGames, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverLoLTeamLastGames, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of League-of-Legends games
        :rtype: List[LoLTeamLastGame]
        """

        Validator(TeamIdOrSlug).validate(team_id_or_slug)
        Validator(FilterOverLoLTeamLastGames).is_optional().validate(filter)
        Validator(RangeOverLoLTeamLastGames).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverLoLTeamLastGames).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/lol/teams/{{team_id_or_slug}}/games",
                self.get_default_headers(),
            )
            .add_path("team_id_or_slug", team_id_or_slug)
            .add_query("filter", filter, style="deepObject")
            .add_query("range", range, style="deepObject")
            .add_query("sort", sort)
            .add_query("search", search, style="deepObject")
            .add_query("page", page)
            .add_query("per_page", per_page)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return [LoLTeamLastGame._unmap(item) for item in response]
