# R6SiegeSeriesService

A list of all methods in the `R6SiegeSeriesService` service. Click on the method name to view detailed information about that method.

| Methods                                                     | Description                                     |
| :---------------------------------------------------------- | :---------------------------------------------- |
| [get_r6siege_series](#get_r6siege_series)                   | List series for the Rainbow Six Siege videogame |
| [get_r6siege_series_past](#get_r6siege_series_past)         | List past Rainbow Six Siege series              |
| [get_r6siege_series_running](#get_r6siege_series_running)   | List running Rainbow Six Siege series           |
| [get_r6siege_series_upcoming](#get_r6siege_series_upcoming) | List upcoming Rainbow Six Siege series          |

## get_r6siege_series

List series for the Rainbow Six Siege videogame

- HTTP Method: `GET`
- Endpoint: `/r6siege/series`

**Parameters**

| Name     | Type                                                            | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverR6SiegeSeries](../models/FilterOverR6SiegeSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverR6SiegeSeries](../models/RangeOverR6SiegeSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                       | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverR6SiegeSeries](../models/SearchOverR6SiegeSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                       | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                             | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverR6SiegeSeries, RangeOverR6SiegeSeries, SearchOverR6SiegeSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverR6SiegeSeries(
    begin_at=[
        "Ut"
    ],
    end_at=[
        "velit veniam"
    ],
    id_=[
        10
    ],
    league_id=[
        10
    ],
    modified_at=[
        "est minim eu Lo"
    ],
    name=[
        "sedut qui ma"
    ],
    season=[
        "ut sunt culpa"
    ],
    slug=[
        "bv9nvys"
    ],
    videogame_title=[
        6
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
range=RangeOverR6SiegeSeries(
    begin_at=[
        "repreh"
    ],
    end_at=[
        "ex"
    ],
    id_=[
        9
    ],
    league_id=[
        4
    ],
    modified_at=[
        "elit et anim"
    ],
    name=[
        "culpa o"
    ],
    season=[
        "cillum aute ali"
    ],
    slug=[
        "sqp"
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
search=SearchOverR6SiegeSeries(
    name="irure in",
    season="ut pariatu",
    slug="ey3",
    winner_type="Player"
)
page=1

result = sdk.r6_siege_series.get_r6siege_series(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_r6siege_series_past

List past Rainbow Six Siege series

- HTTP Method: `GET`
- Endpoint: `/r6siege/series/past`

**Parameters**

| Name     | Type                                                            | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverR6SiegeSeries](../models/FilterOverR6SiegeSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverR6SiegeSeries](../models/RangeOverR6SiegeSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                       | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverR6SiegeSeries](../models/SearchOverR6SiegeSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                       | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                             | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverR6SiegeSeries, RangeOverR6SiegeSeries, SearchOverR6SiegeSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverR6SiegeSeries(
    begin_at=[
        "Ut"
    ],
    end_at=[
        "velit veniam"
    ],
    id_=[
        10
    ],
    league_id=[
        10
    ],
    modified_at=[
        "est minim eu Lo"
    ],
    name=[
        "sedut qui ma"
    ],
    season=[
        "ut sunt culpa"
    ],
    slug=[
        "bv9nvys"
    ],
    videogame_title=[
        6
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
range=RangeOverR6SiegeSeries(
    begin_at=[
        "repreh"
    ],
    end_at=[
        "ex"
    ],
    id_=[
        9
    ],
    league_id=[
        4
    ],
    modified_at=[
        "elit et anim"
    ],
    name=[
        "culpa o"
    ],
    season=[
        "cillum aute ali"
    ],
    slug=[
        "sqp"
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
search=SearchOverR6SiegeSeries(
    name="irure in",
    season="ut pariatu",
    slug="ey3",
    winner_type="Player"
)
page=1

result = sdk.r6_siege_series.get_r6siege_series_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_r6siege_series_running

List running Rainbow Six Siege series

- HTTP Method: `GET`
- Endpoint: `/r6siege/series/running`

**Parameters**

| Name     | Type                                                            | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverR6SiegeSeries](../models/FilterOverR6SiegeSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverR6SiegeSeries](../models/RangeOverR6SiegeSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                       | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverR6SiegeSeries](../models/SearchOverR6SiegeSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                       | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                             | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverR6SiegeSeries, RangeOverR6SiegeSeries, SearchOverR6SiegeSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverR6SiegeSeries(
    begin_at=[
        "Ut"
    ],
    end_at=[
        "velit veniam"
    ],
    id_=[
        10
    ],
    league_id=[
        10
    ],
    modified_at=[
        "est minim eu Lo"
    ],
    name=[
        "sedut qui ma"
    ],
    season=[
        "ut sunt culpa"
    ],
    slug=[
        "bv9nvys"
    ],
    videogame_title=[
        6
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
range=RangeOverR6SiegeSeries(
    begin_at=[
        "repreh"
    ],
    end_at=[
        "ex"
    ],
    id_=[
        9
    ],
    league_id=[
        4
    ],
    modified_at=[
        "elit et anim"
    ],
    name=[
        "culpa o"
    ],
    season=[
        "cillum aute ali"
    ],
    slug=[
        "sqp"
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
search=SearchOverR6SiegeSeries(
    name="irure in",
    season="ut pariatu",
    slug="ey3",
    winner_type="Player"
)
page=1

result = sdk.r6_siege_series.get_r6siege_series_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_r6siege_series_upcoming

List upcoming Rainbow Six Siege series

- HTTP Method: `GET`
- Endpoint: `/r6siege/series/upcoming`

**Parameters**

| Name     | Type                                                            | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverR6SiegeSeries](../models/FilterOverR6SiegeSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverR6SiegeSeries](../models/RangeOverR6SiegeSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                       | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverR6SiegeSeries](../models/SearchOverR6SiegeSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                       | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                             | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverR6SiegeSeries, RangeOverR6SiegeSeries, SearchOverR6SiegeSeries

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverR6SiegeSeries(
    begin_at=[
        "Ut"
    ],
    end_at=[
        "velit veniam"
    ],
    id_=[
        10
    ],
    league_id=[
        10
    ],
    modified_at=[
        "est minim eu Lo"
    ],
    name=[
        "sedut qui ma"
    ],
    season=[
        "ut sunt culpa"
    ],
    slug=[
        "bv9nvys"
    ],
    videogame_title=[
        6
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
range=RangeOverR6SiegeSeries(
    begin_at=[
        "repreh"
    ],
    end_at=[
        "ex"
    ],
    id_=[
        9
    ],
    league_id=[
        4
    ],
    modified_at=[
        "elit et anim"
    ],
    name=[
        "culpa o"
    ],
    season=[
        "cillum aute ali"
    ],
    slug=[
        "sqp"
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
search=SearchOverR6SiegeSeries(
    name="irure in",
    season="ut pariatu",
    slug="ey3",
    winner_type="Player"
)
page=1

result = sdk.r6_siege_series.get_r6siege_series_upcoming(
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
