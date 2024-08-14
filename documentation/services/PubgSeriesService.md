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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverPubgSeries, RangeOverPubgSeries, SearchOverPubgSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverPubgSeries(
    begin_at=[
        "ex"
    ],
    end_at=[
        "Lorem "
    ],
    id_=[
        5
    ],
    league_id=[
        5
    ],
    modified_at=[
        "do"
    ],
    name=[
        "nisi culpa"
    ],
    season=[
        "ut ea i"
    ],
    slug=[
        "ohs"
    ],
    videogame_title=[
        3
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
range=RangeOverPubgSeries(
    begin_at=[
        "c"
    ],
    end_at=[
        "amet elit et i"
    ],
    id_=[
        2
    ],
    league_id=[
        4
    ],
    modified_at=[
        "fugiat id"
    ],
    name=[
        "in enim "
    ],
    season=[
        "occaecat n"
    ],
    slug=[
        "z7v95uzd6"
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
search=SearchOverPubgSeries(
    name="nostrud ipsu",
    season="velit",
    slug="gu",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverPubgSeries, RangeOverPubgSeries, SearchOverPubgSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverPubgSeries(
    begin_at=[
        "ex"
    ],
    end_at=[
        "Lorem "
    ],
    id_=[
        5
    ],
    league_id=[
        5
    ],
    modified_at=[
        "do"
    ],
    name=[
        "nisi culpa"
    ],
    season=[
        "ut ea i"
    ],
    slug=[
        "ohs"
    ],
    videogame_title=[
        3
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
range=RangeOverPubgSeries(
    begin_at=[
        "c"
    ],
    end_at=[
        "amet elit et i"
    ],
    id_=[
        2
    ],
    league_id=[
        4
    ],
    modified_at=[
        "fugiat id"
    ],
    name=[
        "in enim "
    ],
    season=[
        "occaecat n"
    ],
    slug=[
        "z7v95uzd6"
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
search=SearchOverPubgSeries(
    name="nostrud ipsu",
    season="velit",
    slug="gu",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverPubgSeries, RangeOverPubgSeries, SearchOverPubgSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverPubgSeries(
    begin_at=[
        "ex"
    ],
    end_at=[
        "Lorem "
    ],
    id_=[
        5
    ],
    league_id=[
        5
    ],
    modified_at=[
        "do"
    ],
    name=[
        "nisi culpa"
    ],
    season=[
        "ut ea i"
    ],
    slug=[
        "ohs"
    ],
    videogame_title=[
        3
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
range=RangeOverPubgSeries(
    begin_at=[
        "c"
    ],
    end_at=[
        "amet elit et i"
    ],
    id_=[
        2
    ],
    league_id=[
        4
    ],
    modified_at=[
        "fugiat id"
    ],
    name=[
        "in enim "
    ],
    season=[
        "occaecat n"
    ],
    slug=[
        "z7v95uzd6"
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
search=SearchOverPubgSeries(
    name="nostrud ipsu",
    season="velit",
    slug="gu",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverPubgSeries, RangeOverPubgSeries, SearchOverPubgSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverPubgSeries(
    begin_at=[
        "ex"
    ],
    end_at=[
        "Lorem "
    ],
    id_=[
        5
    ],
    league_id=[
        5
    ],
    modified_at=[
        "do"
    ],
    name=[
        "nisi culpa"
    ],
    season=[
        "ut ea i"
    ],
    slug=[
        "ohs"
    ],
    videogame_title=[
        3
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
range=RangeOverPubgSeries(
    begin_at=[
        "c"
    ],
    end_at=[
        "amet elit et i"
    ],
    id_=[
        2
    ],
    league_id=[
        4
    ],
    modified_at=[
        "fugiat id"
    ],
    name=[
        "in enim "
    ],
    season=[
        "occaecat n"
    ],
    slug=[
        "z7v95uzd6"
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
search=SearchOverPubgSeries(
    name="nostrud ipsu",
    season="velit",
    slug="gu",
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

<!-- This file was generated by liblab | https://liblab.com/ -->
