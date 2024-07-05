# KogTeamsService

A list of all methods in the `KogTeamsService` service. Click on the method name to view detailed information about that method.

| Methods                         | Description                                |
| :------------------------------ | :----------------------------------------- |
| [get_kog_teams](#get_kog_teams) | List teams for the King of Glory videogame |

## get_kog_teams

List teams for the King of Glory videogame

- HTTP Method: `GET`
- Endpoint: `/kog/teams`

**Parameters**

| Name     | Type                                                  | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverKogTeams](../models/FilterOverKogTeams.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverKogTeams](../models/RangeOverKogTeams.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverKogTeams](../models/SearchOverKogTeams.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Team]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverKogTeams, RangeOverKogTeams, SearchOverKogTeams

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverKogTeams(
    acronym=[
        "animad voluptat"
    ],
    id_=[
        1
    ],
    location=[
        "dolore p"
    ],
    modified_at=[
        "ad ipsu"
    ],
    name=[
        "occaecat eli"
    ],
    slug=[
        "fez92"
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverKogTeams(
    acronym=[
        "fugiat tem"
    ],
    id_=[
        9
    ],
    location=[
        "nonvelit"
    ],
    modified_at=[
        "ut aute do"
    ],
    name=[
        "commodo"
    ],
    slug=[
        "3"
    ]
)
sort=[
    ""
]
search=SearchOverKogTeams(
    acronym="ullamco",
    location="et nisi occ",
    name="non Duis lab",
    slug="466cd0us"
)
page=1

result = sdk.kog_teams.get_kog_teams(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
