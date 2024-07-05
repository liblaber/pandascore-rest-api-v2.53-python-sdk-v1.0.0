# CounterStrikePlayersService

A list of all methods in the `CounterStrikePlayersService` service. Click on the method name to view detailed information about that method.

| Methods                               | Description                                   |
| :------------------------------------ | :-------------------------------------------- |
| [get_csgo_players](#get_csgo_players) | List players for the Counter-Strike videogame |

## get_csgo_players

List players for the Counter-Strike videogame

- HTTP Method: `GET`
- Endpoint: `/csgo/players`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCsgoPlayers](../models/FilterOverCsgoPlayers.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCsgoPlayers](../models/RangeOverCsgoPlayers.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCsgoPlayers](../models/SearchOverCsgoPlayers.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Player]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverCsgoPlayers, RangeOverCsgoPlayers, SearchOverCsgoPlayers

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverCsgoPlayers(
    active=True,
    birthday=[
        "ad aliquip"
    ],
    first_name=[
        "incididunt do f"
    ],
    id_=[
        2
    ],
    last_name=[
        "ut sint lab"
    ],
    modified_at=[
        "reprehenderit"
    ],
    name=[
        "exercitatio"
    ],
    nationality=[
        "cillum"
    ],
    role=[
        "non ex"
    ],
    slug=[
        "g2yu"
    ],
    team_id=[
        6
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverCsgoPlayers(
    birthday=[
        "sunt volupt"
    ],
    first_name=[
        "eiusmod"
    ],
    id_=[
        3
    ],
    last_name=[
        "reprehen"
    ],
    modified_at=[
        "quis la"
    ],
    name=[
        "inid "
    ],
    nationality=[
        "velit enim ess"
    ],
    role=[
        "aliqua "
    ],
    slug=[
        "mc9l"
    ]
)
sort=[
    ""
]
search=SearchOverCsgoPlayers(
    birthday="nostrud proid",
    first_name="proident l",
    last_name="officia sed dol",
    name="ullamco",
    nationality="qui Exc",
    role="nostrud ",
    slug="lkhim402t5d"
)
page=1

result = sdk.counter_strike_players.get_csgo_players(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
