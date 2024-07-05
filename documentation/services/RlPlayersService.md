# RlPlayersService

A list of all methods in the `RlPlayersService` service. Click on the method name to view detailed information about that method.

| Methods                           | Description                                  |
| :-------------------------------- | :------------------------------------------- |
| [get_rl_players](#get_rl_players) | List players for the Rocket League videogame |

## get_rl_players

List players for the Rocket League videogame

- HTTP Method: `GET`
- Endpoint: `/rl/players`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverRlPlayers](../models/FilterOverRlPlayers.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverRlPlayers](../models/RangeOverRlPlayers.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverRlPlayers](../models/SearchOverRlPlayers.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Player]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverRlPlayers, RangeOverRlPlayers, SearchOverRlPlayers

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverRlPlayers(
    active=False,
    birthday=[
        "utet ips"
    ],
    first_name=[
        "qui of"
    ],
    id_=[
        1
    ],
    last_name=[
        "ullamco co"
    ],
    modified_at=[
        "in cil"
    ],
    name=[
        "sed minim ullam"
    ],
    nationality=[
        "dolore ullamco "
    ],
    role=[
        "officia fu"
    ],
    slug=[
        "_av9a"
    ],
    team_id=[
        5
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverRlPlayers(
    birthday=[
        "enim nulla Lor"
    ],
    first_name=[
        "velit d"
    ],
    id_=[
        2
    ],
    last_name=[
        "nulla co"
    ],
    modified_at=[
        "adipisicing"
    ],
    name=[
        "cupidatat "
    ],
    nationality=[
        "voluptate pa"
    ],
    role=[
        "ipsum labore"
    ],
    slug=[
        "ng9rq9"
    ]
)
sort=[
    ""
]
search=SearchOverRlPlayers(
    birthday="elit Duis",
    first_name="irure",
    last_name="Lorem",
    name="tempor cup",
    nationality="fugiat",
    role="reprehenderit",
    slug="rm8qqej7eqa"
)
page=1

result = sdk.rl_players.get_rl_players(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
