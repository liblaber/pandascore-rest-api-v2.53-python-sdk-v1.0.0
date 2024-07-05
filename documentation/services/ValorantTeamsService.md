# ValorantTeamsService

A list of all methods in the `ValorantTeamsService` service. Click on the method name to view detailed information about that method.

| Methods                                   | Description                           |
| :---------------------------------------- | :------------------------------------ |
| [get_valorant_teams](#get_valorant_teams) | List teams for the Valorant videogame |

## get_valorant_teams

List teams for the Valorant videogame

- HTTP Method: `GET`
- Endpoint: `/valorant/teams`

**Parameters**

| Name     | Type                                                            | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverValorantTeams](../models/FilterOverValorantTeams.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverValorantTeams](../models/RangeOverValorantTeams.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                       | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverValorantTeams](../models/SearchOverValorantTeams.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                       | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                             | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Team]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverValorantTeams, RangeOverValorantTeams, SearchOverValorantTeams

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverValorantTeams(
    acronym=[
        "in dolor"
    ],
    id_=[
        9
    ],
    location=[
        "incididunt "
    ],
    modified_at=[
        "nulla"
    ],
    name=[
        "laborum d"
    ],
    slug=[
        "mequxhp_"
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverValorantTeams(
    acronym=[
        "in ut Duis"
    ],
    id_=[
        8
    ],
    location=[
        "cupidatat"
    ],
    modified_at=[
        "sit min"
    ],
    name=[
        "Duis ut mini"
    ],
    slug=[
        "m5l_ep"
    ]
)
sort=[
    ""
]
search=SearchOverValorantTeams(
    acronym="exercitation ",
    location="aliqua",
    name="adcillum",
    slug="cir"
)
page=1

result = sdk.valorant_teams.get_valorant_teams(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
