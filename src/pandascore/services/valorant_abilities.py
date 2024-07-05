from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.valorant_ability import ValorantAbility
from ..models.utils.cast_models import cast_models
from ..models.search_over_valorant_abilities import SearchOverValorantAbilities
from ..models.range_over_valorant_abilities import RangeOverValorantAbilities
from ..models.page import Page
from ..models.filter_over_valorant_abilities import FilterOverValorantAbilities


class ValorantAbilitiesService(BaseService):

    @cast_models
    def get_valorant_abilities(
        self,
        filter: FilterOverValorantAbilities = None,
        range: RangeOverValorantAbilities = None,
        sort: List[any] = None,
        search: SearchOverValorantAbilities = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[ValorantAbility]:
        """List abilities

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverValorantAbilities, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverValorantAbilities, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverValorantAbilities, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Valorant abilities
        :rtype: List[ValorantAbility]
        """

        Validator(FilterOverValorantAbilities).is_optional().validate(filter)
        Validator(RangeOverValorantAbilities).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverValorantAbilities).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/valorant/abilities", self.get_default_headers()
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

        return [ValorantAbility._unmap(item) for item in response]

    @cast_models
    def get_valorant_abilities_valorant_ability_id(
        self, valorant_ability_id: int
    ) -> ValorantAbility:
        """Get a Valorant ability by its ID

        :param valorant_ability_id: ID of the Valorant ability
        :type valorant_ability_id: int
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A Valorant ability
        :rtype: ValorantAbility
        """

        Validator(int).min(1).validate(valorant_ability_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/valorant/abilities/{{valorant_ability_id}}",
                self.get_default_headers(),
            )
            .add_path("valorant_ability_id", valorant_ability_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return ValorantAbility._unmap(response)
