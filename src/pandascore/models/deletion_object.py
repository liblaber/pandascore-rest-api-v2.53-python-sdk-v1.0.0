from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .incident_deletion_reason import (
    IncidentDeletionReason,
    IncidentDeletionReasonGuard,
)
from .incident_deletion_reason_deleted import IncidentDeletionReasonDeleted
from .videogame_id import VideogameId


@JsonMap({})
class DeletionObject(BaseModel):
    """DeletionObject

    :param deleted_at: deleted_at
    :type deleted_at: str
    :param reason: reason
    :type reason: IncidentDeletionReason
    :param videogame_id: A videogame ID
    :type videogame_id: VideogameId
    """

    def __init__(
        self, deleted_at: str, reason: IncidentDeletionReason, videogame_id: VideogameId
    ):
        self.deleted_at = deleted_at
        self.reason = IncidentDeletionReasonGuard.return_one_of(reason)
        self.videogame_id = self._enum_matching(
            videogame_id, VideogameId.list(), "videogame_id"
        )
