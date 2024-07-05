# StarCraft2PlayersService

A list of all methods in the `StarCraft2PlayersService` service. Click on the method name to view detailed information about that method.

| Methods                                             | Description                                |
| :-------------------------------------------------- | :----------------------------------------- |
| [get_starcraft_2_players](#get_starcraft_2_players) | List players for the StarCraft 2 videogame |

## get_starcraft_2_players

List players for the StarCraft 2 videogame

- HTTP Method: `GET`
- Endpoint: `/starcraft-2/players`

**Parameters**

| Name     | Type                                                                    | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraft2Players](../models/FilterOverStarcraft2Players.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraft2Players](../models/RangeOverStarcraft2Players.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraft2Players](../models/SearchOverStarcraft2Players.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Player]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverStarcraft2Players, RangeOverStarcraft2Players, SearchOverStarcraft2Players

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverStarcraft2Players(
    active=False,
    birthday=[
        "veniam "
    ],
    first_name=[
        "nulla tempor "
    ],
    id_=[
        6
    ],
    last_name=[
        "dolore"
    ],
    modified_at=[
        "adipisicing"
    ],
    name=[
        "ad des"
    ],
    nationality=[
        "laborum"
    ],
    role=[
        "in voluptat"
    ],
    slug=[
        "o8u3uo"
    ],
    team_id=[
        4
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverStarcraft2Players(
    birthday=[
        "offic"
    ],
    first_name=[
        "mollit officia "
    ],
    id_=[
        9
    ],
    last_name=[
        "dolore r"
    ],
    modified_at=[
        "tempor sint"
    ],
    name=[
        "dolore"
    ],
    nationality=[
        "voluptate "
    ],
    role=[
        "dolore nisi"
    ],
    slug=[
        "fx9vej4y"
    ]
)
sort=[
    ""
]
search=SearchOverStarcraft2Players(
    birthday="qui dolor",
    first_name="nisi do",
    last_name="eiusmod sit con",
    name="in consectet",
    nationality="dolor ",
    role="dolor ad labor",
    slug="8ji0r23axp"
)
page=1

result = sdk.star_craft_2_players.get_starcraft_2_players(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
