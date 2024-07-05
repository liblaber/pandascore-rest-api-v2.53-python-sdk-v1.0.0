# CodmwTeamsService

A list of all methods in the `CodmwTeamsService` service. Click on the method name to view detailed information about that method.

| Methods                             | Description                        |
| :---------------------------------- | :--------------------------------- |
| [get_codmw_teams](#get_codmw_teams) | List teams for the CODMW videogame |

## get_codmw_teams

List teams for the CODMW videogame

- HTTP Method: `GET`
- Endpoint: `/codmw/teams`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCodmwTeams](../models/FilterOverCodmwTeams.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCodmwTeams](../models/RangeOverCodmwTeams.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCodmwTeams](../models/SearchOverCodmwTeams.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Team]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverCodmwTeams, RangeOverCodmwTeams, SearchOverCodmwTeams

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverCodmwTeams(
    acronym=[
        "proident nost"
    ],
    id_=[
        8
    ],
    location=[
        "proident ci"
    ],
    modified_at=[
        "ad n"
    ],
    name=[
        "elit dolor "
    ],
    slug=[
        "ht33com0"
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverCodmwTeams(
    acronym=[
        "fugiat dolor"
    ],
    id_=[
        5
    ],
    location=[
        "voluptate"
    ],
    modified_at=[
        "d"
    ],
    name=[
        "elit "
    ],
    slug=[
        "2cfhfozcpfi"
    ]
)
sort=[
    ""
]
search=SearchOverCodmwTeams(
    acronym="occaecat ess",
    location="incididunt temp",
    name="laborum mi",
    slug="6"
)
page=1

result = sdk.codmw_teams.get_codmw_teams(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
