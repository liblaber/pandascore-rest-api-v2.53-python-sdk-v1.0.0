# LoLWildRiftLeaguesService

A list of all methods in the `LoLWildRiftLeaguesService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description                |
| :------------------------------------------------------ | :------------------------- |
| [get_lol_wild_rift_leagues](#get_lol_wild_rift_leagues) | List LoL Wild Rift leagues |

## get_lol_wild_rift_leagues

List LoL Wild Rift leagues

- HTTP Method: `GET`
- Endpoint: `/lol-wild-rift/leagues`

**Parameters**

| Name     | Type                                                                      | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLolWildRiftLeagues](../models/FilterOverLolWildRiftLeagues.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLolWildRiftLeagues](../models/RangeOverLolWildRiftLeagues.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLolWildRiftLeagues](../models/SearchOverLolWildRiftLeagues.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[League]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverLolWildRiftLeagues, RangeOverLolWildRiftLeagues, SearchOverLolWildRiftLeagues

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverLolWildRiftLeagues(
    id_=[
        10
    ],
    modified_at=[
        "con"
    ],
    name=[
        "ipsum in deseru"
    ],
    slug=[
        "64acfo"
    ],
    url=[
        "Duis s"
    ]
)
range=RangeOverLolWildRiftLeagues(
    id_=[
        6
    ],
    modified_at=[
        "est "
    ],
    name=[
        "tempor d"
    ],
    slug=[
        "pebmkxsgt4"
    ],
    url=[
        "dolore eiusmod"
    ]
)
sort=[
    ""
]
search=SearchOverLolWildRiftLeagues(
    name="nisi tempor",
    slug="u9dhqun9",
    url="adipisicin"
)
page=1

result = sdk.lo_l_wild_rift_leagues.get_lol_wild_rift_leagues(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
