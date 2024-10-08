# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.search_over_lo_l_runes_reforged import SearchOverLoLRunesReforged
from ..models.search_over_lo_l_runes import SearchOverLoLRunes
from ..models.search_over_lo_l_rune_paths import SearchOverLoLRunePaths
from ..models.range_over_lo_l_runes_reforged import RangeOverLoLRunesReforged
from ..models.range_over_lo_l_runes import RangeOverLoLRunes
from ..models.range_over_lo_l_rune_paths import RangeOverLoLRunePaths
from ..models.page import Page
from ..models.lo_l_rune_reforged import LoLRuneReforged
from ..models.lo_l_rune_path import LoLRunePath
from ..models.lo_l_rune import LoLRune
from ..models.filter_over_lo_l_runes_reforged import FilterOverLoLRunesReforged
from ..models.filter_over_lo_l_runes import FilterOverLoLRunes
from ..models.filter_over_lo_l_rune_paths import FilterOverLoLRunePaths


class LoLRunesService(BaseService):

    @cast_models
    def get_lol_runes(
        self,
        filter: FilterOverLoLRunes = None,
        range: RangeOverLoLRunes = None,
        sort: List[any] = None,
        search: SearchOverLoLRunes = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[LoLRune]:
        """List runes

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverLoLRunes, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverLoLRunes, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverLoLRunes, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of League-of-Legends runes
        :rtype: List[LoLRune]
        """

        Validator(FilterOverLoLRunes).is_optional().validate(filter)
        Validator(RangeOverLoLRunes).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverLoLRunes).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(f"{self.base_url}/lol/runes", self.get_default_headers())
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

        return [LoLRune._unmap(item) for item in response]

    @cast_models
    def get_lol_runes_reforged(
        self,
        filter: FilterOverLoLRunesReforged = None,
        range: RangeOverLoLRunesReforged = None,
        sort: List[any] = None,
        search: SearchOverLoLRunesReforged = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[LoLRuneReforged]:
        """List the latest version of League of Legends (reforged) runes

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverLoLRunesReforged, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverLoLRunesReforged, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverLoLRunesReforged, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of League-of-Legends (reforged) runes
        :rtype: List[LoLRuneReforged]
        """

        Validator(FilterOverLoLRunesReforged).is_optional().validate(filter)
        Validator(RangeOverLoLRunesReforged).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverLoLRunesReforged).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/lol/runes-reforged", self.get_default_headers()
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

        return [LoLRuneReforged._unmap(item) for item in response]

    @cast_models
    def get_lol_runes_reforged_paths(
        self,
        filter: FilterOverLoLRunePaths = None,
        range: RangeOverLoLRunePaths = None,
        sort: List[any] = None,
        search: SearchOverLoLRunePaths = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[LoLRunePath]:
        """List the latest version of League of Legends (reforged) rune paths

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverLoLRunePaths, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverLoLRunePaths, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverLoLRunePaths, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of League-of-Legends runes paths
        :rtype: List[LoLRunePath]
        """

        Validator(FilterOverLoLRunePaths).is_optional().validate(filter)
        Validator(RangeOverLoLRunePaths).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverLoLRunePaths).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/lol/runes-reforged-paths", self.get_default_headers()
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

        return [LoLRunePath._unmap(item) for item in response]

    @cast_models
    def get_lol_runes_reforged_paths_lol_rune_path_id(
        self, lol_rune_path_id: int
    ) -> LoLRunePath:
        """Retrieve the latest version of a League of Legends (reforged) rune path by its ID

        :param lol_rune_path_id: ID of the LoL rune path
        :type lol_rune_path_id: int
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A League-of-Legends runes path
        :rtype: LoLRunePath
        """

        Validator(int).min(1).validate(lol_rune_path_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/lol/runes-reforged-paths/{{lol_rune_path_id}}",
                self.get_default_headers(),
            )
            .add_path("lol_rune_path_id", lol_rune_path_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return LoLRunePath._unmap(response)

    @cast_models
    def get_lol_runes_reforged_lol_rune_reforged_id(
        self, lol_rune_reforged_id: int
    ) -> LoLRuneReforged:
        """Retrieve the latest version of a League of Legends (reforged) rune by its ID

        :param lol_rune_reforged_id: ID of the LoL rune
        :type lol_rune_reforged_id: int
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A League-of-Legends (reforged) rune
        :rtype: LoLRuneReforged
        """

        Validator(int).min(1).validate(lol_rune_reforged_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/lol/runes-reforged/{{lol_rune_reforged_id}}",
                self.get_default_headers(),
            )
            .add_path("lol_rune_reforged_id", lol_rune_reforged_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return LoLRuneReforged._unmap(response)

    @cast_models
    def get_lol_runes_lol_rune_id(self, lol_rune_id: int) -> LoLRune:
        """Get a single rune by ID

        :param lol_rune_id: A rune ID
        :type lol_rune_id: int
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A League-of-Legends rune
        :rtype: LoLRune
        """

        Validator(int).min(1).validate(lol_rune_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/lol/runes/{{lol_rune_id}}", self.get_default_headers()
            )
            .add_path("lol_rune_id", lol_rune_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return LoLRune._unmap(response)
