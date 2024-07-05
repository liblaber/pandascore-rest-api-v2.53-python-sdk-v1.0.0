# PubgPlayersService

A list of all methods in the `PubgPlayersService` service. Click on the method name to view detailed information about that method.

| Methods                               | Description                         |
| :------------------------------------ | :---------------------------------- |
| [get_pubg_players](#get_pubg_players) | List players for the PUBG videogame |

## get_pubg_players

List players for the PUBG videogame

- HTTP Method: `GET`
- Endpoint: `/pubg/players`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverPubgPlayers](../models/FilterOverPubgPlayers.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverPubgPlayers](../models/RangeOverPubgPlayers.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverPubgPlayers](../models/SearchOverPubgPlayers.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Player]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverPubgPlayers, RangeOverPubgPlayers, SearchOverPubgPlayers

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverPubgPlayers(
    active=False,
    birthday=[
        "deser"
    ],
    first_name=[
        "labore no"
    ],
    id_=[
        7
    ],
    last_name=[
        "Ut nost"
    ],
    modified_at=[
        "adipisicing an"
    ],
    name=[
        "ipsum ex non"
    ],
    nationality=[
        "culpa offici"
    ],
    role=[
        "ullamco lab"
    ],
    slug=[
        "y6442w1ms0n"
    ],
    team_id=[
        8
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverPubgPlayers(
    birthday=[
        "exercitation"
    ],
    first_name=[
        "consectetur"
    ],
    id_=[
        9
    ],
    last_name=[
        "deserunt sed"
    ],
    modified_at=[
        "cillum do"
    ],
    name=[
        "nisiDuis ips"
    ],
    nationality=[
        "elit irure vel"
    ],
    role=[
        "occaecat "
    ],
    slug=[
        "jns5"
    ]
)
sort=[
    ""
]
search=SearchOverPubgPlayers(
    birthday="dolore Lorem",
    first_name="sit eu",
    last_name="dolore cillum",
    name="labor",
    nationality="repreh",
    role="deseru",
    slug="81jo6q_"
)
page=1

result = sdk.pubg_players.get_pubg_players(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
