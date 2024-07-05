# ValorantLeaguesService

A list of all methods in the `ValorantLeaguesService` service. Click on the method name to view detailed information about that method.

| Methods                                       | Description           |
| :-------------------------------------------- | :-------------------- |
| [get_valorant_leagues](#get_valorant_leagues) | List Valorant leagues |

## get_valorant_leagues

List Valorant leagues

- HTTP Method: `GET`
- Endpoint: `/valorant/leagues`

**Parameters**

| Name     | Type                                                                | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverValorantLeagues](../models/FilterOverValorantLeagues.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverValorantLeagues](../models/RangeOverValorantLeagues.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverValorantLeagues](../models/SearchOverValorantLeagues.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[League]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverValorantLeagues, RangeOverValorantLeagues, SearchOverValorantLeagues

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverValorantLeagues(
    id_=[
        5
    ],
    modified_at=[
        "ipsum culpa"
    ],
    name=[
        "non ut d"
    ],
    slug=[
        "lp1bvttjv"
    ],
    url=[
        "amet non"
    ]
)
range=RangeOverValorantLeagues(
    id_=[
        8
    ],
    modified_at=[
        "fugiat"
    ],
    name=[
        "Lorem non cup"
    ],
    slug=[
        "223ylq"
    ],
    url=[
        "consequat"
    ]
)
sort=[
    ""
]
search=SearchOverValorantLeagues(
    name="ad officia e",
    slug="6_1gmcelnb",
    url="Lorem"
)
page=1

result = sdk.valorant_leagues.get_valorant_leagues(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
