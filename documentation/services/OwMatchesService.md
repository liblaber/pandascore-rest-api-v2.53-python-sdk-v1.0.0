# OwMatchesService

A list of all methods in the `OwMatchesService` service. Click on the method name to view detailed information about that method.

| Methods                                             | Description                              |
| :-------------------------------------------------- | :--------------------------------------- |
| [get_ow_matches](#get_ow_matches)                   | List matches for the Overwatch videogame |
| [get_ow_matches_past](#get_ow_matches_past)         | List past Overwatch matches              |
| [get_ow_matches_running](#get_ow_matches_running)   | List running Overwatch matches           |
| [get_ow_matches_upcoming](#get_ow_matches_upcoming) | List upcoming Overwatch matches          |

## get_ow_matches

List matches for the Overwatch videogame

- HTTP Method: `GET`
- Endpoint: `/ow/matches`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverOwMatches](../models/FilterOverOwMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverOwMatches](../models/RangeOverOwMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverOwMatches](../models/SearchOverOwMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverOwMatches, RangeOverOwMatches, SearchOverOwMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverOwMatches(
    begin_at=[
        "Dui"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "d"
    ],
    finished=False,
    forfeit=False,
    future=False,
    id_=[
        10
    ],
    league_id=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "voluptate dol"
    ],
    name=[
        "veniam"
    ],
    not_started=False,
    number_of_games=[
        6
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=True,
    running=False,
    scheduled_at=[
        "laboru"
    ],
    serie_id=[
        8
    ],
    slug=[
        "Bbdi W6S"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        9
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        6
    ],
    videogame_version=[
        "50504779.61189519999"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverOwMatches(
    begin_at=[
        "r"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "incididunt"
    ],
    forfeit=[
        True
    ],
    id_=[
        1
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ipsum labo"
    ],
    name=[
        "inetea "
    ],
    number_of_games=[
        1
    ],
    scheduled_at=[
        "consequat"
    ],
    slug=[
        "epM"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        3
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
search=SearchOverOwMatches(
    match_type="all_games_played",
    name="ex Duis magn",
    slug="B",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.ow_matches.get_ow_matches(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_ow_matches_past

List past Overwatch matches

- HTTP Method: `GET`
- Endpoint: `/ow/matches/past`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverOwMatches](../models/FilterOverOwMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverOwMatches](../models/RangeOverOwMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverOwMatches](../models/SearchOverOwMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverOwMatches, RangeOverOwMatches, SearchOverOwMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverOwMatches(
    begin_at=[
        "Dui"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "d"
    ],
    finished=False,
    forfeit=False,
    future=False,
    id_=[
        10
    ],
    league_id=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "voluptate dol"
    ],
    name=[
        "veniam"
    ],
    not_started=False,
    number_of_games=[
        6
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=True,
    running=False,
    scheduled_at=[
        "laboru"
    ],
    serie_id=[
        8
    ],
    slug=[
        "Bbdi W6S"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        9
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        6
    ],
    videogame_version=[
        "50504779.61189519999"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverOwMatches(
    begin_at=[
        "r"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "incididunt"
    ],
    forfeit=[
        True
    ],
    id_=[
        1
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ipsum labo"
    ],
    name=[
        "inetea "
    ],
    number_of_games=[
        1
    ],
    scheduled_at=[
        "consequat"
    ],
    slug=[
        "epM"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        3
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
search=SearchOverOwMatches(
    match_type="all_games_played",
    name="ex Duis magn",
    slug="B",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.ow_matches.get_ow_matches_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_ow_matches_running

List running Overwatch matches

- HTTP Method: `GET`
- Endpoint: `/ow/matches/running`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverOwMatches](../models/FilterOverOwMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverOwMatches](../models/RangeOverOwMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverOwMatches](../models/SearchOverOwMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverOwMatches, RangeOverOwMatches, SearchOverOwMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverOwMatches(
    begin_at=[
        "Dui"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "d"
    ],
    finished=False,
    forfeit=False,
    future=False,
    id_=[
        10
    ],
    league_id=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "voluptate dol"
    ],
    name=[
        "veniam"
    ],
    not_started=False,
    number_of_games=[
        6
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=True,
    running=False,
    scheduled_at=[
        "laboru"
    ],
    serie_id=[
        8
    ],
    slug=[
        "Bbdi W6S"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        9
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        6
    ],
    videogame_version=[
        "50504779.61189519999"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverOwMatches(
    begin_at=[
        "r"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "incididunt"
    ],
    forfeit=[
        True
    ],
    id_=[
        1
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ipsum labo"
    ],
    name=[
        "inetea "
    ],
    number_of_games=[
        1
    ],
    scheduled_at=[
        "consequat"
    ],
    slug=[
        "epM"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        3
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
search=SearchOverOwMatches(
    match_type="all_games_played",
    name="ex Duis magn",
    slug="B",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.ow_matches.get_ow_matches_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_ow_matches_upcoming

List upcoming Overwatch matches

- HTTP Method: `GET`
- Endpoint: `/ow/matches/upcoming`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverOwMatches](../models/FilterOverOwMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverOwMatches](../models/RangeOverOwMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverOwMatches](../models/SearchOverOwMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverOwMatches, RangeOverOwMatches, SearchOverOwMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverOwMatches(
    begin_at=[
        "Dui"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "d"
    ],
    finished=False,
    forfeit=False,
    future=False,
    id_=[
        10
    ],
    league_id=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "voluptate dol"
    ],
    name=[
        "veniam"
    ],
    not_started=False,
    number_of_games=[
        6
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=True,
    running=False,
    scheduled_at=[
        "laboru"
    ],
    serie_id=[
        8
    ],
    slug=[
        "Bbdi W6S"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        9
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        6
    ],
    videogame_version=[
        "50504779.61189519999"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverOwMatches(
    begin_at=[
        "r"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "incididunt"
    ],
    forfeit=[
        True
    ],
    id_=[
        1
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "ipsum labo"
    ],
    name=[
        "inetea "
    ],
    number_of_games=[
        1
    ],
    scheduled_at=[
        "consequat"
    ],
    slug=[
        "epM"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        3
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
search=SearchOverOwMatches(
    match_type="all_games_played",
    name="ex Duis magn",
    slug="B",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.ow_matches.get_ow_matches_upcoming(
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
