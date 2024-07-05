# PubgSeriesService

A list of all methods in the `PubgSeriesService` service. Click on the method name to view detailed information about that method.

| Methods                                               | Description                        |
| :---------------------------------------------------- | :--------------------------------- |
| [get_pubg_series](#get_pubg_series)                   | List series for the PUBG videogame |
| [get_pubg_series_past](#get_pubg_series_past)         | List past PUBG series              |
| [get_pubg_series_running](#get_pubg_series_running)   | List running PUBG series           |
| [get_pubg_series_upcoming](#get_pubg_series_upcoming) | List upcoming PUBG series          |

## get_pubg_series

List series for the PUBG videogame

- HTTP Method: `GET`
- Endpoint: `/pubg/series`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverPubgSeries](../models/FilterOverPubgSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverPubgSeries](../models/RangeOverPubgSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverPubgSeries](../models/SearchOverPubgSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverPubgSeries, RangeOverPubgSeries, SearchOverPubgSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverPubgSeries(
    begin_at=[
        "exercitation"
    ],
    end_at=[
        "fug"
    ],
    id_=[
        4
    ],
    league_id=[
        4
    ],
    modified_at=[
        "n"
    ],
    name=[
        "aliqua vol"
    ],
    season=[
        "culpa lab"
    ],
    slug=[
        "1gd"
    ],
    videogame_title=[
        8
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
range=RangeOverPubgSeries(
    begin_at=[
        "dolore i"
    ],
    end_at=[
        "do m"
    ],
    id_=[
        9
    ],
    league_id=[
        9
    ],
    modified_at=[
        "nu"
    ],
    name=[
        "dolore e"
    ],
    season=[
        "fugiat"
    ],
    slug=[
        "zsnj8x7"
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
search=SearchOverPubgSeries(
    name="qui commod",
    season="proiden",
    slug="7",
    winner_type="Player"
)
page=1

result = sdk.pubg_series.get_pubg_series(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_pubg_series_past

List past PUBG series

- HTTP Method: `GET`
- Endpoint: `/pubg/series/past`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverPubgSeries](../models/FilterOverPubgSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverPubgSeries](../models/RangeOverPubgSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverPubgSeries](../models/SearchOverPubgSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverPubgSeries, RangeOverPubgSeries, SearchOverPubgSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverPubgSeries(
    begin_at=[
        "exercitation"
    ],
    end_at=[
        "fug"
    ],
    id_=[
        4
    ],
    league_id=[
        4
    ],
    modified_at=[
        "n"
    ],
    name=[
        "aliqua vol"
    ],
    season=[
        "culpa lab"
    ],
    slug=[
        "1gd"
    ],
    videogame_title=[
        8
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
range=RangeOverPubgSeries(
    begin_at=[
        "dolore i"
    ],
    end_at=[
        "do m"
    ],
    id_=[
        9
    ],
    league_id=[
        9
    ],
    modified_at=[
        "nu"
    ],
    name=[
        "dolore e"
    ],
    season=[
        "fugiat"
    ],
    slug=[
        "zsnj8x7"
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
search=SearchOverPubgSeries(
    name="qui commod",
    season="proiden",
    slug="7",
    winner_type="Player"
)
page=1

result = sdk.pubg_series.get_pubg_series_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_pubg_series_running

List running PUBG series

- HTTP Method: `GET`
- Endpoint: `/pubg/series/running`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverPubgSeries](../models/FilterOverPubgSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverPubgSeries](../models/RangeOverPubgSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverPubgSeries](../models/SearchOverPubgSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverPubgSeries, RangeOverPubgSeries, SearchOverPubgSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverPubgSeries(
    begin_at=[
        "exercitation"
    ],
    end_at=[
        "fug"
    ],
    id_=[
        4
    ],
    league_id=[
        4
    ],
    modified_at=[
        "n"
    ],
    name=[
        "aliqua vol"
    ],
    season=[
        "culpa lab"
    ],
    slug=[
        "1gd"
    ],
    videogame_title=[
        8
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
range=RangeOverPubgSeries(
    begin_at=[
        "dolore i"
    ],
    end_at=[
        "do m"
    ],
    id_=[
        9
    ],
    league_id=[
        9
    ],
    modified_at=[
        "nu"
    ],
    name=[
        "dolore e"
    ],
    season=[
        "fugiat"
    ],
    slug=[
        "zsnj8x7"
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
search=SearchOverPubgSeries(
    name="qui commod",
    season="proiden",
    slug="7",
    winner_type="Player"
)
page=1

result = sdk.pubg_series.get_pubg_series_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_pubg_series_upcoming

List upcoming PUBG series

- HTTP Method: `GET`
- Endpoint: `/pubg/series/upcoming`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverPubgSeries](../models/FilterOverPubgSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverPubgSeries](../models/RangeOverPubgSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverPubgSeries](../models/SearchOverPubgSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverPubgSeries, RangeOverPubgSeries, SearchOverPubgSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverPubgSeries(
    begin_at=[
        "exercitation"
    ],
    end_at=[
        "fug"
    ],
    id_=[
        4
    ],
    league_id=[
        4
    ],
    modified_at=[
        "n"
    ],
    name=[
        "aliqua vol"
    ],
    season=[
        "culpa lab"
    ],
    slug=[
        "1gd"
    ],
    videogame_title=[
        8
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
range=RangeOverPubgSeries(
    begin_at=[
        "dolore i"
    ],
    end_at=[
        "do m"
    ],
    id_=[
        9
    ],
    league_id=[
        9
    ],
    modified_at=[
        "nu"
    ],
    name=[
        "dolore e"
    ],
    season=[
        "fugiat"
    ],
    slug=[
        "zsnj8x7"
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
search=SearchOverPubgSeries(
    name="qui commod",
    season="proiden",
    slug="7",
    winner_type="Player"
)
page=1

result = sdk.pubg_series.get_pubg_series_upcoming(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
