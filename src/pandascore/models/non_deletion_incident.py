from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .incident_change_type import IncidentChangeType
from .incident_id import IncidentId, IncidentIdGuard
from .incident_object import IncidentObject, IncidentObjectGuard
from .league import League
from .serie import Serie
from .tournament import Tournament
from .match import Match
from .player import Player
from .team import Team
from .incident_type import IncidentType


@JsonMap({"id_": "id", "type_": "type"})
class NonDeletionIncident(BaseModel):
    """NonDeletionIncident

    :param change_type: change_type
    :type change_type: IncidentChangeType
    :param id_: An incident ID
    :type id_: IncidentId
    :param modified_at: modified_at
    :type modified_at: str
    :param object: object
    :type object: IncidentObject
    :param type_: type_
    :type type_: IncidentType
    """

    def __init__(
        self,
        change_type: IncidentChangeType,
        id_: IncidentId,
        modified_at: str,
        object: IncidentObject,
        type_: IncidentType,
    ):
        self.change_type = self._enum_matching(
            change_type, IncidentChangeType.list(), "change_type"
        )
        self.id_ = IncidentIdGuard.return_one_of(id_)
        self.modified_at = modified_at
        self.object = IncidentObjectGuard.return_one_of(object)
        self.type_ = self._enum_matching(type_, IncidentType.list(), "type_")
