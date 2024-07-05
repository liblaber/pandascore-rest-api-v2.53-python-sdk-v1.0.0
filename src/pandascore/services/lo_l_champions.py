from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.search_over_lo_l_champions import SearchOverLoLChampions
from ..models.range_over_lo_l_champions import RangeOverLoLChampions
from ..models.page import Page
from ..models.lo_l_champion import LoLChampion
from ..models.filter_over_lo_l_champions import FilterOverLoLChampions


class LoLChampionsService(BaseService):

    @cast_models
    def get_lol_champions(
        self,
        filter: FilterOverLoLChampions = None,
        range: RangeOverLoLChampions = None,
        sort: List[any] = None,
        search: SearchOverLoLChampions = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[LoLChampion]:
        """List champions

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverLoLChampions, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverLoLChampions, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverLoLChampions, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of League-of-Legends champions
        :rtype: List[LoLChampion]
        """

        Validator(FilterOverLoLChampions).is_optional().validate(filter)
        Validator(RangeOverLoLChampions).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverLoLChampions).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(f"{self.base_url}/lol/champions", self.get_default_headers())
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

        return [LoLChampion._unmap(item) for item in response]

    @cast_models
    def get_lol_champions_lol_champion_id(self, lol_champion_id: int) -> LoLChampion:
        """Get a single champion by ID or by slug

        :param lol_champion_id: A champion ID
        :type lol_champion_id: int
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A League-of-Legends champion
        :rtype: LoLChampion
        """

        Validator(int).min(1).validate(lol_champion_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/lol/champions/{{lol_champion_id}}",
                self.get_default_headers(),
            )
            .add_path("lol_champion_id", lol_champion_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return LoLChampion._unmap(response)

    @cast_models
    def get_lol_versions_all_champions(
        self,
        filter: FilterOverLoLChampions = None,
        range: RangeOverLoLChampions = None,
        sort: List[any] = None,
        search: SearchOverLoLChampions = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[LoLChampion]:
        """Deprecated. Equivalent route: [/lol/champions?filter[videogame_version]=all](/reference/get_lol_champions)

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverLoLChampions, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverLoLChampions, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverLoLChampions, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of League-of-Legends champions
        :rtype: List[LoLChampion]
        """

        Validator(FilterOverLoLChampions).is_optional().validate(filter)
        Validator(RangeOverLoLChampions).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverLoLChampions).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/lol/versions/all/champions",
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

        return [LoLChampion._unmap(item) for item in response]

    @cast_models
    def get_lol_versions_lol_version_name_champions(
        self,
        lol_version_name: int,
        filter: FilterOverLoLChampions = None,
        range: RangeOverLoLChampions = None,
        sort: List[any] = None,
        search: SearchOverLoLChampions = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[LoLChampion]:
        """Deprecated. Equivalent route: [/lol/champions?filter[videogame_version]={lol_version_name}](/reference/get_lol_champions)

        :param lol_version_name: Video game version
        :type lol_version_name: int
        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverLoLChampions, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverLoLChampions, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverLoLChampions, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of League-of-Legends champions
        :rtype: List[LoLChampion]
        """

        Validator(int).min(1).validate(lol_version_name)
        Validator(FilterOverLoLChampions).is_optional().validate(filter)
        Validator(RangeOverLoLChampions).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverLoLChampions).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/lol/versions/{{lol_version_name}}/champions",
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

        return [LoLChampion._unmap(item) for item in response]
