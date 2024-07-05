# LoLWildRiftTeamsService

A list of all methods in the `LoLWildRiftTeamsService` service. Click on the method name to view detailed information about that method.

| Methods                                             | Description                                |
| :-------------------------------------------------- | :----------------------------------------- |
| [get_lol_wild_rift_teams](#get_lol_wild_rift_teams) | List teams for the LoL Wild Rift videogame |

## get_lol_wild_rift_teams

List teams for the LoL Wild Rift videogame

- HTTP Method: `GET`
- Endpoint: `/lol-wild-rift/teams`

**Parameters**

| Name     | Type                                                                  | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLolWildRiftTeams](../models/FilterOverLolWildRiftTeams.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLolWildRiftTeams](../models/RangeOverLolWildRiftTeams.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLolWildRiftTeams](../models/SearchOverLolWildRiftTeams.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Team]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverLolWildRiftTeams, RangeOverLolWildRiftTeams, SearchOverLolWildRiftTeams

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverLolWildRiftTeams(
    acronym=[
        "eu minim "
    ],
    id_=[
        2
    ],
    location=[
        "non labore"
    ],
    modified_at=[
        "adipisicing"
    ],
    name=[
        "aliquip veniam"
    ],
    slug=[
        "2_"
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverLolWildRiftTeams(
    acronym=[
        "nisi con"
    ],
    id_=[
        8
    ],
    location=[
        "labore al"
    ],
    modified_at=[
        "sunt"
    ],
    name=[
        "esse no"
    ],
    slug=[
        "dct8"
    ]
)
sort=[
    ""
]
search=SearchOverLolWildRiftTeams(
    acronym="sedeius",
    location="quis dese",
    name="elit la",
    slug="sddg9sf44se"
)
page=1

result = sdk.lo_l_wild_rift_teams.get_lol_wild_rift_teams(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
