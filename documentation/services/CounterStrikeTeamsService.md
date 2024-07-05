# CounterStrikeTeamsService

A list of all methods in the `CounterStrikeTeamsService` service. Click on the method name to view detailed information about that method.

| Methods                           | Description                                 |
| :-------------------------------- | :------------------------------------------ |
| [get_csgo_teams](#get_csgo_teams) | List teams for the Counter-Strike videogame |

## get_csgo_teams

List teams for the Counter-Strike videogame

- HTTP Method: `GET`
- Endpoint: `/csgo/teams`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCsgoTeams](../models/FilterOverCsgoTeams.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCsgoTeams](../models/RangeOverCsgoTeams.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCsgoTeams](../models/SearchOverCsgoTeams.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Team]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverCsgoTeams, RangeOverCsgoTeams, SearchOverCsgoTeams

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverCsgoTeams(
    acronym=[
        "labore aute"
    ],
    id_=[
        3
    ],
    location=[
        "nulla "
    ],
    modified_at=[
        "eu dolor adipis"
    ],
    name=[
        "dolor in"
    ],
    slug=[
        "k39-mek"
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverCsgoTeams(
    acronym=[
        "minim ex"
    ],
    id_=[
        8
    ],
    location=[
        "cupidatat repr"
    ],
    modified_at=[
        "ma"
    ],
    name=[
        "veniam amet "
    ],
    slug=[
        "30hvbjnni"
    ]
)
sort=[
    ""
]
search=SearchOverCsgoTeams(
    acronym="id sunt",
    location="exercit",
    name="exercitation ei",
    slug="m6-c2k"
)
page=1

result = sdk.counter_strike_teams.get_csgo_teams(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
