# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.valorant_weapon import ValorantWeapon
from ..models.utils.cast_models import cast_models
from ..models.search_over_valorant_weapons import SearchOverValorantWeapons
from ..models.range_over_valorant_weapons import RangeOverValorantWeapons
from ..models.page import Page
from ..models.filter_over_valorant_weapons import FilterOverValorantWeapons


class ValorantWeaponsService(BaseService):

    @cast_models
    def get_valorant_weapons(
        self,
        filter: FilterOverValorantWeapons = None,
        range: RangeOverValorantWeapons = None,
        sort: List[any] = None,
        search: SearchOverValorantWeapons = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[ValorantWeapon]:
        """List weapons

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverValorantWeapons, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverValorantWeapons, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverValorantWeapons, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Valorant weapons
        :rtype: List[ValorantWeapon]
        """

        Validator(FilterOverValorantWeapons).is_optional().validate(filter)
        Validator(RangeOverValorantWeapons).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverValorantWeapons).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(f"{self.base_url}/valorant/weapons", self.get_default_headers())
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

        return [ValorantWeapon._unmap(item) for item in response]

    @cast_models
    def get_valorant_weapons_valorant_weapon_id(
        self, valorant_weapon_id: int
    ) -> ValorantWeapon:
        """Get a Valorant weapon by its ID

        :param valorant_weapon_id: ID of the Valorant weapon
        :type valorant_weapon_id: int
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A Valorant weapon
        :rtype: ValorantWeapon
        """

        Validator(int).min(1).validate(valorant_weapon_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/valorant/weapons/{{valorant_weapon_id}}",
                self.get_default_headers(),
            )
            .add_path("valorant_weapon_id", valorant_weapon_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return ValorantWeapon._unmap(response)
