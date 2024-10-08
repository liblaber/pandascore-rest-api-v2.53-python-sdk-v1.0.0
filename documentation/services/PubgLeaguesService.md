# PubgLeaguesService

A list of all methods in the `PubgLeaguesService` service. Click on the method name to view detailed information about that method.

| Methods                               | Description       |
| :------------------------------------ | :---------------- |
| [get_pubg_leagues](#get_pubg_leagues) | List PUBG leagues |

## get_pubg_leagues

List PUBG leagues

- HTTP Method: `GET`
- Endpoint: `/pubg/leagues`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverPubgLeagues](../models/FilterOverPubgLeagues.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverPubgLeagues](../models/RangeOverPubgLeagues.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverPubgLeagues](../models/SearchOverPubgLeagues.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[League]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverPubgLeagues, RangeOverPubgLeagues, SearchOverPubgLeagues

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverPubgLeagues(
    id_=[
        8
    ],
    modified_at=[
        "ea"
    ],
    name=[
        "ad ex an"
    ],
    slug=[
        "j"
    ],
    url=[
        "proident adi"
    ]
)
range=RangeOverPubgLeagues(
    id_=[
        4
    ],
    modified_at=[
        "in dolore "
    ],
    name=[
        "Lorem do"
    ],
    slug=[
        "d6p5l"
    ],
    url=[
        "ut aut"
    ]
)
sort=[
    ""
]
search=SearchOverPubgLeagues(
    name="officia",
    slug="ue4e",
    url="in eu des"
)
page=1

result = sdk.pubg_leagues.get_pubg_leagues(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
