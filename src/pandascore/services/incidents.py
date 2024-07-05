from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.videogame_id_or_slug import VideogameIdOrSlug
from ..models.utils.cast_models import cast_models
from ..models.range_over_incidents import RangeOverIncidents
from ..models.range_over_deletion_incidents import RangeOverDeletionIncidents
from ..models.range_over_change_incidents import RangeOverChangeIncidents
from ..models.range_over_addition_incidents import RangeOverAdditionIncidents
from ..models.page import Page
from ..models.non_deletion_incident import NonDeletionIncident
from ..models.incident import Incident, IncidentGuard
from ..models.filter_over_incidents import FilterOverIncidents
from ..models.filter_over_deletion_incidents import FilterOverDeletionIncidents
from ..models.filter_over_change_incidents import FilterOverChangeIncidents
from ..models.filter_over_addition_incidents import FilterOverAdditionIncidents
from ..models.deletion_incident import DeletionIncident


class IncidentsService(BaseService):

    @cast_models
    def get_additions(
        self,
        filter: FilterOverAdditionIncidents = None,
        range: RangeOverAdditionIncidents = None,
        sort: List[any] = None,
        page: Page = None,
        per_page: int = None,
        type_: List[any] = None,
        since: str = None,
        videogame: List[VideogameIdOrSlug] = None,
    ) -> List[NonDeletionIncident]:
        """Get the latest additions. <br/> <br/>This endpoint only shows unchanged objects.

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverAdditionIncidents, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverAdditionIncidents, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        :param type_: Filter by result type(s), defaults to None
        :type type_: List[any], optional
        :param since: Filter out older results, defaults to None
        :type since: str, optional
        :param videogame: Filter by videogame(s), defaults to None
        :type videogame: List[VideogameIdOrSlug], optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of created entities
        :rtype: List[NonDeletionIncident]
        """

        Validator(FilterOverAdditionIncidents).is_optional().validate(filter)
        Validator(RangeOverAdditionIncidents).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)
        Validator(any).is_array().is_optional().validate(type_)
        Validator(str).is_optional().validate(since)
        Validator(VideogameIdOrSlug).is_array().is_optional().validate(videogame)

        serialized_request = (
            Serializer(f"{self.base_url}/additions", self.get_default_headers())
            .add_query("filter", filter, style="deepObject")
            .add_query("range", range, style="deepObject")
            .add_query("sort", sort)
            .add_query("page", page)
            .add_query("per_page", per_page)
            .add_query("type", type_)
            .add_query("since", since)
            .add_query("videogame", videogame)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return [NonDeletionIncident._unmap(item) for item in response]

    @cast_models
    def get_changes(
        self,
        filter: FilterOverChangeIncidents = None,
        range: RangeOverChangeIncidents = None,
        sort: List[any] = None,
        page: Page = None,
        per_page: int = None,
        type_: List[any] = None,
        since: str = None,
        videogame: List[VideogameIdOrSlug] = None,
    ) -> List[Incident]:
        """Get the latest updates. <br/> <br/>This endpoint only provides the latest change for an object. It does not keep track of previous changes.

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverChangeIncidents, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverChangeIncidents, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        :param type_: Filter by result type(s), defaults to None
        :type type_: List[any], optional
        :param since: Filter out older results, defaults to None
        :type since: str, optional
        :param videogame: Filter by videogame(s), defaults to None
        :type videogame: List[VideogameIdOrSlug], optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of changed entities
        :rtype: List[Incident]
        """

        Validator(FilterOverChangeIncidents).is_optional().validate(filter)
        Validator(RangeOverChangeIncidents).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)
        Validator(any).is_array().is_optional().validate(type_)
        Validator(str).is_optional().validate(since)
        Validator(VideogameIdOrSlug).is_array().is_optional().validate(videogame)

        serialized_request = (
            Serializer(f"{self.base_url}/changes", self.get_default_headers())
            .add_query("filter", filter, style="deepObject")
            .add_query("range", range, style="deepObject")
            .add_query("sort", sort)
            .add_query("page", page)
            .add_query("per_page", per_page)
            .add_query("type", type_)
            .add_query("since", since)
            .add_query("videogame", videogame)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return [IncidentGuard.return_one_of(item) for item in response]

    @cast_models
    def get_deletions(
        self,
        filter: FilterOverDeletionIncidents = None,
        range: RangeOverDeletionIncidents = None,
        sort: List[any] = None,
        page: Page = None,
        per_page: int = None,
        type_: List[any] = None,
        since: str = None,
        videogame: List[VideogameIdOrSlug] = None,
    ) -> List[DeletionIncident]:
        """Get the latest deleted documents

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverDeletionIncidents, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverDeletionIncidents, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        :param type_: Filter by result type(s), defaults to None
        :type type_: List[any], optional
        :param since: Filter out older results, defaults to None
        :type since: str, optional
        :param videogame: Filter by videogame(s), defaults to None
        :type videogame: List[VideogameIdOrSlug], optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of deleted entities
        :rtype: List[DeletionIncident]
        """

        Validator(FilterOverDeletionIncidents).is_optional().validate(filter)
        Validator(RangeOverDeletionIncidents).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)
        Validator(any).is_array().is_optional().validate(type_)
        Validator(str).is_optional().validate(since)
        Validator(VideogameIdOrSlug).is_array().is_optional().validate(videogame)

        serialized_request = (
            Serializer(f"{self.base_url}/deletions", self.get_default_headers())
            .add_query("filter", filter, style="deepObject")
            .add_query("range", range, style="deepObject")
            .add_query("sort", sort)
            .add_query("page", page)
            .add_query("per_page", per_page)
            .add_query("type", type_)
            .add_query("since", since)
            .add_query("videogame", videogame)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return [DeletionIncident._unmap(item) for item in response]

    @cast_models
    def get_incidents(
        self,
        filter: FilterOverIncidents = None,
        range: RangeOverIncidents = None,
        sort: List[any] = None,
        page: Page = None,
        per_page: int = None,
        type_: List[any] = None,
        since: str = None,
        videogame: List[VideogameIdOrSlug] = None,
    ) -> List[Incident]:
        """Get the latest updates and additions. <br/> <br/>This endpoint only provides the latest incident for an object. It does not keep track of previous incidents.

        :param filter: Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter)., defaults to None
        :type filter: FilterOverIncidents, optional
        :param range: Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range)., defaults to None
        :type range: RangeOverIncidents, optional
        :param sort: Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort)., defaults to None
        :type sort: List[any], optional
        :param page: Pagination in the form of `page=2` or `page[size]=30&page[number]=2`, defaults to None
        :type page: Page, optional
        :param per_page: Equivalent to `page[size]`, defaults to None
        :type per_page: int, optional
        :param type_: Filter by result type(s), defaults to None
        :type type_: List[any], optional
        :param since: Filter out older results, defaults to None
        :type since: str, optional
        :param videogame: Filter by videogame(s), defaults to None
        :type videogame: List[VideogameIdOrSlug], optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: A list of created or updated entities
        :rtype: List[Incident]
        """

        Validator(FilterOverIncidents).is_optional().validate(filter)
        Validator(RangeOverIncidents).is_optional().validate(range)
        Validator(any).is_array().is_optional().validate(sort)
        Validator(Page).is_optional().validate(page)
        Validator(int).is_optional().min(1).max(100).validate(per_page)
        Validator(any).is_array().is_optional().validate(type_)
        Validator(str).is_optional().validate(since)
        Validator(VideogameIdOrSlug).is_array().is_optional().validate(videogame)

        serialized_request = (
            Serializer(f"{self.base_url}/incidents", self.get_default_headers())
            .add_query("filter", filter, style="deepObject")
            .add_query("range", range, style="deepObject")
            .add_query("sort", sort)
            .add_query("page", page)
            .add_query("per_page", per_page)
            .add_query("type", type_)
            .add_query("since", since)
            .add_query("videogame", videogame)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return [IncidentGuard.return_one_of(item) for item in response]
