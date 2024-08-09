# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"id_": "id"})
class FilterOverValorantWeapons(BaseModel):
    """FilterOverValorantWeapons

    :param creds: creds, defaults to None
    :type creds: List[float], optional
    :param id_: id_, defaults to None
    :type id_: List[int], optional
    :param name: name, defaults to None
    :type name: List[str], optional
    :param videogame_version: Filter by the names of videogame versions, all versions using `filter[videogame_version]=all`, or by the latest version using `filter[videogame_version]=latest`, defaults to None
    :type videogame_version: any, optional
    """

    def __init__(
        self,
        creds: List[float] = None,
        id_: List[int] = None,
        name: List[str] = None,
        videogame_version: any = None,
    ):
        """FilterOverValorantWeapons

        :param creds: creds, defaults to None
        :type creds: List[float], optional
        :param id_: id_, defaults to None
        :type id_: List[int], optional
        :param name: name, defaults to None
        :type name: List[str], optional
        :param videogame_version: Filter by the names of videogame versions, all versions using `filter[videogame_version]=all`, or by the latest version using `filter[videogame_version]=latest`, defaults to None
        :type videogame_version: any, optional
        """
        if creds is not None:
            self.creds = creds
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if videogame_version is not None:
            self.videogame_version = videogame_version