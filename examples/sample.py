# This file was generated by liblab | https://liblab.com/

from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import (
    FilterOverAdditionIncidents,
    RangeOverAdditionIncidents,
)

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN", base_url=Environment.DEFAULT.value, timeout=10000
)
filter = FilterOverAdditionIncidents(
    id_=[9], modified_at=["labore nul"], opponents_filled=False
)
range = RangeOverAdditionIncidents(id_=[9], modified_at=["id a"])
sort = [""]
page = 1
type_ = [""]
videogame = [1]

result = sdk.incidents.get_additions(
    filter=filter,
    range=range,
    sort=sort,
    page=page,
    per_page=50,
    type_=type_,
    since="mollit magna no",
    videogame=videogame,
)

print(result)
