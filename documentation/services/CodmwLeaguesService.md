# CodmwLeaguesService

A list of all methods in the `CodmwLeaguesService` service. Click on the method name to view detailed information about that method.

| Methods                                 | Description        |
| :-------------------------------------- | :----------------- |
| [get_codmw_leagues](#get_codmw_leagues) | List CODMW leagues |

## get_codmw_leagues

List CODMW leagues

- HTTP Method: `GET`
- Endpoint: `/codmw/leagues`

**Parameters**

| Name     | Type                                                          | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCodmwLeagues](../models/FilterOverCodmwLeagues.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCodmwLeagues](../models/RangeOverCodmwLeagues.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCodmwLeagues](../models/SearchOverCodmwLeagues.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[League]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverCodmwLeagues, RangeOverCodmwLeagues, SearchOverCodmwLeagues

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverCodmwLeagues(
    id_=[
        3
    ],
    modified_at=[
        "ali"
    ],
    name=[
        "laborum sint"
    ],
    slug=[
        "1u12k9"
    ],
    url=[
        "Ut volupta"
    ]
)
range=RangeOverCodmwLeagues(
    id_=[
        4
    ],
    modified_at=[
        "ut aute Dui"
    ],
    name=[
        "incididunt"
    ],
    slug=[
        "29gqnv7_:9r"
    ],
    url=[
        "nulla"
    ]
)
sort=[
    ""
]
search=SearchOverCodmwLeagues(
    name="incididunt",
    slug="far3r",
    url="consequat "
)
page=1

result = sdk.codmw_leagues.get_codmw_leagues(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
