# LoLSeriesService

A list of all methods in the `LoLSeriesService` service. Click on the method name to view detailed information about that method.

| Methods                                             | Description                                     |
| :-------------------------------------------------- | :---------------------------------------------- |
| [get_lol_series](#get_lol_series)                   | List series for the League of Legends videogame |
| [get_lol_series_past](#get_lol_series_past)         | List past League of Legends series              |
| [get_lol_series_running](#get_lol_series_running)   | List running League of Legends series           |
| [get_lol_series_upcoming](#get_lol_series_upcoming) | List upcoming League of Legends series          |

## get_lol_series

List series for the League of Legends videogame

- HTTP Method: `GET`
- Endpoint: `/lol/series`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLoLSeries](../models/FilterOverLoLSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLoLSeries](../models/RangeOverLoLSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLoLSeries](../models/SearchOverLoLSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverLoLSeries, RangeOverLoLSeries, SearchOverLoLSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverLoLSeries(
    begin_at=[
        "id Except"
    ],
    end_at=[
        "dolore fugiat "
    ],
    id_=[
        1
    ],
    league_id=[
        7
    ],
    modified_at=[
        "nisi "
    ],
    name=[
        "ea labore d"
    ],
    season=[
        "voluptate"
    ],
    slug=[
        "1yr7hs"
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
range=RangeOverLoLSeries(
    begin_at=[
        "ut dolore elit"
    ],
    end_at=[
        "Duis ex est"
    ],
    id_=[
        7
    ],
    league_id=[
        8
    ],
    modified_at=[
        "sunt null"
    ],
    name=[
        "sint do sit e"
    ],
    season=[
        "in in dolore no"
    ],
    slug=[
        "h9uz8-"
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
search=SearchOverLoLSeries(
    name="veniam cillu",
    season="mollit nost",
    slug="rlq5ktf0t",
    winner_type="Player"
)
page=1

result = sdk.lo_l_series.get_lol_series(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_series_past

List past League of Legends series

- HTTP Method: `GET`
- Endpoint: `/lol/series/past`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLoLSeries](../models/FilterOverLoLSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLoLSeries](../models/RangeOverLoLSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLoLSeries](../models/SearchOverLoLSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverLoLSeries, RangeOverLoLSeries, SearchOverLoLSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverLoLSeries(
    begin_at=[
        "id Except"
    ],
    end_at=[
        "dolore fugiat "
    ],
    id_=[
        1
    ],
    league_id=[
        7
    ],
    modified_at=[
        "nisi "
    ],
    name=[
        "ea labore d"
    ],
    season=[
        "voluptate"
    ],
    slug=[
        "1yr7hs"
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
range=RangeOverLoLSeries(
    begin_at=[
        "ut dolore elit"
    ],
    end_at=[
        "Duis ex est"
    ],
    id_=[
        7
    ],
    league_id=[
        8
    ],
    modified_at=[
        "sunt null"
    ],
    name=[
        "sint do sit e"
    ],
    season=[
        "in in dolore no"
    ],
    slug=[
        "h9uz8-"
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
search=SearchOverLoLSeries(
    name="veniam cillu",
    season="mollit nost",
    slug="rlq5ktf0t",
    winner_type="Player"
)
page=1

result = sdk.lo_l_series.get_lol_series_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_series_running

List running League of Legends series

- HTTP Method: `GET`
- Endpoint: `/lol/series/running`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLoLSeries](../models/FilterOverLoLSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLoLSeries](../models/RangeOverLoLSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLoLSeries](../models/SearchOverLoLSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverLoLSeries, RangeOverLoLSeries, SearchOverLoLSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverLoLSeries(
    begin_at=[
        "id Except"
    ],
    end_at=[
        "dolore fugiat "
    ],
    id_=[
        1
    ],
    league_id=[
        7
    ],
    modified_at=[
        "nisi "
    ],
    name=[
        "ea labore d"
    ],
    season=[
        "voluptate"
    ],
    slug=[
        "1yr7hs"
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
range=RangeOverLoLSeries(
    begin_at=[
        "ut dolore elit"
    ],
    end_at=[
        "Duis ex est"
    ],
    id_=[
        7
    ],
    league_id=[
        8
    ],
    modified_at=[
        "sunt null"
    ],
    name=[
        "sint do sit e"
    ],
    season=[
        "in in dolore no"
    ],
    slug=[
        "h9uz8-"
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
search=SearchOverLoLSeries(
    name="veniam cillu",
    season="mollit nost",
    slug="rlq5ktf0t",
    winner_type="Player"
)
page=1

result = sdk.lo_l_series.get_lol_series_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_series_upcoming

List upcoming League of Legends series

- HTTP Method: `GET`
- Endpoint: `/lol/series/upcoming`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLoLSeries](../models/FilterOverLoLSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLoLSeries](../models/RangeOverLoLSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLoLSeries](../models/SearchOverLoLSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverLoLSeries, RangeOverLoLSeries, SearchOverLoLSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverLoLSeries(
    begin_at=[
        "id Except"
    ],
    end_at=[
        "dolore fugiat "
    ],
    id_=[
        1
    ],
    league_id=[
        7
    ],
    modified_at=[
        "nisi "
    ],
    name=[
        "ea labore d"
    ],
    season=[
        "voluptate"
    ],
    slug=[
        "1yr7hs"
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
range=RangeOverLoLSeries(
    begin_at=[
        "ut dolore elit"
    ],
    end_at=[
        "Duis ex est"
    ],
    id_=[
        7
    ],
    league_id=[
        8
    ],
    modified_at=[
        "sunt null"
    ],
    name=[
        "sint do sit e"
    ],
    season=[
        "in in dolore no"
    ],
    slug=[
        "h9uz8-"
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
search=SearchOverLoLSeries(
    name="veniam cillu",
    season="mollit nost",
    slug="rlq5ktf0t",
    winner_type="Player"
)
page=1

result = sdk.lo_l_series.get_lol_series_upcoming(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
