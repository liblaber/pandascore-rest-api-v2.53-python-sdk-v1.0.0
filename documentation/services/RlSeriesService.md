# RlSeriesService

A list of all methods in the `RlSeriesService` service. Click on the method name to view detailed information about that method.

| Methods                                           | Description                                 |
| :------------------------------------------------ | :------------------------------------------ |
| [get_rl_series](#get_rl_series)                   | List series for the Rocket League videogame |
| [get_rl_series_past](#get_rl_series_past)         | List past Rocket League series              |
| [get_rl_series_running](#get_rl_series_running)   | List running Rocket League series           |
| [get_rl_series_upcoming](#get_rl_series_upcoming) | List upcoming Rocket League series          |

## get_rl_series

List series for the Rocket League videogame

- HTTP Method: `GET`
- Endpoint: `/rl/series`

**Parameters**

| Name     | Type                                                  | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverRlSeries](../models/FilterOverRlSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverRlSeries](../models/RangeOverRlSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverRlSeries](../models/SearchOverRlSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverRlSeries, RangeOverRlSeries, SearchOverRlSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverRlSeries(
    begin_at=[
        "dolore"
    ],
    end_at=[
        "of"
    ],
    id_=[
        2
    ],
    league_id=[
        5
    ],
    modified_at=[
        "eiusmod"
    ],
    name=[
        "eiusmod"
    ],
    season=[
        "labore ex"
    ],
    slug=[
        "kw-jbm1vmo"
    ],
    videogame_title=[
        6
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
range=RangeOverRlSeries(
    begin_at=[
        "Duis anim p"
    ],
    end_at=[
        "ipsu"
    ],
    id_=[
        7
    ],
    league_id=[
        2
    ],
    modified_at=[
        "elit Duis in"
    ],
    name=[
        "cupidatat"
    ],
    season=[
        "enim id com"
    ],
    slug=[
        "s44cu66"
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
search=SearchOverRlSeries(
    name="irure com",
    season="deseru",
    slug="sb4enl",
    winner_type="Player"
)
page=1

result = sdk.rl_series.get_rl_series(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_rl_series_past

List past Rocket League series

- HTTP Method: `GET`
- Endpoint: `/rl/series/past`

**Parameters**

| Name     | Type                                                  | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverRlSeries](../models/FilterOverRlSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverRlSeries](../models/RangeOverRlSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverRlSeries](../models/SearchOverRlSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverRlSeries, RangeOverRlSeries, SearchOverRlSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverRlSeries(
    begin_at=[
        "dolore"
    ],
    end_at=[
        "of"
    ],
    id_=[
        2
    ],
    league_id=[
        5
    ],
    modified_at=[
        "eiusmod"
    ],
    name=[
        "eiusmod"
    ],
    season=[
        "labore ex"
    ],
    slug=[
        "kw-jbm1vmo"
    ],
    videogame_title=[
        6
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
range=RangeOverRlSeries(
    begin_at=[
        "Duis anim p"
    ],
    end_at=[
        "ipsu"
    ],
    id_=[
        7
    ],
    league_id=[
        2
    ],
    modified_at=[
        "elit Duis in"
    ],
    name=[
        "cupidatat"
    ],
    season=[
        "enim id com"
    ],
    slug=[
        "s44cu66"
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
search=SearchOverRlSeries(
    name="irure com",
    season="deseru",
    slug="sb4enl",
    winner_type="Player"
)
page=1

result = sdk.rl_series.get_rl_series_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_rl_series_running

List running Rocket League series

- HTTP Method: `GET`
- Endpoint: `/rl/series/running`

**Parameters**

| Name     | Type                                                  | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverRlSeries](../models/FilterOverRlSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverRlSeries](../models/RangeOverRlSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverRlSeries](../models/SearchOverRlSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverRlSeries, RangeOverRlSeries, SearchOverRlSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverRlSeries(
    begin_at=[
        "dolore"
    ],
    end_at=[
        "of"
    ],
    id_=[
        2
    ],
    league_id=[
        5
    ],
    modified_at=[
        "eiusmod"
    ],
    name=[
        "eiusmod"
    ],
    season=[
        "labore ex"
    ],
    slug=[
        "kw-jbm1vmo"
    ],
    videogame_title=[
        6
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
range=RangeOverRlSeries(
    begin_at=[
        "Duis anim p"
    ],
    end_at=[
        "ipsu"
    ],
    id_=[
        7
    ],
    league_id=[
        2
    ],
    modified_at=[
        "elit Duis in"
    ],
    name=[
        "cupidatat"
    ],
    season=[
        "enim id com"
    ],
    slug=[
        "s44cu66"
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
search=SearchOverRlSeries(
    name="irure com",
    season="deseru",
    slug="sb4enl",
    winner_type="Player"
)
page=1

result = sdk.rl_series.get_rl_series_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_rl_series_upcoming

List upcoming Rocket League series

- HTTP Method: `GET`
- Endpoint: `/rl/series/upcoming`

**Parameters**

| Name     | Type                                                  | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverRlSeries](../models/FilterOverRlSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverRlSeries](../models/RangeOverRlSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverRlSeries](../models/SearchOverRlSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverRlSeries, RangeOverRlSeries, SearchOverRlSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverRlSeries(
    begin_at=[
        "dolore"
    ],
    end_at=[
        "of"
    ],
    id_=[
        2
    ],
    league_id=[
        5
    ],
    modified_at=[
        "eiusmod"
    ],
    name=[
        "eiusmod"
    ],
    season=[
        "labore ex"
    ],
    slug=[
        "kw-jbm1vmo"
    ],
    videogame_title=[
        6
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
range=RangeOverRlSeries(
    begin_at=[
        "Duis anim p"
    ],
    end_at=[
        "ipsu"
    ],
    id_=[
        7
    ],
    league_id=[
        2
    ],
    modified_at=[
        "elit Duis in"
    ],
    name=[
        "cupidatat"
    ],
    season=[
        "enim id com"
    ],
    slug=[
        "s44cu66"
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
search=SearchOverRlSeries(
    name="irure com",
    season="deseru",
    slug="sb4enl",
    winner_type="Player"
)
page=1

result = sdk.rl_series.get_rl_series_upcoming(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
