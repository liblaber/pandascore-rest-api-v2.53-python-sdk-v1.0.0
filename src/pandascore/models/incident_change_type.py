from enum import Enum


class IncidentChangeType(Enum):
    """An enumeration representing different categories.

    :cvar CREATION: "creation"
    :vartype CREATION: str
    :cvar DELETION: "deletion"
    :vartype DELETION: str
    :cvar UPDATE: "update"
    :vartype UPDATE: str
    """

    CREATION = "creation"
    DELETION = "deletion"
    UPDATE = "update"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, IncidentChangeType._member_map_.values()))
