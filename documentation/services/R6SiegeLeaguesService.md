# R6SiegeLeaguesService

A list of all methods in the `R6SiegeLeaguesService` service. Click on the method name to view detailed information about that method.

| Methods                                     | Description                    |
| :------------------------------------------ | :----------------------------- |
| [get_r6siege_leagues](#get_r6siege_leagues) | List Rainbow Six Siege leagues |

## get_r6siege_leagues

List Rainbow Six Siege leagues

- HTTP Method: `GET`
- Endpoint: `/r6siege/leagues`

**Parameters**

| Name     | Type                                                              | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverR6SiegeLeagues](../models/FilterOverR6SiegeLeagues.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverR6SiegeLeagues](../models/RangeOverR6SiegeLeagues.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                         | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverR6SiegeLeagues](../models/SearchOverR6SiegeLeagues.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                         | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                               | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[League]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverR6SiegeLeagues, RangeOverR6SiegeLeagues, SearchOverR6SiegeLeagues

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverR6SiegeLeagues(
    id_=[
        7
    ],
    modified_at=[
        "officia ame"
    ],
    name=[
        "eiusmod eu"
    ],
    slug=[
        "3"
    ],
    url=[
        "non r"
    ]
)
range=RangeOverR6SiegeLeagues(
    id_=[
        1
    ],
    modified_at=[
        "ipsum"
    ],
    name=[
        "fugiat"
    ],
    slug=[
        "of0uk"
    ],
    url=[
        "in ex"
    ]
)
sort=[
    ""
]
search=SearchOverR6SiegeLeagues(
    name="aute id",
    slug="goj",
    url="quis in nulla"
)
page=1

result = sdk.r6_siege_leagues.get_r6siege_leagues(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
