# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .incident_id import IncidentId, IncidentIdGuard


@JsonMap({"id_": "id"})
class RangeOverIncidents(BaseModel):
    """RangeOverIncidents

    :param id_: id_, defaults to None
    :type id_: List[IncidentId], optional
    :param modified_at: modified_at, defaults to None
    :type modified_at: List[str], optional
    """

    def __init__(self, id_: List[IncidentId] = None, modified_at: List[str] = None):
        if id_ is not None:
            self.id_ = self._define_list(id_, IncidentId)
        if modified_at is not None:
            self.modified_at = modified_at
