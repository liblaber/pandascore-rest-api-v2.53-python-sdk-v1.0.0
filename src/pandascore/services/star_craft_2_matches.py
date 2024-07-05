from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.search_over_starcraft2_matches import SearchOverStarcraft2Matches
from ..models.range_over_starcraft2_matches import RangeOverStarcraft2Matches
from ..models.page import Page
from ..models.match import Match
from ..models.filter_over_starcraft2_matches import FilterOverStarcraft2Matches


class StarCraft2MatchesService(BaseService):

    @cast_models
    def get_starcraft_2_matches(
        self,
        filter: FilterOverStarcraft2Matches = None,
        range: RangeOverStarcraft2Matches = None,
        sort: List[any] = None,
        search: SearchOverStarcraft2Matches = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[Match]:
        """List matches for the StarCraft 2 videogame

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverStarcraft2Matches, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverStarcraft2Matches, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverStarcraft2Matches, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of StarCraft 2 matches
        :rtype: List[Match]
        """

        Validator(FilterOverStarcraft2Matches).is_optional().validate(filter)
        Validator(RangeOverStarcraft2Matches).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverStarcraft2Matches).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/starcraft-2/matches", self.get_default_headers()
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

        return [Match._unmap(item) for item in response]

    @cast_models
    def get_starcraft_2_matches_past(
        self,
        filter: FilterOverStarcraft2Matches = None,
        range: RangeOverStarcraft2Matches = None,
        sort: List[any] = None,
        search: SearchOverStarcraft2Matches = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[Match]:
        """List past StarCraft 2 matches

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverStarcraft2Matches, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverStarcraft2Matches, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverStarcraft2Matches, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of StarCraft 2 matches
        :rtype: List[Match]
        """

        Validator(FilterOverStarcraft2Matches).is_optional().validate(filter)
        Validator(RangeOverStarcraft2Matches).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverStarcraft2Matches).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/starcraft-2/matches/past", self.get_default_headers()
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

        return [Match._unmap(item) for item in response]

    @cast_models
    def get_starcraft_2_matches_running(
        self,
        filter: FilterOverStarcraft2Matches = None,
        range: RangeOverStarcraft2Matches = None,
        sort: List[any] = None,
        search: SearchOverStarcraft2Matches = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[Match]:
        """List running StarCraft 2 matches

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverStarcraft2Matches, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverStarcraft2Matches, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverStarcraft2Matches, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of StarCraft 2 matches
        :rtype: List[Match]
        """

        Validator(FilterOverStarcraft2Matches).is_optional().validate(filter)
        Validator(RangeOverStarcraft2Matches).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverStarcraft2Matches).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/starcraft-2/matches/running",
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

        return [Match._unmap(item) for item in response]

    @cast_models
    def get_starcraft_2_matches_upcoming(
        self,
        filter: FilterOverStarcraft2Matches = None,
        range: RangeOverStarcraft2Matches = None,
        sort: List[any] = None,
        search: SearchOverStarcraft2Matches = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[Match]:
        """List upcoming StarCraft 2 matches

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverStarcraft2Matches, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverStarcraft2Matches, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverStarcraft2Matches, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of StarCraft 2 matches
        :rtype: List[Match]
        """

        Validator(FilterOverStarcraft2Matches).is_optional().validate(filter)
        Validator(RangeOverStarcraft2Matches).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverStarcraft2Matches).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/starcraft-2/matches/upcoming",
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

        return [Match._unmap(item) for item in response]
