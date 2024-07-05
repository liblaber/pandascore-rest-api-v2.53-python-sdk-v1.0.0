# LoLPlayersService

A list of all methods in the `LoLPlayersService` service. Click on the method name to view detailed information about that method.

| Methods                             | Description                                      |
| :---------------------------------- | :----------------------------------------------- |
| [get_lol_players](#get_lol_players) | List players for the League of Legends videogame |

## get_lol_players

List players for the League of Legends videogame

- HTTP Method: `GET`
- Endpoint: `/lol/players`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLoLPlayers](../models/FilterOverLoLPlayers.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLoLPlayers](../models/RangeOverLoLPlayers.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLoLPlayers](../models/SearchOverLoLPlayers.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Player]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverLoLPlayers, RangeOverLoLPlayers, SearchOverLoLPlayers

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverLoLPlayers(
    active=False,
    birthday=[
        "aliqui"
    ],
    first_name=[
        "occaecat"
    ],
    id_=[
        2
    ],
    last_name=[
        "inaliqua"
    ],
    modified_at=[
        "dolor"
    ],
    name=[
        "consequ"
    ],
    nationality=[
        "sint ali"
    ],
    role=[
        "aliqui"
    ],
    slug=[
        "kzhfi-"
    ],
    team_id=[
        3
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverLoLPlayers(
    birthday=[
        "sint Duis magna"
    ],
    first_name=[
        "elit Ut Du"
    ],
    id_=[
        7
    ],
    last_name=[
        "consequat "
    ],
    modified_at=[
        "commo"
    ],
    name=[
        "exercit"
    ],
    nationality=[
        "in Duis o"
    ],
    role=[
        "fugia"
    ],
    slug=[
        "pv-4ummx_k"
    ]
)
sort=[
    ""
]
search=SearchOverLoLPlayers(
    birthday="enim ",
    first_name="amet en",
    last_name="eu ea",
    name="sed sit off",
    nationality="sit veni",
    role="amet sit",
    slug="5pa"
)
page=1

result = sdk.lo_l_players.get_lol_players(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
