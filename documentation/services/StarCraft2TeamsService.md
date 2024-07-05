# StarCraft2TeamsService

A list of all methods in the `StarCraft2TeamsService` service. Click on the method name to view detailed information about that method.

| Methods                                         | Description                              |
| :---------------------------------------------- | :--------------------------------------- |
| [get_starcraft_2_teams](#get_starcraft_2_teams) | List teams for the StarCraft 2 videogame |

## get_starcraft_2_teams

List teams for the StarCraft 2 videogame

- HTTP Method: `GET`
- Endpoint: `/starcraft-2/teams`

**Parameters**

| Name     | Type                                                                | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraft2Teams](../models/FilterOverStarcraft2Teams.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraft2Teams](../models/RangeOverStarcraft2Teams.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraft2Teams](../models/SearchOverStarcraft2Teams.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Team]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverStarcraft2Teams, RangeOverStarcraft2Teams, SearchOverStarcraft2Teams

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverStarcraft2Teams(
    acronym=[
        "Lorem al"
    ],
    id_=[
        6
    ],
    location=[
        "id enim velit"
    ],
    modified_at=[
        "exercitation"
    ],
    name=[
        "laboris"
    ],
    slug=[
        "uot369zc"
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverStarcraft2Teams(
    acronym=[
        "commodo"
    ],
    id_=[
        8
    ],
    location=[
        "cillum consequa"
    ],
    modified_at=[
        "ve"
    ],
    name=[
        "dolore exe"
    ],
    slug=[
        "-cu6qrmqbnu"
    ]
)
sort=[
    ""
]
search=SearchOverStarcraft2Teams(
    acronym="et es",
    location="irure cillum o",
    name="et laborum",
    slug="xovp7b"
)
page=1

result = sdk.star_craft_2_teams.get_starcraft_2_teams(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
