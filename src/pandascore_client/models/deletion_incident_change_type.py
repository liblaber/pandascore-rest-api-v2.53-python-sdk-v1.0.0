# This file was generated by liblab | https://liblab.com/

from enum import Enum


class DeletionIncidentChangeType(Enum):
    """An enumeration representing different categories.

    :cvar DELETION: "deletion"
    :vartype DELETION: str
    """

    DELETION = "deletion"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, DeletionIncidentChangeType._member_map_.values())
        )
