# Dota2MatchesService

A list of all methods in the `Dota2MatchesService` service. Click on the method name to view detailed information about that method.

| Methods                                                   | Description                           |
| :-------------------------------------------------------- | :------------------------------------ |
| [get_dota2_matches](#get_dota2_matches)                   | List matches for the Dota 2 videogame |
| [get_dota2_matches_past](#get_dota2_matches_past)         | List past Dota 2 matches              |
| [get_dota2_matches_running](#get_dota2_matches_running)   | List running Dota 2 matches           |
| [get_dota2_matches_upcoming](#get_dota2_matches_upcoming) | List upcoming Dota 2 matches          |

## get_dota2_matches

List matches for the Dota 2 videogame

- HTTP Method: `GET`
- Endpoint: `/dota2/matches`

**Parameters**

| Name     | Type                                                          | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverDota2Matches](../models/FilterOverDota2Matches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverDota2Matches](../models/RangeOverDota2Matches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverDota2Matches](../models/SearchOverDota2Matches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverDota2Matches, RangeOverDota2Matches, SearchOverDota2Matches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverDota2Matches(
    begin_at=[
        "exercita"
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "occaecat con"
    ],
    finished=False,
    forfeit=True,
    future=True,
    id_=[
        5
    ],
    league_id=[
        2
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "c"
    ],
    name=[
        "consectetu"
    ],
    not_started=True,
    number_of_games=[
        6
    ],
    opponent_id=[
        7
    ],
    opponents_filled=True,
    past=False,
    running=True,
    scheduled_at=[
        "cons"
    ],
    serie_id=[
        2
    ],
    slug=[
        "KkWSQF"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        7
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        5
    ],
    videogame_version=[
        "2814994544.670513.63045297199"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverDota2Matches(
    begin_at=[
        "mollit an"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "Ut enim"
    ],
    forfeit=[
        False
    ],
    id_=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "sed"
    ],
    name=[
        "amet eu"
    ],
    number_of_games=[
        5
    ],
    scheduled_at=[
        "mollit nisi en"
    ],
    slug=[
        "aC7 VRN8vMK"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        7
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
search=SearchOverDota2Matches(
    match_type="all_games_played",
    name="ex ei",
    slug="KS-Pbe-j",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.dota2_matches.get_dota2_matches(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_dota2_matches_past

List past Dota 2 matches

- HTTP Method: `GET`
- Endpoint: `/dota2/matches/past`

**Parameters**

| Name     | Type                                                          | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverDota2Matches](../models/FilterOverDota2Matches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverDota2Matches](../models/RangeOverDota2Matches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverDota2Matches](../models/SearchOverDota2Matches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverDota2Matches, RangeOverDota2Matches, SearchOverDota2Matches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverDota2Matches(
    begin_at=[
        "exercita"
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "occaecat con"
    ],
    finished=False,
    forfeit=True,
    future=True,
    id_=[
        5
    ],
    league_id=[
        2
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "c"
    ],
    name=[
        "consectetu"
    ],
    not_started=True,
    number_of_games=[
        6
    ],
    opponent_id=[
        7
    ],
    opponents_filled=True,
    past=False,
    running=True,
    scheduled_at=[
        "cons"
    ],
    serie_id=[
        2
    ],
    slug=[
        "KkWSQF"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        7
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        5
    ],
    videogame_version=[
        "2814994544.670513.63045297199"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverDota2Matches(
    begin_at=[
        "mollit an"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "Ut enim"
    ],
    forfeit=[
        False
    ],
    id_=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "sed"
    ],
    name=[
        "amet eu"
    ],
    number_of_games=[
        5
    ],
    scheduled_at=[
        "mollit nisi en"
    ],
    slug=[
        "aC7 VRN8vMK"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        7
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
search=SearchOverDota2Matches(
    match_type="all_games_played",
    name="ex ei",
    slug="KS-Pbe-j",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.dota2_matches.get_dota2_matches_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_dota2_matches_running

List running Dota 2 matches

- HTTP Method: `GET`
- Endpoint: `/dota2/matches/running`

**Parameters**

| Name     | Type                                                          | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverDota2Matches](../models/FilterOverDota2Matches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverDota2Matches](../models/RangeOverDota2Matches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverDota2Matches](../models/SearchOverDota2Matches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverDota2Matches, RangeOverDota2Matches, SearchOverDota2Matches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverDota2Matches(
    begin_at=[
        "exercita"
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "occaecat con"
    ],
    finished=False,
    forfeit=True,
    future=True,
    id_=[
        5
    ],
    league_id=[
        2
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "c"
    ],
    name=[
        "consectetu"
    ],
    not_started=True,
    number_of_games=[
        6
    ],
    opponent_id=[
        7
    ],
    opponents_filled=True,
    past=False,
    running=True,
    scheduled_at=[
        "cons"
    ],
    serie_id=[
        2
    ],
    slug=[
        "KkWSQF"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        7
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        5
    ],
    videogame_version=[
        "2814994544.670513.63045297199"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverDota2Matches(
    begin_at=[
        "mollit an"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "Ut enim"
    ],
    forfeit=[
        False
    ],
    id_=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "sed"
    ],
    name=[
        "amet eu"
    ],
    number_of_games=[
        5
    ],
    scheduled_at=[
        "mollit nisi en"
    ],
    slug=[
        "aC7 VRN8vMK"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        7
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
search=SearchOverDota2Matches(
    match_type="all_games_played",
    name="ex ei",
    slug="KS-Pbe-j",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.dota2_matches.get_dota2_matches_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_dota2_matches_upcoming

List upcoming Dota 2 matches

- HTTP Method: `GET`
- Endpoint: `/dota2/matches/upcoming`

**Parameters**

| Name     | Type                                                          | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverDota2Matches](../models/FilterOverDota2Matches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverDota2Matches](../models/RangeOverDota2Matches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverDota2Matches](../models/SearchOverDota2Matches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverDota2Matches, RangeOverDota2Matches, SearchOverDota2Matches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverDota2Matches(
    begin_at=[
        "exercita"
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "occaecat con"
    ],
    finished=False,
    forfeit=True,
    future=True,
    id_=[
        5
    ],
    league_id=[
        2
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "c"
    ],
    name=[
        "consectetu"
    ],
    not_started=True,
    number_of_games=[
        6
    ],
    opponent_id=[
        7
    ],
    opponents_filled=True,
    past=False,
    running=True,
    scheduled_at=[
        "cons"
    ],
    serie_id=[
        2
    ],
    slug=[
        "KkWSQF"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        7
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        5
    ],
    videogame_version=[
        "2814994544.670513.63045297199"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverDota2Matches(
    begin_at=[
        "mollit an"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "Ut enim"
    ],
    forfeit=[
        False
    ],
    id_=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "sed"
    ],
    name=[
        "amet eu"
    ],
    number_of_games=[
        5
    ],
    scheduled_at=[
        "mollit nisi en"
    ],
    slug=[
        "aC7 VRN8vMK"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        7
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
search=SearchOverDota2Matches(
    match_type="all_games_played",
    name="ex ei",
    slug="KS-Pbe-j",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.dota2_matches.get_dota2_matches_upcoming(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
