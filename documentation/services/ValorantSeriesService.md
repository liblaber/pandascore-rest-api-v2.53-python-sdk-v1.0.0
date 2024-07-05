# ValorantSeriesService

A list of all methods in the `ValorantSeriesService` service. Click on the method name to view detailed information about that method.

| Methods                                                       | Description                            |
| :------------------------------------------------------------ | :------------------------------------- |
| [get_valorant_series](#get_valorant_series)                   | List series for the Valorant videogame |
| [get_valorant_series_past](#get_valorant_series_past)         | List past Valorant series              |
| [get_valorant_series_running](#get_valorant_series_running)   | List running Valorant series           |
| [get_valorant_series_upcoming](#get_valorant_series_upcoming) | List upcoming Valorant series          |

## get_valorant_series

List series for the Valorant videogame

- HTTP Method: `GET`
- Endpoint: `/valorant/series`

**Parameters**

| Name     | Type                                                              | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverValorantSeries](../models/FilterOverValorantSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverValorantSeries](../models/RangeOverValorantSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                         | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverValorantSeries](../models/SearchOverValorantSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                         | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                               | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverValorantSeries, RangeOverValorantSeries, SearchOverValorantSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverValorantSeries(
    begin_at=[
        "veniam Ut inci"
    ],
    end_at=[
        "culpa est t"
    ],
    id_=[
        10
    ],
    league_id=[
        9
    ],
    modified_at=[
        "p"
    ],
    name=[
        "cillu"
    ],
    season=[
        "autenostr"
    ],
    slug=[
        "gnh6hc_tp"
    ],
    videogame_title=[
        2
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
range=RangeOverValorantSeries(
    begin_at=[
        "do dolore"
    ],
    end_at=[
        "i"
    ],
    id_=[
        3
    ],
    league_id=[
        3
    ],
    modified_at=[
        "ipsum sint q"
    ],
    name=[
        "conseq"
    ],
    season=[
        "ad dolo"
    ],
    slug=[
        "vpazo5qc863"
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
search=SearchOverValorantSeries(
    name="ullamco",
    season="aliqua",
    slug="a9pz",
    winner_type="Player"
)
page=1

result = sdk.valorant_series.get_valorant_series(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_valorant_series_past

List past Valorant series

- HTTP Method: `GET`
- Endpoint: `/valorant/series/past`

**Parameters**

| Name     | Type                                                              | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverValorantSeries](../models/FilterOverValorantSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverValorantSeries](../models/RangeOverValorantSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                         | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverValorantSeries](../models/SearchOverValorantSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                         | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                               | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverValorantSeries, RangeOverValorantSeries, SearchOverValorantSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverValorantSeries(
    begin_at=[
        "veniam Ut inci"
    ],
    end_at=[
        "culpa est t"
    ],
    id_=[
        10
    ],
    league_id=[
        9
    ],
    modified_at=[
        "p"
    ],
    name=[
        "cillu"
    ],
    season=[
        "autenostr"
    ],
    slug=[
        "gnh6hc_tp"
    ],
    videogame_title=[
        2
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
range=RangeOverValorantSeries(
    begin_at=[
        "do dolore"
    ],
    end_at=[
        "i"
    ],
    id_=[
        3
    ],
    league_id=[
        3
    ],
    modified_at=[
        "ipsum sint q"
    ],
    name=[
        "conseq"
    ],
    season=[
        "ad dolo"
    ],
    slug=[
        "vpazo5qc863"
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
search=SearchOverValorantSeries(
    name="ullamco",
    season="aliqua",
    slug="a9pz",
    winner_type="Player"
)
page=1

result = sdk.valorant_series.get_valorant_series_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_valorant_series_running

List running Valorant series

- HTTP Method: `GET`
- Endpoint: `/valorant/series/running`

**Parameters**

| Name     | Type                                                              | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverValorantSeries](../models/FilterOverValorantSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverValorantSeries](../models/RangeOverValorantSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                         | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverValorantSeries](../models/SearchOverValorantSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                         | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                               | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverValorantSeries, RangeOverValorantSeries, SearchOverValorantSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverValorantSeries(
    begin_at=[
        "veniam Ut inci"
    ],
    end_at=[
        "culpa est t"
    ],
    id_=[
        10
    ],
    league_id=[
        9
    ],
    modified_at=[
        "p"
    ],
    name=[
        "cillu"
    ],
    season=[
        "autenostr"
    ],
    slug=[
        "gnh6hc_tp"
    ],
    videogame_title=[
        2
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
range=RangeOverValorantSeries(
    begin_at=[
        "do dolore"
    ],
    end_at=[
        "i"
    ],
    id_=[
        3
    ],
    league_id=[
        3
    ],
    modified_at=[
        "ipsum sint q"
    ],
    name=[
        "conseq"
    ],
    season=[
        "ad dolo"
    ],
    slug=[
        "vpazo5qc863"
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
search=SearchOverValorantSeries(
    name="ullamco",
    season="aliqua",
    slug="a9pz",
    winner_type="Player"
)
page=1

result = sdk.valorant_series.get_valorant_series_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_valorant_series_upcoming

List upcoming Valorant series

- HTTP Method: `GET`
- Endpoint: `/valorant/series/upcoming`

**Parameters**

| Name     | Type                                                              | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverValorantSeries](../models/FilterOverValorantSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverValorantSeries](../models/RangeOverValorantSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                         | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverValorantSeries](../models/SearchOverValorantSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                         | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                               | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverValorantSeries, RangeOverValorantSeries, SearchOverValorantSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverValorantSeries(
    begin_at=[
        "veniam Ut inci"
    ],
    end_at=[
        "culpa est t"
    ],
    id_=[
        10
    ],
    league_id=[
        9
    ],
    modified_at=[
        "p"
    ],
    name=[
        "cillu"
    ],
    season=[
        "autenostr"
    ],
    slug=[
        "gnh6hc_tp"
    ],
    videogame_title=[
        2
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
range=RangeOverValorantSeries(
    begin_at=[
        "do dolore"
    ],
    end_at=[
        "i"
    ],
    id_=[
        3
    ],
    league_id=[
        3
    ],
    modified_at=[
        "ipsum sint q"
    ],
    name=[
        "conseq"
    ],
    season=[
        "ad dolo"
    ],
    slug=[
        "vpazo5qc863"
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
search=SearchOverValorantSeries(
    name="ullamco",
    season="aliqua",
    slug="a9pz",
    winner_type="Player"
)
page=1

result = sdk.valorant_series.get_valorant_series_upcoming(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
