from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.search_over_dota2_players import SearchOverDota2Players
from ..models.range_over_dota2_players import RangeOverDota2Players
from ..models.player import Player
from ..models.page import Page
from ..models.filter_over_dota2_players import FilterOverDota2Players


class Dota2PlayersService(BaseService):

    @cast_models
    def get_dota2_players(
        self,
        filter: FilterOverDota2Players = None,
        range: RangeOverDota2Players = None,
        sort: List[any] = None,
        search: SearchOverDota2Players = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[Player]:
        """List players for the Dota 2 videogame

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverDota2Players, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverDota2Players, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverDota2Players, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Dota2 players
        :rtype: List[Player]
        """

        Validator(FilterOverDota2Players).is_optional().validate(filter)
        Validator(RangeOverDota2Players).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverDota2Players).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(f"{self.base_url}/dota2/players", self.get_default_headers())
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

        return [Player._unmap(item) for item in response]
