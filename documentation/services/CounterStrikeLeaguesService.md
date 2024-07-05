# CounterStrikeLeaguesService

A list of all methods in the `CounterStrikeLeaguesService` service. Click on the method name to view detailed information about that method.

| Methods                               | Description                 |
| :------------------------------------ | :-------------------------- |
| [get_csgo_leagues](#get_csgo_leagues) | List Counter-Strike leagues |

## get_csgo_leagues

List Counter-Strike leagues

- HTTP Method: `GET`
- Endpoint: `/csgo/leagues`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCsgoLeagues](../models/FilterOverCsgoLeagues.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCsgoLeagues](../models/RangeOverCsgoLeagues.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCsgoLeagues](../models/SearchOverCsgoLeagues.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[League]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverCsgoLeagues, RangeOverCsgoLeagues, SearchOverCsgoLeagues

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverCsgoLeagues(
    id_=[
        2
    ],
    modified_at=[
        "exercitatio"
    ],
    name=[
        "ut Duis exercit"
    ],
    slug=[
        "vzce"
    ],
    url=[
        "ad consequat"
    ]
)
range=RangeOverCsgoLeagues(
    id_=[
        1
    ],
    modified_at=[
        "Excepteur"
    ],
    name=[
        "labore deseru"
    ],
    slug=[
        "hhr"
    ],
    url=[
        "ea dolor ame"
    ]
)
sort=[
    ""
]
search=SearchOverCsgoLeagues(
    name="sed veni",
    slug="kipv0xz",
    url="proid"
)
page=1

result = sdk.counter_strike_leagues.get_csgo_leagues(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
