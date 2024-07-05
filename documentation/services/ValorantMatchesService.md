# ValorantMatchesService

A list of all methods in the `ValorantMatchesService` service. Click on the method name to view detailed information about that method.

| Methods                                                         | Description                             |
| :-------------------------------------------------------------- | :-------------------------------------- |
| [get_valorant_matches](#get_valorant_matches)                   | List matches for the Valorant videogame |
| [get_valorant_matches_past](#get_valorant_matches_past)         | List past Valorant matches              |
| [get_valorant_matches_running](#get_valorant_matches_running)   | List running Valorant matches           |
| [get_valorant_matches_upcoming](#get_valorant_matches_upcoming) | List upcoming Valorant matches          |

## get_valorant_matches

List matches for the Valorant videogame

- HTTP Method: `GET`
- Endpoint: `/valorant/matches`

**Parameters**

| Name     | Type                                                                | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverValorantMatches](../models/FilterOverValorantMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverValorantMatches](../models/RangeOverValorantMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverValorantMatches](../models/SearchOverValorantMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverValorantMatches, RangeOverValorantMatches, SearchOverValorantMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverValorantMatches(
    begin_at=[
        "aute amet"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "proident ulla"
    ],
    finished=True,
    forfeit=False,
    future=False,
    id_=[
        1
    ],
    league_id=[
        2
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "el"
    ],
    name=[
        "sed consectetu"
    ],
    not_started=True,
    number_of_games=[
        7
    ],
    opponent_id=[
        7
    ],
    opponents_filled=True,
    past=False,
    running=False,
    scheduled_at=[
        "consectetu"
    ],
    serie_id=[
        3
    ],
    slug=[
        "BoG3NK"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        4
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        7
    ],
    videogame_version=[
        "0755.7301095"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverValorantMatches(
    begin_at=[
        "a"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        True
    ],
    end_at=[
        "volupta"
    ],
    forfeit=[
        True
    ],
    id_=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "non"
    ],
    name=[
        "Duis reprehende"
    ],
    number_of_games=[
        1
    ],
    scheduled_at=[
        "anim non "
    ],
    slug=[
        "naaDjb"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        4
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverValorantMatches(
    match_type="all_games_played",
    name="consequat",
    slug="aL1K",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.valorant_matches.get_valorant_matches(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_valorant_matches_past

List past Valorant matches

- HTTP Method: `GET`
- Endpoint: `/valorant/matches/past`

**Parameters**

| Name     | Type                                                                | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverValorantMatches](../models/FilterOverValorantMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverValorantMatches](../models/RangeOverValorantMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverValorantMatches](../models/SearchOverValorantMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverValorantMatches, RangeOverValorantMatches, SearchOverValorantMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverValorantMatches(
    begin_at=[
        "aute amet"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "proident ulla"
    ],
    finished=True,
    forfeit=False,
    future=False,
    id_=[
        1
    ],
    league_id=[
        2
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "el"
    ],
    name=[
        "sed consectetu"
    ],
    not_started=True,
    number_of_games=[
        7
    ],
    opponent_id=[
        7
    ],
    opponents_filled=True,
    past=False,
    running=False,
    scheduled_at=[
        "consectetu"
    ],
    serie_id=[
        3
    ],
    slug=[
        "BoG3NK"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        4
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        7
    ],
    videogame_version=[
        "0755.7301095"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverValorantMatches(
    begin_at=[
        "a"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        True
    ],
    end_at=[
        "volupta"
    ],
    forfeit=[
        True
    ],
    id_=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "non"
    ],
    name=[
        "Duis reprehende"
    ],
    number_of_games=[
        1
    ],
    scheduled_at=[
        "anim non "
    ],
    slug=[
        "naaDjb"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        4
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverValorantMatches(
    match_type="all_games_played",
    name="consequat",
    slug="aL1K",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.valorant_matches.get_valorant_matches_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_valorant_matches_running

List running Valorant matches

- HTTP Method: `GET`
- Endpoint: `/valorant/matches/running`

**Parameters**

| Name     | Type                                                                | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverValorantMatches](../models/FilterOverValorantMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverValorantMatches](../models/RangeOverValorantMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverValorantMatches](../models/SearchOverValorantMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverValorantMatches, RangeOverValorantMatches, SearchOverValorantMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverValorantMatches(
    begin_at=[
        "aute amet"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "proident ulla"
    ],
    finished=True,
    forfeit=False,
    future=False,
    id_=[
        1
    ],
    league_id=[
        2
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "el"
    ],
    name=[
        "sed consectetu"
    ],
    not_started=True,
    number_of_games=[
        7
    ],
    opponent_id=[
        7
    ],
    opponents_filled=True,
    past=False,
    running=False,
    scheduled_at=[
        "consectetu"
    ],
    serie_id=[
        3
    ],
    slug=[
        "BoG3NK"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        4
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        7
    ],
    videogame_version=[
        "0755.7301095"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverValorantMatches(
    begin_at=[
        "a"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        True
    ],
    end_at=[
        "volupta"
    ],
    forfeit=[
        True
    ],
    id_=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "non"
    ],
    name=[
        "Duis reprehende"
    ],
    number_of_games=[
        1
    ],
    scheduled_at=[
        "anim non "
    ],
    slug=[
        "naaDjb"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        4
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverValorantMatches(
    match_type="all_games_played",
    name="consequat",
    slug="aL1K",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.valorant_matches.get_valorant_matches_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_valorant_matches_upcoming

List upcoming Valorant matches

- HTTP Method: `GET`
- Endpoint: `/valorant/matches/upcoming`

**Parameters**

| Name     | Type                                                                | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverValorantMatches](../models/FilterOverValorantMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverValorantMatches](../models/RangeOverValorantMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverValorantMatches](../models/SearchOverValorantMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverValorantMatches, RangeOverValorantMatches, SearchOverValorantMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverValorantMatches(
    begin_at=[
        "aute amet"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "proident ulla"
    ],
    finished=True,
    forfeit=False,
    future=False,
    id_=[
        1
    ],
    league_id=[
        2
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "el"
    ],
    name=[
        "sed consectetu"
    ],
    not_started=True,
    number_of_games=[
        7
    ],
    opponent_id=[
        7
    ],
    opponents_filled=True,
    past=False,
    running=False,
    scheduled_at=[
        "consectetu"
    ],
    serie_id=[
        3
    ],
    slug=[
        "BoG3NK"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        4
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        7
    ],
    videogame_version=[
        "0755.7301095"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverValorantMatches(
    begin_at=[
        "a"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        True
    ],
    end_at=[
        "volupta"
    ],
    forfeit=[
        True
    ],
    id_=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "non"
    ],
    name=[
        "Duis reprehende"
    ],
    number_of_games=[
        1
    ],
    scheduled_at=[
        "anim non "
    ],
    slug=[
        "naaDjb"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        4
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverValorantMatches(
    match_type="all_games_played",
    name="consequat",
    slug="aL1K",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.valorant_matches.get_valorant_matches_upcoming(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
