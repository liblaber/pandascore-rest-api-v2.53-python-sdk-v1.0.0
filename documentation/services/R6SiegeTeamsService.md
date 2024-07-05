# R6SiegeTeamsService

A list of all methods in the `R6SiegeTeamsService` service. Click on the method name to view detailed information about that method.

| Methods                                 | Description                                    |
| :-------------------------------------- | :--------------------------------------------- |
| [get_r6siege_teams](#get_r6siege_teams) | List teams for the Rainbow Six Siege videogame |

## get_r6siege_teams

List teams for the Rainbow Six Siege videogame

- HTTP Method: `GET`
- Endpoint: `/r6siege/teams`

**Parameters**

| Name     | Type                                                          | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverR6SiegeTeams](../models/FilterOverR6SiegeTeams.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverR6SiegeTeams](../models/RangeOverR6SiegeTeams.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverR6SiegeTeams](../models/SearchOverR6SiegeTeams.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Team]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverR6SiegeTeams, RangeOverR6SiegeTeams, SearchOverR6SiegeTeams

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverR6SiegeTeams(
    acronym=[
        "consectetur"
    ],
    id_=[
        8
    ],
    location=[
        "velit "
    ],
    modified_at=[
        "en"
    ],
    name=[
        "ex Duis "
    ],
    slug=[
        "r9v3ujvx81f"
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverR6SiegeTeams(
    acronym=[
        "esse et"
    ],
    id_=[
        6
    ],
    location=[
        "dolore q"
    ],
    modified_at=[
        "do reprehenderi"
    ],
    name=[
        "Duis temp"
    ],
    slug=[
        "qny5q82pn"
    ]
)
sort=[
    ""
]
search=SearchOverR6SiegeTeams(
    acronym="culpa",
    location="nisi volup",
    name="in fugiat ma",
    slug="neuh"
)
page=1

result = sdk.r6_siege_teams.get_r6siege_teams(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
