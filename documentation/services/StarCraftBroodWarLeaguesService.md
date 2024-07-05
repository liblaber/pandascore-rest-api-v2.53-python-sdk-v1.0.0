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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverStarcraftBroodWarLeagues, RangeOverStarcraftBroodWarLeagues, SearchOverStarcraftBroodWarLeagues

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverStarcraftBroodWarLeagues(
    id_=[
        4
    ],
    modified_at=[
        "Lorem do"
    ],
    name=[
        "sed consect"
    ],
    slug=[
        "tfs85i93iq5"
    ],
    url=[
        "voluptate"
    ]
)
range=RangeOverStarcraftBroodWarLeagues(
    id_=[
        8
    ],
    modified_at=[
        "irure"
    ],
    name=[
        "incididunt"
    ],
    slug=[
        "zsmt8prh"
    ],
    url=[
        "essequi eni"
    ]
)
sort=[
    ""
]
search=SearchOverStarcraftBroodWarLeagues(
    name="labor",
    slug="z8j72ax",
    url="conse"
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
