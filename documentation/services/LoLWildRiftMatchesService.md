# LoLWildRiftMatchesService

A list of all methods in the `LoLWildRiftMatchesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                   | Description                                  |
| :------------------------------------------------------------------------ | :------------------------------------------- |
| [get_lol_wild_rift_matches](#get_lol_wild_rift_matches)                   | List matches for the LoL Wild Rift videogame |
| [get_lol_wild_rift_matches_past](#get_lol_wild_rift_matches_past)         | List past LoL Wild Rift matches              |
| [get_lol_wild_rift_matches_running](#get_lol_wild_rift_matches_running)   | List running LoL Wild Rift matches           |
| [get_lol_wild_rift_matches_upcoming](#get_lol_wild_rift_matches_upcoming) | List upcoming LoL Wild Rift matches          |

## get_lol_wild_rift_matches

List matches for the LoL Wild Rift videogame

- HTTP Method: `GET`
- Endpoint: `/lol-wild-rift/matches`

**Parameters**

| Name     | Type                                                                      | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLolWildRiftMatches](../models/FilterOverLolWildRiftMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLolWildRiftMatches](../models/RangeOverLolWildRiftMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLolWildRiftMatches](../models/SearchOverLolWildRiftMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverLolWildRiftMatches, RangeOverLolWildRiftMatches, SearchOverLolWildRiftMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverLolWildRiftMatches(
    begin_at=[
        "sit dol"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "occaecat id "
    ],
    finished=False,
    forfeit=True,
    future=True,
    id_=[
        5
    ],
    league_id=[
        7
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ut consequa"
    ],
    name=[
        "sint u"
    ],
    not_started=True,
    number_of_games=[
        0
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "aliquip"
    ],
    serie_id=[
        1
    ],
    slug=[
        "qUOA7MvT6YZ"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        10
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        4
    ],
    videogame_version=[
        "38165.26035"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverLolWildRiftMatches(
    begin_at=[
        "d"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "dolore"
    ],
    forfeit=[
        False
    ],
    id_=[
        6
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "d"
    ],
    name=[
        "esse tempo"
    ],
    number_of_games=[
        7
    ],
    scheduled_at=[
        "cup"
    ],
    slug=[
        "2QD9Sdox"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        5
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
search=SearchOverLolWildRiftMatches(
    match_type="all_games_played",
    name="incididunt in",
    slug="R6Hpmg5AJR",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.lo_l_wild_rift_matches.get_lol_wild_rift_matches(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_wild_rift_matches_past

List past LoL Wild Rift matches

- HTTP Method: `GET`
- Endpoint: `/lol-wild-rift/matches/past`

**Parameters**

| Name     | Type                                                                      | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLolWildRiftMatches](../models/FilterOverLolWildRiftMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLolWildRiftMatches](../models/RangeOverLolWildRiftMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLolWildRiftMatches](../models/SearchOverLolWildRiftMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverLolWildRiftMatches, RangeOverLolWildRiftMatches, SearchOverLolWildRiftMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverLolWildRiftMatches(
    begin_at=[
        "sit dol"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "occaecat id "
    ],
    finished=False,
    forfeit=True,
    future=True,
    id_=[
        5
    ],
    league_id=[
        7
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ut consequa"
    ],
    name=[
        "sint u"
    ],
    not_started=True,
    number_of_games=[
        0
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "aliquip"
    ],
    serie_id=[
        1
    ],
    slug=[
        "qUOA7MvT6YZ"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        10
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        4
    ],
    videogame_version=[
        "38165.26035"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverLolWildRiftMatches(
    begin_at=[
        "d"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "dolore"
    ],
    forfeit=[
        False
    ],
    id_=[
        6
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "d"
    ],
    name=[
        "esse tempo"
    ],
    number_of_games=[
        7
    ],
    scheduled_at=[
        "cup"
    ],
    slug=[
        "2QD9Sdox"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        5
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
search=SearchOverLolWildRiftMatches(
    match_type="all_games_played",
    name="incididunt in",
    slug="R6Hpmg5AJR",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.lo_l_wild_rift_matches.get_lol_wild_rift_matches_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_wild_rift_matches_running

List running LoL Wild Rift matches

- HTTP Method: `GET`
- Endpoint: `/lol-wild-rift/matches/running`

**Parameters**

| Name     | Type                                                                      | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLolWildRiftMatches](../models/FilterOverLolWildRiftMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLolWildRiftMatches](../models/RangeOverLolWildRiftMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLolWildRiftMatches](../models/SearchOverLolWildRiftMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverLolWildRiftMatches, RangeOverLolWildRiftMatches, SearchOverLolWildRiftMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverLolWildRiftMatches(
    begin_at=[
        "sit dol"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "occaecat id "
    ],
    finished=False,
    forfeit=True,
    future=True,
    id_=[
        5
    ],
    league_id=[
        7
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ut consequa"
    ],
    name=[
        "sint u"
    ],
    not_started=True,
    number_of_games=[
        0
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "aliquip"
    ],
    serie_id=[
        1
    ],
    slug=[
        "qUOA7MvT6YZ"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        10
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        4
    ],
    videogame_version=[
        "38165.26035"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverLolWildRiftMatches(
    begin_at=[
        "d"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "dolore"
    ],
    forfeit=[
        False
    ],
    id_=[
        6
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "d"
    ],
    name=[
        "esse tempo"
    ],
    number_of_games=[
        7
    ],
    scheduled_at=[
        "cup"
    ],
    slug=[
        "2QD9Sdox"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        5
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
search=SearchOverLolWildRiftMatches(
    match_type="all_games_played",
    name="incididunt in",
    slug="R6Hpmg5AJR",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.lo_l_wild_rift_matches.get_lol_wild_rift_matches_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_wild_rift_matches_upcoming

List upcoming LoL Wild Rift matches

- HTTP Method: `GET`
- Endpoint: `/lol-wild-rift/matches/upcoming`

**Parameters**

| Name     | Type                                                                      | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverLolWildRiftMatches](../models/FilterOverLolWildRiftMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverLolWildRiftMatches](../models/RangeOverLolWildRiftMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverLolWildRiftMatches](../models/SearchOverLolWildRiftMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverLolWildRiftMatches, RangeOverLolWildRiftMatches, SearchOverLolWildRiftMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverLolWildRiftMatches(
    begin_at=[
        "sit dol"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "occaecat id "
    ],
    finished=False,
    forfeit=True,
    future=True,
    id_=[
        5
    ],
    league_id=[
        7
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ut consequa"
    ],
    name=[
        "sint u"
    ],
    not_started=True,
    number_of_games=[
        0
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "aliquip"
    ],
    serie_id=[
        1
    ],
    slug=[
        "qUOA7MvT6YZ"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        10
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        4
    ],
    videogame_version=[
        "38165.26035"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverLolWildRiftMatches(
    begin_at=[
        "d"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "dolore"
    ],
    forfeit=[
        False
    ],
    id_=[
        6
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "d"
    ],
    name=[
        "esse tempo"
    ],
    number_of_games=[
        7
    ],
    scheduled_at=[
        "cup"
    ],
    slug=[
        "2QD9Sdox"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        5
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
search=SearchOverLolWildRiftMatches(
    match_type="all_games_played",
    name="incididunt in",
    slug="R6Hpmg5AJR",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.lo_l_wild_rift_matches.get_lol_wild_rift_matches_upcoming(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
