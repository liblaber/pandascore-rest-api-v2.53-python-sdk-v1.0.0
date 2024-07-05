# CodmwPlayersService

A list of all methods in the `CodmwPlayersService` service. Click on the method name to view detailed information about that method.

| Methods                                 | Description                          |
| :-------------------------------------- | :----------------------------------- |
| [get_codmw_players](#get_codmw_players) | List players for the CODMW videogame |

## get_codmw_players

List players for the CODMW videogame

- HTTP Method: `GET`
- Endpoint: `/codmw/players`

**Parameters**

| Name     | Type                                                          | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCodmwPlayers](../models/FilterOverCodmwPlayers.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCodmwPlayers](../models/RangeOverCodmwPlayers.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCodmwPlayers](../models/SearchOverCodmwPlayers.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Player]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverCodmwPlayers, RangeOverCodmwPlayers, SearchOverCodmwPlayers

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverCodmwPlayers(
    active=True,
    birthday=[
        "labore "
    ],
    first_name=[
        "ullamco a"
    ],
    id_=[
        9
    ],
    last_name=[
        "est sed "
    ],
    modified_at=[
        "culpa am"
    ],
    name=[
        "ea consectetur "
    ],
    nationality=[
        "fugiat"
    ],
    role=[
        "aliqua anim "
    ],
    slug=[
        "9r5obsn"
    ],
    team_id=[
        10
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverCodmwPlayers(
    birthday=[
        "in magn"
    ],
    first_name=[
        "nulla labor"
    ],
    id_=[
        1
    ],
    last_name=[
        "aliquip sint "
    ],
    modified_at=[
        "laborum"
    ],
    name=[
        "sit anim ips"
    ],
    nationality=[
        "adipisicing fug"
    ],
    role=[
        "nostrud dolo"
    ],
    slug=[
        "e8amjf"
    ]
)
sort=[
    ""
]
search=SearchOverCodmwPlayers(
    birthday="qui sunt",
    first_name="sint eli",
    last_name="veniam nul",
    name="ipsum",
    nationality="in sunt Lor",
    role="proiden",
    slug="fin-mr0cc"
)
page=1

result = sdk.codmw_players.get_codmw_players(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
