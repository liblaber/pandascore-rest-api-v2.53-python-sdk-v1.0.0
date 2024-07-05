# RlTeamsService

A list of all methods in the `RlTeamsService` service. Click on the method name to view detailed information about that method.

| Methods                       | Description                                |
| :---------------------------- | :----------------------------------------- |
| [get_rl_teams](#get_rl_teams) | List teams for the Rocket League videogame |

## get_rl_teams

List teams for the Rocket League videogame

- HTTP Method: `GET`
- Endpoint: `/rl/teams`

**Parameters**

| Name     | Type                                                | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverRlTeams](../models/FilterOverRlTeams.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverRlTeams](../models/RangeOverRlTeams.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverRlTeams](../models/SearchOverRlTeams.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Team]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverRlTeams, RangeOverRlTeams, SearchOverRlTeams

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverRlTeams(
    acronym=[
        "aliquip nisi ex"
    ],
    id_=[
        8
    ],
    location=[
        "nisi do irur"
    ],
    modified_at=[
        "exerci"
    ],
    name=[
        "tempor ei"
    ],
    slug=[
        "b7dt84"
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverRlTeams(
    acronym=[
        "sunt Lorem id q"
    ],
    id_=[
        8
    ],
    location=[
        "nulla "
    ],
    modified_at=[
        "et"
    ],
    name=[
        "ut aliqua v"
    ],
    slug=[
        "6lb1cn3ttr"
    ]
)
sort=[
    ""
]
search=SearchOverRlTeams(
    acronym="dolore ",
    location="dolore cupidat",
    name="dolore ut",
    slug="q"
)
page=1

result = sdk.rl_teams.get_rl_teams(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
