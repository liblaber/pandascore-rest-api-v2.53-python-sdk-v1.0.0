from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class RangeOverLoLChampions(BaseModel):
    """RangeOverLoLChampions

    :param armor: armor, defaults to None
    :type armor: List[float], optional
    :param armorperlevel: armorperlevel, defaults to None
    :type armorperlevel: List[float], optional
    :param attackdamage: attackdamage, defaults to None
    :type attackdamage: List[float], optional
    :param attackdamageperlevel: attackdamageperlevel, defaults to None
    :type attackdamageperlevel: List[float], optional
    :param attackrange: attackrange, defaults to None
    :type attackrange: List[float], optional
    :param attackspeedoffset: attackspeedoffset, defaults to None
    :type attackspeedoffset: List[float], optional
    :param attackspeedperlevel: attackspeedperlevel, defaults to None
    :type attackspeedperlevel: List[float], optional
    :param crit: crit, defaults to None
    :type crit: List[float], optional
    :param critperlevel: critperlevel, defaults to None
    :type critperlevel: List[float], optional
    :param hp: hp, defaults to None
    :type hp: List[float], optional
    :param hpperlevel: hpperlevel, defaults to None
    :type hpperlevel: List[float], optional
    :param hpregen: hpregen, defaults to None
    :type hpregen: List[float], optional
    :param hpregenperlevel: hpregenperlevel, defaults to None
    :type hpregenperlevel: List[float], optional
    :param id_: id_, defaults to None
    :type id_: List[int], optional
    :param movespeed: movespeed, defaults to None
    :type movespeed: List[float], optional
    :param mp: mp, defaults to None
    :type mp: List[float], optional
    :param mpperlevel: mpperlevel, defaults to None
    :type mpperlevel: List[float], optional
    :param mpregen: mpregen, defaults to None
    :type mpregen: List[float], optional
    :param mpregenperlevel: mpregenperlevel, defaults to None
    :type mpregenperlevel: List[float], optional
    :param name: name, defaults to None
    :type name: List[str], optional
    :param spellblock: spellblock, defaults to None
    :type spellblock: List[float], optional
    :param spellblockperlevel: spellblockperlevel, defaults to None
    :type spellblockperlevel: List[float], optional
    """

    def __init__(
        self,
        armor: List[float] = None,
        armorperlevel: List[float] = None,
        attackdamage: List[float] = None,
        attackdamageperlevel: List[float] = None,
        attackrange: List[float] = None,
        attackspeedoffset: List[float] = None,
        attackspeedperlevel: List[float] = None,
        crit: List[float] = None,
        critperlevel: List[float] = None,
        hp: List[float] = None,
        hpperlevel: List[float] = None,
        hpregen: List[float] = None,
        hpregenperlevel: List[float] = None,
        id_: List[int] = None,
        movespeed: List[float] = None,
        mp: List[float] = None,
        mpperlevel: List[float] = None,
        mpregen: List[float] = None,
        mpregenperlevel: List[float] = None,
        name: List[str] = None,
        spellblock: List[float] = None,
        spellblockperlevel: List[float] = None,
    ):
        if armor is not None:
            self.armor = armor
        if armorperlevel is not None:
            self.armorperlevel = armorperlevel
        if attackdamage is not None:
            self.attackdamage = attackdamage
        if attackdamageperlevel is not None:
            self.attackdamageperlevel = attackdamageperlevel
        if attackrange is not None:
            self.attackrange = attackrange
        if attackspeedoffset is not None:
            self.attackspeedoffset = attackspeedoffset
        if attackspeedperlevel is not None:
            self.attackspeedperlevel = attackspeedperlevel
        if crit is not None:
            self.crit = crit
        if critperlevel is not None:
            self.critperlevel = critperlevel
        if hp is not None:
            self.hp = hp
        if hpperlevel is not None:
            self.hpperlevel = hpperlevel
        if hpregen is not None:
            self.hpregen = hpregen
        if hpregenperlevel is not None:
            self.hpregenperlevel = hpregenperlevel
        if id_ is not None:
            self.id_ = id_
        if movespeed is not None:
            self.movespeed = movespeed
        if mp is not None:
            self.mp = mp
        if mpperlevel is not None:
            self.mpperlevel = mpperlevel
        if mpregen is not None:
            self.mpregen = mpregen
        if mpregenperlevel is not None:
            self.mpregenperlevel = mpregenperlevel
        if name is not None:
            self.name = name
        if spellblock is not None:
            self.spellblock = spellblock
        if spellblockperlevel is not None:
            self.spellblockperlevel = spellblockperlevel
