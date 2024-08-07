from __future__ import annotations
from typing import Union
from .base import OneOfBaseModel
from .non_deletion_incident import NonDeletionIncident
from .deletion_incident import DeletionIncident


class IncidentGuard(OneOfBaseModel):
    class_list = {
        "NonDeletionIncident": NonDeletionIncident,
        "DeletionIncident": DeletionIncident,
    }


Incident = Union[NonDeletionIncident, DeletionIncident]
