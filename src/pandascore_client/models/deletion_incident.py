# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .deletion_incident_change_type import DeletionIncidentChangeType
from .incident_id import IncidentId, IncidentIdGuard
from .deletion_object import DeletionObject
from .incident_type import IncidentType


@JsonMap({"id_": "id", "type_": "type"})
class DeletionIncident(BaseModel):
    """DeletionIncident

    :param change_type: change_type
    :type change_type: DeletionIncidentChangeType
    :param id_: An incident ID
    :type id_: IncidentId
    :param modified_at: modified_at
    :type modified_at: str
    :param object: object
    :type object: DeletionObject
    :param type_: type_
    :type type_: IncidentType
    """

    def __init__(
        self,
        change_type: DeletionIncidentChangeType,
        id_: IncidentId,
        modified_at: str,
        object: DeletionObject,
        type_: IncidentType,
    ):
        """DeletionIncident

        :param change_type: change_type
        :type change_type: DeletionIncidentChangeType
        :param id_: An incident ID
        :type id_: IncidentId
        :param modified_at: modified_at
        :type modified_at: str
        :param object: object
        :type object: DeletionObject
        :param type_: type_
        :type type_: IncidentType
        """
        self.change_type = self._enum_matching(
            change_type, DeletionIncidentChangeType.list(), "change_type"
        )
        self.id_ = IncidentIdGuard.return_one_of(id_)
        self.modified_at = self._define_str("modified_at", modified_at, min_length=1)
        self.object = self._define_object(object, DeletionObject)
        self.type_ = self._enum_matching(type_, IncidentType.list(), "type_")
