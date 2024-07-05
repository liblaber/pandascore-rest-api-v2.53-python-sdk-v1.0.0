# Dota2PlayersService

A list of all methods in the `Dota2PlayersService` service. Click on the method name to view detailed information about that method.

| Methods                                 | Description                           |
| :-------------------------------------- | :------------------------------------ |
| [get_dota2_players](#get_dota2_players) | List players for the Dota 2 videogame |

## get_dota2_players

List players for the Dota 2 videogame

- HTTP Method: `GET`
- Endpoint: `/dota2/players`

**Parameters**

| Name     | Type                                                          | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverDota2Players](../models/FilterOverDota2Players.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverDota2Players](../models/RangeOverDota2Players.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverDota2Players](../models/SearchOverDota2Players.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Player]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverDota2Players, RangeOverDota2Players, SearchOverDota2Players

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverDota2Players(
    active=False,
    birthday=[
        "laboru"
    ],
    first_name=[
        "sit vo"
    ],
    id_=[
        6
    ],
    last_name=[
        "voluptate do"
    ],
    modified_at=[
        "Duis irure"
    ],
    name=[
        "minim labor"
    ],
    nationality=[
        "irure vel"
    ],
    role=[
        "minim nisi "
    ],
    slug=[
        "qon4zjb"
    ],
    team_id=[
        7
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverDota2Players(
    birthday=[
        "et dolore"
    ],
    first_name=[
        "nulla"
    ],
    id_=[
        10
    ],
    last_name=[
        "consequat sint"
    ],
    modified_at=[
        "veniam of"
    ],
    name=[
        "nisi et"
    ],
    nationality=[
        "aliquip"
    ],
    role=[
        "id proident"
    ],
    slug=[
        "lk1wtxjz19"
    ]
)
sort=[
    ""
]
search=SearchOverDota2Players(
    birthday="eu ut dolo",
    first_name="exercitation e",
    last_name="adipisi",
    name="exercitation i",
    nationality="quis mollit",
    role="dolore",
    slug="94m30cut8q"
)
page=1

result = sdk.dota2_players.get_dota2_players(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
