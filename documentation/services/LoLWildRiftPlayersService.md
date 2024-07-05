# LoLWildRiftPlayersService

A list of all methods in the `LoLWildRiftPlayersService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description                                  |
| :------------------------------------------------------ | :------------------------------------------- |
| [get_lol_wild_rift_players](#get_lol_wild_rift_players) | List players for the LoL Wild Rift videogame |

## get_lol_wild_rift_players

List players for the LoL Wild Rift videogame

- HTTP Method: `GET`
- Endpoint: `/lol-wild-rift/players`

**Parameters**

| Name     | Type                                                                      | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLolWildRiftPlayers](../models/FilterOverLolWildRiftPlayers.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLolWildRiftPlayers](../models/RangeOverLolWildRiftPlayers.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLolWildRiftPlayers](../models/SearchOverLolWildRiftPlayers.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Player]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverLolWildRiftPlayers, RangeOverLolWildRiftPlayers, SearchOverLolWildRiftPlayers

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverLolWildRiftPlayers(
    active=True,
    birthday=[
        "officia est c"
    ],
    first_name=[
        "nulla nostrud "
    ],
    id_=[
        4
    ],
    last_name=[
        "ut ex"
    ],
    modified_at=[
        "Ut"
    ],
    name=[
        "consequat"
    ],
    nationality=[
        "magna U"
    ],
    role=[
        "nostrud"
    ],
    slug=[
        "b6thv_mwydr"
    ],
    team_id=[
        3
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverLolWildRiftPlayers(
    birthday=[
        "elit "
    ],
    first_name=[
        "exercitation "
    ],
    id_=[
        5
    ],
    last_name=[
        "laboris deser"
    ],
    modified_at=[
        "ir"
    ],
    name=[
        "aliqua lab"
    ],
    nationality=[
        "dolor qui"
    ],
    role=[
        "ut et dolore"
    ],
    slug=[
        "-a6c4qb2o"
    ]
)
sort=[
    ""
]
search=SearchOverLolWildRiftPlayers(
    birthday="sintamet sed ",
    first_name="ullamco",
    last_name="consect",
    name="sunt deser",
    nationality="exercit",
    role="laborum",
    slug="9"
)
page=1

result = sdk.lo_l_wild_rift_players.get_lol_wild_rift_players(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
