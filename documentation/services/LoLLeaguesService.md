# LoLLeaguesService

A list of all methods in the `LoLLeaguesService` service. Click on the method name to view detailed information about that method.

| Methods                             | Description                    |
| :---------------------------------- | :----------------------------- |
| [get_lol_leagues](#get_lol_leagues) | List League of Legends leagues |

## get_lol_leagues

List League of Legends leagues

- HTTP Method: `GET`
- Endpoint: `/lol/leagues`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLoLLeagues](../models/FilterOverLoLLeagues.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLoLLeagues](../models/RangeOverLoLLeagues.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLoLLeagues](../models/SearchOverLoLLeagues.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[League]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverLoLLeagues, RangeOverLoLLeagues, SearchOverLoLLeagues

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverLoLLeagues(
    id_=[
        6
    ],
    modified_at=[
        "esse"
    ],
    name=[
        "laboris sint "
    ],
    slug=[
        "-xon8"
    ],
    url=[
        "dolor"
    ]
)
range=RangeOverLoLLeagues(
    id_=[
        2
    ],
    modified_at=[
        "aute null"
    ],
    name=[
        "aliquip dolor"
    ],
    slug=[
        "yn-"
    ],
    url=[
        "veniam Exce"
    ]
)
sort=[
    ""
]
search=SearchOverLoLLeagues(
    name="culpa",
    slug="z7j32:",
    url="magna"
)
page=1

result = sdk.lo_l_leagues.get_lol_leagues(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
