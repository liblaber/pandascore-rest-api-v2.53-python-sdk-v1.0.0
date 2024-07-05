# OwTeamsService

A list of all methods in the `OwTeamsService` service. Click on the method name to view detailed information about that method.

| Methods                       | Description                            |
| :---------------------------- | :------------------------------------- |
| [get_ow_teams](#get_ow_teams) | List teams for the Overwatch videogame |

## get_ow_teams

List teams for the Overwatch videogame

- HTTP Method: `GET`
- Endpoint: `/ow/teams`

**Parameters**

| Name     | Type                                                | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverOwTeams](../models/FilterOverOwTeams.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverOwTeams](../models/RangeOverOwTeams.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverOwTeams](../models/SearchOverOwTeams.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Team]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverOwTeams, RangeOverOwTeams, SearchOverOwTeams

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverOwTeams(
    acronym=[
        "id veniam n"
    ],
    id_=[
        1
    ],
    location=[
        "aliquip irur"
    ],
    modified_at=[
        "minim"
    ],
    name=[
        "do con"
    ],
    slug=[
        "80k9"
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverOwTeams(
    acronym=[
        "proident"
    ],
    id_=[
        8
    ],
    location=[
        "idnon"
    ],
    modified_at=[
        "ipsum"
    ],
    name=[
        "ipsum e"
    ],
    slug=[
        "fm8k4nq2"
    ]
)
sort=[
    ""
]
search=SearchOverOwTeams(
    acronym="veniam",
    location="ex ea",
    name="qui pariatur",
    slug="g2m"
)
page=1

result = sdk.ow_teams.get_ow_teams(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
