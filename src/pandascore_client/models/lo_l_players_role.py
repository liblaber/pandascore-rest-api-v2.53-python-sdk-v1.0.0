# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .lo_l_players_role_detail import LoLPlayersRoleDetail


@JsonMap({})
class LoLPlayersRole(BaseModel):
    """LoLPlayersRole

    :param adc: adc
    :type adc: LoLPlayersRoleDetail
    :param jun: jun
    :type jun: LoLPlayersRoleDetail
    :param mid: mid
    :type mid: LoLPlayersRoleDetail
    :param sup: sup
    :type sup: LoLPlayersRoleDetail
    :param top: top
    :type top: LoLPlayersRoleDetail
    """

    def __init__(
        self,
        adc: LoLPlayersRoleDetail,
        jun: LoLPlayersRoleDetail,
        mid: LoLPlayersRoleDetail,
        sup: LoLPlayersRoleDetail,
        top: LoLPlayersRoleDetail,
    ):
        """LoLPlayersRole

        :param adc: adc
        :type adc: LoLPlayersRoleDetail
        :param jun: jun
        :type jun: LoLPlayersRoleDetail
        :param mid: mid
        :type mid: LoLPlayersRoleDetail
        :param sup: sup
        :type sup: LoLPlayersRoleDetail
        :param top: top
        :type top: LoLPlayersRoleDetail
        """
        self.adc = self._define_object(adc, LoLPlayersRoleDetail)
        self.jun = self._define_object(jun, LoLPlayersRoleDetail)
        self.mid = self._define_object(mid, LoLPlayersRoleDetail)
        self.sup = self._define_object(sup, LoLPlayersRoleDetail)
        self.top = self._define_object(top, LoLPlayersRoleDetail)
