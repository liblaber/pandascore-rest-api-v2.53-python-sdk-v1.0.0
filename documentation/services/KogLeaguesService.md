# KogLeaguesService

A list of all methods in the `KogLeaguesService` service. Click on the method name to view detailed information about that method.

| Methods                             | Description                |
| :---------------------------------- | :------------------------- |
| [get_kog_leagues](#get_kog_leagues) | List King of Glory leagues |

## get_kog_leagues

List King of Glory leagues

- HTTP Method: `GET`
- Endpoint: `/kog/leagues`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverKogLeagues](../models/FilterOverKogLeagues.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverKogLeagues](../models/RangeOverKogLeagues.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverKogLeagues](../models/SearchOverKogLeagues.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[League]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverKogLeagues, RangeOverKogLeagues, SearchOverKogLeagues

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverKogLeagues(
    id_=[
        5
    ],
    modified_at=[
        "minim ut"
    ],
    name=[
        "Duisut et"
    ],
    slug=[
        "stg990v"
    ],
    url=[
        "deserun"
    ]
)
range=RangeOverKogLeagues(
    id_=[
        4
    ],
    modified_at=[
        "Duis do"
    ],
    name=[
        "elit "
    ],
    slug=[
        "hbcg22xoj"
    ],
    url=[
        "consect"
    ]
)
sort=[
    ""
]
search=SearchOverKogLeagues(
    name="et ut",
    slug=":o1vt",
    url="amet magna"
)
page=1

result = sdk.kog_leagues.get_kog_leagues(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
