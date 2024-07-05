from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.search_over_dota2_abilities import SearchOverDota2Abilities
from ..models.range_over_dota2_abilities import RangeOverDota2Abilities
from ..models.page import Page
from ..models.filter_over_dota2_abilities import FilterOverDota2Abilities
from ..models.dota2_ability_id_or_slug import Dota2AbilityIdOrSlug
from ..models.dota2_ability import Dota2Ability


class Dota2AbilitiesService(BaseService):

    @cast_models
    def get_dota2_abilities(
        self,
        filter: FilterOverDota2Abilities = None,
        range: RangeOverDota2Abilities = None,
        sort: List[any] = None,
        search: SearchOverDota2Abilities = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[Dota2Ability]:
        """List abilities

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverDota2Abilities, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverDota2Abilities, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverDota2Abilities, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Dota2 abilities
        :rtype: List[Dota2Ability]
        """

        Validator(FilterOverDota2Abilities).is_optional().validate(filter)
        Validator(RangeOverDota2Abilities).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverDota2Abilities).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(f"{self.base_url}/dota2/abilities", self.get_default_headers())
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

        return [Dota2Ability._unmap(item) for item in response]

    @cast_models
    def get_dota2_abilities_dota2_ability_id_or_slug(
        self, dota2_ability_id_or_slug: Dota2AbilityIdOrSlug
    ) -> Dota2Ability:
        """Get a single ability by ID or by slug

        :param dota2_ability_id_or_slug: An ability ID or slug
        :type dota2_ability_id_or_slug: Dota2AbilityIdOrSlug
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A Dota2 ability
        :rtype: Dota2Ability
        """

        Validator(Dota2AbilityIdOrSlug).validate(dota2_ability_id_or_slug)

        serialized_request = (
            Serializer(
                f"{self.base_url}/dota2/abilities/{{dota2_ability_id_or_slug}}",
                self.get_default_headers(),
            )
            .add_path("dota2_ability_id_or_slug", dota2_ability_id_or_slug)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return Dota2Ability._unmap(response)
