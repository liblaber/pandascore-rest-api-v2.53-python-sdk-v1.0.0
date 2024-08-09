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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverKogMatches, RangeOverKogMatches, SearchOverKogMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverKogMatches(
    begin_at=[
        "Du"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "voluptate"
    ],
    finished=False,
    forfeit=True,
    future=True,
    id_=[
        6
    ],
    league_id=[
        6
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "labore id fugi"
    ],
    name=[
        "nostrud veniam"
    ],
    not_started=True,
    number_of_games=[
        7
    ],
    opponent_id=[
        10
    ],
    opponents_filled=False,
    past=True,
    running=False,
    scheduled_at=[
        "sed Du"
    ],
    serie_id=[
        10
    ],
    slug=[
        "GJ7GWuEfy"
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
        6
    ],
    videogame_version=[
        "6.4314860.74685349364"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverKogMatches(
    begin_at=[
        "Lo"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        False
    ],
    end_at=[
        "eu minim par"
    ],
    forfeit=[
        True
    ],
    id_=[
        6
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "est"
    ],
    name=[
        "Lorem "
    ],
    number_of_games=[
        2
    ],
    scheduled_at=[
        "et"
    ],
    slug=[
        "vBKKlSKdbR"
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
search=SearchOverKogMatches(
    match_type="all_games_played",
    name="cillum v",
    slug="Vy-2dZKJxf",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverKogMatches, RangeOverKogMatches, SearchOverKogMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverKogMatches(
    begin_at=[
        "Du"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "voluptate"
    ],
    finished=False,
    forfeit=True,
    future=True,
    id_=[
        6
    ],
    league_id=[
        6
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "labore id fugi"
    ],
    name=[
        "nostrud veniam"
    ],
    not_started=True,
    number_of_games=[
        7
    ],
    opponent_id=[
        10
    ],
    opponents_filled=False,
    past=True,
    running=False,
    scheduled_at=[
        "sed Du"
    ],
    serie_id=[
        10
    ],
    slug=[
        "GJ7GWuEfy"
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
        6
    ],
    videogame_version=[
        "6.4314860.74685349364"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverKogMatches(
    begin_at=[
        "Lo"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        False
    ],
    end_at=[
        "eu minim par"
    ],
    forfeit=[
        True
    ],
    id_=[
        6
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "est"
    ],
    name=[
        "Lorem "
    ],
    number_of_games=[
        2
    ],
    scheduled_at=[
        "et"
    ],
    slug=[
        "vBKKlSKdbR"
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
search=SearchOverKogMatches(
    match_type="all_games_played",
    name="cillum v",
    slug="Vy-2dZKJxf",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverKogMatches, RangeOverKogMatches, SearchOverKogMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverKogMatches(
    begin_at=[
        "Du"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "voluptate"
    ],
    finished=False,
    forfeit=True,
    future=True,
    id_=[
        6
    ],
    league_id=[
        6
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "labore id fugi"
    ],
    name=[
        "nostrud veniam"
    ],
    not_started=True,
    number_of_games=[
        7
    ],
    opponent_id=[
        10
    ],
    opponents_filled=False,
    past=True,
    running=False,
    scheduled_at=[
        "sed Du"
    ],
    serie_id=[
        10
    ],
    slug=[
        "GJ7GWuEfy"
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
        6
    ],
    videogame_version=[
        "6.4314860.74685349364"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverKogMatches(
    begin_at=[
        "Lo"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        False
    ],
    end_at=[
        "eu minim par"
    ],
    forfeit=[
        True
    ],
    id_=[
        6
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "est"
    ],
    name=[
        "Lorem "
    ],
    number_of_games=[
        2
    ],
    scheduled_at=[
        "et"
    ],
    slug=[
        "vBKKlSKdbR"
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
search=SearchOverKogMatches(
    match_type="all_games_played",
    name="cillum v",
    slug="Vy-2dZKJxf",
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
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverKogMatches, RangeOverKogMatches, SearchOverKogMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverKogMatches(
    begin_at=[
        "Du"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "voluptate"
    ],
    finished=False,
    forfeit=True,
    future=True,
    id_=[
        6
    ],
    league_id=[
        6
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "labore id fugi"
    ],
    name=[
        "nostrud veniam"
    ],
    not_started=True,
    number_of_games=[
        7
    ],
    opponent_id=[
        10
    ],
    opponents_filled=False,
    past=True,
    running=False,
    scheduled_at=[
        "sed Du"
    ],
    serie_id=[
        10
    ],
    slug=[
        "GJ7GWuEfy"
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
        6
    ],
    videogame_version=[
        "6.4314860.74685349364"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverKogMatches(
    begin_at=[
        "Lo"
    ],
    detailed_stats=[
        True
    ],
    draw=[
        False
    ],
    end_at=[
        "eu minim par"
    ],
    forfeit=[
        True
    ],
    id_=[
        6
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "est"
    ],
    name=[
        "Lorem "
    ],
    number_of_games=[
        2
    ],
    scheduled_at=[
        "et"
    ],
    slug=[
        "vBKKlSKdbR"
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
search=SearchOverKogMatches(
    match_type="all_games_played",
    name="cillum v",
    slug="Vy-2dZKJxf",
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

<!-- This file was generated by liblab | https://liblab.com/ -->
