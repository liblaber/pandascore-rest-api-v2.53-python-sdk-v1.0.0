# StarCraftBroodWarTeamsService

A list of all methods in the `StarCraftBroodWarTeamsService` service. Click on the method name to view detailed information about that method.

| Methods                                                         | Description                                      |
| :-------------------------------------------------------------- | :----------------------------------------------- |
| [get_starcraft_brood_war_teams](#get_starcraft_brood_war_teams) | List teams for the StarCraft Brood War videogame |

## get_starcraft_brood_war_teams

List teams for the StarCraft Brood War videogame

- HTTP Method: `GET`
- Endpoint: `/starcraft-brood-war/teams`

**Parameters**

| Name     | Type                                                                              | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraftBroodWarTeams](../models/FilterOverStarcraftBroodWarTeams.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraftBroodWarTeams](../models/RangeOverStarcraftBroodWarTeams.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                         | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraftBroodWarTeams](../models/SearchOverStarcraftBroodWarTeams.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                         | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                               | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Team]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverStarcraftBroodWarTeams, RangeOverStarcraftBroodWarTeams, SearchOverStarcraftBroodWarTeams

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverStarcraftBroodWarTeams(
    acronym=[
        "incid"
    ],
    id_=[
        2
    ],
    location=[
        "qui consequat"
    ],
    modified_at=[
        "in"
    ],
    name=[
        "laboris mag"
    ],
    slug=[
        "d8qsvn2z8g"
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverStarcraftBroodWarTeams(
    acronym=[
        "fugiat volupta"
    ],
    id_=[
        4
    ],
    location=[
        "utin et in dol"
    ],
    modified_at=[
        "au"
    ],
    name=[
        "ut laboris n"
    ],
    slug=[
        "18_oot5j"
    ]
)
sort=[
    ""
]
search=SearchOverStarcraftBroodWarTeams(
    acronym="repre",
    location="eu aliquip ",
    name="in sed e",
    slug="lcxlzxzay"
)
page=1

result = sdk.star_craft_brood_war_teams.get_starcraft_brood_war_teams(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
