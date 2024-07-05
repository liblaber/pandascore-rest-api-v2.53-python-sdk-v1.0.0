from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.videogame_id_or_slug import VideogameIdOrSlug
from ..models.videogame import Videogame, VideogameGuard
from ..models.utils.cast_models import cast_models
from ..models.short_videogame_version import ShortVideogameVersion
from ..models.short_videogame_title import ShortVideogameTitle
from ..models.short_tournament import ShortTournament
from ..models.serie import Serie
from ..models.search_over_short_tournaments import SearchOverShortTournaments
from ..models.search_over_series import SearchOverSeries
from ..models.search_over_leagues import SearchOverLeagues
from ..models.range_over_short_tournaments import RangeOverShortTournaments
from ..models.range_over_series import RangeOverSeries
from ..models.range_over_leagues import RangeOverLeagues
from ..models.page import Page
from ..models.league import League
from ..models.filter_over_short_tournaments import FilterOverShortTournaments
from ..models.filter_over_series import FilterOverSeries
from ..models.filter_over_leagues import FilterOverLeagues


class VideogamesService(BaseService):

    @cast_models
    def get_videogames(
        self, page: Page = None, per_page: int = None
    ) -> List[Videogame]:
        """List videogames

        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of videogames
        :rtype: List[Videogame]
        """

        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(f"{self.base_url}/videogames", self.get_default_headers())
            .add_query("page", page)
            .add_query("per_page", per_page)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return [VideogameGuard.return_one_of(item) for item in response]

    @cast_models
    def get_videogames_videogame_id_or_slug(
        self, videogame_id_or_slug: VideogameIdOrSlug
    ) -> Videogame:
        """Get a single videogame by ID or by slug

        :param videogame_id_or_slug: A videogame ID or slug
        :type videogame_id_or_slug: VideogameIdOrSlug
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A videogame
        :rtype: Videogame
        """

        Validator(VideogameIdOrSlug).validate(videogame_id_or_slug)

        serialized_request = (
            Serializer(
                f"{self.base_url}/videogames/{{videogame_id_or_slug}}",
                self.get_default_headers(),
            )
            .add_path("videogame_id_or_slug", videogame_id_or_slug)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return VideogameGuard.return_one_of(response)

    @cast_models
    def get_videogames_videogame_id_or_slug_leagues(
        self,
        videogame_id_or_slug: VideogameIdOrSlug,
        filter: FilterOverLeagues = None,
        range: RangeOverLeagues = None,
        sort: List[any] = None,
        search: SearchOverLeagues = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[League]:
        """List leagues for a given videogame

        :param videogame_id_or_slug: A videogame ID or slug
        :type videogame_id_or_slug: VideogameIdOrSlug
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

        Validator(VideogameIdOrSlug).validate(videogame_id_or_slug)
        Validator(FilterOverLeagues).is_optional().validate(filter)
        Validator(RangeOverLeagues).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverLeagues).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/videogames/{{videogame_id_or_slug}}/leagues",
                self.get_default_headers(),
            )
            .add_path("videogame_id_or_slug", videogame_id_or_slug)
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
    def get_videogames_videogame_id_or_slug_series(
        self,
        videogame_id_or_slug: VideogameIdOrSlug,
        filter: FilterOverSeries = None,
        range: RangeOverSeries = None,
        sort: List[any] = None,
        search: SearchOverSeries = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[Serie]:
        """List series for the given videogame

        :param videogame_id_or_slug: A videogame ID or slug
        :type videogame_id_or_slug: VideogameIdOrSlug
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

        Validator(VideogameIdOrSlug).validate(videogame_id_or_slug)
        Validator(FilterOverSeries).is_optional().validate(filter)
        Validator(RangeOverSeries).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverSeries).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/videogames/{{videogame_id_or_slug}}/series",
                self.get_default_headers(),
            )
            .add_path("videogame_id_or_slug", videogame_id_or_slug)
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
    def get_videogames_videogame_id_or_slug_titles(
        self,
        videogame_id_or_slug: VideogameIdOrSlug,
        page: Page = None,
        per_page: int = None,
    ) -> List[ShortVideogameTitle]:
        """List available titles for a given videogame

        :param videogame_id_or_slug: A videogame ID or slug
        :type videogame_id_or_slug: VideogameIdOrSlug
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of a videogame versions
        :rtype: List[ShortVideogameTitle]
        """

        Validator(VideogameIdOrSlug).validate(videogame_id_or_slug)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/videogames/{{videogame_id_or_slug}}/titles",
                self.get_default_headers(),
            )
            .add_path("videogame_id_or_slug", videogame_id_or_slug)
            .add_query("page", page)
            .add_query("per_page", per_page)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return [ShortVideogameTitle._unmap(item) for item in response]

    @cast_models
    def get_videogames_videogame_id_or_slug_tournaments(
        self,
        videogame_id_or_slug: VideogameIdOrSlug,
        filter: FilterOverShortTournaments = None,
        range: RangeOverShortTournaments = None,
        sort: List[any] = None,
        search: SearchOverShortTournaments = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[ShortTournament]:
        """List tournaments of the given videogame

        :param videogame_id_or_slug: A videogame ID or slug
        :type videogame_id_or_slug: VideogameIdOrSlug
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

        Validator(VideogameIdOrSlug).validate(videogame_id_or_slug)
        Validator(FilterOverShortTournaments).is_optional().validate(filter)
        Validator(RangeOverShortTournaments).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverShortTournaments).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/videogames/{{videogame_id_or_slug}}/tournaments",
                self.get_default_headers(),
            )
            .add_path("videogame_id_or_slug", videogame_id_or_slug)
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
    def get_videogames_videogame_id_or_slug_versions(
        self,
        videogame_id_or_slug: VideogameIdOrSlug,
        page: Page = None,
        per_page: int = None,
    ) -> List[ShortVideogameVersion]:
        """List available versions for a given videogame

        :param videogame_id_or_slug: A videogame ID or slug
        :type videogame_id_or_slug: VideogameIdOrSlug
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of a videogame's versions
        :rtype: List[ShortVideogameVersion]
        """

        Validator(VideogameIdOrSlug).validate(videogame_id_or_slug)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/videogames/{{videogame_id_or_slug}}/versions",
                self.get_default_headers(),
            )
            .add_path("videogame_id_or_slug", videogame_id_or_slug)
            .add_query("page", page)
            .add_query("per_page", per_page)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return [ShortVideogameVersion._unmap(item) for item in response]
