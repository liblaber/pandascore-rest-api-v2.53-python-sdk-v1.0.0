# StarCraft2MatchesService

A list of all methods in the `StarCraft2MatchesService` service. Click on the method name to view detailed information about that method.

| Methods                                                               | Description                                |
| :-------------------------------------------------------------------- | :----------------------------------------- |
| [get_starcraft_2_matches](#get_starcraft_2_matches)                   | List matches for the StarCraft 2 videogame |
| [get_starcraft_2_matches_past](#get_starcraft_2_matches_past)         | List past StarCraft 2 matches              |
| [get_starcraft_2_matches_running](#get_starcraft_2_matches_running)   | List running StarCraft 2 matches           |
| [get_starcraft_2_matches_upcoming](#get_starcraft_2_matches_upcoming) | List upcoming StarCraft 2 matches          |

## get_starcraft_2_matches

List matches for the StarCraft 2 videogame

- HTTP Method: `GET`
- Endpoint: `/starcraft-2/matches`

**Parameters**

| Name     | Type                                                                    | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraft2Matches](../models/FilterOverStarcraft2Matches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraft2Matches](../models/RangeOverStarcraft2Matches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraft2Matches](../models/SearchOverStarcraft2Matches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverStarcraft2Matches, RangeOverStarcraft2Matches, SearchOverStarcraft2Matches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverStarcraft2Matches(
    begin_at=[
        "in et cupidatat"
    ],
    detailed_stats=False,
    draw=True,
    end_at=[
        "q"
    ],
    finished=True,
    forfeit=True,
    future=True,
    id_=[
        4
    ],
    league_id=[
        8
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "e"
    ],
    name=[
        "consequ"
    ],
    not_started=True,
    number_of_games=[
        6
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "nostru"
    ],
    serie_id=[
        7
    ],
    slug=[
        "Qh1a6aVgHP"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        2
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        10
    ],
    videogame_version=[
        "96293702.1127"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverStarcraft2Matches(
    begin_at=[
        "Ut"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "adipisicing mi"
    ],
    forfeit=[
        True
    ],
    id_=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "Ut"
    ],
    name=[
        "non dolore cup"
    ],
    number_of_games=[
        9
    ],
    scheduled_at=[
        "mollit ad"
    ],
    slug=[
        "pv3p"
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
search=SearchOverStarcraft2Matches(
    match_type="all_games_played",
    name="non labore ",
    slug="Hc",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.star_craft_2_matches.get_starcraft_2_matches(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_starcraft_2_matches_past

List past StarCraft 2 matches

- HTTP Method: `GET`
- Endpoint: `/starcraft-2/matches/past`

**Parameters**

| Name     | Type                                                                    | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraft2Matches](../models/FilterOverStarcraft2Matches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraft2Matches](../models/RangeOverStarcraft2Matches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraft2Matches](../models/SearchOverStarcraft2Matches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverStarcraft2Matches, RangeOverStarcraft2Matches, SearchOverStarcraft2Matches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverStarcraft2Matches(
    begin_at=[
        "in et cupidatat"
    ],
    detailed_stats=False,
    draw=True,
    end_at=[
        "q"
    ],
    finished=True,
    forfeit=True,
    future=True,
    id_=[
        4
    ],
    league_id=[
        8
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "e"
    ],
    name=[
        "consequ"
    ],
    not_started=True,
    number_of_games=[
        6
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "nostru"
    ],
    serie_id=[
        7
    ],
    slug=[
        "Qh1a6aVgHP"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        2
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        10
    ],
    videogame_version=[
        "96293702.1127"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverStarcraft2Matches(
    begin_at=[
        "Ut"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "adipisicing mi"
    ],
    forfeit=[
        True
    ],
    id_=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "Ut"
    ],
    name=[
        "non dolore cup"
    ],
    number_of_games=[
        9
    ],
    scheduled_at=[
        "mollit ad"
    ],
    slug=[
        "pv3p"
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
search=SearchOverStarcraft2Matches(
    match_type="all_games_played",
    name="non labore ",
    slug="Hc",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.star_craft_2_matches.get_starcraft_2_matches_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_starcraft_2_matches_running

List running StarCraft 2 matches

- HTTP Method: `GET`
- Endpoint: `/starcraft-2/matches/running`

**Parameters**

| Name     | Type                                                                    | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraft2Matches](../models/FilterOverStarcraft2Matches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraft2Matches](../models/RangeOverStarcraft2Matches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraft2Matches](../models/SearchOverStarcraft2Matches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverStarcraft2Matches, RangeOverStarcraft2Matches, SearchOverStarcraft2Matches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverStarcraft2Matches(
    begin_at=[
        "in et cupidatat"
    ],
    detailed_stats=False,
    draw=True,
    end_at=[
        "q"
    ],
    finished=True,
    forfeit=True,
    future=True,
    id_=[
        4
    ],
    league_id=[
        8
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "e"
    ],
    name=[
        "consequ"
    ],
    not_started=True,
    number_of_games=[
        6
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "nostru"
    ],
    serie_id=[
        7
    ],
    slug=[
        "Qh1a6aVgHP"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        2
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        10
    ],
    videogame_version=[
        "96293702.1127"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverStarcraft2Matches(
    begin_at=[
        "Ut"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "adipisicing mi"
    ],
    forfeit=[
        True
    ],
    id_=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "Ut"
    ],
    name=[
        "non dolore cup"
    ],
    number_of_games=[
        9
    ],
    scheduled_at=[
        "mollit ad"
    ],
    slug=[
        "pv3p"
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
search=SearchOverStarcraft2Matches(
    match_type="all_games_played",
    name="non labore ",
    slug="Hc",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.star_craft_2_matches.get_starcraft_2_matches_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_starcraft_2_matches_upcoming

List upcoming StarCraft 2 matches

- HTTP Method: `GET`
- Endpoint: `/starcraft-2/matches/upcoming`

**Parameters**

| Name     | Type                                                                    | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraft2Matches](../models/FilterOverStarcraft2Matches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraft2Matches](../models/RangeOverStarcraft2Matches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraft2Matches](../models/SearchOverStarcraft2Matches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverStarcraft2Matches, RangeOverStarcraft2Matches, SearchOverStarcraft2Matches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverStarcraft2Matches(
    begin_at=[
        "in et cupidatat"
    ],
    detailed_stats=False,
    draw=True,
    end_at=[
        "q"
    ],
    finished=True,
    forfeit=True,
    future=True,
    id_=[
        4
    ],
    league_id=[
        8
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "e"
    ],
    name=[
        "consequ"
    ],
    not_started=True,
    number_of_games=[
        6
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "nostru"
    ],
    serie_id=[
        7
    ],
    slug=[
        "Qh1a6aVgHP"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        2
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        10
    ],
    videogame_version=[
        "96293702.1127"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverStarcraft2Matches(
    begin_at=[
        "Ut"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "adipisicing mi"
    ],
    forfeit=[
        True
    ],
    id_=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "Ut"
    ],
    name=[
        "non dolore cup"
    ],
    number_of_games=[
        9
    ],
    scheduled_at=[
        "mollit ad"
    ],
    slug=[
        "pv3p"
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
search=SearchOverStarcraft2Matches(
    match_type="all_games_played",
    name="non labore ",
    slug="Hc",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.star_craft_2_matches.get_starcraft_2_matches_upcoming(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
