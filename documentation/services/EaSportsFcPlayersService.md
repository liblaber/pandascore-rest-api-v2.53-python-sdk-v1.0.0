# EaSportsFcPlayersService

A list of all methods in the `EaSportsFcPlayersService` service. Click on the method name to view detailed information about that method.

| Methods                               | Description                                 |
| :------------------------------------ | :------------------------------------------ |
| [get_fifa_players](#get_fifa_players) | List players for the EA Sports FC videogame |

## get_fifa_players

List players for the EA Sports FC videogame

- HTTP Method: `GET`
- Endpoint: `/fifa/players`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverFifaPlayers](../models/FilterOverFifaPlayers.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverFifaPlayers](../models/RangeOverFifaPlayers.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverFifaPlayers](../models/SearchOverFifaPlayers.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Player]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverFifaPlayers, RangeOverFifaPlayers, SearchOverFifaPlayers

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverFifaPlayers(
    active=True,
    birthday=[
        "consect"
    ],
    first_name=[
        "sit de"
    ],
    id_=[
        1
    ],
    last_name=[
        "enim "
    ],
    modified_at=[
        "est l"
    ],
    name=[
        "fugiat dolo"
    ],
    nationality=[
        "etamet"
    ],
    role=[
        "voluptate"
    ],
    slug=[
        "ppuhc5k"
    ],
    team_id=[
        9
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverFifaPlayers(
    birthday=[
        "dolor la"
    ],
    first_name=[
        "dolor"
    ],
    id_=[
        7
    ],
    last_name=[
        "euofficia"
    ],
    modified_at=[
        "laboris d"
    ],
    name=[
        "utest laborum "
    ],
    nationality=[
        "tempor "
    ],
    role=[
        "paria"
    ],
    slug=[
        "x2u"
    ]
)
sort=[
    ""
]
search=SearchOverFifaPlayers(
    birthday="cillum ",
    first_name="et Ut qui in",
    last_name="dolor dolore ma",
    name="proid",
    nationality="sunt in ",
    role="laboris e",
    slug="r68"
)
page=1

result = sdk.ea_sports_fc_players.get_fifa_players(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
