from pandascore import Pandascore, Environment
from pandascore.models import FilterOverAdditionIncidents, RangeOverAdditionIncidents

sdk = Pandascore(access_token="YOUR_ACCESS_TOKEN", base_url=Environment.DEFAULT.value)
filter = FilterOverAdditionIncidents(
    id_=[7], modified_at=["dolor adipi"], opponents_filled=True
)
range = RangeOverAdditionIncidents(id_=[7], modified_at=["exer"])
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
    since="labore dolore",
    videogame=videogame,
)

print(result)
