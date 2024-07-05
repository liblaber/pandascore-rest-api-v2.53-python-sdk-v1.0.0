# EaSportsFcSeriesService

A list of all methods in the `EaSportsFcSeriesService` service. Click on the method name to view detailed information about that method.

| Methods                                               | Description                                |
| :---------------------------------------------------- | :----------------------------------------- |
| [get_fifa_series](#get_fifa_series)                   | List series for the EA Sports FC videogame |
| [get_fifa_series_past](#get_fifa_series_past)         | List past EA Sports FC series              |
| [get_fifa_series_running](#get_fifa_series_running)   | List running EA Sports FC series           |
| [get_fifa_series_upcoming](#get_fifa_series_upcoming) | List upcoming EA Sports FC series          |

## get_fifa_series

List series for the EA Sports FC videogame

- HTTP Method: `GET`
- Endpoint: `/fifa/series`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverFifaSeries](../models/FilterOverFifaSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverFifaSeries](../models/RangeOverFifaSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverFifaSeries](../models/SearchOverFifaSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverFifaSeries, RangeOverFifaSeries, SearchOverFifaSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverFifaSeries(
    begin_at=[
        "consequa"
    ],
    end_at=[
        "ma"
    ],
    id_=[
        7
    ],
    league_id=[
        2
    ],
    modified_at=[
        "occae"
    ],
    name=[
        "adipisicing ve"
    ],
    season=[
        "nostrud ea in "
    ],
    slug=[
        "-lgfva814_8"
    ],
    videogame_title=[
        7
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
range=RangeOverFifaSeries(
    begin_at=[
        "amet e"
    ],
    end_at=[
        "Lo"
    ],
    id_=[
        6
    ],
    league_id=[
        6
    ],
    modified_at=[
        "eli"
    ],
    name=[
        "nisi "
    ],
    season=[
        "exercitation m"
    ],
    slug=[
        "0ue"
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
search=SearchOverFifaSeries(
    name="in culpa ni",
    season="dolore",
    slug="r6go-",
    winner_type="Player"
)
page=1

result = sdk.ea_sports_fc_series.get_fifa_series(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_fifa_series_past

List past EA Sports FC series

- HTTP Method: `GET`
- Endpoint: `/fifa/series/past`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverFifaSeries](../models/FilterOverFifaSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverFifaSeries](../models/RangeOverFifaSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverFifaSeries](../models/SearchOverFifaSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverFifaSeries, RangeOverFifaSeries, SearchOverFifaSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverFifaSeries(
    begin_at=[
        "consequa"
    ],
    end_at=[
        "ma"
    ],
    id_=[
        7
    ],
    league_id=[
        2
    ],
    modified_at=[
        "occae"
    ],
    name=[
        "adipisicing ve"
    ],
    season=[
        "nostrud ea in "
    ],
    slug=[
        "-lgfva814_8"
    ],
    videogame_title=[
        7
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
range=RangeOverFifaSeries(
    begin_at=[
        "amet e"
    ],
    end_at=[
        "Lo"
    ],
    id_=[
        6
    ],
    league_id=[
        6
    ],
    modified_at=[
        "eli"
    ],
    name=[
        "nisi "
    ],
    season=[
        "exercitation m"
    ],
    slug=[
        "0ue"
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
search=SearchOverFifaSeries(
    name="in culpa ni",
    season="dolore",
    slug="r6go-",
    winner_type="Player"
)
page=1

result = sdk.ea_sports_fc_series.get_fifa_series_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_fifa_series_running

List running EA Sports FC series

- HTTP Method: `GET`
- Endpoint: `/fifa/series/running`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverFifaSeries](../models/FilterOverFifaSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverFifaSeries](../models/RangeOverFifaSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverFifaSeries](../models/SearchOverFifaSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverFifaSeries, RangeOverFifaSeries, SearchOverFifaSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverFifaSeries(
    begin_at=[
        "consequa"
    ],
    end_at=[
        "ma"
    ],
    id_=[
        7
    ],
    league_id=[
        2
    ],
    modified_at=[
        "occae"
    ],
    name=[
        "adipisicing ve"
    ],
    season=[
        "nostrud ea in "
    ],
    slug=[
        "-lgfva814_8"
    ],
    videogame_title=[
        7
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
range=RangeOverFifaSeries(
    begin_at=[
        "amet e"
    ],
    end_at=[
        "Lo"
    ],
    id_=[
        6
    ],
    league_id=[
        6
    ],
    modified_at=[
        "eli"
    ],
    name=[
        "nisi "
    ],
    season=[
        "exercitation m"
    ],
    slug=[
        "0ue"
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
search=SearchOverFifaSeries(
    name="in culpa ni",
    season="dolore",
    slug="r6go-",
    winner_type="Player"
)
page=1

result = sdk.ea_sports_fc_series.get_fifa_series_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_fifa_series_upcoming

List upcoming EA Sports FC series

- HTTP Method: `GET`
- Endpoint: `/fifa/series/upcoming`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverFifaSeries](../models/FilterOverFifaSeries.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverFifaSeries](../models/RangeOverFifaSeries.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverFifaSeries](../models/SearchOverFifaSeries.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverFifaSeries, RangeOverFifaSeries, SearchOverFifaSeries

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverFifaSeries(
    begin_at=[
        "consequa"
    ],
    end_at=[
        "ma"
    ],
    id_=[
        7
    ],
    league_id=[
        2
    ],
    modified_at=[
        "occae"
    ],
    name=[
        "adipisicing ve"
    ],
    season=[
        "nostrud ea in "
    ],
    slug=[
        "-lgfva814_8"
    ],
    videogame_title=[
        7
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
range=RangeOverFifaSeries(
    begin_at=[
        "amet e"
    ],
    end_at=[
        "Lo"
    ],
    id_=[
        6
    ],
    league_id=[
        6
    ],
    modified_at=[
        "eli"
    ],
    name=[
        "nisi "
    ],
    season=[
        "exercitation m"
    ],
    slug=[
        "0ue"
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
search=SearchOverFifaSeries(
    name="in culpa ni",
    season="dolore",
    slug="r6go-",
    winner_type="Player"
)
page=1

result = sdk.ea_sports_fc_series.get_fifa_series_upcoming(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
