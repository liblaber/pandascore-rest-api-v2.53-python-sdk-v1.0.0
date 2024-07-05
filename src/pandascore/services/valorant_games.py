from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.valorant_game_event import ValorantGameEvent, ValorantGameEventGuard
from ..models.valorant_game import ValorantGame
from ..models.valorant_full_round import ValorantFullRound
from ..models.utils.cast_models import cast_models
from ..models.search_over_valorant_games import SearchOverValorantGames
from ..models.range_over_valorant_games import RangeOverValorantGames
from ..models.page import Page
from ..models.match_id_or_slug import MatchIdOrSlug
from ..models.filter_over_valorant_games import FilterOverValorantGames


class ValorantGamesService(BaseService):

    @cast_models
    def get_valorant_games_valorant_game_id(
        self, valorant_game_id: int
    ) -> ValorantGame:
        """Get a single Valorant game by ID

        :param valorant_game_id: A Valorant game ID
        :type valorant_game_id: int
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A Valorant game
        :rtype: ValorantGame
        """

        Validator(int).min(1).validate(valorant_game_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/valorant/games/{{valorant_game_id}}",
                self.get_default_headers(),
            )
            .add_path("valorant_game_id", valorant_game_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return ValorantGame._unmap(response)

    @cast_models
    def get_valorant_games_valorant_game_id_events(
        self, valorant_game_id: int, page: Page = None, per_page: int = None
    ) -> List[ValorantGameEvent]:
        """List events for a given Valorant game

        :param valorant_game_id: A Valorant game ID
        :type valorant_game_id: int
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Valorant game events
        :rtype: List[ValorantGameEvent]
        """

        Validator(int).min(1).validate(valorant_game_id)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/valorant/games/{{valorant_game_id}}/events",
                self.get_default_headers(),
            )
            .add_path("valorant_game_id", valorant_game_id)
            .add_query("page", page)
            .add_query("per_page", per_page)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return [ValorantGameEventGuard.return_one_of(item) for item in response]

    @cast_models
    def get_valorant_games_valorant_game_id_rounds(
        self, valorant_game_id: int, page: Page = None, per_page: int = None
    ) -> List[ValorantFullRound]:
        """List rounds in a Valorant game

        :param valorant_game_id: A Valorant game ID
        :type valorant_game_id: int
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Valorant game rounds
        :rtype: List[ValorantFullRound]
        """

        Validator(int).min(1).validate(valorant_game_id)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/valorant/games/{{valorant_game_id}}/rounds",
                self.get_default_headers(),
            )
            .add_path("valorant_game_id", valorant_game_id)
            .add_query("page", page)
            .add_query("per_page", per_page)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return [ValorantFullRound._unmap(item) for item in response]

    @cast_models
    def get_valorant_matches_match_id_or_slug_games(
        self,
        match_id_or_slug: MatchIdOrSlug,
        filter: FilterOverValorantGames = None,
        range: RangeOverValorantGames = None,
        sort: List[any] = None,
        search: SearchOverValorantGames = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[ValorantGame]:
        """List games for a given Valorant match

        :param match_id_or_slug: A match ID or slug
        :type match_id_or_slug: MatchIdOrSlug
        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverValorantGames, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverValorantGames, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverValorantGames, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Valorant games
        :rtype: List[ValorantGame]
        """

        Validator(MatchIdOrSlug).validate(match_id_or_slug)
        Validator(FilterOverValorantGames).is_optional().validate(filter)
        Validator(RangeOverValorantGames).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverValorantGames).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/valorant/matches/{{match_id_or_slug}}/games",
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

        return [ValorantGame._unmap(item) for item in response]
