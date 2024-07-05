from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.valorant_map import ValorantMap
from ..models.utils.cast_models import cast_models
from ..models.search_over_valorant_maps import SearchOverValorantMaps
from ..models.range_over_valorant_maps import RangeOverValorantMaps
from ..models.page import Page
from ..models.filter_over_valorant_maps import FilterOverValorantMaps


class ValorantMapsService(BaseService):

    @cast_models
    def get_valorant_maps(
        self,
        filter: FilterOverValorantMaps = None,
        range: RangeOverValorantMaps = None,
        sort: List[any] = None,
        search: SearchOverValorantMaps = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[ValorantMap]:
        """List maps

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverValorantMaps, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverValorantMaps, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverValorantMaps, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Valorant maps
        :rtype: List[ValorantMap]
        """

        Validator(FilterOverValorantMaps).is_optional().validate(filter)
        Validator(RangeOverValorantMaps).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverValorantMaps).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(f"{self.base_url}/valorant/maps", self.get_default_headers())
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

        return [ValorantMap._unmap(item) for item in response]

    @cast_models
    def get_valorant_maps_valorant_map_id(self, valorant_map_id: int) -> ValorantMap:
        """Get a Valorant map by its ID

        :param valorant_map_id: ID of the Valorant map
        :type valorant_map_id: int
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A Valorant map
        :rtype: ValorantMap
        """

        Validator(int).min(1).validate(valorant_map_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/valorant/maps/{{valorant_map_id}}",
                self.get_default_headers(),
            )
            .add_path("valorant_map_id", valorant_map_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return ValorantMap._unmap(response)

    @cast_models
    def get_valorant_versions_all_maps(
        self,
        filter: FilterOverValorantMaps = None,
        range: RangeOverValorantMaps = None,
        sort: List[any] = None,
        search: SearchOverValorantMaps = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[ValorantMap]:
        """Deprecated. Equivalent route: [/valorant/maps?filter[videogame_version]=all](/reference/get_valorant_maps)

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverValorantMaps, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverValorantMaps, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverValorantMaps, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Valorant maps
        :rtype: List[ValorantMap]
        """

        Validator(FilterOverValorantMaps).is_optional().validate(filter)
        Validator(RangeOverValorantMaps).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverValorantMaps).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/valorant/versions/all/maps",
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

        return [ValorantMap._unmap(item) for item in response]

    @cast_models
    def get_valorant_versions_valorant_version_name_maps(
        self,
        valorant_version_name: str,
        filter: FilterOverValorantMaps = None,
        range: RangeOverValorantMaps = None,
        sort: List[any] = None,
        search: SearchOverValorantMaps = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[ValorantMap]:
        """Deprecated. Equivalent route: [/valorant/maps?filter[videogame_version]={valorant_version_name}](/reference/get_valorant_maps)

        :param valorant_version_name: A video game version
        :type valorant_version_name: str
        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverValorantMaps, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverValorantMaps, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverValorantMaps, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Valorant maps
        :rtype: List[ValorantMap]
        """

        Validator(str).validate(valorant_version_name)
        Validator(FilterOverValorantMaps).is_optional().validate(filter)
        Validator(RangeOverValorantMaps).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverValorantMaps).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/valorant/versions/{{valorant_version_name}}/maps",
                self.get_default_headers(),
            )
            .add_path("valorant_version_name", valorant_version_name)
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

        return [ValorantMap._unmap(item) for item in response]
