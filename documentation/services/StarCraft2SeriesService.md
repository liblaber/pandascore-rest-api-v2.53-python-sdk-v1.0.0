# StarCraft2SeriesService

A list of all methods in the `StarCraft2SeriesService` service. Click on the method name to view detailed information about that method.

| Methods                                                             | Description                               |
| :------------------------------------------------------------------ | :---------------------------------------- |
| [get_starcraft_2_series](#get_starcraft_2_series)                   | List series for the StarCraft 2 videogame |
| [get_starcraft_2_series_past](#get_starcraft_2_series_past)         | List past StarCraft 2 series              |
| [get_starcraft_2_series_running](#get_starcraft_2_series_running)   | List running StarCraft 2 series           |
| [get_starcraft_2_series_upcoming](#get_starcraft_2_series_upcoming) | List upcoming StarCraft 2 series          |

## get_starcraft_2_series

List series for the StarCraft 2 videogame

- HTTP Method: `GET`
- Endpoint: `/starcraft-2/series`

**Parameters**

| Name     | Type                                                                  | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraft2Series](../models/FilterOverStarcraft2Series.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraft2Series](../models/RangeOverStarcraft2Series.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraft2Series](../models/SearchOverStarcraft2Series.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverStarcraft2Series, RangeOverStarcraft2Series, SearchOverStarcraft2Series

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverStarcraft2Series(
    begin_at=[
        "occaec"
    ],
    end_at=[
        "exercitation"
    ],
    id_=[
        1
    ],
    league_id=[
        1
    ],
    modified_at=[
        "fugia"
    ],
    name=[
        "utproident"
    ],
    season=[
        "in sint"
    ],
    slug=[
        "61yalkjc"
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
range=RangeOverStarcraft2Series(
    begin_at=[
        "id aliqua"
    ],
    end_at=[
        "nisi ad dolore "
    ],
    id_=[
        7
    ],
    league_id=[
        1
    ],
    modified_at=[
        "irure"
    ],
    name=[
        "minim sint"
    ],
    season=[
        "deseru"
    ],
    slug=[
        "0-6uko32j"
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
search=SearchOverStarcraft2Series(
    name="id labore ",
    season="aute si",
    slug="u5sc",
    winner_type="Player"
)
page=1

result = sdk.star_craft_2_series.get_starcraft_2_series(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_starcraft_2_series_past

List past StarCraft 2 series

- HTTP Method: `GET`
- Endpoint: `/starcraft-2/series/past`

**Parameters**

| Name     | Type                                                                  | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraft2Series](../models/FilterOverStarcraft2Series.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraft2Series](../models/RangeOverStarcraft2Series.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraft2Series](../models/SearchOverStarcraft2Series.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverStarcraft2Series, RangeOverStarcraft2Series, SearchOverStarcraft2Series

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverStarcraft2Series(
    begin_at=[
        "occaec"
    ],
    end_at=[
        "exercitation"
    ],
    id_=[
        1
    ],
    league_id=[
        1
    ],
    modified_at=[
        "fugia"
    ],
    name=[
        "utproident"
    ],
    season=[
        "in sint"
    ],
    slug=[
        "61yalkjc"
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
range=RangeOverStarcraft2Series(
    begin_at=[
        "id aliqua"
    ],
    end_at=[
        "nisi ad dolore "
    ],
    id_=[
        7
    ],
    league_id=[
        1
    ],
    modified_at=[
        "irure"
    ],
    name=[
        "minim sint"
    ],
    season=[
        "deseru"
    ],
    slug=[
        "0-6uko32j"
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
search=SearchOverStarcraft2Series(
    name="id labore ",
    season="aute si",
    slug="u5sc",
    winner_type="Player"
)
page=1

result = sdk.star_craft_2_series.get_starcraft_2_series_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_starcraft_2_series_running

List running StarCraft 2 series

- HTTP Method: `GET`
- Endpoint: `/starcraft-2/series/running`

**Parameters**

| Name     | Type                                                                  | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraft2Series](../models/FilterOverStarcraft2Series.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraft2Series](../models/RangeOverStarcraft2Series.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraft2Series](../models/SearchOverStarcraft2Series.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverStarcraft2Series, RangeOverStarcraft2Series, SearchOverStarcraft2Series

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverStarcraft2Series(
    begin_at=[
        "occaec"
    ],
    end_at=[
        "exercitation"
    ],
    id_=[
        1
    ],
    league_id=[
        1
    ],
    modified_at=[
        "fugia"
    ],
    name=[
        "utproident"
    ],
    season=[
        "in sint"
    ],
    slug=[
        "61yalkjc"
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
range=RangeOverStarcraft2Series(
    begin_at=[
        "id aliqua"
    ],
    end_at=[
        "nisi ad dolore "
    ],
    id_=[
        7
    ],
    league_id=[
        1
    ],
    modified_at=[
        "irure"
    ],
    name=[
        "minim sint"
    ],
    season=[
        "deseru"
    ],
    slug=[
        "0-6uko32j"
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
search=SearchOverStarcraft2Series(
    name="id labore ",
    season="aute si",
    slug="u5sc",
    winner_type="Player"
)
page=1

result = sdk.star_craft_2_series.get_starcraft_2_series_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_starcraft_2_series_upcoming

List upcoming StarCraft 2 series

- HTTP Method: `GET`
- Endpoint: `/starcraft-2/series/upcoming`

**Parameters**

| Name     | Type                                                                  | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraft2Series](../models/FilterOverStarcraft2Series.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraft2Series](../models/RangeOverStarcraft2Series.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraft2Series](../models/SearchOverStarcraft2Series.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Serie]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverStarcraft2Series, RangeOverStarcraft2Series, SearchOverStarcraft2Series

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverStarcraft2Series(
    begin_at=[
        "occaec"
    ],
    end_at=[
        "exercitation"
    ],
    id_=[
        1
    ],
    league_id=[
        1
    ],
    modified_at=[
        "fugia"
    ],
    name=[
        "utproident"
    ],
    season=[
        "in sint"
    ],
    slug=[
        "61yalkjc"
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
range=RangeOverStarcraft2Series(
    begin_at=[
        "id aliqua"
    ],
    end_at=[
        "nisi ad dolore "
    ],
    id_=[
        7
    ],
    league_id=[
        1
    ],
    modified_at=[
        "irure"
    ],
    name=[
        "minim sint"
    ],
    season=[
        "deseru"
    ],
    slug=[
        "0-6uko32j"
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
search=SearchOverStarcraft2Series(
    name="id labore ",
    season="aute si",
    slug="u5sc",
    winner_type="Player"
)
page=1

result = sdk.star_craft_2_series.get_starcraft_2_series_upcoming(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
