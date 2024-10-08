# This file was generated by liblab | https://liblab.com/

from enum import Enum
from typing import Any
from ...models.utils.base_model import BaseModel


def extract_original_data(data: Any) -> Any:
    """
    Extracts the original data from internal models and enums.

    :param Any data: The data to be extracted.
    :return: The extracted data.
    :rtype: Any
    """
    if data is None:
        return None

    data_type = type(data)

    if issubclass(data_type, BaseModel):
        return data._map()

    if issubclass(data_type, Enum):
        return data.value

    if issubclass(data_type, list):
        return [extract_original_data(item) for item in data]

    return data
