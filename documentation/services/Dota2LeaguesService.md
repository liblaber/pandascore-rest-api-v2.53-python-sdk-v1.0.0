# Dota2LeaguesService

A list of all methods in the `Dota2LeaguesService` service. Click on the method name to view detailed information about that method.

| Methods                                 | Description        |
| :-------------------------------------- | :----------------- |
| [get_dota2_leagues](#get_dota2_leagues) | List Dota2 leagues |

## get_dota2_leagues

List Dota2 leagues

- HTTP Method: `GET`
- Endpoint: `/dota2/leagues`

**Parameters**

| Name     | Type                                                          | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverDota2Leagues](../models/FilterOverDota2Leagues.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverDota2Leagues](../models/RangeOverDota2Leagues.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverDota2Leagues](../models/SearchOverDota2Leagues.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[League]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverDota2Leagues, RangeOverDota2Leagues, SearchOverDota2Leagues

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverDota2Leagues(
    id_=[
        9
    ],
    modified_at=[
        "culpa"
    ],
    name=[
        "elit in in n"
    ],
    slug=[
        "a5y:26qlmo4"
    ],
    url=[
        "consect"
    ]
)
range=RangeOverDota2Leagues(
    id_=[
        7
    ],
    modified_at=[
        "reprehende"
    ],
    name=[
        "eiusmod"
    ],
    slug=[
        "p8"
    ],
    url=[
        "pariatur irure"
    ]
)
sort=[
    ""
]
search=SearchOverDota2Leagues(
    name="culpa dolor p",
    slug="jby04j-4f",
    url="laborum magna"
)
page=1

result = sdk.dota2_leagues.get_dota2_leagues(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
