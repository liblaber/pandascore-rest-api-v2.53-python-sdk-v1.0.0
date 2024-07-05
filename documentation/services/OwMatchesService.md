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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverOwMatches, RangeOverOwMatches, SearchOverOwMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverOwMatches(
    begin_at=[
        "nisi o"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "ut cupidat"
    ],
    finished=True,
    forfeit=True,
    future=False,
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
        "ut nu"
    ],
    name=[
        "labore"
    ],
    not_started=True,
    number_of_games=[
        2
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "id la"
    ],
    serie_id=[
        8
    ],
    slug=[
        "AxM1CNP"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        8
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        10
    ],
    videogame_version=[
        "0329546.69"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverOwMatches(
    begin_at=[
        "incidid"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "veniam"
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
        "aute"
    ],
    name=[
        "voluptate"
    ],
    number_of_games=[
        7
    ],
    scheduled_at=[
        "aute n"
    ],
    slug=[
        "Ht8"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        5
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
search=SearchOverOwMatches(
    match_type="all_games_played",
    name="sunt ut",
    slug="m3sjw21R7a2",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverOwMatches, RangeOverOwMatches, SearchOverOwMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverOwMatches(
    begin_at=[
        "nisi o"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "ut cupidat"
    ],
    finished=True,
    forfeit=True,
    future=False,
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
        "ut nu"
    ],
    name=[
        "labore"
    ],
    not_started=True,
    number_of_games=[
        2
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "id la"
    ],
    serie_id=[
        8
    ],
    slug=[
        "AxM1CNP"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        8
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        10
    ],
    videogame_version=[
        "0329546.69"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverOwMatches(
    begin_at=[
        "incidid"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "veniam"
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
        "aute"
    ],
    name=[
        "voluptate"
    ],
    number_of_games=[
        7
    ],
    scheduled_at=[
        "aute n"
    ],
    slug=[
        "Ht8"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        5
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
search=SearchOverOwMatches(
    match_type="all_games_played",
    name="sunt ut",
    slug="m3sjw21R7a2",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverOwMatches, RangeOverOwMatches, SearchOverOwMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverOwMatches(
    begin_at=[
        "nisi o"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "ut cupidat"
    ],
    finished=True,
    forfeit=True,
    future=False,
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
        "ut nu"
    ],
    name=[
        "labore"
    ],
    not_started=True,
    number_of_games=[
        2
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "id la"
    ],
    serie_id=[
        8
    ],
    slug=[
        "AxM1CNP"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        8
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        10
    ],
    videogame_version=[
        "0329546.69"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverOwMatches(
    begin_at=[
        "incidid"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "veniam"
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
        "aute"
    ],
    name=[
        "voluptate"
    ],
    number_of_games=[
        7
    ],
    scheduled_at=[
        "aute n"
    ],
    slug=[
        "Ht8"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        5
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
search=SearchOverOwMatches(
    match_type="all_games_played",
    name="sunt ut",
    slug="m3sjw21R7a2",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverOwMatches, RangeOverOwMatches, SearchOverOwMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverOwMatches(
    begin_at=[
        "nisi o"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "ut cupidat"
    ],
    finished=True,
    forfeit=True,
    future=False,
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
        "ut nu"
    ],
    name=[
        "labore"
    ],
    not_started=True,
    number_of_games=[
        2
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "id la"
    ],
    serie_id=[
        8
    ],
    slug=[
        "AxM1CNP"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        8
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        10
    ],
    videogame_version=[
        "0329546.69"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverOwMatches(
    begin_at=[
        "incidid"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "veniam"
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
        "aute"
    ],
    name=[
        "voluptate"
    ],
    number_of_games=[
        7
    ],
    scheduled_at=[
        "aute n"
    ],
    slug=[
        "Ht8"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        5
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
search=SearchOverOwMatches(
    match_type="all_games_played",
    name="sunt ut",
    slug="m3sjw21R7a2",
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
