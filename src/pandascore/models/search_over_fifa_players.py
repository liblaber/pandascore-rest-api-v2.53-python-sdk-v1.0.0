from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class SearchOverFifaPlayers(BaseModel):
    """SearchOverFifaPlayers

    :param birthday: Birth day of the player, `YYYY-MM-DD` format. `null` if unknown. <br/>**Note**: This field is only present for users running the Historical plan or above., defaults to None
    :type birthday: str, optional
    :param first_name: First name of the player. `null` if unknown, defaults to None
    :type first_name: str, optional
    :param last_name: Last name of the player. `null` if unknown, defaults to None
    :type last_name: str, optional
    :param name: Professional name of the player, defaults to None
    :type name: str, optional
    :param nationality: Country code matching the nationality of the player according to the ISO 3166-1 standard (Alpha-2 code). <br/>In addition to the standard, the `XK` code is used for Kosovo. <br/>`null` if unknown, defaults to None
    :type nationality: str, optional
    :param role: Role/position of the player. Field value varies depending on the video game.`null` if unknown. <br/>**Note**: role is only available for DotA 2, League of Legends, and Overwatch players. <br/>`null` for other video games., defaults to None
    :type role: str, optional
    :param slug: Unique, human-readable identifier for the player. <br/>`id` and `slug` can be used interchangeably throughout the API., defaults to None
    :type slug: str, optional
    """

    def __init__(
        self,
        birthday: str = None,
        first_name: str = None,
        last_name: str = None,
        name: str = None,
        nationality: str = None,
        role: str = None,
        slug: str = None,
    ):
        if birthday is not None:
            self.birthday = birthday
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if name is not None:
            self.name = name
        if nationality is not None:
            self.nationality = nationality
        if role is not None:
            self.role = role
        if slug is not None:
            self.slug = self._pattern_matching(slug, "^[a-z0-9_-]+$", "slug")
