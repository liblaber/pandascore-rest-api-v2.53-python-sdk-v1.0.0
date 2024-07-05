# R6SiegePlayersService

A list of all methods in the `R6SiegePlayersService` service. Click on the method name to view detailed information about that method.

| Methods                                     | Description                                      |
| :------------------------------------------ | :----------------------------------------------- |
| [get_r6siege_players](#get_r6siege_players) | List players for the Rainbow Six Siege videogame |

## get_r6siege_players

List players for the Rainbow Six Siege videogame

- HTTP Method: `GET`
- Endpoint: `/r6siege/players`

**Parameters**

| Name     | Type                                                              | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverR6SiegePlayers](../models/FilterOverR6SiegePlayers.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverR6SiegePlayers](../models/RangeOverR6SiegePlayers.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                         | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverR6SiegePlayers](../models/SearchOverR6SiegePlayers.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                         | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                               | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Player]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverR6SiegePlayers, RangeOverR6SiegePlayers, SearchOverR6SiegePlayers

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverR6SiegePlayers(
    active=True,
    birthday=[
        "cillum qui "
    ],
    first_name=[
        "minim est ad"
    ],
    id_=[
        3
    ],
    last_name=[
        "ipsum exercita"
    ],
    modified_at=[
        "occaecat dolor"
    ],
    name=[
        "sitquis"
    ],
    nationality=[
        "reprehenderit o"
    ],
    role=[
        "dolor volupta"
    ],
    slug=[
        "62xq9t_43"
    ],
    team_id=[
        10
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverR6SiegePlayers(
    birthday=[
        "animExcept"
    ],
    first_name=[
        "officia eu"
    ],
    id_=[
        2
    ],
    last_name=[
        "irure"
    ],
    modified_at=[
        "minim"
    ],
    name=[
        "proide"
    ],
    nationality=[
        "amet cillum"
    ],
    role=[
        "inin Duis in "
    ],
    slug=[
        "gdv8ew3"
    ]
)
sort=[
    ""
]
search=SearchOverR6SiegePlayers(
    birthday="eavolup",
    first_name="tempor consecte",
    last_name="nostrud",
    name="commo",
    nationality="Ut culpa no",
    role="elitfugi",
    slug="-"
)
page=1

result = sdk.r6_siege_players.get_r6siege_players(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
