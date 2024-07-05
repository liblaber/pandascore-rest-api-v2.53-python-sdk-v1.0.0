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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverStarcraftBroodWarSeries, RangeOverStarcraftBroodWarSeries, SearchOverStarcraftBroodWarSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverStarcraftBroodWarSeries(
    begin_at=[
        "Duis q"
    ],
    end_at=[
        "ex c"
    ],
    id_=[
        1
    ],
    league_id=[
        3
    ],
    modified_at=[
        "occaecat"
    ],
    name=[
        "adipisicing id "
    ],
    season=[
        "nostrud aliq"
    ],
    slug=[
        "v"
    ],
    videogame_title=[
        3
    ],
    winner_id=[
        9
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
        "esse "
    ],
    end_at=[
        "voluptate des"
    ],
    id_=[
        1
    ],
    league_id=[
        8
    ],
    modified_at=[
        "sunt esse"
    ],
    name=[
        "officia in ad "
    ],
    season=[
        "enimin aliq"
    ],
    slug=[
        "7s28hjgdg"
    ],
    winner_id=[
        9
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
    name="dolore",
    season="occaecat",
    slug="ai",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverStarcraftBroodWarSeries, RangeOverStarcraftBroodWarSeries, SearchOverStarcraftBroodWarSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverStarcraftBroodWarSeries(
    begin_at=[
        "Duis q"
    ],
    end_at=[
        "ex c"
    ],
    id_=[
        1
    ],
    league_id=[
        3
    ],
    modified_at=[
        "occaecat"
    ],
    name=[
        "adipisicing id "
    ],
    season=[
        "nostrud aliq"
    ],
    slug=[
        "v"
    ],
    videogame_title=[
        3
    ],
    winner_id=[
        9
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
        "esse "
    ],
    end_at=[
        "voluptate des"
    ],
    id_=[
        1
    ],
    league_id=[
        8
    ],
    modified_at=[
        "sunt esse"
    ],
    name=[
        "officia in ad "
    ],
    season=[
        "enimin aliq"
    ],
    slug=[
        "7s28hjgdg"
    ],
    winner_id=[
        9
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
    name="dolore",
    season="occaecat",
    slug="ai",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverStarcraftBroodWarSeries, RangeOverStarcraftBroodWarSeries, SearchOverStarcraftBroodWarSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverStarcraftBroodWarSeries(
    begin_at=[
        "Duis q"
    ],
    end_at=[
        "ex c"
    ],
    id_=[
        1
    ],
    league_id=[
        3
    ],
    modified_at=[
        "occaecat"
    ],
    name=[
        "adipisicing id "
    ],
    season=[
        "nostrud aliq"
    ],
    slug=[
        "v"
    ],
    videogame_title=[
        3
    ],
    winner_id=[
        9
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
        "esse "
    ],
    end_at=[
        "voluptate des"
    ],
    id_=[
        1
    ],
    league_id=[
        8
    ],
    modified_at=[
        "sunt esse"
    ],
    name=[
        "officia in ad "
    ],
    season=[
        "enimin aliq"
    ],
    slug=[
        "7s28hjgdg"
    ],
    winner_id=[
        9
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
    name="dolore",
    season="occaecat",
    slug="ai",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverStarcraftBroodWarSeries, RangeOverStarcraftBroodWarSeries, SearchOverStarcraftBroodWarSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverStarcraftBroodWarSeries(
    begin_at=[
        "Duis q"
    ],
    end_at=[
        "ex c"
    ],
    id_=[
        1
    ],
    league_id=[
        3
    ],
    modified_at=[
        "occaecat"
    ],
    name=[
        "adipisicing id "
    ],
    season=[
        "nostrud aliq"
    ],
    slug=[
        "v"
    ],
    videogame_title=[
        3
    ],
    winner_id=[
        9
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
        "esse "
    ],
    end_at=[
        "voluptate des"
    ],
    id_=[
        1
    ],
    league_id=[
        8
    ],
    modified_at=[
        "sunt esse"
    ],
    name=[
        "officia in ad "
    ],
    season=[
        "enimin aliq"
    ],
    slug=[
        "7s28hjgdg"
    ],
    winner_id=[
        9
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
    name="dolore",
    season="occaecat",
    slug="ai",
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
