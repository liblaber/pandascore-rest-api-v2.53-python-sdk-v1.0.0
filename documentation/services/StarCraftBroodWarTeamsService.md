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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverStarcraftBroodWarTeams, RangeOverStarcraftBroodWarTeams, SearchOverStarcraftBroodWarTeams

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverStarcraftBroodWarTeams(
    acronym=[
        "sint co"
    ],
    id_=[
        8
    ],
    location=[
        "ut dolo"
    ],
    modified_at=[
        "iru"
    ],
    name=[
        "cillum e"
    ],
    slug=[
        "m"
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverStarcraftBroodWarTeams(
    acronym=[
        "deserunt a"
    ],
    id_=[
        3
    ],
    location=[
        "sunt aut"
    ],
    modified_at=[
        "deserunt aute"
    ],
    name=[
        "labor"
    ],
    slug=[
        "qt3q1roio"
    ]
)
sort=[
    ""
]
search=SearchOverStarcraftBroodWarTeams(
    acronym="dolore fugia",
    location="dolore cillum",
    name="irure ven",
    slug="j"
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

<!-- This file was generated by liblab | https://liblab.com/ -->
