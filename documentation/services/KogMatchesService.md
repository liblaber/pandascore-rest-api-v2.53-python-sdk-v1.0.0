# KogMatchesService

A list of all methods in the `KogMatchesService` service. Click on the method name to view detailed information about that method.

| Methods                                               | Description                                  |
| :---------------------------------------------------- | :------------------------------------------- |
| [get_kog_matches](#get_kog_matches)                   | List matches for the King of Glory videogame |
| [get_kog_matches_past](#get_kog_matches_past)         | List past King of Glory matches              |
| [get_kog_matches_running](#get_kog_matches_running)   | List running King of Glory matches           |
| [get_kog_matches_upcoming](#get_kog_matches_upcoming) | List upcoming King of Glory matches          |

## get_kog_matches

List matches for the King of Glory videogame

- HTTP Method: `GET`
- Endpoint: `/kog/matches`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverKogMatches](../models/FilterOverKogMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverKogMatches](../models/RangeOverKogMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverKogMatches](../models/SearchOverKogMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverKogMatches, RangeOverKogMatches, SearchOverKogMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverKogMatches(
    begin_at=[
        "si"
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "incididunt"
    ],
    finished=True,
    forfeit=True,
    future=False,
    id_=[
        3
    ],
    league_id=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "vol"
    ],
    name=[
        "occaecat incid"
    ],
    not_started=False,
    number_of_games=[
        8
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "ex Lorem"
    ],
    serie_id=[
        10
    ],
    slug=[
        "W"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        10
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        1
    ],
    videogame_version=[
        "999910.0.28456811073"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverKogMatches(
    begin_at=[
        "cillum quis "
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "ut nulla i"
    ],
    forfeit=[
        False
    ],
    id_=[
        2
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "eu dolor"
    ],
    name=[
        "ea ad Ut consec"
    ],
    number_of_games=[
        5
    ],
    scheduled_at=[
        "do enim sunt "
    ],
    slug=[
        "h NmcNL9-0"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        2
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
search=SearchOverKogMatches(
    match_type="all_games_played",
    name="volupta",
    slug="-7nlLhwc",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.kog_matches.get_kog_matches(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_kog_matches_past

List past King of Glory matches

- HTTP Method: `GET`
- Endpoint: `/kog/matches/past`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverKogMatches](../models/FilterOverKogMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverKogMatches](../models/RangeOverKogMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverKogMatches](../models/SearchOverKogMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverKogMatches, RangeOverKogMatches, SearchOverKogMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverKogMatches(
    begin_at=[
        "si"
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "incididunt"
    ],
    finished=True,
    forfeit=True,
    future=False,
    id_=[
        3
    ],
    league_id=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "vol"
    ],
    name=[
        "occaecat incid"
    ],
    not_started=False,
    number_of_games=[
        8
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "ex Lorem"
    ],
    serie_id=[
        10
    ],
    slug=[
        "W"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        10
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        1
    ],
    videogame_version=[
        "999910.0.28456811073"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverKogMatches(
    begin_at=[
        "cillum quis "
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "ut nulla i"
    ],
    forfeit=[
        False
    ],
    id_=[
        2
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "eu dolor"
    ],
    name=[
        "ea ad Ut consec"
    ],
    number_of_games=[
        5
    ],
    scheduled_at=[
        "do enim sunt "
    ],
    slug=[
        "h NmcNL9-0"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        2
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
search=SearchOverKogMatches(
    match_type="all_games_played",
    name="volupta",
    slug="-7nlLhwc",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.kog_matches.get_kog_matches_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_kog_matches_running

List running King of Glory matches

- HTTP Method: `GET`
- Endpoint: `/kog/matches/running`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverKogMatches](../models/FilterOverKogMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverKogMatches](../models/RangeOverKogMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverKogMatches](../models/SearchOverKogMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverKogMatches, RangeOverKogMatches, SearchOverKogMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverKogMatches(
    begin_at=[
        "si"
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "incididunt"
    ],
    finished=True,
    forfeit=True,
    future=False,
    id_=[
        3
    ],
    league_id=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "vol"
    ],
    name=[
        "occaecat incid"
    ],
    not_started=False,
    number_of_games=[
        8
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "ex Lorem"
    ],
    serie_id=[
        10
    ],
    slug=[
        "W"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        10
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        1
    ],
    videogame_version=[
        "999910.0.28456811073"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverKogMatches(
    begin_at=[
        "cillum quis "
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "ut nulla i"
    ],
    forfeit=[
        False
    ],
    id_=[
        2
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "eu dolor"
    ],
    name=[
        "ea ad Ut consec"
    ],
    number_of_games=[
        5
    ],
    scheduled_at=[
        "do enim sunt "
    ],
    slug=[
        "h NmcNL9-0"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        2
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
search=SearchOverKogMatches(
    match_type="all_games_played",
    name="volupta",
    slug="-7nlLhwc",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.kog_matches.get_kog_matches_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_kog_matches_upcoming

List upcoming King of Glory matches

- HTTP Method: `GET`
- Endpoint: `/kog/matches/upcoming`

**Parameters**

| Name     | Type                                                      | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverKogMatches](../models/FilterOverKogMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverKogMatches](../models/RangeOverKogMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                 | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverKogMatches](../models/SearchOverKogMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                 | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                       | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverKogMatches, RangeOverKogMatches, SearchOverKogMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverKogMatches(
    begin_at=[
        "si"
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "incididunt"
    ],
    finished=True,
    forfeit=True,
    future=False,
    id_=[
        3
    ],
    league_id=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "vol"
    ],
    name=[
        "occaecat incid"
    ],
    not_started=False,
    number_of_games=[
        8
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "ex Lorem"
    ],
    serie_id=[
        10
    ],
    slug=[
        "W"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        10
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        1
    ],
    videogame_version=[
        "999910.0.28456811073"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverKogMatches(
    begin_at=[
        "cillum quis "
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "ut nulla i"
    ],
    forfeit=[
        False
    ],
    id_=[
        2
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "eu dolor"
    ],
    name=[
        "ea ad Ut consec"
    ],
    number_of_games=[
        5
    ],
    scheduled_at=[
        "do enim sunt "
    ],
    slug=[
        "h NmcNL9-0"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        2
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
search=SearchOverKogMatches(
    match_type="all_games_played",
    name="volupta",
    slug="-7nlLhwc",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.kog_matches.get_kog_matches_upcoming(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
