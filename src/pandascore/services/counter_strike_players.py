from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.search_over_csgo_players import SearchOverCsgoPlayers
from ..models.range_over_csgo_players import RangeOverCsgoPlayers
from ..models.player import Player
from ..models.page import Page
from ..models.filter_over_csgo_players import FilterOverCsgoPlayers


class CounterStrikePlayersService(BaseService):

    @cast_models
    def get_csgo_players(
        self,
        filter: FilterOverCsgoPlayers = None,
        range: RangeOverCsgoPlayers = None,
        sort: List[any] = None,
        search: SearchOverCsgoPlayers = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[Player]:
        """List players for the Counter-Strike videogame

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverCsgoPlayers, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverCsgoPlayers, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverCsgoPlayers, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Counter-Strike players
        :rtype: List[Player]
        """

        Validator(FilterOverCsgoPlayers).is_optional().validate(filter)
        Validator(RangeOverCsgoPlayers).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverCsgoPlayers).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(f"{self.base_url}/csgo/players", self.get_default_headers())
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
