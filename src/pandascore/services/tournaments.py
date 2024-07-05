from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.tournament_rosters import TournamentRosters, TournamentRostersGuard
from ..models.tournament_id_or_slug import TournamentIdOrSlug
from ..models.tournament import Tournament
from ..models.team import Team
from ..models.standing import Standing, StandingGuard
from ..models.short_tournament import ShortTournament
from ..models.search_over_teams import SearchOverTeams
from ..models.search_over_short_tournaments import SearchOverShortTournaments
from ..models.search_over_matches import SearchOverMatches
from ..models.search_over_brackets import SearchOverBrackets
from ..models.range_over_teams import RangeOverTeams
from ..models.range_over_short_tournaments import RangeOverShortTournaments
from ..models.range_over_matches import RangeOverMatches
from ..models.range_over_brackets import RangeOverBrackets
from ..models.page import Page
from ..models.match import Match
from ..models.filter_over_teams import FilterOverTeams
from ..models.filter_over_short_tournaments import FilterOverShortTournaments
from ..models.filter_over_matches import FilterOverMatches
from ..models.filter_over_brackets import FilterOverBrackets
from ..models.bracket import Bracket


class TournamentsService(BaseService):

    @cast_models
    def get_tournaments(
        self,
        filter: FilterOverShortTournaments = None,
        range: RangeOverShortTournaments = None,
        sort: List[any] = None,
        search: SearchOverShortTournaments = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[ShortTournament]:
        """List tournaments

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

        Validator(FilterOverShortTournaments).is_optional().validate(filter)
        Validator(RangeOverShortTournaments).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverShortTournaments).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(f"{self.base_url}/tournaments", self.get_default_headers())
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

    @cast_models
    def get_tournaments_past(
        self,
        filter: FilterOverShortTournaments = None,
        range: RangeOverShortTournaments = None,
        sort: List[any] = None,
        search: SearchOverShortTournaments = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[ShortTournament]:
        """List past tournaments

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

        Validator(FilterOverShortTournaments).is_optional().validate(filter)
        Validator(RangeOverShortTournaments).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverShortTournaments).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(f"{self.base_url}/tournaments/past", self.get_default_headers())
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

    @cast_models
    def get_tournaments_running(
        self,
        filter: FilterOverShortTournaments = None,
        range: RangeOverShortTournaments = None,
        sort: List[any] = None,
        search: SearchOverShortTournaments = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[ShortTournament]:
        """List currently running tournaments

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

        Validator(FilterOverShortTournaments).is_optional().validate(filter)
        Validator(RangeOverShortTournaments).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverShortTournaments).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/tournaments/running", self.get_default_headers()
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

        return [ShortTournament._unmap(item) for item in response]

    @cast_models
    def get_tournaments_upcoming(
        self,
        filter: FilterOverShortTournaments = None,
        range: RangeOverShortTournaments = None,
        sort: List[any] = None,
        search: SearchOverShortTournaments = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[ShortTournament]:
        """List upcoming tournaments

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

        Validator(FilterOverShortTournaments).is_optional().validate(filter)
        Validator(RangeOverShortTournaments).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverShortTournaments).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/tournaments/upcoming", self.get_default_headers()
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

        return [ShortTournament._unmap(item) for item in response]

    @cast_models
    def get_tournaments_tournament_id_or_slug(
        self, tournament_id_or_slug: TournamentIdOrSlug
    ) -> Tournament:
        """Get a single tournament by ID or by slug

        :param tournament_id_or_slug: A tournament ID or slug
        :type tournament_id_or_slug: TournamentIdOrSlug
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A detailed tournament
        :rtype: Tournament
        """

        Validator(TournamentIdOrSlug).validate(tournament_id_or_slug)

        serialized_request = (
            Serializer(
                f"{self.base_url}/tournaments/{{tournament_id_or_slug}}",
                self.get_default_headers(),
            )
            .add_path("tournament_id_or_slug", tournament_id_or_slug)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return Tournament._unmap(response)

    @cast_models
    def get_tournaments_tournament_id_or_slug_brackets(
        self,
        tournament_id_or_slug: TournamentIdOrSlug,
        filter: FilterOverBrackets = None,
        range: RangeOverBrackets = None,
        sort: List[any] = None,
        search: SearchOverBrackets = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[Bracket]:
        """Get the brackets of the given tournament

        :param tournament_id_or_slug: A tournament ID or slug
        :type tournament_id_or_slug: TournamentIdOrSlug
        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverBrackets, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverBrackets, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverBrackets, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A tree of games played during a tournament
        :rtype: List[Bracket]
        """

        Validator(TournamentIdOrSlug).validate(tournament_id_or_slug)
        Validator(FilterOverBrackets).is_optional().validate(filter)
        Validator(RangeOverBrackets).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverBrackets).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/tournaments/{{tournament_id_or_slug}}/brackets",
                self.get_default_headers(),
            )
            .add_path("tournament_id_or_slug", tournament_id_or_slug)
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

        return [Bracket._unmap(item) for item in response]

    @cast_models
    def get_tournaments_tournament_id_or_slug_matches(
        self,
        tournament_id_or_slug: TournamentIdOrSlug,
        filter: FilterOverMatches = None,
        range: RangeOverMatches = None,
        sort: List[any] = None,
        search: SearchOverMatches = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[Match]:
        """List matches for the given tournament

        :param tournament_id_or_slug: A tournament ID or slug
        :type tournament_id_or_slug: TournamentIdOrSlug
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

        Validator(TournamentIdOrSlug).validate(tournament_id_or_slug)
        Validator(FilterOverMatches).is_optional().validate(filter)
        Validator(RangeOverMatches).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverMatches).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/tournaments/{{tournament_id_or_slug}}/matches",
                self.get_default_headers(),
            )
            .add_path("tournament_id_or_slug", tournament_id_or_slug)
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
    def get_tournaments_tournament_id_or_slug_rosters(
        self, tournament_id_or_slug: TournamentIdOrSlug
    ) -> TournamentRosters:
        """List participants (player or team) for a given tournament.

        :param tournament_id_or_slug: A tournament ID or slug
        :type tournament_id_or_slug: TournamentIdOrSlug
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Tournament rosters (team or player)
        :rtype: TournamentRosters
        """

        Validator(TournamentIdOrSlug).validate(tournament_id_or_slug)

        serialized_request = (
            Serializer(
                f"{self.base_url}/tournaments/{{tournament_id_or_slug}}/rosters",
                self.get_default_headers(),
            )
            .add_path("tournament_id_or_slug", tournament_id_or_slug)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return TournamentRostersGuard.return_one_of(response)

    @cast_models
    def get_tournaments_tournament_id_or_slug_standings(
        self,
        tournament_id_or_slug: TournamentIdOrSlug,
        page: Page = None,
        per_page: int = None,
    ) -> List[Standing]:
        """Get the current standings for a given tournament

        :param tournament_id_or_slug: A tournament ID or slug
        :type tournament_id_or_slug: TournamentIdOrSlug
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Ranking of teams in a tournament
        :rtype: List[Standing]
        """

        Validator(TournamentIdOrSlug).validate(tournament_id_or_slug)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/tournaments/{{tournament_id_or_slug}}/standings",
                self.get_default_headers(),
            )
            .add_path("tournament_id_or_slug", tournament_id_or_slug)
            .add_query("page", page)
            .add_query("per_page", per_page)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return [StandingGuard.return_one_of(item) for item in response]

    @cast_models
    def get_tournaments_tournament_id_or_slug_teams(
        self,
        tournament_id_or_slug: TournamentIdOrSlug,
        filter: FilterOverTeams = None,
        range: RangeOverTeams = None,
        sort: List[any] = None,
        search: SearchOverTeams = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[Team]:
        """List teams for the given tournament

        :param tournament_id_or_slug: A tournament ID or slug
        :type tournament_id_or_slug: TournamentIdOrSlug
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

        Validator(TournamentIdOrSlug).validate(tournament_id_or_slug)
        Validator(FilterOverTeams).is_optional().validate(filter)
        Validator(RangeOverTeams).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverTeams).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/tournaments/{{tournament_id_or_slug}}/teams",
                self.get_default_headers(),
            )
            .add_path("tournament_id_or_slug", tournament_id_or_slug)
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
