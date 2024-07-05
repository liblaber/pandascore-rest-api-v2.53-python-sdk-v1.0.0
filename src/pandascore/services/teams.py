from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.team_id_or_slug import TeamIdOrSlug
from ..models.team import Team
from ..models.short_tournament import ShortTournament
from ..models.serie import Serie
from ..models.search_over_teams import SearchOverTeams
from ..models.search_over_short_tournaments import SearchOverShortTournaments
from ..models.search_over_series import SearchOverSeries
from ..models.search_over_matches import SearchOverMatches
from ..models.search_over_leagues import SearchOverLeagues
from ..models.range_over_teams import RangeOverTeams
from ..models.range_over_short_tournaments import RangeOverShortTournaments
from ..models.range_over_series import RangeOverSeries
from ..models.range_over_matches import RangeOverMatches
from ..models.range_over_leagues import RangeOverLeagues
from ..models.page import Page
from ..models.match import Match
from ..models.league import League
from ..models.filter_over_teams import FilterOverTeams
from ..models.filter_over_short_tournaments import FilterOverShortTournaments
from ..models.filter_over_series import FilterOverSeries
from ..models.filter_over_matches import FilterOverMatches
from ..models.filter_over_leagues import FilterOverLeagues


class TeamsService(BaseService):

    @cast_models
    def get_teams(
        self,
        filter: FilterOverTeams = None,
        range: RangeOverTeams = None,
        sort: List[any] = None,
        search: SearchOverTeams = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[Team]:
        """List teams

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverTeams, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverTeams, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverTeams, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of teams
        :rtype: List[Team]
        """

        Validator(FilterOverTeams).is_optional().validate(filter)
        Validator(RangeOverTeams).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverTeams).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(f"{self.base_url}/teams", self.get_default_headers())
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

    @cast_models
    def get_teams_team_id_or_slug(self, team_id_or_slug: TeamIdOrSlug) -> Team:
        """Get a single team by ID or by slug

        :param team_id_or_slug: A team ID or slug
        :type team_id_or_slug: TeamIdOrSlug
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A team
        :rtype: Team
        """

        Validator(TeamIdOrSlug).validate(team_id_or_slug)

        serialized_request = (
            Serializer(
                f"{self.base_url}/teams/{{team_id_or_slug}}", self.get_default_headers()
            )
            .add_path("team_id_or_slug", team_id_or_slug)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return Team._unmap(response)

    @cast_models
    def get_teams_team_id_or_slug_leagues(
        self,
        team_id_or_slug: TeamIdOrSlug,
        filter: FilterOverLeagues = None,
        range: RangeOverLeagues = None,
        sort: List[any] = None,
        search: SearchOverLeagues = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[League]:
        """List leagues in which the given team was part of

        :param team_id_or_slug: A team ID or slug
        :type team_id_or_slug: TeamIdOrSlug
        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverLeagues, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverLeagues, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverLeagues, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of leagues
        :rtype: List[League]
        """

        Validator(TeamIdOrSlug).validate(team_id_or_slug)
        Validator(FilterOverLeagues).is_optional().validate(filter)
        Validator(RangeOverLeagues).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverLeagues).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/teams/{{team_id_or_slug}}/leagues",
                self.get_default_headers(),
            )
            .add_path("team_id_or_slug", team_id_or_slug)
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

        return [League._unmap(item) for item in response]

    @cast_models
    def get_teams_team_id_or_slug_matches(
        self,
        team_id_or_slug: TeamIdOrSlug,
        filter: FilterOverMatches = None,
        range: RangeOverMatches = None,
        sort: List[any] = None,
        search: SearchOverMatches = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[Match]:
        """List matches for the given team

        :param team_id_or_slug: A team ID or slug
        :type team_id_or_slug: TeamIdOrSlug
        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverMatches, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverMatches, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverMatches, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of matches of any e-sport
        :rtype: List[Match]
        """

        Validator(TeamIdOrSlug).validate(team_id_or_slug)
        Validator(FilterOverMatches).is_optional().validate(filter)
        Validator(RangeOverMatches).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverMatches).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/teams/{{team_id_or_slug}}/matches",
                self.get_default_headers(),
            )
            .add_path("team_id_or_slug", team_id_or_slug)
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

        return [Match._unmap(item) for item in response]

    @cast_models
    def get_teams_team_id_or_slug_series(
        self,
        team_id_or_slug: TeamIdOrSlug,
        filter: FilterOverSeries = None,
        range: RangeOverSeries = None,
        sort: List[any] = None,
        search: SearchOverSeries = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[Serie]:
        """List series in which the given team was part of

        :param team_id_or_slug: A team ID or slug
        :type team_id_or_slug: TeamIdOrSlug
        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverSeries, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverSeries, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverSeries, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of series
        :rtype: List[Serie]
        """

        Validator(TeamIdOrSlug).validate(team_id_or_slug)
        Validator(FilterOverSeries).is_optional().validate(filter)
        Validator(RangeOverSeries).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverSeries).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/teams/{{team_id_or_slug}}/series",
                self.get_default_headers(),
            )
            .add_path("team_id_or_slug", team_id_or_slug)
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

        return [Serie._unmap(item) for item in response]

    @cast_models
    def get_teams_team_id_or_slug_tournaments(
        self,
        team_id_or_slug: TeamIdOrSlug,
        filter: FilterOverShortTournaments = None,
        range: RangeOverShortTournaments = None,
        sort: List[any] = None,
        search: SearchOverShortTournaments = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[ShortTournament]:
        """List tournaments in which the given team was part of

        :param team_id_or_slug: A team ID or slug
        :type team_id_or_slug: TeamIdOrSlug
        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverShortTournaments, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverShortTournaments, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverShortTournaments, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of tournaments
        :rtype: List[ShortTournament]
        """

        Validator(TeamIdOrSlug).validate(team_id_or_slug)
        Validator(FilterOverShortTournaments).is_optional().validate(filter)
        Validator(RangeOverShortTournaments).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverShortTournaments).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/teams/{{team_id_or_slug}}/tournaments",
                self.get_default_headers(),
            )
            .add_path("team_id_or_slug", team_id_or_slug)
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

        return [ShortTournament._unmap(item) for item in response]
