# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .incident_deletion_reason_deleted import IncidentDeletionReasonDeleted


class IncidentDeletionReasonGuard(OneOfBaseModel):
    class_list = {"str": str, "str": str, "IncidentDeletionReasonDeletedEnum": str}


IncidentDeletionReason = Union[str, str, str]