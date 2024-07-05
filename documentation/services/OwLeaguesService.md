# OwLeaguesService

A list of all methods in the `OwLeaguesService` service. Click on the method name to view detailed information about that method.

| Methods                           | Description            |
| :-------------------------------- | :--------------------- |
| [get_ow_leagues](#get_ow_leagues) | List Overwatch leagues |

## get_ow_leagues

List Overwatch leagues

- HTTP Method: `GET`
- Endpoint: `/ow/leagues`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverOwLeagues](../models/FilterOverOwLeagues.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverOwLeagues](../models/RangeOverOwLeagues.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverOwLeagues](../models/SearchOverOwLeagues.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[League]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverOwLeagues, RangeOverOwLeagues, SearchOverOwLeagues

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverOwLeagues(
    id_=[
        8
    ],
    modified_at=[
        "nisi amet Duis"
    ],
    name=[
        "est volup"
    ],
    slug=[
        ":1qpid"
    ],
    url=[
        "eiusmod"
    ]
)
range=RangeOverOwLeagues(
    id_=[
        5
    ],
    modified_at=[
        "dolor velit e"
    ],
    name=[
        "velit "
    ],
    slug=[
        "n"
    ],
    url=[
        "eiusmod c"
    ]
)
sort=[
    ""
]
search=SearchOverOwLeagues(
    name="non est v",
    slug="ubub2mh0_",
    url="sunt o"
)
page=1

result = sdk.ow_leagues.get_ow_leagues(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
