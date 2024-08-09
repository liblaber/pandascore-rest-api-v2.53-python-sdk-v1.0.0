# EaSportsFcMatchesService

A list of all methods in the `EaSportsFcMatchesService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description                                 |
| :------------------------------------------------------ | :------------------------------------------ |
| [get_fifa_matches](#get_fifa_matches)                   | List matches for the EA Sports FC videogame |
| [get_fifa_matches_past](#get_fifa_matches_past)         | List past EA Sports FC matches              |
| [get_fifa_matches_running](#get_fifa_matches_running)   | List running EA Sports FC matches           |
| [get_fifa_matches_upcoming](#get_fifa_matches_upcoming) | List upcoming EA Sports FC matches          |

## get_fifa_matches

List matches for the EA Sports FC videogame

- HTTP Method: `GET`
- Endpoint: `/fifa/matches`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverFifaMatches](../models/FilterOverFifaMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverFifaMatches](../models/RangeOverFifaMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverFifaMatches](../models/SearchOverFifaMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverFifaMatches, RangeOverFifaMatches, SearchOverFifaMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverFifaMatches(
    begin_at=[
        "laboris elit"
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "ad enim incidi"
    ],
    finished=True,
    forfeit=False,
    future=False,
    id_=[
        2
    ],
    league_id=[
        6
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "elit "
    ],
    name=[
        "laborum do "
    ],
    not_started=True,
    number_of_games=[
        9
    ],
    opponent_id=[
        10
    ],
    opponents_filled=False,
    past=False,
    running=False,
    scheduled_at=[
        "dolor cupida"
    ],
    serie_id=[
        9
    ],
    slug=[
        "5y-BKFQ "
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        5
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        10
    ],
    videogame_version=[
        "5793643.972"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverFifaMatches(
    begin_at=[
        "labore ea p"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "con"
    ],
    forfeit=[
        False
    ],
    id_=[
        9
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "dolore"
    ],
    name=[
        "id deserunt "
    ],
    number_of_games=[
        0
    ],
    scheduled_at=[
        "al"
    ],
    slug=[
        "AH"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverFifaMatches(
    match_type="all_games_played",
    name="dolore ci",
    slug="L",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.ea_sports_fc_matches.get_fifa_matches(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_fifa_matches_past

List past EA Sports FC matches

- HTTP Method: `GET`
- Endpoint: `/fifa/matches/past`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverFifaMatches](../models/FilterOverFifaMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverFifaMatches](../models/RangeOverFifaMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverFifaMatches](../models/SearchOverFifaMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverFifaMatches, RangeOverFifaMatches, SearchOverFifaMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverFifaMatches(
    begin_at=[
        "laboris elit"
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "ad enim incidi"
    ],
    finished=True,
    forfeit=False,
    future=False,
    id_=[
        2
    ],
    league_id=[
        6
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "elit "
    ],
    name=[
        "laborum do "
    ],
    not_started=True,
    number_of_games=[
        9
    ],
    opponent_id=[
        10
    ],
    opponents_filled=False,
    past=False,
    running=False,
    scheduled_at=[
        "dolor cupida"
    ],
    serie_id=[
        9
    ],
    slug=[
        "5y-BKFQ "
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        5
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        10
    ],
    videogame_version=[
        "5793643.972"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverFifaMatches(
    begin_at=[
        "labore ea p"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "con"
    ],
    forfeit=[
        False
    ],
    id_=[
        9
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "dolore"
    ],
    name=[
        "id deserunt "
    ],
    number_of_games=[
        0
    ],
    scheduled_at=[
        "al"
    ],
    slug=[
        "AH"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverFifaMatches(
    match_type="all_games_played",
    name="dolore ci",
    slug="L",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.ea_sports_fc_matches.get_fifa_matches_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_fifa_matches_running

List running EA Sports FC matches

- HTTP Method: `GET`
- Endpoint: `/fifa/matches/running`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverFifaMatches](../models/FilterOverFifaMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverFifaMatches](../models/RangeOverFifaMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverFifaMatches](../models/SearchOverFifaMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverFifaMatches, RangeOverFifaMatches, SearchOverFifaMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverFifaMatches(
    begin_at=[
        "laboris elit"
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "ad enim incidi"
    ],
    finished=True,
    forfeit=False,
    future=False,
    id_=[
        2
    ],
    league_id=[
        6
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "elit "
    ],
    name=[
        "laborum do "
    ],
    not_started=True,
    number_of_games=[
        9
    ],
    opponent_id=[
        10
    ],
    opponents_filled=False,
    past=False,
    running=False,
    scheduled_at=[
        "dolor cupida"
    ],
    serie_id=[
        9
    ],
    slug=[
        "5y-BKFQ "
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        5
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        10
    ],
    videogame_version=[
        "5793643.972"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverFifaMatches(
    begin_at=[
        "labore ea p"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "con"
    ],
    forfeit=[
        False
    ],
    id_=[
        9
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "dolore"
    ],
    name=[
        "id deserunt "
    ],
    number_of_games=[
        0
    ],
    scheduled_at=[
        "al"
    ],
    slug=[
        "AH"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverFifaMatches(
    match_type="all_games_played",
    name="dolore ci",
    slug="L",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.ea_sports_fc_matches.get_fifa_matches_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_fifa_matches_upcoming

List upcoming EA Sports FC matches

- HTTP Method: `GET`
- Endpoint: `/fifa/matches/upcoming`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverFifaMatches](../models/FilterOverFifaMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverFifaMatches](../models/RangeOverFifaMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverFifaMatches](../models/SearchOverFifaMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverFifaMatches, RangeOverFifaMatches, SearchOverFifaMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverFifaMatches(
    begin_at=[
        "laboris elit"
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "ad enim incidi"
    ],
    finished=True,
    forfeit=False,
    future=False,
    id_=[
        2
    ],
    league_id=[
        6
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "elit "
    ],
    name=[
        "laborum do "
    ],
    not_started=True,
    number_of_games=[
        9
    ],
    opponent_id=[
        10
    ],
    opponents_filled=False,
    past=False,
    running=False,
    scheduled_at=[
        "dolor cupida"
    ],
    serie_id=[
        9
    ],
    slug=[
        "5y-BKFQ "
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        5
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        10
    ],
    videogame_version=[
        "5793643.972"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverFifaMatches(
    begin_at=[
        "labore ea p"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "con"
    ],
    forfeit=[
        False
    ],
    id_=[
        9
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "dolore"
    ],
    name=[
        "id deserunt "
    ],
    number_of_games=[
        0
    ],
    scheduled_at=[
        "al"
    ],
    slug=[
        "AH"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverFifaMatches(
    match_type="all_games_played",
    name="dolore ci",
    slug="L",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.ea_sports_fc_matches.get_fifa_matches_upcoming(
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
