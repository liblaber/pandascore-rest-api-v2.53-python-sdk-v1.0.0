# EaSportsFcTeamsService

A list of all methods in the `EaSportsFcTeamsService` service. Click on the method name to view detailed information about that method.

| Methods                           | Description                               |
| :-------------------------------- | :---------------------------------------- |
| [get_fifa_teams](#get_fifa_teams) | List teams for the EA Sports FC videogame |

## get_fifa_teams

List teams for the EA Sports FC videogame

- HTTP Method: `GET`
- Endpoint: `/fifa/teams`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverFifaTeams](../models/FilterOverFifaTeams.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverFifaTeams](../models/RangeOverFifaTeams.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverFifaTeams](../models/SearchOverFifaTeams.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Team]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverFifaTeams, RangeOverFifaTeams, SearchOverFifaTeams

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverFifaTeams(
    acronym=[
        "nisi eni"
    ],
    id_=[
        4
    ],
    location=[
        "Duisdeser"
    ],
    modified_at=[
        "elit"
    ],
    name=[
        "aliqu"
    ],
    slug=[
        "olaxsmx"
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverFifaTeams(
    acronym=[
        "dolor exe"
    ],
    id_=[
        3
    ],
    location=[
        "labore su"
    ],
    modified_at=[
        "dolore in"
    ],
    name=[
        "deserunt"
    ],
    slug=[
        "7"
    ]
)
sort=[
    ""
]
search=SearchOverFifaTeams(
    acronym="ut nostr",
    location="exercita",
    name="aliquip a",
    slug="o_y5we64ij"
)
page=1

result = sdk.ea_sports_fc_teams.get_fifa_teams(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
