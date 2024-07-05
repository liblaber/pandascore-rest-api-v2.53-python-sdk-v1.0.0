# CounterStrikeSeriesService

A list of all methods in the `CounterStrikeSeriesService` service. Click on the method name to view detailed information about that method.

| Methods                                               | Description                                  |
| :---------------------------------------------------- | :------------------------------------------- |
| [get_csgo_series](#get_csgo_series)                   | List series for the Counter-Strike videogame |
| [get_csgo_series_past](#get_csgo_series_past)         | List past Counter-Strike series              |
| [get_csgo_series_running](#get_csgo_series_running)   | List running Counter-Strike series           |
| [get_csgo_series_upcoming](#get_csgo_series_upcoming) | List upcoming Counter-Strike series          |

## get_csgo_series

List series for the Counter-Strike videogame

- HTTP Method: `GET`
- Endpoint: `/csgo/series`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCsgoSeries](../models/FilterOverCsgoSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCsgoSeries](../models/RangeOverCsgoSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCsgoSeries](../models/SearchOverCsgoSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverCsgoSeries, RangeOverCsgoSeries, SearchOverCsgoSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverCsgoSeries(
    begin_at=[
        "d"
    ],
    end_at=[
        "off"
    ],
    id_=[
        6
    ],
    league_id=[
        1
    ],
    modified_at=[
        "do"
    ],
    name=[
        "velit tempor "
    ],
    season=[
        "dolore sunt i"
    ],
    slug=[
        "mt6dhnc62zi"
    ],
    videogame_title=[
        1
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
range=RangeOverCsgoSeries(
    begin_at=[
        "occaecat d"
    ],
    end_at=[
        "aute Ut in"
    ],
    id_=[
        4
    ],
    league_id=[
        5
    ],
    modified_at=[
        "magna ex"
    ],
    name=[
        "aliquip Ut elit"
    ],
    season=[
        "sintconsectetu"
    ],
    slug=[
        "a6k"
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
search=SearchOverCsgoSeries(
    name="quis aute la",
    season="exercita",
    slug="0i8i",
    winner_type="Player"
)
page=1

result = sdk.counter_strike_series.get_csgo_series(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_csgo_series_past

List past Counter-Strike series

- HTTP Method: `GET`
- Endpoint: `/csgo/series/past`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCsgoSeries](../models/FilterOverCsgoSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCsgoSeries](../models/RangeOverCsgoSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCsgoSeries](../models/SearchOverCsgoSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverCsgoSeries, RangeOverCsgoSeries, SearchOverCsgoSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverCsgoSeries(
    begin_at=[
        "d"
    ],
    end_at=[
        "off"
    ],
    id_=[
        6
    ],
    league_id=[
        1
    ],
    modified_at=[
        "do"
    ],
    name=[
        "velit tempor "
    ],
    season=[
        "dolore sunt i"
    ],
    slug=[
        "mt6dhnc62zi"
    ],
    videogame_title=[
        1
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
range=RangeOverCsgoSeries(
    begin_at=[
        "occaecat d"
    ],
    end_at=[
        "aute Ut in"
    ],
    id_=[
        4
    ],
    league_id=[
        5
    ],
    modified_at=[
        "magna ex"
    ],
    name=[
        "aliquip Ut elit"
    ],
    season=[
        "sintconsectetu"
    ],
    slug=[
        "a6k"
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
search=SearchOverCsgoSeries(
    name="quis aute la",
    season="exercita",
    slug="0i8i",
    winner_type="Player"
)
page=1

result = sdk.counter_strike_series.get_csgo_series_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_csgo_series_running

List running Counter-Strike series

- HTTP Method: `GET`
- Endpoint: `/csgo/series/running`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCsgoSeries](../models/FilterOverCsgoSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCsgoSeries](../models/RangeOverCsgoSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCsgoSeries](../models/SearchOverCsgoSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverCsgoSeries, RangeOverCsgoSeries, SearchOverCsgoSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverCsgoSeries(
    begin_at=[
        "d"
    ],
    end_at=[
        "off"
    ],
    id_=[
        6
    ],
    league_id=[
        1
    ],
    modified_at=[
        "do"
    ],
    name=[
        "velit tempor "
    ],
    season=[
        "dolore sunt i"
    ],
    slug=[
        "mt6dhnc62zi"
    ],
    videogame_title=[
        1
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
range=RangeOverCsgoSeries(
    begin_at=[
        "occaecat d"
    ],
    end_at=[
        "aute Ut in"
    ],
    id_=[
        4
    ],
    league_id=[
        5
    ],
    modified_at=[
        "magna ex"
    ],
    name=[
        "aliquip Ut elit"
    ],
    season=[
        "sintconsectetu"
    ],
    slug=[
        "a6k"
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
search=SearchOverCsgoSeries(
    name="quis aute la",
    season="exercita",
    slug="0i8i",
    winner_type="Player"
)
page=1

result = sdk.counter_strike_series.get_csgo_series_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_csgo_series_upcoming

List upcoming Counter-Strike series

- HTTP Method: `GET`
- Endpoint: `/csgo/series/upcoming`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCsgoSeries](../models/FilterOverCsgoSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCsgoSeries](../models/RangeOverCsgoSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCsgoSeries](../models/SearchOverCsgoSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverCsgoSeries, RangeOverCsgoSeries, SearchOverCsgoSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverCsgoSeries(
    begin_at=[
        "d"
    ],
    end_at=[
        "off"
    ],
    id_=[
        6
    ],
    league_id=[
        1
    ],
    modified_at=[
        "do"
    ],
    name=[
        "velit tempor "
    ],
    season=[
        "dolore sunt i"
    ],
    slug=[
        "mt6dhnc62zi"
    ],
    videogame_title=[
        1
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
range=RangeOverCsgoSeries(
    begin_at=[
        "occaecat d"
    ],
    end_at=[
        "aute Ut in"
    ],
    id_=[
        4
    ],
    league_id=[
        5
    ],
    modified_at=[
        "magna ex"
    ],
    name=[
        "aliquip Ut elit"
    ],
    season=[
        "sintconsectetu"
    ],
    slug=[
        "a6k"
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
search=SearchOverCsgoSeries(
    name="quis aute la",
    season="exercita",
    slug="0i8i",
    winner_type="Player"
)
page=1

result = sdk.counter_strike_series.get_csgo_series_upcoming(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
