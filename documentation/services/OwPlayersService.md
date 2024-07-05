# OwPlayersService

A list of all methods in the `OwPlayersService` service. Click on the method name to view detailed information about that method.

| Methods                           | Description                              |
| :-------------------------------- | :--------------------------------------- |
| [get_ow_players](#get_ow_players) | List players for the Overwatch videogame |

## get_ow_players

List players for the Overwatch videogame

- HTTP Method: `GET`
- Endpoint: `/ow/players`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverOwPlayers](../models/FilterOverOwPlayers.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverOwPlayers](../models/RangeOverOwPlayers.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverOwPlayers](../models/SearchOverOwPlayers.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Player]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverOwPlayers, RangeOverOwPlayers, SearchOverOwPlayers

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverOwPlayers(
    active=False,
    birthday=[
        "cillum d"
    ],
    first_name=[
        "adipis"
    ],
    id_=[
        1
    ],
    last_name=[
        "culpa aute"
    ],
    modified_at=[
        "aute Excepteu"
    ],
    name=[
        "non ad consecte"
    ],
    nationality=[
        "aliqua"
    ],
    role=[
        "sintelit repreh"
    ],
    slug=[
        "nrpd3a8jm_x"
    ],
    team_id=[
        8
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverOwPlayers(
    birthday=[
        "commodo ul"
    ],
    first_name=[
        "aute sin"
    ],
    id_=[
        9
    ],
    last_name=[
        "nostrud offi"
    ],
    modified_at=[
        "quis veniam "
    ],
    name=[
        "officia magna"
    ],
    nationality=[
        "dolor Duis"
    ],
    role=[
        "labore"
    ],
    slug=[
        "z334gwyadn"
    ]
)
sort=[
    ""
]
search=SearchOverOwPlayers(
    birthday="aliqua",
    first_name="Ut ex s",
    last_name="magna c",
    name="ut dolore deser",
    nationality="non nulla",
    role="fugiat",
    slug="_rxiiocxfpg"
)
page=1

result = sdk.ow_players.get_ow_players(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
