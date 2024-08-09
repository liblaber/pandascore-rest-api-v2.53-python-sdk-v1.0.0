# Dota2TeamsService

A list of all methods in the `Dota2TeamsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                             | Description                                           |
| :---------------------------------------------------------------------------------- | :---------------------------------------------------- |
| [get_dota2_series_serie_id_or_slug_teams](#get_dota2_series_serie_id_or_slug_teams) | List teams for the Dota 2 videogame for a given serie |
| [get_dota2_teams](#get_dota2_teams)                                                 | List teams for the Dota 2 videogame                   |

## get_dota2_series_serie_id_or_slug_teams

List teams for the Dota 2 videogame for a given serie

- HTTP Method: `GET`
- Endpoint: `/dota2/series/{serie_id_or_slug}/teams`

**Parameters**

| Name             | Type                                                      | Required | Description                                                                                                                                         |
| :--------------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| serie_id_or_slug | [SerieIdOrSlug](../models/SerieIdOrSlug.md)               | ✅       | A serie ID or slug                                                                                                                                  |
| filter           | [FilterOverDota2Teams](../models/FilterOverDota2Teams.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range            | [RangeOverDota2Teams](../models/RangeOverDota2Teams.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort             | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search           | [SearchOverDota2Teams](../models/SearchOverDota2Teams.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page             | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page         | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Team]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverDota2Teams, RangeOverDota2Teams, SearchOverDota2Teams

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
serie_id_or_slug=10
filter=FilterOverDota2Teams(
    acronym=[
        "molli"
    ],
    id_=[
        3
    ],
    location=[
        "qui dolore"
    ],
    modified_at=[
        "id"
    ],
    name=[
        "commodo ex"
    ],
    slug=[
        "8h6y1-yo"
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverDota2Teams(
    acronym=[
        "ut vel"
    ],
    id_=[
        10
    ],
    location=[
        "ut minim"
    ],
    modified_at=[
        "veniam mo"
    ],
    name=[
        "idelit exercita"
    ],
    slug=[
        "psh"
    ]
)
sort=[
    ""
]
search=SearchOverDota2Teams(
    acronym="ullamco",
    location="in ex",
    name="mollit co",
    slug="7oiow"
)
page=1

result = sdk.dota2_teams.get_dota2_series_serie_id_or_slug_teams(
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

## get_dota2_teams

List teams for the Dota 2 videogame

- HTTP Method: `GET`
- Endpoint: `/dota2/teams`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverDota2Teams](../models/FilterOverDota2Teams.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverDota2Teams](../models/RangeOverDota2Teams.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverDota2Teams](../models/SearchOverDota2Teams.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Team]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverDota2Teams, RangeOverDota2Teams, SearchOverDota2Teams

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverDota2Teams(
    acronym=[
        "molli"
    ],
    id_=[
        3
    ],
    location=[
        "qui dolore"
    ],
    modified_at=[
        "id"
    ],
    name=[
        "commodo ex"
    ],
    slug=[
        "8h6y1-yo"
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverDota2Teams(
    acronym=[
        "ut vel"
    ],
    id_=[
        10
    ],
    location=[
        "ut minim"
    ],
    modified_at=[
        "veniam mo"
    ],
    name=[
        "idelit exercita"
    ],
    slug=[
        "psh"
    ]
)
sort=[
    ""
]
search=SearchOverDota2Teams(
    acronym="ullamco",
    location="in ex",
    name="mollit co",
    slug="7oiow"
)
page=1

result = sdk.dota2_teams.get_dota2_teams(
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
