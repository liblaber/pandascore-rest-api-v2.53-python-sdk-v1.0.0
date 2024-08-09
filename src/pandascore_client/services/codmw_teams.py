# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.team import Team
from ..models.search_over_codmw_teams import SearchOverCodmwTeams
from ..models.range_over_codmw_teams import RangeOverCodmwTeams
from ..models.page import Page
from ..models.filter_over_codmw_teams import FilterOverCodmwTeams


class CodmwTeamsService(BaseService):

    @cast_models
    def get_codmw_teams(
        self,
        filter: FilterOverCodmwTeams = None,
        range: RangeOverCodmwTeams = None,
        sort: List[any] = None,
        search: SearchOverCodmwTeams = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[Team]:
        """List teams for the CODMW videogame

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverCodmwTeams, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverCodmwTeams, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverCodmwTeams, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Call of Duty Modern Warfare teams
        :rtype: List[Team]
        """

        Validator(FilterOverCodmwTeams).is_optional().validate(filter)
        Validator(RangeOverCodmwTeams).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverCodmwTeams).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(f"{self.base_url}/codmw/teams", self.get_default_headers())
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

        return [Team._unmap(item) for item in response]