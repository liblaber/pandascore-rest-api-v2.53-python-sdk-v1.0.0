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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverFifaMatches, RangeOverFifaMatches, SearchOverFifaMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverFifaMatches(
    begin_at=[
        "id"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "velit aut"
    ],
    finished=False,
    forfeit=False,
    future=True,
    id_=[
        7
    ],
    league_id=[
        7
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ut "
    ],
    name=[
        "aliquip ea "
    ],
    not_started=True,
    number_of_games=[
        3
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=False,
    running=False,
    scheduled_at=[
        "eu"
    ],
    serie_id=[
        6
    ],
    slug=[
        "ekOBhd25X"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        8
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        7
    ],
    videogame_version=[
        "9242.1106"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverFifaMatches(
    begin_at=[
        "adipi"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        True
    ],
    end_at=[
        "dolor"
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
        "ipsu"
    ],
    name=[
        "sint magna"
    ],
    number_of_games=[
        10
    ],
    scheduled_at=[
        "ve"
    ],
    slug=[
        "_2ZnoXZ l"
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
search=SearchOverFifaMatches(
    match_type="all_games_played",
    name="nulla",
    slug="bXNGNhENGu",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverFifaMatches, RangeOverFifaMatches, SearchOverFifaMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverFifaMatches(
    begin_at=[
        "id"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "velit aut"
    ],
    finished=False,
    forfeit=False,
    future=True,
    id_=[
        7
    ],
    league_id=[
        7
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ut "
    ],
    name=[
        "aliquip ea "
    ],
    not_started=True,
    number_of_games=[
        3
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=False,
    running=False,
    scheduled_at=[
        "eu"
    ],
    serie_id=[
        6
    ],
    slug=[
        "ekOBhd25X"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        8
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        7
    ],
    videogame_version=[
        "9242.1106"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverFifaMatches(
    begin_at=[
        "adipi"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        True
    ],
    end_at=[
        "dolor"
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
        "ipsu"
    ],
    name=[
        "sint magna"
    ],
    number_of_games=[
        10
    ],
    scheduled_at=[
        "ve"
    ],
    slug=[
        "_2ZnoXZ l"
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
search=SearchOverFifaMatches(
    match_type="all_games_played",
    name="nulla",
    slug="bXNGNhENGu",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverFifaMatches, RangeOverFifaMatches, SearchOverFifaMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverFifaMatches(
    begin_at=[
        "id"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "velit aut"
    ],
    finished=False,
    forfeit=False,
    future=True,
    id_=[
        7
    ],
    league_id=[
        7
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ut "
    ],
    name=[
        "aliquip ea "
    ],
    not_started=True,
    number_of_games=[
        3
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=False,
    running=False,
    scheduled_at=[
        "eu"
    ],
    serie_id=[
        6
    ],
    slug=[
        "ekOBhd25X"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        8
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        7
    ],
    videogame_version=[
        "9242.1106"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverFifaMatches(
    begin_at=[
        "adipi"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        True
    ],
    end_at=[
        "dolor"
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
        "ipsu"
    ],
    name=[
        "sint magna"
    ],
    number_of_games=[
        10
    ],
    scheduled_at=[
        "ve"
    ],
    slug=[
        "_2ZnoXZ l"
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
search=SearchOverFifaMatches(
    match_type="all_games_played",
    name="nulla",
    slug="bXNGNhENGu",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverFifaMatches, RangeOverFifaMatches, SearchOverFifaMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverFifaMatches(
    begin_at=[
        "id"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "velit aut"
    ],
    finished=False,
    forfeit=False,
    future=True,
    id_=[
        7
    ],
    league_id=[
        7
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ut "
    ],
    name=[
        "aliquip ea "
    ],
    not_started=True,
    number_of_games=[
        3
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=False,
    running=False,
    scheduled_at=[
        "eu"
    ],
    serie_id=[
        6
    ],
    slug=[
        "ekOBhd25X"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        8
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        7
    ],
    videogame_version=[
        "9242.1106"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverFifaMatches(
    begin_at=[
        "adipi"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        True
    ],
    end_at=[
        "dolor"
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
        "ipsu"
    ],
    name=[
        "sint magna"
    ],
    number_of_games=[
        10
    ],
    scheduled_at=[
        "ve"
    ],
    slug=[
        "_2ZnoXZ l"
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
search=SearchOverFifaMatches(
    match_type="all_games_played",
    name="nulla",
    slug="bXNGNhENGu",
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
