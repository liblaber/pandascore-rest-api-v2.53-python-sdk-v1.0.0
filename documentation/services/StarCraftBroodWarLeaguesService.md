# StarCraftBroodWarLeaguesService

A list of all methods in the `StarCraftBroodWarLeaguesService` service. Click on the method name to view detailed information about that method.

| Methods                                                             | Description                      |
| :------------------------------------------------------------------ | :------------------------------- |
| [get_starcraft_brood_war_leagues](#get_starcraft_brood_war_leagues) | List StarCraft Brood War leagues |

## get_starcraft_brood_war_leagues

List StarCraft Brood War leagues

- HTTP Method: `GET`
- Endpoint: `/starcraft-brood-war/leagues`

**Parameters**

| Name     | Type                                                                                  | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraftBroodWarLeagues](../models/FilterOverStarcraftBroodWarLeagues.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraftBroodWarLeagues](../models/RangeOverStarcraftBroodWarLeagues.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraftBroodWarLeagues](../models/SearchOverStarcraftBroodWarLeagues.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[League]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverStarcraftBroodWarLeagues, RangeOverStarcraftBroodWarLeagues, SearchOverStarcraftBroodWarLeagues

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverStarcraftBroodWarLeagues(
    id_=[
        7
    ],
    modified_at=[
        "magna "
    ],
    name=[
        "ea cu"
    ],
    slug=[
        "zf_27"
    ],
    url=[
        "cillum labore "
    ]
)
range=RangeOverStarcraftBroodWarLeagues(
    id_=[
        6
    ],
    modified_at=[
        "reprehender"
    ],
    name=[
        "sintelit"
    ],
    slug=[
        "xa9vcblu"
    ],
    url=[
        "dolore non"
    ]
)
sort=[
    ""
]
search=SearchOverStarcraftBroodWarLeagues(
    name="ex dolore do",
    slug="4-9",
    url="nulla "
)
page=1

result = sdk.star_craft_brood_war_leagues.get_starcraft_brood_war_leagues(
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
