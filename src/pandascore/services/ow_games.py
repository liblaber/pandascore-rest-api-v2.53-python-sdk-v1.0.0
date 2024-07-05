from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.search_over_ow_games import SearchOverOwGames
from ..models.range_over_ow_games import RangeOverOwGames
from ..models.page import Page
from ..models.ow_game import OwGame
from ..models.match_id_or_slug import MatchIdOrSlug
from ..models.filter_over_ow_games import FilterOverOwGames


class OwGamesService(BaseService):

    @cast_models
    def get_ow_games_ow_game_id(self, ow_game_id: int) -> OwGame:
        """Get a single Overwatch game by ID

        :param ow_game_id: An Overwatch game ID
        :type ow_game_id: int
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: An Overwatch game
        :rtype: OwGame
        """

        Validator(int).min(1).validate(ow_game_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/ow/games/{{ow_game_id}}", self.get_default_headers()
            )
            .add_path("ow_game_id", ow_game_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return OwGame._unmap(response)

    @cast_models
    def get_ow_matches_match_id_or_slug_games(
        self,
        match_id_or_slug: MatchIdOrSlug,
        filter: FilterOverOwGames = None,
        range: RangeOverOwGames = None,
        sort: List[any] = None,
        search: SearchOverOwGames = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[OwGame]:
        """List games for a given Overwatch match

        :param match_id_or_slug: A match ID or slug
        :type match_id_or_slug: MatchIdOrSlug
        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverOwGames, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverOwGames, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverOwGames, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Overwatch games
        :rtype: List[OwGame]
        """

        Validator(MatchIdOrSlug).validate(match_id_or_slug)
        Validator(FilterOverOwGames).is_optional().validate(filter)
        Validator(RangeOverOwGames).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverOwGames).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/ow/matches/{{match_id_or_slug}}/games",
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

        return [OwGame._unmap(item) for item in response]
