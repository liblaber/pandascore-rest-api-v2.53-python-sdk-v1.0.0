# StarCraft2SeriesService

A list of all methods in the `StarCraft2SeriesService` service. Click on the method name to view detailed information about that method.

| Methods                                                             | Description                               |
| :------------------------------------------------------------------ | :---------------------------------------- |
| [get_starcraft_2_series](#get_starcraft_2_series)                   | List series for the StarCraft 2 videogame |
| [get_starcraft_2_series_past](#get_starcraft_2_series_past)         | List past StarCraft 2 series              |
| [get_starcraft_2_series_running](#get_starcraft_2_series_running)   | List running StarCraft 2 series           |
| [get_starcraft_2_series_upcoming](#get_starcraft_2_series_upcoming) | List upcoming StarCraft 2 series          |

## get_starcraft_2_series

List series for the StarCraft 2 videogame

- HTTP Method: `GET`
- Endpoint: `/starcraft-2/series`

**Parameters**

| Name     | Type                                                                  | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraft2Series](../models/FilterOverStarcraft2Series.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraft2Series](../models/RangeOverStarcraft2Series.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraft2Series](../models/SearchOverStarcraft2Series.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverStarcraft2Series, RangeOverStarcraft2Series, SearchOverStarcraft2Series

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverStarcraft2Series(
    begin_at=[
        "id commodo dolo"
    ],
    end_at=[
        "id labore"
    ],
    id_=[
        5
    ],
    league_id=[
        1
    ],
    modified_at=[
        "laboris Exce"
    ],
    name=[
        "utdeserunt c"
    ],
    season=[
        "labore"
    ],
    slug=[
        "ci"
    ],
    videogame_title=[
        8
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ],
    year=[
        None
    ]
)
range=RangeOverStarcraft2Series(
    begin_at=[
        "in des"
    ],
    end_at=[
        "cup"
    ],
    id_=[
        5
    ],
    league_id=[
        10
    ],
    modified_at=[
        "nostru"
    ],
    name=[
        "aliquip"
    ],
    season=[
        "do consecte"
    ],
    slug=[
        "4nb7"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ],
    year=[
        None
    ]
)
sort=[
    ""
]
search=SearchOverStarcraft2Series(
    name="occae",
    season="esse id rep",
    slug="l3b",
    winner_type="Player"
)
page=1

result = sdk.star_craft_2_series.get_starcraft_2_series(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_starcraft_2_series_past

List past StarCraft 2 series

- HTTP Method: `GET`
- Endpoint: `/starcraft-2/series/past`

**Parameters**

| Name     | Type                                                                  | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraft2Series](../models/FilterOverStarcraft2Series.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraft2Series](../models/RangeOverStarcraft2Series.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraft2Series](../models/SearchOverStarcraft2Series.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverStarcraft2Series, RangeOverStarcraft2Series, SearchOverStarcraft2Series

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverStarcraft2Series(
    begin_at=[
        "id commodo dolo"
    ],
    end_at=[
        "id labore"
    ],
    id_=[
        5
    ],
    league_id=[
        1
    ],
    modified_at=[
        "laboris Exce"
    ],
    name=[
        "utdeserunt c"
    ],
    season=[
        "labore"
    ],
    slug=[
        "ci"
    ],
    videogame_title=[
        8
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ],
    year=[
        None
    ]
)
range=RangeOverStarcraft2Series(
    begin_at=[
        "in des"
    ],
    end_at=[
        "cup"
    ],
    id_=[
        5
    ],
    league_id=[
        10
    ],
    modified_at=[
        "nostru"
    ],
    name=[
        "aliquip"
    ],
    season=[
        "do consecte"
    ],
    slug=[
        "4nb7"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ],
    year=[
        None
    ]
)
sort=[
    ""
]
search=SearchOverStarcraft2Series(
    name="occae",
    season="esse id rep",
    slug="l3b",
    winner_type="Player"
)
page=1

result = sdk.star_craft_2_series.get_starcraft_2_series_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_starcraft_2_series_running

List running StarCraft 2 series

- HTTP Method: `GET`
- Endpoint: `/starcraft-2/series/running`

**Parameters**

| Name     | Type                                                                  | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraft2Series](../models/FilterOverStarcraft2Series.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraft2Series](../models/RangeOverStarcraft2Series.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraft2Series](../models/SearchOverStarcraft2Series.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverStarcraft2Series, RangeOverStarcraft2Series, SearchOverStarcraft2Series

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverStarcraft2Series(
    begin_at=[
        "id commodo dolo"
    ],
    end_at=[
        "id labore"
    ],
    id_=[
        5
    ],
    league_id=[
        1
    ],
    modified_at=[
        "laboris Exce"
    ],
    name=[
        "utdeserunt c"
    ],
    season=[
        "labore"
    ],
    slug=[
        "ci"
    ],
    videogame_title=[
        8
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ],
    year=[
        None
    ]
)
range=RangeOverStarcraft2Series(
    begin_at=[
        "in des"
    ],
    end_at=[
        "cup"
    ],
    id_=[
        5
    ],
    league_id=[
        10
    ],
    modified_at=[
        "nostru"
    ],
    name=[
        "aliquip"
    ],
    season=[
        "do consecte"
    ],
    slug=[
        "4nb7"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ],
    year=[
        None
    ]
)
sort=[
    ""
]
search=SearchOverStarcraft2Series(
    name="occae",
    season="esse id rep",
    slug="l3b",
    winner_type="Player"
)
page=1

result = sdk.star_craft_2_series.get_starcraft_2_series_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_starcraft_2_series_upcoming

List upcoming StarCraft 2 series

- HTTP Method: `GET`
- Endpoint: `/starcraft-2/series/upcoming`

**Parameters**

| Name     | Type                                                                  | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraft2Series](../models/FilterOverStarcraft2Series.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraft2Series](../models/RangeOverStarcraft2Series.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraft2Series](../models/SearchOverStarcraft2Series.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverStarcraft2Series, RangeOverStarcraft2Series, SearchOverStarcraft2Series

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverStarcraft2Series(
    begin_at=[
        "id commodo dolo"
    ],
    end_at=[
        "id labore"
    ],
    id_=[
        5
    ],
    league_id=[
        1
    ],
    modified_at=[
        "laboris Exce"
    ],
    name=[
        "utdeserunt c"
    ],
    season=[
        "labore"
    ],
    slug=[
        "ci"
    ],
    videogame_title=[
        8
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ],
    year=[
        None
    ]
)
range=RangeOverStarcraft2Series(
    begin_at=[
        "in des"
    ],
    end_at=[
        "cup"
    ],
    id_=[
        5
    ],
    league_id=[
        10
    ],
    modified_at=[
        "nostru"
    ],
    name=[
        "aliquip"
    ],
    season=[
        "do consecte"
    ],
    slug=[
        "4nb7"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ],
    year=[
        None
    ]
)
sort=[
    ""
]
search=SearchOverStarcraft2Series(
    name="occae",
    season="esse id rep",
    slug="l3b",
    winner_type="Player"
)
page=1

result = sdk.star_craft_2_series.get_starcraft_2_series_upcoming(
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
