from enum import Enum


class IncidentDeletionReasonDeleted(Enum):
    """An enumeration representing different categories.

    :cvar MODEL_DELETED: "Model deleted"
    :vartype MODEL_DELETED: str
    """

    MODEL_DELETED = "Model deleted"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, IncidentDeletionReasonDeleted._member_map_.values())
        )
