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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverR6SiegeSeries, RangeOverR6SiegeSeries, SearchOverR6SiegeSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverR6SiegeSeries(
    begin_at=[
        "est deserunt"
    ],
    end_at=[
        "in fugiat"
    ],
    id_=[
        5
    ],
    league_id=[
        5
    ],
    modified_at=[
        "sint aliqua f"
    ],
    name=[
        "fugia"
    ],
    season=[
        "inproi"
    ],
    slug=[
        "1-fbyc"
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
range=RangeOverR6SiegeSeries(
    begin_at=[
        "conseq"
    ],
    end_at=[
        "in "
    ],
    id_=[
        8
    ],
    league_id=[
        1
    ],
    modified_at=[
        "r"
    ],
    name=[
        "voluptate c"
    ],
    season=[
        "et eiusmo"
    ],
    slug=[
        "gtpv1x1ehf"
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
search=SearchOverR6SiegeSeries(
    name="ipsum esse",
    season="magna",
    slug="y7t41",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverR6SiegeSeries, RangeOverR6SiegeSeries, SearchOverR6SiegeSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverR6SiegeSeries(
    begin_at=[
        "est deserunt"
    ],
    end_at=[
        "in fugiat"
    ],
    id_=[
        5
    ],
    league_id=[
        5
    ],
    modified_at=[
        "sint aliqua f"
    ],
    name=[
        "fugia"
    ],
    season=[
        "inproi"
    ],
    slug=[
        "1-fbyc"
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
range=RangeOverR6SiegeSeries(
    begin_at=[
        "conseq"
    ],
    end_at=[
        "in "
    ],
    id_=[
        8
    ],
    league_id=[
        1
    ],
    modified_at=[
        "r"
    ],
    name=[
        "voluptate c"
    ],
    season=[
        "et eiusmo"
    ],
    slug=[
        "gtpv1x1ehf"
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
search=SearchOverR6SiegeSeries(
    name="ipsum esse",
    season="magna",
    slug="y7t41",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverR6SiegeSeries, RangeOverR6SiegeSeries, SearchOverR6SiegeSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverR6SiegeSeries(
    begin_at=[
        "est deserunt"
    ],
    end_at=[
        "in fugiat"
    ],
    id_=[
        5
    ],
    league_id=[
        5
    ],
    modified_at=[
        "sint aliqua f"
    ],
    name=[
        "fugia"
    ],
    season=[
        "inproi"
    ],
    slug=[
        "1-fbyc"
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
range=RangeOverR6SiegeSeries(
    begin_at=[
        "conseq"
    ],
    end_at=[
        "in "
    ],
    id_=[
        8
    ],
    league_id=[
        1
    ],
    modified_at=[
        "r"
    ],
    name=[
        "voluptate c"
    ],
    season=[
        "et eiusmo"
    ],
    slug=[
        "gtpv1x1ehf"
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
search=SearchOverR6SiegeSeries(
    name="ipsum esse",
    season="magna",
    slug="y7t41",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverR6SiegeSeries, RangeOverR6SiegeSeries, SearchOverR6SiegeSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverR6SiegeSeries(
    begin_at=[
        "est deserunt"
    ],
    end_at=[
        "in fugiat"
    ],
    id_=[
        5
    ],
    league_id=[
        5
    ],
    modified_at=[
        "sint aliqua f"
    ],
    name=[
        "fugia"
    ],
    season=[
        "inproi"
    ],
    slug=[
        "1-fbyc"
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
range=RangeOverR6SiegeSeries(
    begin_at=[
        "conseq"
    ],
    end_at=[
        "in "
    ],
    id_=[
        8
    ],
    league_id=[
        1
    ],
    modified_at=[
        "r"
    ],
    name=[
        "voluptate c"
    ],
    season=[
        "et eiusmo"
    ],
    slug=[
        "gtpv1x1ehf"
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
search=SearchOverR6SiegeSeries(
    name="ipsum esse",
    season="magna",
    slug="y7t41",
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
