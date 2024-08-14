# StarCraftBroodWarMatchesService

A list of all methods in the `StarCraftBroodWarMatchesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                               | Description                                        |
| :------------------------------------------------------------------------------------ | :------------------------------------------------- |
| [get_starcraft_brood_war_matches](#get_starcraft_brood_war_matches)                   | List matches for the StarCraft Brood War videogame |
| [get_starcraft_brood_war_matches_past](#get_starcraft_brood_war_matches_past)         | List past StarCraft Brood War matches              |
| [get_starcraft_brood_war_matches_running](#get_starcraft_brood_war_matches_running)   | List running StarCraft Brood War matches           |
| [get_starcraft_brood_war_matches_upcoming](#get_starcraft_brood_war_matches_upcoming) | List upcoming StarCraft Brood War matches          |

## get_starcraft_brood_war_matches

List matches for the StarCraft Brood War videogame

- HTTP Method: `GET`
- Endpoint: `/starcraft-brood-war/matches`

**Parameters**

| Name     | Type                                                                                  | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraftBroodWarMatches](../models/FilterOverStarcraftBroodWarMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraftBroodWarMatches](../models/RangeOverStarcraftBroodWarMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraftBroodWarMatches](../models/SearchOverStarcraftBroodWarMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverStarcraftBroodWarMatches, RangeOverStarcraftBroodWarMatches, SearchOverStarcraftBroodWarMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverStarcraftBroodWarMatches(
    begin_at=[
        "eu exe"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "irure lab"
    ],
    finished=True,
    forfeit=False,
    future=False,
    id_=[
        7
    ],
    league_id=[
        1
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "exercita"
    ],
    name=[
        "Lorem "
    ],
    not_started=False,
    number_of_games=[
        0
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=True,
    running=False,
    scheduled_at=[
        "sed culpa la"
    ],
    serie_id=[
        3
    ],
    slug=[
        "UDtH"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        9
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        7
    ],
    videogame_version=[
        "36795.89.22961879"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverStarcraftBroodWarMatches(
    begin_at=[
        "Duis incididu"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        False
    ],
    end_at=[
        "ex do cupi"
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
        "aliqu"
    ],
    name=[
        "in no"
    ],
    number_of_games=[
        0
    ],
    scheduled_at=[
        "elit nisi"
    ],
    slug=[
        "EZr49Ap-"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        5
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
search=SearchOverStarcraftBroodWarMatches(
    match_type="all_games_played",
    name="dolor ut enim",
    slug="KpN_Jh",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.star_craft_brood_war_matches.get_starcraft_brood_war_matches(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_starcraft_brood_war_matches_past

List past StarCraft Brood War matches

- HTTP Method: `GET`
- Endpoint: `/starcraft-brood-war/matches/past`

**Parameters**

| Name     | Type                                                                                  | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraftBroodWarMatches](../models/FilterOverStarcraftBroodWarMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraftBroodWarMatches](../models/RangeOverStarcraftBroodWarMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraftBroodWarMatches](../models/SearchOverStarcraftBroodWarMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverStarcraftBroodWarMatches, RangeOverStarcraftBroodWarMatches, SearchOverStarcraftBroodWarMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverStarcraftBroodWarMatches(
    begin_at=[
        "eu exe"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "irure lab"
    ],
    finished=True,
    forfeit=False,
    future=False,
    id_=[
        7
    ],
    league_id=[
        1
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "exercita"
    ],
    name=[
        "Lorem "
    ],
    not_started=False,
    number_of_games=[
        0
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=True,
    running=False,
    scheduled_at=[
        "sed culpa la"
    ],
    serie_id=[
        3
    ],
    slug=[
        "UDtH"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        9
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        7
    ],
    videogame_version=[
        "36795.89.22961879"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverStarcraftBroodWarMatches(
    begin_at=[
        "Duis incididu"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        False
    ],
    end_at=[
        "ex do cupi"
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
        "aliqu"
    ],
    name=[
        "in no"
    ],
    number_of_games=[
        0
    ],
    scheduled_at=[
        "elit nisi"
    ],
    slug=[
        "EZr49Ap-"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        5
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
search=SearchOverStarcraftBroodWarMatches(
    match_type="all_games_played",
    name="dolor ut enim",
    slug="KpN_Jh",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.star_craft_brood_war_matches.get_starcraft_brood_war_matches_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_starcraft_brood_war_matches_running

List running StarCraft Brood War matches

- HTTP Method: `GET`
- Endpoint: `/starcraft-brood-war/matches/running`

**Parameters**

| Name     | Type                                                                                  | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraftBroodWarMatches](../models/FilterOverStarcraftBroodWarMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraftBroodWarMatches](../models/RangeOverStarcraftBroodWarMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraftBroodWarMatches](../models/SearchOverStarcraftBroodWarMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverStarcraftBroodWarMatches, RangeOverStarcraftBroodWarMatches, SearchOverStarcraftBroodWarMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverStarcraftBroodWarMatches(
    begin_at=[
        "eu exe"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "irure lab"
    ],
    finished=True,
    forfeit=False,
    future=False,
    id_=[
        7
    ],
    league_id=[
        1
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "exercita"
    ],
    name=[
        "Lorem "
    ],
    not_started=False,
    number_of_games=[
        0
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=True,
    running=False,
    scheduled_at=[
        "sed culpa la"
    ],
    serie_id=[
        3
    ],
    slug=[
        "UDtH"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        9
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        7
    ],
    videogame_version=[
        "36795.89.22961879"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverStarcraftBroodWarMatches(
    begin_at=[
        "Duis incididu"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        False
    ],
    end_at=[
        "ex do cupi"
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
        "aliqu"
    ],
    name=[
        "in no"
    ],
    number_of_games=[
        0
    ],
    scheduled_at=[
        "elit nisi"
    ],
    slug=[
        "EZr49Ap-"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        5
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
search=SearchOverStarcraftBroodWarMatches(
    match_type="all_games_played",
    name="dolor ut enim",
    slug="KpN_Jh",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.star_craft_brood_war_matches.get_starcraft_brood_war_matches_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_starcraft_brood_war_matches_upcoming

List upcoming StarCraft Brood War matches

- HTTP Method: `GET`
- Endpoint: `/starcraft-brood-war/matches/upcoming`

**Parameters**

| Name     | Type                                                                                  | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverStarcraftBroodWarMatches](../models/FilterOverStarcraftBroodWarMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverStarcraftBroodWarMatches](../models/RangeOverStarcraftBroodWarMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverStarcraftBroodWarMatches](../models/SearchOverStarcraftBroodWarMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverStarcraftBroodWarMatches, RangeOverStarcraftBroodWarMatches, SearchOverStarcraftBroodWarMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverStarcraftBroodWarMatches(
    begin_at=[
        "eu exe"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "irure lab"
    ],
    finished=True,
    forfeit=False,
    future=False,
    id_=[
        7
    ],
    league_id=[
        1
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "exercita"
    ],
    name=[
        "Lorem "
    ],
    not_started=False,
    number_of_games=[
        0
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=True,
    running=False,
    scheduled_at=[
        "sed culpa la"
    ],
    serie_id=[
        3
    ],
    slug=[
        "UDtH"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        9
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        7
    ],
    videogame_version=[
        "36795.89.22961879"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverStarcraftBroodWarMatches(
    begin_at=[
        "Duis incididu"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        False
    ],
    end_at=[
        "ex do cupi"
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
        "aliqu"
    ],
    name=[
        "in no"
    ],
    number_of_games=[
        0
    ],
    scheduled_at=[
        "elit nisi"
    ],
    slug=[
        "EZr49Ap-"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        5
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
search=SearchOverStarcraftBroodWarMatches(
    match_type="all_games_played",
    name="dolor ut enim",
    slug="KpN_Jh",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.star_craft_brood_war_matches.get_starcraft_brood_war_matches_upcoming(
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
