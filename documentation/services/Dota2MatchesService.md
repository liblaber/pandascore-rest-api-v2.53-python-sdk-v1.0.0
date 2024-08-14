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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverDota2Matches, RangeOverDota2Matches, SearchOverDota2Matches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverDota2Matches(
    begin_at=[
        "voluptate"
    ],
    detailed_stats=False,
    draw=True,
    end_at=[
        "laborum exerci"
    ],
    finished=True,
    forfeit=False,
    future=False,
    id_=[
        2
    ],
    league_id=[
        8
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "q"
    ],
    name=[
        "in occaecat"
    ],
    not_started=True,
    number_of_games=[
        8
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=True,
    running=False,
    scheduled_at=[
        "sed Lorem"
    ],
    serie_id=[
        2
    ],
    slug=[
        "l1K2WGjRGmW"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        4
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        10
    ],
    videogame_version=[
        "44537.153947.67145"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverDota2Matches(
    begin_at=[
        "enim cupid"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "et "
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
        "mollit labori"
    ],
    name=[
        "non enim"
    ],
    number_of_games=[
        1
    ],
    scheduled_at=[
        "anim tempor"
    ],
    slug=[
        "StboFnI"
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
search=SearchOverDota2Matches(
    match_type="all_games_played",
    name="officia",
    slug="R ",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverDota2Matches, RangeOverDota2Matches, SearchOverDota2Matches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverDota2Matches(
    begin_at=[
        "voluptate"
    ],
    detailed_stats=False,
    draw=True,
    end_at=[
        "laborum exerci"
    ],
    finished=True,
    forfeit=False,
    future=False,
    id_=[
        2
    ],
    league_id=[
        8
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "q"
    ],
    name=[
        "in occaecat"
    ],
    not_started=True,
    number_of_games=[
        8
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=True,
    running=False,
    scheduled_at=[
        "sed Lorem"
    ],
    serie_id=[
        2
    ],
    slug=[
        "l1K2WGjRGmW"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        4
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        10
    ],
    videogame_version=[
        "44537.153947.67145"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverDota2Matches(
    begin_at=[
        "enim cupid"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "et "
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
        "mollit labori"
    ],
    name=[
        "non enim"
    ],
    number_of_games=[
        1
    ],
    scheduled_at=[
        "anim tempor"
    ],
    slug=[
        "StboFnI"
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
search=SearchOverDota2Matches(
    match_type="all_games_played",
    name="officia",
    slug="R ",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverDota2Matches, RangeOverDota2Matches, SearchOverDota2Matches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverDota2Matches(
    begin_at=[
        "voluptate"
    ],
    detailed_stats=False,
    draw=True,
    end_at=[
        "laborum exerci"
    ],
    finished=True,
    forfeit=False,
    future=False,
    id_=[
        2
    ],
    league_id=[
        8
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "q"
    ],
    name=[
        "in occaecat"
    ],
    not_started=True,
    number_of_games=[
        8
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=True,
    running=False,
    scheduled_at=[
        "sed Lorem"
    ],
    serie_id=[
        2
    ],
    slug=[
        "l1K2WGjRGmW"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        4
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        10
    ],
    videogame_version=[
        "44537.153947.67145"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverDota2Matches(
    begin_at=[
        "enim cupid"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "et "
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
        "mollit labori"
    ],
    name=[
        "non enim"
    ],
    number_of_games=[
        1
    ],
    scheduled_at=[
        "anim tempor"
    ],
    slug=[
        "StboFnI"
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
search=SearchOverDota2Matches(
    match_type="all_games_played",
    name="officia",
    slug="R ",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverDota2Matches, RangeOverDota2Matches, SearchOverDota2Matches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverDota2Matches(
    begin_at=[
        "voluptate"
    ],
    detailed_stats=False,
    draw=True,
    end_at=[
        "laborum exerci"
    ],
    finished=True,
    forfeit=False,
    future=False,
    id_=[
        2
    ],
    league_id=[
        8
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "q"
    ],
    name=[
        "in occaecat"
    ],
    not_started=True,
    number_of_games=[
        8
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=True,
    running=False,
    scheduled_at=[
        "sed Lorem"
    ],
    serie_id=[
        2
    ],
    slug=[
        "l1K2WGjRGmW"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        4
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        10
    ],
    videogame_version=[
        "44537.153947.67145"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverDota2Matches(
    begin_at=[
        "enim cupid"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "et "
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
        "mollit labori"
    ],
    name=[
        "non enim"
    ],
    number_of_games=[
        1
    ],
    scheduled_at=[
        "anim tempor"
    ],
    slug=[
        "StboFnI"
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
search=SearchOverDota2Matches(
    match_type="all_games_played",
    name="officia",
    slug="R ",
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

<!-- This file was generated by liblab | https://liblab.com/ -->
