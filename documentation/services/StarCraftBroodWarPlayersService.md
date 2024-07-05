# StarCraftBroodWarPlayersService

A list of all methods in the `StarCraftBroodWarPlayersService` service. Click on the method name to view detailed information about that method.

| Methods                                                             | Description                                        |
| :------------------------------------------------------------------ | :------------------------------------------------- |
| [get_starcraft_brood_war_players](#get_starcraft_brood_war_players) | List players for the StarCraft Brood War videogame |

## get_starcraft_brood_war_players

List players for the StarCraft Brood War videogame

- HTTP Method: `GET`
- Endpoint: `/starcraft-brood-war/players`

**Parameters**

| Name     | Type                                                                                  | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraftBroodWarPlayers](../models/FilterOverStarcraftBroodWarPlayers.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraftBroodWarPlayers](../models/RangeOverStarcraftBroodWarPlayers.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraftBroodWarPlayers](../models/SearchOverStarcraftBroodWarPlayers.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Player]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverStarcraftBroodWarPlayers, RangeOverStarcraftBroodWarPlayers, SearchOverStarcraftBroodWarPlayers

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverStarcraftBroodWarPlayers(
    active=True,
    birthday=[
        "esse "
    ],
    first_name=[
        "labore sun"
    ],
    id_=[
        9
    ],
    last_name=[
        "Excepteur non "
    ],
    modified_at=[
        "ci"
    ],
    name=[
        "ipsum ull"
    ],
    nationality=[
        "irure a"
    ],
    role=[
        "in qui"
    ],
    slug=[
        "h78qjfdv4f9"
    ],
    team_id=[
        6
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverStarcraftBroodWarPlayers(
    birthday=[
        "nulla eiusmod"
    ],
    first_name=[
        "nostrud deseru"
    ],
    id_=[
        4
    ],
    last_name=[
        "velit d"
    ],
    modified_at=[
        "reprehenderit "
    ],
    name=[
        "nostrud dol"
    ],
    nationality=[
        "ullamco cons"
    ],
    role=[
        "anim dolor "
    ],
    slug=[
        "-il"
    ]
)
sort=[
    ""
]
search=SearchOverStarcraftBroodWarPlayers(
    birthday="incididunt",
    first_name="ullamco ad ",
    last_name="amet ",
    name="in ut eu non",
    nationality="nostrud c",
    role="in officia eius",
    slug="udfmp76jk"
)
page=1

result = sdk.star_craft_brood_war_players.get_starcraft_brood_war_players(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
