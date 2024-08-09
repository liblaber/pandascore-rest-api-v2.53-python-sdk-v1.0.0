# This file was generated by liblab | https://liblab.com/

from enum import Enum


class IncidentDeletionReasonDeleted(Enum):
    """An enumeration representing different categories.

    :cvar MODELDELETED: "Model deleted"
    :vartype MODELDELETED: str
    """

    MODELDELETED = "Model deleted"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, IncidentDeletionReasonDeleted._member_map_.values())
        )