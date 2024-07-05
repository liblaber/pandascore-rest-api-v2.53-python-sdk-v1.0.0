from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.search_over_ow_heroes import SearchOverOwHeroes
from ..models.range_over_ow_heroes import RangeOverOwHeroes
from ..models.page import Page
from ..models.ow_hero_id_or_slug import OwHeroIdOrSlug
from ..models.ow_hero import OwHero
from ..models.filter_over_ow_heroes import FilterOverOwHeroes


class OwHeroesService(BaseService):

    @cast_models
    def get_ow_heroes(
        self,
        filter: FilterOverOwHeroes = None,
        range: RangeOverOwHeroes = None,
        sort: List[any] = None,
        search: SearchOverOwHeroes = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[OwHero]:
        """List heroes

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverOwHeroes, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverOwHeroes, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverOwHeroes, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Overwatch heroes
        :rtype: List[OwHero]
        """

        Validator(FilterOverOwHeroes).is_optional().validate(filter)
        Validator(RangeOverOwHeroes).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverOwHeroes).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(f"{self.base_url}/ow/heroes", self.get_default_headers())
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

        return [OwHero._unmap(item) for item in response]

    @cast_models
    def get_ow_heroes_ow_hero_id_or_slug(
        self, ow_hero_id_or_slug: OwHeroIdOrSlug
    ) -> OwHero:
        """Get a single hero by ID or by slug

        :param ow_hero_id_or_slug: A hero ID or slug
        :type ow_hero_id_or_slug: OwHeroIdOrSlug
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: An Overwatch hero
        :rtype: OwHero
        """

        Validator(OwHeroIdOrSlug).validate(ow_hero_id_or_slug)

        serialized_request = (
            Serializer(
                f"{self.base_url}/ow/heroes/{{ow_hero_id_or_slug}}",
                self.get_default_headers(),
            )
            .add_path("ow_hero_id_or_slug", ow_hero_id_or_slug)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return OwHero._unmap(response)
