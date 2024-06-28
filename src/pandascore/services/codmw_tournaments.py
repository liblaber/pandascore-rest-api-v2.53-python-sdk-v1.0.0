# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.short_tournament import ShortTournament
from ..models.search_over_codmw_short_tournaments import SearchOverCodmwShortTournaments
from ..models.range_over_codmw_short_tournaments import RangeOverCodmwShortTournaments
from ..models.get_codmw_tournaments_upcoming_page import GetCodmwTournamentsUpcomingPage
from ..models.get_codmw_tournaments_running_page import GetCodmwTournamentsRunningPage
from ..models.get_codmw_tournaments_past_page import GetCodmwTournamentsPastPage
from ..models.get_codmw_tournaments_page import GetCodmwTournamentsPage
from ..models.filter_over_codmw_short_tournaments import FilterOverCodmwShortTournaments


class CodmwTournamentsService(BaseService):

    @cast_models
    def get_codmw_tournaments(
        self,
        filter: FilterOverCodmwShortTournaments = None,
        range: RangeOverCodmwShortTournaments = None,
        sort: List[any] = None,
        search: SearchOverCodmwShortTournaments = None,
        page: GetCodmwTournamentsPage = None,
        per_page: int = None,
    ) -> List[ShortTournament]:
        """List tournaments for the CODMW videogame

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverCodmwShortTournaments, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverCodmwShortTournaments, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverCodmwShortTournaments, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: GetCodmwTournamentsPage, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Call of Duty Modern Warfare tournaments
        :rtype: List[ShortTournament]
        """

        Validator(FilterOverCodmwShortTournaments).is_optional().validate(filter)
        Validator(RangeOverCodmwShortTournaments).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverCodmwShortTournaments).is_optional().validate(search)
        Validator(GetCodmwTournamentsPage).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(f"{self.base_url}/codmw/tournaments", self.get_default_headers())
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
    def get_codmw_tournaments_past(
        self,
        filter: FilterOverCodmwShortTournaments = None,
        range: RangeOverCodmwShortTournaments = None,
        sort: List[any] = None,
        search: SearchOverCodmwShortTournaments = None,
        page: GetCodmwTournamentsPastPage = None,
        per_page: int = None,
    ) -> List[ShortTournament]:
        """List past CODMW tournaments

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverCodmwShortTournaments, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverCodmwShortTournaments, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverCodmwShortTournaments, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: GetCodmwTournamentsPastPage, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Call of Duty Modern Warfare tournaments
        :rtype: List[ShortTournament]
        """

        Validator(FilterOverCodmwShortTournaments).is_optional().validate(filter)
        Validator(RangeOverCodmwShortTournaments).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverCodmwShortTournaments).is_optional().validate(search)
        Validator(GetCodmwTournamentsPastPage).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/codmw/tournaments/past", self.get_default_headers()
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
    def get_codmw_tournaments_running(
        self,
        filter: FilterOverCodmwShortTournaments = None,
        range: RangeOverCodmwShortTournaments = None,
        sort: List[any] = None,
        search: SearchOverCodmwShortTournaments = None,
        page: GetCodmwTournamentsRunningPage = None,
        per_page: int = None,
    ) -> List[ShortTournament]:
        """List running CODMW tournaments

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverCodmwShortTournaments, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverCodmwShortTournaments, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverCodmwShortTournaments, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: GetCodmwTournamentsRunningPage, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Call of Duty Modern Warfare tournaments
        :rtype: List[ShortTournament]
        """

        Validator(FilterOverCodmwShortTournaments).is_optional().validate(filter)
        Validator(RangeOverCodmwShortTournaments).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverCodmwShortTournaments).is_optional().validate(search)
        Validator(GetCodmwTournamentsRunningPage).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/codmw/tournaments/running", self.get_default_headers()
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
    def get_codmw_tournaments_upcoming(
        self,
        filter: FilterOverCodmwShortTournaments = None,
        range: RangeOverCodmwShortTournaments = None,
        sort: List[any] = None,
        search: SearchOverCodmwShortTournaments = None,
        page: GetCodmwTournamentsUpcomingPage = None,
        per_page: int = None,
    ) -> List[ShortTournament]:
        """List upcoming CODMW tournaments

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverCodmwShortTournaments, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverCodmwShortTournaments, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverCodmwShortTournaments, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: GetCodmwTournamentsUpcomingPage, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Call of Duty Modern Warfare tournaments
        :rtype: List[ShortTournament]
        """

        Validator(FilterOverCodmwShortTournaments).is_optional().validate(filter)
        Validator(RangeOverCodmwShortTournaments).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverCodmwShortTournaments).is_optional().validate(search)
        Validator(GetCodmwTournamentsUpcomingPage).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/codmw/tournaments/upcoming",
                self.get_default_headers(),
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
