# RlLeaguesService

A list of all methods in the `RlLeaguesService` service. Click on the method name to view detailed information about that method.

| Methods                           | Description     |
| :-------------------------------- | :-------------- |
| [get_rl_leagues](#get_rl_leagues) | List RL leagues |

## get_rl_leagues

List RL leagues

- HTTP Method: `GET`
- Endpoint: `/rl/leagues`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverRlLeagues](../models/FilterOverRlLeagues.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverRlLeagues](../models/RangeOverRlLeagues.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverRlLeagues](../models/SearchOverRlLeagues.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[League]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverRlLeagues, RangeOverRlLeagues, SearchOverRlLeagues

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverRlLeagues(
    id_=[
        4
    ],
    modified_at=[
        "et esse dolor"
    ],
    name=[
        "tempor ve"
    ],
    slug=[
        "w"
    ],
    url=[
        "dolor e"
    ]
)
range=RangeOverRlLeagues(
    id_=[
        10
    ],
    modified_at=[
        "oc"
    ],
    name=[
        "Lorem"
    ],
    slug=[
        "riigw33s"
    ],
    url=[
        "consecte"
    ]
)
sort=[
    ""
]
search=SearchOverRlLeagues(
    name="ullamco",
    slug="9_4i02v",
    url="adipisicing sun"
)
page=1

result = sdk.rl_leagues.get_rl_leagues(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
