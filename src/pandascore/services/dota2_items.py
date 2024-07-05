from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.search_over_dota2_items import SearchOverDota2Items
from ..models.range_over_dota2_items import RangeOverDota2Items
from ..models.page import Page
from ..models.filter_over_dota2_items import FilterOverDota2Items
from ..models.dota2_item_id_or_slug import Dota2ItemIdOrSlug
from ..models.dota2_item import Dota2Item


class Dota2ItemsService(BaseService):

    @cast_models
    def get_dota2_items(
        self,
        filter: FilterOverDota2Items = None,
        range: RangeOverDota2Items = None,
        sort: List[any] = None,
        search: SearchOverDota2Items = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[Dota2Item]:
        """List items

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverDota2Items, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverDota2Items, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverDota2Items, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Dota2 items
        :rtype: List[Dota2Item]
        """

        Validator(FilterOverDota2Items).is_optional().validate(filter)
        Validator(RangeOverDota2Items).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverDota2Items).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(f"{self.base_url}/dota2/items", self.get_default_headers())
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

        return [Dota2Item._unmap(item) for item in response]

    @cast_models
    def get_dota2_items_dota2_item_id_or_slug(
        self, dota2_item_id_or_slug: Dota2ItemIdOrSlug
    ) -> Dota2Item:
        """Get a single item by ID or by slug

        :param dota2_item_id_or_slug: An item ID or slug
        :type dota2_item_id_or_slug: Dota2ItemIdOrSlug
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A Dota2 item
        :rtype: Dota2Item
        """

        Validator(Dota2ItemIdOrSlug).validate(dota2_item_id_or_slug)

        serialized_request = (
            Serializer(
                f"{self.base_url}/dota2/items/{{dota2_item_id_or_slug}}",
                self.get_default_headers(),
            )
            .add_path("dota2_item_id_or_slug", dota2_item_id_or_slug)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return Dota2Item._unmap(response)
