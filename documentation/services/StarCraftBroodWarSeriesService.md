# StarCraftBroodWarSeriesService

A list of all methods in the `StarCraftBroodWarSeriesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                             | Description                                       |
| :---------------------------------------------------------------------------------- | :------------------------------------------------ |
| [get_starcraft_brood_war_series](#get_starcraft_brood_war_series)                   | List series for the StarCraft Brood War videogame |
| [get_starcraft_brood_war_series_past](#get_starcraft_brood_war_series_past)         | List past StarCraft Brood War series              |
| [get_starcraft_brood_war_series_running](#get_starcraft_brood_war_series_running)   | List running StarCraft Brood War series           |
| [get_starcraft_brood_war_series_upcoming](#get_starcraft_brood_war_series_upcoming) | List upcoming StarCraft Brood War series          |

## get_starcraft_brood_war_series

List series for the StarCraft Brood War videogame

- HTTP Method: `GET`
- Endpoint: `/starcraft-brood-war/series`

**Parameters**

| Name     | Type                                                                                | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraftBroodWarSeries](../models/FilterOverStarcraftBroodWarSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraftBroodWarSeries](../models/RangeOverStarcraftBroodWarSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraftBroodWarSeries](../models/SearchOverStarcraftBroodWarSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverStarcraftBroodWarSeries, RangeOverStarcraftBroodWarSeries, SearchOverStarcraftBroodWarSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverStarcraftBroodWarSeries(
    begin_at=[
        "D"
    ],
    end_at=[
        "e"
    ],
    id_=[
        9
    ],
    league_id=[
        6
    ],
    modified_at=[
        "a"
    ],
    name=[
        "laborum offi"
    ],
    season=[
        "dolor"
    ],
    slug=[
        "s4shus"
    ],
    videogame_title=[
        10
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
range=RangeOverStarcraftBroodWarSeries(
    begin_at=[
        "dolor"
    ],
    end_at=[
        "ut volu"
    ],
    id_=[
        7
    ],
    league_id=[
        6
    ],
    modified_at=[
        "enim in l"
    ],
    name=[
        "Ut Lorem"
    ],
    season=[
        "exadipisicing v"
    ],
    slug=[
        "exz4jb3a"
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
search=SearchOverStarcraftBroodWarSeries(
    name="nostrud labo",
    season="occaecat do ",
    slug="k",
    winner_type="Player"
)
page=1

result = sdk.star_craft_brood_war_series.get_starcraft_brood_war_series(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_starcraft_brood_war_series_past

List past StarCraft Brood War series

- HTTP Method: `GET`
- Endpoint: `/starcraft-brood-war/series/past`

**Parameters**

| Name     | Type                                                                                | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraftBroodWarSeries](../models/FilterOverStarcraftBroodWarSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraftBroodWarSeries](../models/RangeOverStarcraftBroodWarSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraftBroodWarSeries](../models/SearchOverStarcraftBroodWarSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverStarcraftBroodWarSeries, RangeOverStarcraftBroodWarSeries, SearchOverStarcraftBroodWarSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverStarcraftBroodWarSeries(
    begin_at=[
        "D"
    ],
    end_at=[
        "e"
    ],
    id_=[
        9
    ],
    league_id=[
        6
    ],
    modified_at=[
        "a"
    ],
    name=[
        "laborum offi"
    ],
    season=[
        "dolor"
    ],
    slug=[
        "s4shus"
    ],
    videogame_title=[
        10
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
range=RangeOverStarcraftBroodWarSeries(
    begin_at=[
        "dolor"
    ],
    end_at=[
        "ut volu"
    ],
    id_=[
        7
    ],
    league_id=[
        6
    ],
    modified_at=[
        "enim in l"
    ],
    name=[
        "Ut Lorem"
    ],
    season=[
        "exadipisicing v"
    ],
    slug=[
        "exz4jb3a"
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
search=SearchOverStarcraftBroodWarSeries(
    name="nostrud labo",
    season="occaecat do ",
    slug="k",
    winner_type="Player"
)
page=1

result = sdk.star_craft_brood_war_series.get_starcraft_brood_war_series_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_starcraft_brood_war_series_running

List running StarCraft Brood War series

- HTTP Method: `GET`
- Endpoint: `/starcraft-brood-war/series/running`

**Parameters**

| Name     | Type                                                                                | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraftBroodWarSeries](../models/FilterOverStarcraftBroodWarSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraftBroodWarSeries](../models/RangeOverStarcraftBroodWarSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraftBroodWarSeries](../models/SearchOverStarcraftBroodWarSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverStarcraftBroodWarSeries, RangeOverStarcraftBroodWarSeries, SearchOverStarcraftBroodWarSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverStarcraftBroodWarSeries(
    begin_at=[
        "D"
    ],
    end_at=[
        "e"
    ],
    id_=[
        9
    ],
    league_id=[
        6
    ],
    modified_at=[
        "a"
    ],
    name=[
        "laborum offi"
    ],
    season=[
        "dolor"
    ],
    slug=[
        "s4shus"
    ],
    videogame_title=[
        10
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
range=RangeOverStarcraftBroodWarSeries(
    begin_at=[
        "dolor"
    ],
    end_at=[
        "ut volu"
    ],
    id_=[
        7
    ],
    league_id=[
        6
    ],
    modified_at=[
        "enim in l"
    ],
    name=[
        "Ut Lorem"
    ],
    season=[
        "exadipisicing v"
    ],
    slug=[
        "exz4jb3a"
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
search=SearchOverStarcraftBroodWarSeries(
    name="nostrud labo",
    season="occaecat do ",
    slug="k",
    winner_type="Player"
)
page=1

result = sdk.star_craft_brood_war_series.get_starcraft_brood_war_series_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_starcraft_brood_war_series_upcoming

List upcoming StarCraft Brood War series

- HTTP Method: `GET`
- Endpoint: `/starcraft-brood-war/series/upcoming`

**Parameters**

| Name     | Type                                                                                | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraftBroodWarSeries](../models/FilterOverStarcraftBroodWarSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraftBroodWarSeries](../models/RangeOverStarcraftBroodWarSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraftBroodWarSeries](../models/SearchOverStarcraftBroodWarSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverStarcraftBroodWarSeries, RangeOverStarcraftBroodWarSeries, SearchOverStarcraftBroodWarSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverStarcraftBroodWarSeries(
    begin_at=[
        "D"
    ],
    end_at=[
        "e"
    ],
    id_=[
        9
    ],
    league_id=[
        6
    ],
    modified_at=[
        "a"
    ],
    name=[
        "laborum offi"
    ],
    season=[
        "dolor"
    ],
    slug=[
        "s4shus"
    ],
    videogame_title=[
        10
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
range=RangeOverStarcraftBroodWarSeries(
    begin_at=[
        "dolor"
    ],
    end_at=[
        "ut volu"
    ],
    id_=[
        7
    ],
    league_id=[
        6
    ],
    modified_at=[
        "enim in l"
    ],
    name=[
        "Ut Lorem"
    ],
    season=[
        "exadipisicing v"
    ],
    slug=[
        "exz4jb3a"
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
search=SearchOverStarcraftBroodWarSeries(
    name="nostrud labo",
    season="occaecat do ",
    slug="k",
    winner_type="Player"
)
page=1

result = sdk.star_craft_brood_war_series.get_starcraft_brood_war_series_upcoming(
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
