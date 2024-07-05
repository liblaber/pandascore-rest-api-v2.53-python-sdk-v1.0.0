# KogPlayersService

A list of all methods in the `KogPlayersService` service. Click on the method name to view detailed information about that method.

| Methods                             | Description                                  |
| :---------------------------------- | :------------------------------------------- |
| [get_kog_players](#get_kog_players) | List players for the King of Glory videogame |

## get_kog_players

List players for the King of Glory videogame

- HTTP Method: `GET`
- Endpoint: `/kog/players`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverKogPlayers](../models/FilterOverKogPlayers.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverKogPlayers](../models/RangeOverKogPlayers.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverKogPlayers](../models/SearchOverKogPlayers.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Player]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverKogPlayers, RangeOverKogPlayers, SearchOverKogPlayers

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverKogPlayers(
    active=True,
    birthday=[
        "aliqua "
    ],
    first_name=[
        "nisi vel"
    ],
    id_=[
        8
    ],
    last_name=[
        "reprehenderit"
    ],
    modified_at=[
        "ullamco ad"
    ],
    name=[
        "labore mi"
    ],
    nationality=[
        "cillum dol"
    ],
    role=[
        "deserunt l"
    ],
    slug=[
        "8ls1qfnjw"
    ],
    team_id=[
        8
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverKogPlayers(
    birthday=[
        "consectetur"
    ],
    first_name=[
        "culpa ad dolor"
    ],
    id_=[
        6
    ],
    last_name=[
        "ipsum"
    ],
    modified_at=[
        "v"
    ],
    name=[
        "aliquip s"
    ],
    nationality=[
        "culpa"
    ],
    role=[
        "enim tempor "
    ],
    slug=[
        "sfdj"
    ]
)
sort=[
    ""
]
search=SearchOverKogPlayers(
    birthday="dolor enim aliq",
    first_name="velit ex cillum",
    last_name="labore cillum ",
    name="occaecat",
    nationality="velit est",
    role="est ex ",
    slug="g"
)
page=1

result = sdk.kog_players.get_kog_players(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
