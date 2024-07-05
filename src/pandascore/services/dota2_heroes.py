from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.search_over_dota2_heroes import SearchOverDota2Heroes
from ..models.range_over_dota2_heroes import RangeOverDota2Heroes
from ..models.page import Page
from ..models.filter_over_dota2_heroes import FilterOverDota2Heroes
from ..models.dota2_hero_id_or_slug import Dota2HeroIdOrSlug
from ..models.dota2_hero import Dota2Hero


class Dota2HeroesService(BaseService):

    @cast_models
    def get_dota2_heroes(
        self,
        filter: FilterOverDota2Heroes = None,
        range: RangeOverDota2Heroes = None,
        sort: List[any] = None,
        search: SearchOverDota2Heroes = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[Dota2Hero]:
        """List heroes

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverDota2Heroes, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverDota2Heroes, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverDota2Heroes, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Dota2 heroes
        :rtype: List[Dota2Hero]
        """

        Validator(FilterOverDota2Heroes).is_optional().validate(filter)
        Validator(RangeOverDota2Heroes).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverDota2Heroes).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(f"{self.base_url}/dota2/heroes", self.get_default_headers())
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

        return [Dota2Hero._unmap(item) for item in response]

    @cast_models
    def get_dota2_heroes_dota2_hero_id_or_slug(
        self, dota2_hero_id_or_slug: Dota2HeroIdOrSlug
    ) -> Dota2Hero:
        """Get a single hero by ID or by slug

        :param dota2_hero_id_or_slug: A hero ID or slug
        :type dota2_hero_id_or_slug: Dota2HeroIdOrSlug
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A Dota2 hero
        :rtype: Dota2Hero
        """

        Validator(Dota2HeroIdOrSlug).validate(dota2_hero_id_or_slug)

        serialized_request = (
            Serializer(
                f"{self.base_url}/dota2/heroes/{{dota2_hero_id_or_slug}}",
                self.get_default_headers(),
            )
            .add_path("dota2_hero_id_or_slug", dota2_hero_id_or_slug)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return Dota2Hero._unmap(response)
