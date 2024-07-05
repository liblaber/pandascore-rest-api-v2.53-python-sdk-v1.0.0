# ValorantPlayersService

A list of all methods in the `ValorantPlayersService` service. Click on the method name to view detailed information about that method.

| Methods                                       | Description                             |
| :-------------------------------------------- | :-------------------------------------- |
| [get_valorant_players](#get_valorant_players) | List players for the Valorant videogame |

## get_valorant_players

List players for the Valorant videogame

- HTTP Method: `GET`
- Endpoint: `/valorant/players`

**Parameters**

| Name     | Type                                                                | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverValorantPlayers](../models/FilterOverValorantPlayers.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverValorantPlayers](../models/RangeOverValorantPlayers.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverValorantPlayers](../models/SearchOverValorantPlayers.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Player]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverValorantPlayers, RangeOverValorantPlayers, SearchOverValorantPlayers

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverValorantPlayers(
    active=False,
    birthday=[
        "utirure"
    ],
    first_name=[
        "cillu"
    ],
    id_=[
        4
    ],
    last_name=[
        "estquis"
    ],
    modified_at=[
        "amet do"
    ],
    name=[
        "in eu volupta"
    ],
    nationality=[
        "occaec"
    ],
    role=[
        "culpa ut n"
    ],
    slug=[
        "8xpf"
    ],
    team_id=[
        9
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverValorantPlayers(
    birthday=[
        "ipsum"
    ],
    first_name=[
        "reprehend"
    ],
    id_=[
        5
    ],
    last_name=[
        "in volu"
    ],
    modified_at=[
        "cupidata"
    ],
    name=[
        "reprehenderi"
    ],
    nationality=[
        "officia"
    ],
    role=[
        "sed mollit "
    ],
    slug=[
        "m961qf"
    ]
)
sort=[
    ""
]
search=SearchOverValorantPlayers(
    birthday="ad anim",
    first_name="adipisicing d",
    last_name="id dol",
    name="ad pariat",
    nationality="officia co",
    role="eu tempor",
    slug="s"
)
page=1

result = sdk.valorant_players.get_valorant_players(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
