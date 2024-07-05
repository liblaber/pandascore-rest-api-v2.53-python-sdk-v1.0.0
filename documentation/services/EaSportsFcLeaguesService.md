# EaSportsFcLeaguesService

A list of all methods in the `EaSportsFcLeaguesService` service. Click on the method name to view detailed information about that method.

| Methods                               | Description               |
| :------------------------------------ | :------------------------ |
| [get_fifa_leagues](#get_fifa_leagues) | List EA Sports FC leagues |

## get_fifa_leagues

List EA Sports FC leagues

- HTTP Method: `GET`
- Endpoint: `/fifa/leagues`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverFifaLeagues](../models/FilterOverFifaLeagues.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverFifaLeagues](../models/RangeOverFifaLeagues.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverFifaLeagues](../models/SearchOverFifaLeagues.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[League]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverFifaLeagues, RangeOverFifaLeagues, SearchOverFifaLeagues

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverFifaLeagues(
    id_=[
        10
    ],
    modified_at=[
        "venia"
    ],
    name=[
        "deserunt "
    ],
    slug=[
        "uj6"
    ],
    url=[
        "dolor minim sit"
    ]
)
range=RangeOverFifaLeagues(
    id_=[
        7
    ],
    modified_at=[
        "veniam c"
    ],
    name=[
        "ipsum"
    ],
    slug=[
        "bytsa"
    ],
    url=[
        "esse c"
    ]
)
sort=[
    ""
]
search=SearchOverFifaLeagues(
    name="sit sint ",
    slug="3vzvwhdo",
    url="dolor adipisi"
)
page=1

result = sdk.ea_sports_fc_leagues.get_fifa_leagues(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
