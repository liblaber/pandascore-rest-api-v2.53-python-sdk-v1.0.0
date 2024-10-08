# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.search_over_lo_l_items import SearchOverLoLItems
from ..models.range_over_lo_l_items import RangeOverLoLItems
from ..models.page import Page
from ..models.lo_l_item import LoLItem
from ..models.filter_over_lo_l_items import FilterOverLoLItems


class LoLItemsService(BaseService):

    @cast_models
    def get_lol_items(
        self,
        filter: FilterOverLoLItems = None,
        range: RangeOverLoLItems = None,
        sort: List[any] = None,
        search: SearchOverLoLItems = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[LoLItem]:
        """List items

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverLoLItems, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverLoLItems, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverLoLItems, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of League-of-Legends items
        :rtype: List[LoLItem]
        """

        Validator(FilterOverLoLItems).is_optional().validate(filter)
        Validator(RangeOverLoLItems).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverLoLItems).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(f"{self.base_url}/lol/items", self.get_default_headers())
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

        return [LoLItem._unmap(item) for item in response]

    @cast_models
    def get_lol_items_lol_item_id(self, lol_item_id: int) -> LoLItem:
        """Get a single item by ID or by slug

        :param lol_item_id: An item ID
        :type lol_item_id: int
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A League-of-Legends item
        :rtype: LoLItem
        """

        Validator(int).min(1).validate(lol_item_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/lol/items/{{lol_item_id}}", self.get_default_headers()
            )
            .add_path("lol_item_id", lol_item_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return LoLItem._unmap(response)

    @cast_models
    def get_lol_versions_all_items(
        self,
        filter: FilterOverLoLItems = None,
        range: RangeOverLoLItems = None,
        sort: List[any] = None,
        search: SearchOverLoLItems = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[LoLItem]:
        """Deprecated. Equivalent route: [/lol/items?filter[videogame_version]=all](/reference/get_lol_items)

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverLoLItems, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverLoLItems, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverLoLItems, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of League-of-Legends items
        :rtype: List[LoLItem]
        """

        Validator(FilterOverLoLItems).is_optional().validate(filter)
        Validator(RangeOverLoLItems).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverLoLItems).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/lol/versions/all/items", self.get_default_headers()
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

        return [LoLItem._unmap(item) for item in response]

    @cast_models
    def get_lol_versions_lol_version_name_items(
        self,
        lol_version_name: int,
        filter: FilterOverLoLItems = None,
        range: RangeOverLoLItems = None,
        sort: List[any] = None,
        search: SearchOverLoLItems = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[LoLItem]:
        """Deprecated. Equivalent route: [/lol/items?filter[videogame_version]={lol_version_name}](/reference/get_lol_items)

        :param lol_version_name: Video game version
        :type lol_version_name: int
        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverLoLItems, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverLoLItems, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverLoLItems, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of League-of-Legends items
        :rtype: List[LoLItem]
        """

        Validator(int).min(1).validate(lol_version_name)
        Validator(FilterOverLoLItems).is_optional().validate(filter)
        Validator(RangeOverLoLItems).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverLoLItems).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/lol/versions/{{lol_version_name}}/items",
                self.get_default_headers(),
            )
            .add_path("lol_version_name", lol_version_name)
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

        return [LoLItem._unmap(item) for item in response]
