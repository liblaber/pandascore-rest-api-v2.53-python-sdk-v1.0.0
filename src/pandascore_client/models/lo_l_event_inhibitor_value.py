# This file was generated by liblab | https://liblab.com/

from enum import Enum


class LoLEventInhibitorValue(Enum):
    """An enumeration representing different categories.

    :cvar INHIBITOR: "Inhibitor"
    :vartype INHIBITOR: str
    """

    INHIBITOR = "Inhibitor"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, LoLEventInhibitorValue._member_map_.values())
        )
