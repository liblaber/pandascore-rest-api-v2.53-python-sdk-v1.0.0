# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.search_over_csgo_weapons import SearchOverCsgoWeapons
from ..models.range_over_csgo_weapons import RangeOverCsgoWeapons
from ..models.page import Page
from ..models.filter_over_csgo_weapons import FilterOverCsgoWeapons
from ..models.csgo_weapon_id_or_slug import CsgoWeaponIdOrSlug
from ..models.csgo_weapon import CsgoWeapon


class CounterStrikeWeaponsService(BaseService):

    @cast_models
    def get_csgo_weapons(
        self,
        filter: FilterOverCsgoWeapons = None,
        range: RangeOverCsgoWeapons = None,
        sort: List[any] = None,
        search: SearchOverCsgoWeapons = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[CsgoWeapon]:
        """List weapons

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverCsgoWeapons, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverCsgoWeapons, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverCsgoWeapons, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Counter-Strike weapons
        :rtype: List[CsgoWeapon]
        """

        Validator(FilterOverCsgoWeapons).is_optional().validate(filter)
        Validator(RangeOverCsgoWeapons).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverCsgoWeapons).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(f"{self.base_url}/csgo/weapons", self.get_default_headers())
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

        return [CsgoWeapon._unmap(item) for item in response]

    @cast_models
    def get_csgo_weapons_csgo_weapon_id_or_slug(
        self, csgo_weapon_id_or_slug: CsgoWeaponIdOrSlug
    ) -> CsgoWeapon:
        """Get a single weapon by ID or by slug

        :param csgo_weapon_id_or_slug: A weapon ID or slug
        :type csgo_weapon_id_or_slug: CsgoWeaponIdOrSlug
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A Counter-Strike weapon
        :rtype: CsgoWeapon
        """

        Validator(CsgoWeaponIdOrSlug).validate(csgo_weapon_id_or_slug)

        serialized_request = (
            Serializer(
                f"{self.base_url}/csgo/weapons/{{csgo_weapon_id_or_slug}}",
                self.get_default_headers(),
            )
            .add_path("csgo_weapon_id_or_slug", csgo_weapon_id_or_slug)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return CsgoWeapon._unmap(response)
