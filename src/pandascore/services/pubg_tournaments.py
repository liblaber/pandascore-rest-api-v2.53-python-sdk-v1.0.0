from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.short_tournament import ShortTournament
from ..models.search_over_pubg_short_tournaments import SearchOverPubgShortTournaments
from ..models.range_over_pubg_short_tournaments import RangeOverPubgShortTournaments
from ..models.page import Page
from ..models.filter_over_pubg_short_tournaments import FilterOverPubgShortTournaments


class PubgTournamentsService(BaseService):

    @cast_models
    def get_pubg_tournaments(
        self,
        filter: FilterOverPubgShortTournaments = None,
        range: RangeOverPubgShortTournaments = None,
        sort: List[any] = None,
        search: SearchOverPubgShortTournaments = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[ShortTournament]:
        """List tournaments for the PUBG videogame

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverPubgShortTournaments, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverPubgShortTournaments, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverPubgShortTournaments, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of PlayerUnknown's Battlegrounds tournaments
        :rtype: List[ShortTournament]
        """

        Validator(FilterOverPubgShortTournaments).is_optional().validate(filter)
        Validator(RangeOverPubgShortTournaments).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverPubgShortTournaments).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(f"{self.base_url}/pubg/tournaments", self.get_default_headers())
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

        return [ShortTournament._unmap(item) for item in response]

    @cast_models
    def get_pubg_tournaments_past(
        self,
        filter: FilterOverPubgShortTournaments = None,
        range: RangeOverPubgShortTournaments = None,
        sort: List[any] = None,
        search: SearchOverPubgShortTournaments = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[ShortTournament]:
        """List past PUBG tournaments

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverPubgShortTournaments, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverPubgShortTournaments, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverPubgShortTournaments, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of PlayerUnknown's Battlegrounds tournaments
        :rtype: List[ShortTournament]
        """

        Validator(FilterOverPubgShortTournaments).is_optional().validate(filter)
        Validator(RangeOverPubgShortTournaments).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverPubgShortTournaments).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/pubg/tournaments/past", self.get_default_headers()
            )
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

        return [ShortTournament._unmap(item) for item in response]

    @cast_models
    def get_pubg_tournaments_running(
        self,
        filter: FilterOverPubgShortTournaments = None,
        range: RangeOverPubgShortTournaments = None,
        sort: List[any] = None,
        search: SearchOverPubgShortTournaments = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[ShortTournament]:
        """List running PUBG tournaments

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverPubgShortTournaments, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverPubgShortTournaments, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverPubgShortTournaments, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of PlayerUnknown's Battlegrounds tournaments
        :rtype: List[ShortTournament]
        """

        Validator(FilterOverPubgShortTournaments).is_optional().validate(filter)
        Validator(RangeOverPubgShortTournaments).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverPubgShortTournaments).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/pubg/tournaments/running", self.get_default_headers()
            )
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

        return [ShortTournament._unmap(item) for item in response]

    @cast_models
    def get_pubg_tournaments_upcoming(
        self,
        filter: FilterOverPubgShortTournaments = None,
        range: RangeOverPubgShortTournaments = None,
        sort: List[any] = None,
        search: SearchOverPubgShortTournaments = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[ShortTournament]:
        """List upcoming PUBG tournaments

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverPubgShortTournaments, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverPubgShortTournaments, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverPubgShortTournaments, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of PlayerUnknown's Battlegrounds tournaments
        :rtype: List[ShortTournament]
        """

        Validator(FilterOverPubgShortTournaments).is_optional().validate(filter)
        Validator(RangeOverPubgShortTournaments).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverPubgShortTournaments).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/pubg/tournaments/upcoming", self.get_default_headers()
            )
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

        return [ShortTournament._unmap(item) for item in response]
