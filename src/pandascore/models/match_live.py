from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class MatchLive(BaseModel):
    """MatchLive

    :param opens_at: opens_at
    :type opens_at: str
    :param supported: Whether live is supported
    :type supported: bool
    :param url: url
    :type url: str
    """

    def __init__(self, opens_at: str, supported: bool, url: str):
        self.opens_at = opens_at
        self.supported = supported
        self.url = url
