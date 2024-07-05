# LoLTeamsService

A list of all methods in the `LoLTeamsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                         | Description                                                      |
| :------------------------------------------------------------------------------ | :--------------------------------------------------------------- |
| [get_lol_series_serie_id_or_slug_teams](#get_lol_series_serie_id_or_slug_teams) | List teams for the League of Legends videogame for a given serie |
| [get_lol_teams](#get_lol_teams)                                                 | List teams for the League of Legends videogame                   |

## get_lol_series_serie_id_or_slug_teams

List teams for the League of Legends videogame for a given serie

- HTTP Method: `GET`
- Endpoint: `/lol/series/{serie_id_or_slug}/teams`

**Parameters**

| Name             | Type                                                  | Required | Description                                                                                                                                         |
| :--------------- | :---------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| serie_id_or_slug | [SerieIdOrSlug](../models/SerieIdOrSlug.md)           | ✅       | A serie ID or slug                                                                                                                                  |
| filter           | [FilterOverLoLTeams](../models/FilterOverLoLTeams.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range            | [RangeOverLoLTeams](../models/RangeOverLoLTeams.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort             | List[any]                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search           | [SearchOverLoLTeams](../models/SearchOverLoLTeams.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page             | [Page](../models/Page.md)                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page         | int                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Team]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverLoLTeams, RangeOverLoLTeams, SearchOverLoLTeams

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
serie_id_or_slug=3
filter=FilterOverLoLTeams(
    acronym=[
        "esse occ"
    ],
    id_=[
        10
    ],
    location=[
        "incididun"
    ],
    modified_at=[
        "in magna cill"
    ],
    name=[
        "nonlabore ve"
    ],
    slug=[
        "yi7yv02-p"
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverLoLTeams(
    acronym=[
        "exercitati"
    ],
    id_=[
        2
    ],
    location=[
        "ullamco aliqui"
    ],
    modified_at=[
        "i"
    ],
    name=[
        "qui en"
    ],
    slug=[
        "zs_lj653"
    ]
)
sort=[
    ""
]
search=SearchOverLoLTeams(
    acronym="cupidatat sunt ",
    location="dolor",
    name="occaecat sit e",
    slug="tqq"
)
page=1

result = sdk.lo_l_teams.get_lol_series_serie_id_or_slug_teams(
    serie_id_or_slug=serie_id_or_slug,
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_teams

List teams for the League of Legends videogame

- HTTP Method: `GET`
- Endpoint: `/lol/teams`

**Parameters**

| Name     | Type                                                  | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLoLTeams](../models/FilterOverLoLTeams.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLoLTeams](../models/RangeOverLoLTeams.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLoLTeams](../models/SearchOverLoLTeams.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Team]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverLoLTeams, RangeOverLoLTeams, SearchOverLoLTeams

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverLoLTeams(
    acronym=[
        "esse occ"
    ],
    id_=[
        10
    ],
    location=[
        "incididun"
    ],
    modified_at=[
        "in magna cill"
    ],
    name=[
        "nonlabore ve"
    ],
    slug=[
        "yi7yv02-p"
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverLoLTeams(
    acronym=[
        "exercitati"
    ],
    id_=[
        2
    ],
    location=[
        "ullamco aliqui"
    ],
    modified_at=[
        "i"
    ],
    name=[
        "qui en"
    ],
    slug=[
        "zs_lj653"
    ]
)
sort=[
    ""
]
search=SearchOverLoLTeams(
    acronym="cupidatat sunt ",
    location="dolor",
    name="occaecat sit e",
    slug="tqq"
)
page=1

result = sdk.lo_l_teams.get_lol_teams(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
