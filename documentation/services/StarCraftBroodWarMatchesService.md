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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverStarcraftBroodWarMatches, RangeOverStarcraftBroodWarMatches, SearchOverStarcraftBroodWarMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverStarcraftBroodWarMatches(
    begin_at=[
        "quis pariatur"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "mollit Lorem"
    ],
    finished=False,
    forfeit=True,
    future=True,
    id_=[
        10
    ],
    league_id=[
        6
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ull"
    ],
    name=[
        "ea aliqua fug"
    ],
    not_started=True,
    number_of_games=[
        5
    ],
    opponent_id=[
        7
    ],
    opponents_filled=True,
    past=False,
    running=True,
    scheduled_at=[
        "volupt"
    ],
    serie_id=[
        4
    ],
    slug=[
        "xf"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        8
    ],
    videogame_version=[
        "9241.35718719411.5439860285"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverStarcraftBroodWarMatches(
    begin_at=[
        "eu q"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "nu"
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
        "aliq"
    ],
    name=[
        "incididunt"
    ],
    number_of_games=[
        10
    ],
    scheduled_at=[
        "consectetu"
    ],
    slug=[
        "zbHMXhEaC39"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
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
search=SearchOverStarcraftBroodWarMatches(
    match_type="all_games_played",
    name="ea venia",
    slug="vpENLXh",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverStarcraftBroodWarMatches, RangeOverStarcraftBroodWarMatches, SearchOverStarcraftBroodWarMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverStarcraftBroodWarMatches(
    begin_at=[
        "quis pariatur"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "mollit Lorem"
    ],
    finished=False,
    forfeit=True,
    future=True,
    id_=[
        10
    ],
    league_id=[
        6
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ull"
    ],
    name=[
        "ea aliqua fug"
    ],
    not_started=True,
    number_of_games=[
        5
    ],
    opponent_id=[
        7
    ],
    opponents_filled=True,
    past=False,
    running=True,
    scheduled_at=[
        "volupt"
    ],
    serie_id=[
        4
    ],
    slug=[
        "xf"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        8
    ],
    videogame_version=[
        "9241.35718719411.5439860285"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverStarcraftBroodWarMatches(
    begin_at=[
        "eu q"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "nu"
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
        "aliq"
    ],
    name=[
        "incididunt"
    ],
    number_of_games=[
        10
    ],
    scheduled_at=[
        "consectetu"
    ],
    slug=[
        "zbHMXhEaC39"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
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
search=SearchOverStarcraftBroodWarMatches(
    match_type="all_games_played",
    name="ea venia",
    slug="vpENLXh",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverStarcraftBroodWarMatches, RangeOverStarcraftBroodWarMatches, SearchOverStarcraftBroodWarMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverStarcraftBroodWarMatches(
    begin_at=[
        "quis pariatur"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "mollit Lorem"
    ],
    finished=False,
    forfeit=True,
    future=True,
    id_=[
        10
    ],
    league_id=[
        6
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ull"
    ],
    name=[
        "ea aliqua fug"
    ],
    not_started=True,
    number_of_games=[
        5
    ],
    opponent_id=[
        7
    ],
    opponents_filled=True,
    past=False,
    running=True,
    scheduled_at=[
        "volupt"
    ],
    serie_id=[
        4
    ],
    slug=[
        "xf"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        8
    ],
    videogame_version=[
        "9241.35718719411.5439860285"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverStarcraftBroodWarMatches(
    begin_at=[
        "eu q"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "nu"
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
        "aliq"
    ],
    name=[
        "incididunt"
    ],
    number_of_games=[
        10
    ],
    scheduled_at=[
        "consectetu"
    ],
    slug=[
        "zbHMXhEaC39"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
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
search=SearchOverStarcraftBroodWarMatches(
    match_type="all_games_played",
    name="ea venia",
    slug="vpENLXh",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverStarcraftBroodWarMatches, RangeOverStarcraftBroodWarMatches, SearchOverStarcraftBroodWarMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverStarcraftBroodWarMatches(
    begin_at=[
        "quis pariatur"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "mollit Lorem"
    ],
    finished=False,
    forfeit=True,
    future=True,
    id_=[
        10
    ],
    league_id=[
        6
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ull"
    ],
    name=[
        "ea aliqua fug"
    ],
    not_started=True,
    number_of_games=[
        5
    ],
    opponent_id=[
        7
    ],
    opponents_filled=True,
    past=False,
    running=True,
    scheduled_at=[
        "volupt"
    ],
    serie_id=[
        4
    ],
    slug=[
        "xf"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        8
    ],
    videogame_version=[
        "9241.35718719411.5439860285"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverStarcraftBroodWarMatches(
    begin_at=[
        "eu q"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "nu"
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
        "aliq"
    ],
    name=[
        "incididunt"
    ],
    number_of_games=[
        10
    ],
    scheduled_at=[
        "consectetu"
    ],
    slug=[
        "zbHMXhEaC39"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
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
search=SearchOverStarcraftBroodWarMatches(
    match_type="all_games_played",
    name="ea venia",
    slug="vpENLXh",
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
