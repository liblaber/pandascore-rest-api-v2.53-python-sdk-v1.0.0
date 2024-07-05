from __future__ import annotations
from .utils.json_map import JsonMap
from .base import BaseModel
from .stream_language import StreamLanguage


@JsonMap({})
class Stream(BaseModel):
    """Stream

    :param embed_url: URL to embed in an iframe.
    :type embed_url: str
    :param language: Language alpha-2 code according to ISO 649-1 standard.
    :type language: StreamLanguage
    :param main: Whether it is the main stream. Main stream is always official.
    :type main: bool
    :param official: Whether it is an official broadcast.
    :type official: bool
    :param raw_url: URL to the stream on host website.
    :type raw_url: str
    """

    def __init__(
        self,
        embed_url: str,
        language: StreamLanguage,
        main: bool,
        official: bool,
        raw_url: str,
    ):
        self.embed_url = embed_url
        self.language = self._enum_matching(language, StreamLanguage.list(), "language")
        self.main = main
        self.official = official
        self.raw_url = raw_url
