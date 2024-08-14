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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCsgoSeries, RangeOverCsgoSeries, SearchOverCsgoSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCsgoSeries(
    begin_at=[
        "consectet"
    ],
    end_at=[
        "ut Ut dolo"
    ],
    id_=[
        10
    ],
    league_id=[
        3
    ],
    modified_at=[
        "do commodo in "
    ],
    name=[
        "ut sed mag"
    ],
    season=[
        "deserunt no"
    ],
    slug=[
        "xn5ho"
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
range=RangeOverCsgoSeries(
    begin_at=[
        "ipsum tempo"
    ],
    end_at=[
        "ad "
    ],
    id_=[
        9
    ],
    league_id=[
        10
    ],
    modified_at=[
        "mini"
    ],
    name=[
        "quis "
    ],
    season=[
        "est ea aliqu"
    ],
    slug=[
        "v9v6xpow"
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
search=SearchOverCsgoSeries(
    name="in mollit offic",
    season="nostrud elit",
    slug="n-l-8j",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCsgoSeries, RangeOverCsgoSeries, SearchOverCsgoSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCsgoSeries(
    begin_at=[
        "consectet"
    ],
    end_at=[
        "ut Ut dolo"
    ],
    id_=[
        10
    ],
    league_id=[
        3
    ],
    modified_at=[
        "do commodo in "
    ],
    name=[
        "ut sed mag"
    ],
    season=[
        "deserunt no"
    ],
    slug=[
        "xn5ho"
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
range=RangeOverCsgoSeries(
    begin_at=[
        "ipsum tempo"
    ],
    end_at=[
        "ad "
    ],
    id_=[
        9
    ],
    league_id=[
        10
    ],
    modified_at=[
        "mini"
    ],
    name=[
        "quis "
    ],
    season=[
        "est ea aliqu"
    ],
    slug=[
        "v9v6xpow"
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
search=SearchOverCsgoSeries(
    name="in mollit offic",
    season="nostrud elit",
    slug="n-l-8j",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCsgoSeries, RangeOverCsgoSeries, SearchOverCsgoSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCsgoSeries(
    begin_at=[
        "consectet"
    ],
    end_at=[
        "ut Ut dolo"
    ],
    id_=[
        10
    ],
    league_id=[
        3
    ],
    modified_at=[
        "do commodo in "
    ],
    name=[
        "ut sed mag"
    ],
    season=[
        "deserunt no"
    ],
    slug=[
        "xn5ho"
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
range=RangeOverCsgoSeries(
    begin_at=[
        "ipsum tempo"
    ],
    end_at=[
        "ad "
    ],
    id_=[
        9
    ],
    league_id=[
        10
    ],
    modified_at=[
        "mini"
    ],
    name=[
        "quis "
    ],
    season=[
        "est ea aliqu"
    ],
    slug=[
        "v9v6xpow"
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
search=SearchOverCsgoSeries(
    name="in mollit offic",
    season="nostrud elit",
    slug="n-l-8j",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCsgoSeries, RangeOverCsgoSeries, SearchOverCsgoSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCsgoSeries(
    begin_at=[
        "consectet"
    ],
    end_at=[
        "ut Ut dolo"
    ],
    id_=[
        10
    ],
    league_id=[
        3
    ],
    modified_at=[
        "do commodo in "
    ],
    name=[
        "ut sed mag"
    ],
    season=[
        "deserunt no"
    ],
    slug=[
        "xn5ho"
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
range=RangeOverCsgoSeries(
    begin_at=[
        "ipsum tempo"
    ],
    end_at=[
        "ad "
    ],
    id_=[
        9
    ],
    league_id=[
        10
    ],
    modified_at=[
        "mini"
    ],
    name=[
        "quis "
    ],
    season=[
        "est ea aliqu"
    ],
    slug=[
        "v9v6xpow"
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
search=SearchOverCsgoSeries(
    name="in mollit offic",
    season="nostrud elit",
    slug="n-l-8j",
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

<!-- This file was generated by liblab | https://liblab.com/ -->
