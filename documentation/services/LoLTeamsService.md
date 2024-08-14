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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLoLTeams, RangeOverLoLTeams, SearchOverLoLTeams

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
serie_id_or_slug=10
filter=FilterOverLoLTeams(
    acronym=[
        "cupidatat"
    ],
    id_=[
        10
    ],
    location=[
        "eu commodo magn"
    ],
    modified_at=[
        "velit sed cons"
    ],
    name=[
        "aliqua ei"
    ],
    slug=[
        "4b"
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverLoLTeams(
    acronym=[
        "in ut sunt"
    ],
    id_=[
        1
    ],
    location=[
        "dolor"
    ],
    modified_at=[
        "labor"
    ],
    name=[
        "veniam sed inci"
    ],
    slug=[
        "pibzwr_n1xc"
    ]
)
sort=[
    ""
]
search=SearchOverLoLTeams(
    acronym="elit id nisi",
    location="incididunt",
    name="sit non ",
    slug="6k_6"
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLoLTeams, RangeOverLoLTeams, SearchOverLoLTeams

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverLoLTeams(
    acronym=[
        "cupidatat"
    ],
    id_=[
        10
    ],
    location=[
        "eu commodo magn"
    ],
    modified_at=[
        "velit sed cons"
    ],
    name=[
        "aliqua ei"
    ],
    slug=[
        "4b"
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverLoLTeams(
    acronym=[
        "in ut sunt"
    ],
    id_=[
        1
    ],
    location=[
        "dolor"
    ],
    modified_at=[
        "labor"
    ],
    name=[
        "veniam sed inci"
    ],
    slug=[
        "pibzwr_n1xc"
    ]
)
sort=[
    ""
]
search=SearchOverLoLTeams(
    acronym="elit id nisi",
    location="incididunt",
    name="sit non ",
    slug="6k_6"
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

<!-- This file was generated by liblab | https://liblab.com/ -->
