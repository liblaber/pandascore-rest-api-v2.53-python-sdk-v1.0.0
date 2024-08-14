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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverStarcraft2Matches, RangeOverStarcraft2Matches, SearchOverStarcraft2Matches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverStarcraft2Matches(
    begin_at=[
        "dol"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "repr"
    ],
    finished=False,
    forfeit=False,
    future=False,
    id_=[
        5
    ],
    league_id=[
        8
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "aliquip dolore "
    ],
    name=[
        "sint i"
    ],
    not_started=False,
    number_of_games=[
        8
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=True,
    running=True,
    scheduled_at=[
        "adipisicin"
    ],
    serie_id=[
        7
    ],
    slug=[
        "blK8WjKK"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        5
    ],
    videogame_version=[
        "002743.84027555632.65809687197"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverStarcraft2Matches(
    begin_at=[
        "sit"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "nostrud magna m"
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
        "ve"
    ],
    name=[
        "inesse dolor "
    ],
    number_of_games=[
        2
    ],
    scheduled_at=[
        "ullam"
    ],
    slug=[
        "QFi 0L"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        4
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
search=SearchOverStarcraft2Matches(
    match_type="all_games_played",
    name="esse am",
    slug="5x5wgZT_",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverStarcraft2Matches, RangeOverStarcraft2Matches, SearchOverStarcraft2Matches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverStarcraft2Matches(
    begin_at=[
        "dol"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "repr"
    ],
    finished=False,
    forfeit=False,
    future=False,
    id_=[
        5
    ],
    league_id=[
        8
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "aliquip dolore "
    ],
    name=[
        "sint i"
    ],
    not_started=False,
    number_of_games=[
        8
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=True,
    running=True,
    scheduled_at=[
        "adipisicin"
    ],
    serie_id=[
        7
    ],
    slug=[
        "blK8WjKK"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        5
    ],
    videogame_version=[
        "002743.84027555632.65809687197"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverStarcraft2Matches(
    begin_at=[
        "sit"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "nostrud magna m"
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
        "ve"
    ],
    name=[
        "inesse dolor "
    ],
    number_of_games=[
        2
    ],
    scheduled_at=[
        "ullam"
    ],
    slug=[
        "QFi 0L"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        4
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
search=SearchOverStarcraft2Matches(
    match_type="all_games_played",
    name="esse am",
    slug="5x5wgZT_",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverStarcraft2Matches, RangeOverStarcraft2Matches, SearchOverStarcraft2Matches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverStarcraft2Matches(
    begin_at=[
        "dol"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "repr"
    ],
    finished=False,
    forfeit=False,
    future=False,
    id_=[
        5
    ],
    league_id=[
        8
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "aliquip dolore "
    ],
    name=[
        "sint i"
    ],
    not_started=False,
    number_of_games=[
        8
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=True,
    running=True,
    scheduled_at=[
        "adipisicin"
    ],
    serie_id=[
        7
    ],
    slug=[
        "blK8WjKK"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        5
    ],
    videogame_version=[
        "002743.84027555632.65809687197"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverStarcraft2Matches(
    begin_at=[
        "sit"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "nostrud magna m"
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
        "ve"
    ],
    name=[
        "inesse dolor "
    ],
    number_of_games=[
        2
    ],
    scheduled_at=[
        "ullam"
    ],
    slug=[
        "QFi 0L"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        4
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
search=SearchOverStarcraft2Matches(
    match_type="all_games_played",
    name="esse am",
    slug="5x5wgZT_",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverStarcraft2Matches, RangeOverStarcraft2Matches, SearchOverStarcraft2Matches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverStarcraft2Matches(
    begin_at=[
        "dol"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "repr"
    ],
    finished=False,
    forfeit=False,
    future=False,
    id_=[
        5
    ],
    league_id=[
        8
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "aliquip dolore "
    ],
    name=[
        "sint i"
    ],
    not_started=False,
    number_of_games=[
        8
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=True,
    running=True,
    scheduled_at=[
        "adipisicin"
    ],
    serie_id=[
        7
    ],
    slug=[
        "blK8WjKK"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        1
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        5
    ],
    videogame_version=[
        "002743.84027555632.65809687197"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverStarcraft2Matches(
    begin_at=[
        "sit"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "nostrud magna m"
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
        "ve"
    ],
    name=[
        "inesse dolor "
    ],
    number_of_games=[
        2
    ],
    scheduled_at=[
        "ullam"
    ],
    slug=[
        "QFi 0L"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        4
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
search=SearchOverStarcraft2Matches(
    match_type="all_games_played",
    name="esse am",
    slug="5x5wgZT_",
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

<!-- This file was generated by liblab | https://liblab.com/ -->
