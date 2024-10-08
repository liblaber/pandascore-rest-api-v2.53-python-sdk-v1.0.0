# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.team_id_or_slug import TeamIdOrSlug
from ..models.search_over_dota2_games import SearchOverDota2Games
from ..models.range_over_dota2_games import RangeOverDota2Games
from ..models.page import Page
from ..models.match_id_or_slug import MatchIdOrSlug
from ..models.filter_over_dota2_games import FilterOverDota2Games
from ..models.dota2_game import Dota2Game
from ..models.dota2_frame import Dota2Frame
from ..models.base_dota2_game import BaseDota2Game


class Dota2GamesService(BaseService):

    @cast_models
    def get_dota2_games_dota2_game_id(self, dota2_game_id: int) -> Dota2Game:
        """Get a single Dota 2 game by ID

        :param dota2_game_id: A game ID
        :type dota2_game_id: int
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A Dota2 game
        :rtype: Dota2Game
        """

        Validator(int).min(1).validate(dota2_game_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/dota2/games/{{dota2_game_id}}",
                self.get_default_headers(),
            )
            .add_path("dota2_game_id", dota2_game_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return Dota2Game._unmap(response)

    @cast_models
    def get_dota2_games_dota2_game_id_frames(
        self, dota2_game_id: int, page: Page = None, per_page: int = None
    ) -> List[Dota2Frame]:
        """List frames for a given Dota 2 game

        :param dota2_game_id: A game ID
        :type dota2_game_id: int
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Dota2 game frames
        :rtype: List[Dota2Frame]
        """

        Validator(int).min(1).validate(dota2_game_id)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/dota2/games/{{dota2_game_id}}/frames",
                self.get_default_headers(),
            )
            .add_path("dota2_game_id", dota2_game_id)
            .add_query("page", page)
            .add_query("per_page", per_page)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return [Dota2Frame._unmap(item) for item in response]

    @cast_models
    def get_dota2_matches_match_id_or_slug_games(
        self,
        match_id_or_slug: MatchIdOrSlug,
        filter: FilterOverDota2Games = None,
        range: RangeOverDota2Games = None,
        sort: List[any] = None,
        search: SearchOverDota2Games = None,
        page: Page = None,
        per_page: int = None,
    ) -> List[Dota2Game]:
        """List games for a given Dota 2 match

        :param match_id_or_slug: A match ID or slug
        :type match_id_or_slug: MatchIdOrSlug
        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverDota2Games, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverDota2Games, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param search: Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search)., defaults to None
        :type search: SearchOverDota2Games, optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Dota2 games
        :rtype: List[Dota2Game]
        """

        Validator(MatchIdOrSlug).validate(match_id_or_slug)
        Validator(FilterOverDota2Games).is_optional().validate(filter)
        Validator(RangeOverDota2Games).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(SearchOverDota2Games).is_optional().validate(search)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/dota2/matches/{{match_id_or_slug}}/games",
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

        return [Dota2Game._unmap(item) for item in response]

    @cast_models
    def get_dota2_teams_team_id_or_slug_games(
        self, team_id_or_slug: TeamIdOrSlug, page: Page = None, per_page: int = None
    ) -> List[BaseDota2Game]:
        """List finished games for a given Dota 2 team

        :param team_id_or_slug: A team ID or slug
        :type team_id_or_slug: TeamIdOrSlug
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of Dota2 games
        :rtype: List[BaseDota2Game]
        """

        Validator(TeamIdOrSlug).validate(team_id_or_slug)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)

        serialized_request = (
            Serializer(
                f"{self.base_url}/dota2/teams/{{team_id_or_slug}}/games",
                self.get_default_headers(),
            )
            .add_path("team_id_or_slug", team_id_or_slug)
            .add_query("page", page)
            .add_query("per_page", per_page)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return [BaseDota2Game._unmap(item) for item in response]
