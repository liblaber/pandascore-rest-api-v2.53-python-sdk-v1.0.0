from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.search_over_csgo_games import SearchOverCsgoGames
from ..models.range_over_csgo_games import RangeOverCsgoGames
from ..models.page import Page
from ..models.match_id_or_slug import MatchIdOrSlug
from ..models.filter_over_csgo_games import FilterOverCsgoGames
from ..models.csgo_game import CsgoGame
from ..models.csgo_full_round import CsgoFullRound
from ..models.csgo_event import CsgoEvent, CsgoEventGuard


class CounterStrikeGamesService(BaseService):

    @cast_models
    def get_csgo_games_csgo_game_id(self, csgo_game_id: int) -> CsgoGame:
        """Get a single Counter-Strike game by ID

        :param csgo_game_id: A Counter-Strike game ID
        :type csgo_game_id: int
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A Counter-Strike game
        :rtype: CsgoGame
        """

        Validator(int).min(1).validate(csgo_game_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/csgo/games/{{csgo_game_id}}",
                self.get_default_headers(),
            )
            .add_path("csgo_game_id", csgo_game_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return CsgoGame._unmap(response)

    @cast_models
    def get_csgo_games_csgo_game_id_events(
        self, csgo_game_id: int, page: Page = None, per_page: int = None
    ) -> List[CsgoEvent]:
        """List events for a given Counter-Strike game

        :param csgo_game_id: A Counter-Strike game ID
        :type csgo_game_id: int
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Counter-Strike game events
        :rtype: List[CsgoEvent]
        """

        Validator(int).min(1).validate(csgo_game_id)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/csgo/games/{{csgo_game_id}}/events",
                self.get_default_headers(),
            )
            .add_path("csgo_game_id", csgo_game_id)
            .add_query("page", page)
            .add_query("per_page", per_page)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return [CsgoEventGuard.return_one_of(item) for item in response]

    @cast_models
    def get_csgo_games_csgo_game_id_rounds(
        self, csgo_game_id: int, page: Page = None, per_page: int = None
    ) -> List[CsgoFullRound]:
        """List rounds in a Counter-Strike game

        :param csgo_game_id: A Counter-Strike game ID
        :type csgo_game_id: int
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: List rounds in a Counter-Strike game
        :rtype: List[CsgoFullRound]
        """

        Validator(int).min(1).validate(csgo_game_id)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/csgo/games/{{csgo_game_id}}/rounds",
                self.get_default_headers(),
            )
            .add_path("csgo_game_id", csgo_game_id)
            .add_query("page", page)
            .add_query("per_page", per_page)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return [CsgoFullRound._unmap(item) for item in response]

    @cast_models
    def get_csgo_matches_match_id_or_slug_games(
        self,
        match_id_or_slug: MatchIdOrSlug,
        filter: FilterOverCsgoGames = None,
        range: RangeOverCsgoGames = None,
        sort: List[any] = None,
        search: SearchOverCsgoGames = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[CsgoGame]:
        """List games for a given Counter-Strike match

        :param match_id_or_slug: A match ID or slug
        :type match_id_or_slug: MatchIdOrSlug
        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverCsgoGames, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverCsgoGames, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverCsgoGames, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Counter-Strike games
        :rtype: List[CsgoGame]
        """

        Validator(MatchIdOrSlug).validate(match_id_or_slug)
        Validator(FilterOverCsgoGames).is_optional().validate(filter)
        Validator(RangeOverCsgoGames).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverCsgoGames).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/csgo/matches/{{match_id_or_slug}}/games",
                self.get_default_headers(),
            )
            .add_path("match_id_or_slug", match_id_or_slug)
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

        return [CsgoGame._unmap(item) for item in response]
