# TournamentsService

A list of all methods in the `TournamentsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                             | Description                                                |
| :-------------------------------------------------------------------------------------------------- | :--------------------------------------------------------- |
| [get_tournaments](#get_tournaments)                                                                 | List tournaments                                           |
| [get_tournaments_past](#get_tournaments_past)                                                       | List past tournaments                                      |
| [get_tournaments_running](#get_tournaments_running)                                                 | List currently running tournaments                         |
| [get_tournaments_upcoming](#get_tournaments_upcoming)                                               | List upcoming tournaments                                  |
| [get_tournaments_tournament_id_or_slug](#get_tournaments_tournament_id_or_slug)                     | Get a single tournament by ID or by slug                   |
| [get_tournaments_tournament_id_or_slug_brackets](#get_tournaments_tournament_id_or_slug_brackets)   | Get the brackets of the given tournament                   |
| [get_tournaments_tournament_id_or_slug_matches](#get_tournaments_tournament_id_or_slug_matches)     | List matches for the given tournament                      |
| [get_tournaments_tournament_id_or_slug_rosters](#get_tournaments_tournament_id_or_slug_rosters)     | List participants (player or team) for a given tournament. |
| [get_tournaments_tournament_id_or_slug_standings](#get_tournaments_tournament_id_or_slug_standings) | Get the current standings for a given tournament           |
| [get_tournaments_tournament_id_or_slug_teams](#get_tournaments_tournament_id_or_slug_teams)         | List teams for the given tournament                        |

## get_tournaments

List tournaments

- HTTP Method: `GET`
- Endpoint: `/tournaments`

**Parameters**

| Name     | Type                                                                  | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverShortTournaments](../models/FilterOverShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverShortTournaments](../models/RangeOverShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverShortTournaments](../models/SearchOverShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverShortTournaments, RangeOverShortTournaments, SearchOverShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverShortTournaments(
    begin_at=[
        "pariat"
    ],
    detailed_stats=True,
    end_at=[
        "eli"
    ],
    has_bracket=False,
    id_=[
        4
    ],
    live_supported=False,
    modified_at=[
        "cillu"
    ],
    name=[
        "Excepteur do"
    ],
    prizepool=[
        "in ut veniam "
    ],
    serie_id=[
        10
    ],
    slug=[
        "z160_"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        5
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverShortTournaments(
    begin_at=[
        "et"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "commo"
    ],
    has_bracket=[
        False
    ],
    id_=[
        1
    ],
    modified_at=[
        "nul"
    ],
    name=[
        "enim "
    ],
    prizepool=[
        "qui ull"
    ],
    serie_id=[
        3
    ],
    slug=[
        "vyokv"
    ],
    tier=[
        "a"
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
search=SearchOverShortTournaments(
    name="sunt minim",
    prizepool="utid magna es",
    slug="50l9n",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.tournaments.get_tournaments(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_tournaments_past

List past tournaments

- HTTP Method: `GET`
- Endpoint: `/tournaments/past`

**Parameters**

| Name     | Type                                                                  | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverShortTournaments](../models/FilterOverShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverShortTournaments](../models/RangeOverShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverShortTournaments](../models/SearchOverShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverShortTournaments, RangeOverShortTournaments, SearchOverShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverShortTournaments(
    begin_at=[
        "pariat"
    ],
    detailed_stats=True,
    end_at=[
        "eli"
    ],
    has_bracket=False,
    id_=[
        4
    ],
    live_supported=False,
    modified_at=[
        "cillu"
    ],
    name=[
        "Excepteur do"
    ],
    prizepool=[
        "in ut veniam "
    ],
    serie_id=[
        10
    ],
    slug=[
        "z160_"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        5
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverShortTournaments(
    begin_at=[
        "et"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "commo"
    ],
    has_bracket=[
        False
    ],
    id_=[
        1
    ],
    modified_at=[
        "nul"
    ],
    name=[
        "enim "
    ],
    prizepool=[
        "qui ull"
    ],
    serie_id=[
        3
    ],
    slug=[
        "vyokv"
    ],
    tier=[
        "a"
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
search=SearchOverShortTournaments(
    name="sunt minim",
    prizepool="utid magna es",
    slug="50l9n",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.tournaments.get_tournaments_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_tournaments_running

List currently running tournaments

- HTTP Method: `GET`
- Endpoint: `/tournaments/running`

**Parameters**

| Name     | Type                                                                  | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverShortTournaments](../models/FilterOverShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverShortTournaments](../models/RangeOverShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverShortTournaments](../models/SearchOverShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverShortTournaments, RangeOverShortTournaments, SearchOverShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverShortTournaments(
    begin_at=[
        "pariat"
    ],
    detailed_stats=True,
    end_at=[
        "eli"
    ],
    has_bracket=False,
    id_=[
        4
    ],
    live_supported=False,
    modified_at=[
        "cillu"
    ],
    name=[
        "Excepteur do"
    ],
    prizepool=[
        "in ut veniam "
    ],
    serie_id=[
        10
    ],
    slug=[
        "z160_"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        5
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverShortTournaments(
    begin_at=[
        "et"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "commo"
    ],
    has_bracket=[
        False
    ],
    id_=[
        1
    ],
    modified_at=[
        "nul"
    ],
    name=[
        "enim "
    ],
    prizepool=[
        "qui ull"
    ],
    serie_id=[
        3
    ],
    slug=[
        "vyokv"
    ],
    tier=[
        "a"
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
search=SearchOverShortTournaments(
    name="sunt minim",
    prizepool="utid magna es",
    slug="50l9n",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.tournaments.get_tournaments_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_tournaments_upcoming

List upcoming tournaments

- HTTP Method: `GET`
- Endpoint: `/tournaments/upcoming`

**Parameters**

| Name     | Type                                                                  | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverShortTournaments](../models/FilterOverShortTournaments.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverShortTournaments](../models/RangeOverShortTournaments.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverShortTournaments](../models/SearchOverShortTournaments.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[ShortTournament]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverShortTournaments, RangeOverShortTournaments, SearchOverShortTournaments

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverShortTournaments(
    begin_at=[
        "pariat"
    ],
    detailed_stats=True,
    end_at=[
        "eli"
    ],
    has_bracket=False,
    id_=[
        4
    ],
    live_supported=False,
    modified_at=[
        "cillu"
    ],
    name=[
        "Excepteur do"
    ],
    prizepool=[
        "in ut veniam "
    ],
    serie_id=[
        10
    ],
    slug=[
        "z160_"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        5
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverShortTournaments(
    begin_at=[
        "et"
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "commo"
    ],
    has_bracket=[
        False
    ],
    id_=[
        1
    ],
    modified_at=[
        "nul"
    ],
    name=[
        "enim "
    ],
    prizepool=[
        "qui ull"
    ],
    serie_id=[
        3
    ],
    slug=[
        "vyokv"
    ],
    tier=[
        "a"
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
search=SearchOverShortTournaments(
    name="sunt minim",
    prizepool="utid magna es",
    slug="50l9n",
    tier="a",
    winner_type="Player"
)
page=1

result = sdk.tournaments.get_tournaments_upcoming(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_tournaments_tournament_id_or_slug

Get a single tournament by ID or by slug

- HTTP Method: `GET`
- Endpoint: `/tournaments/{tournament_id_or_slug}`

**Parameters**

| Name                  | Type                                                  | Required | Description             |
| :-------------------- | :---------------------------------------------------- | :------- | :---------------------- |
| tournament_id_or_slug | [TournamentIdOrSlug](../models/TournamentIdOrSlug.md) | ✅       | A tournament ID or slug |

**Return Type**

`Tournament`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
tournament_id_or_slug=2

result = sdk.tournaments.get_tournaments_tournament_id_or_slug(tournament_id_or_slug=tournament_id_or_slug)

print(result)
```

## get_tournaments_tournament_id_or_slug_brackets

Get the brackets of the given tournament

- HTTP Method: `GET`
- Endpoint: `/tournaments/{tournament_id_or_slug}/brackets`

**Parameters**

| Name                  | Type                                                  | Required | Description                                                                                                                                         |
| :-------------------- | :---------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| tournament_id_or_slug | [TournamentIdOrSlug](../models/TournamentIdOrSlug.md) | ✅       | A tournament ID or slug                                                                                                                             |
| filter                | [FilterOverBrackets](../models/FilterOverBrackets.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range                 | [RangeOverBrackets](../models/RangeOverBrackets.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort                  | List[any]                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search                | [SearchOverBrackets](../models/SearchOverBrackets.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page                  | [Page](../models/Page.md)                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page              | int                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Bracket]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverBrackets, RangeOverBrackets, SearchOverBrackets

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
tournament_id_or_slug=2
filter=FilterOverBrackets(
    begin_at=[
        "velit dolor "
    ],
    detailed_stats=False,
    draw=True,
    end_at=[
        "elit "
    ],
    forfeit=True,
    id_=[
        1
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "irure id"
    ],
    name=[
        "nostrud ex "
    ],
    number_of_games=[
        0
    ],
    scheduled_at=[
        "tempor ut qui "
    ],
    slug=[
        "e HEgmFUZPl"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        10
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverBrackets(
    begin_at=[
        "tem"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        True
    ],
    end_at=[
        "irure an"
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
        "labore n"
    ],
    name=[
        "mollit nulla"
    ],
    number_of_games=[
        0
    ],
    scheduled_at=[
        "in volupta"
    ],
    slug=[
        "-"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        7
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
search=SearchOverBrackets(
    match_type="all_games_played",
    name="quiscon",
    slug="EvVWpSZ",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.tournaments.get_tournaments_tournament_id_or_slug_brackets(
    tournament_id_or_slug=tournament_id_or_slug,
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_tournaments_tournament_id_or_slug_matches

List matches for the given tournament

- HTTP Method: `GET`
- Endpoint: `/tournaments/{tournament_id_or_slug}/matches`

**Parameters**

| Name                  | Type                                                  | Required | Description                                                                                                                                         |
| :-------------------- | :---------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| tournament_id_or_slug | [TournamentIdOrSlug](../models/TournamentIdOrSlug.md) | ✅       | A tournament ID or slug                                                                                                                             |
| filter                | [FilterOverMatches](../models/FilterOverMatches.md)   | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range                 | [RangeOverMatches](../models/RangeOverMatches.md)     | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort                  | List[any]                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search                | [SearchOverMatches](../models/SearchOverMatches.md)   | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page                  | [Page](../models/Page.md)                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page              | int                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverMatches, RangeOverMatches, SearchOverMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
tournament_id_or_slug=2
filter=FilterOverMatches(
    begin_at=[
        "ani"
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "ad ut com"
    ],
    finished=False,
    forfeit=False,
    future=True,
    id_=[
        3
    ],
    league_id=[
        9
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "aute sit"
    ],
    name=[
        "exercitation te"
    ],
    not_started=False,
    number_of_games=[
        8
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=False,
    running=True,
    scheduled_at=[
        "esse aute n"
    ],
    serie_id=[
        10
    ],
    slug=[
        "HiGqjR9"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        3
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        6
    ],
    videogame_version=[
        "1125897835.45"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverMatches(
    begin_at=[
        "al"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "do d"
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
        "dolore ve"
    ],
    name=[
        "dolore "
    ],
    number_of_games=[
        10
    ],
    scheduled_at=[
        "nisi sed aut"
    ],
    slug=[
        "bAjOZ"
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
search=SearchOverMatches(
    match_type="all_games_played",
    name="nulla veniam ",
    slug="WfL1ZPQ",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.tournaments.get_tournaments_tournament_id_or_slug_matches(
    tournament_id_or_slug=tournament_id_or_slug,
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_tournaments_tournament_id_or_slug_rosters

List participants (player or team) for a given tournament.

- HTTP Method: `GET`
- Endpoint: `/tournaments/{tournament_id_or_slug}/rosters`

**Parameters**

| Name                  | Type                                                  | Required | Description             |
| :-------------------- | :---------------------------------------------------- | :------- | :---------------------- |
| tournament_id_or_slug | [TournamentIdOrSlug](../models/TournamentIdOrSlug.md) | ✅       | A tournament ID or slug |

**Return Type**

`TournamentRosters`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
tournament_id_or_slug=2

result = sdk.tournaments.get_tournaments_tournament_id_or_slug_rosters(tournament_id_or_slug=tournament_id_or_slug)

print(result)
```

## get_tournaments_tournament_id_or_slug_standings

Get the current standings for a given tournament

- HTTP Method: `GET`
- Endpoint: `/tournaments/{tournament_id_or_slug}/standings`

**Parameters**

| Name                  | Type                                                  | Required | Description                                                          |
| :-------------------- | :---------------------------------------------------- | :------- | :------------------------------------------------------------------- |
| tournament_id_or_slug | [TournamentIdOrSlug](../models/TournamentIdOrSlug.md) | ✅       | A tournament ID or slug                                              |
| page                  | [Page](../models/Page.md)                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2` |
| per_page              | int                                                   | ❌       | Equivalent to `page[size]`                                           |

**Return Type**

`List[Standing]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
tournament_id_or_slug=2
page=1

result = sdk.tournaments.get_tournaments_tournament_id_or_slug_standings(
    tournament_id_or_slug=tournament_id_or_slug,
    page=page,
    per_page=50
)

print(result)
```

## get_tournaments_tournament_id_or_slug_teams

List teams for the given tournament

- HTTP Method: `GET`
- Endpoint: `/tournaments/{tournament_id_or_slug}/teams`

**Parameters**

| Name                  | Type                                                  | Required | Description                                                                                                                                         |
| :-------------------- | :---------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| tournament_id_or_slug | [TournamentIdOrSlug](../models/TournamentIdOrSlug.md) | ✅       | A tournament ID or slug                                                                                                                             |
| filter                | [FilterOverTeams](../models/FilterOverTeams.md)       | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range                 | [RangeOverTeams](../models/RangeOverTeams.md)         | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort                  | List[any]                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search                | [SearchOverTeams](../models/SearchOverTeams.md)       | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page                  | [Page](../models/Page.md)                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page              | int                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Team]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverTeams, RangeOverTeams, SearchOverTeams

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
tournament_id_or_slug=2
filter=FilterOverTeams(
    acronym=[
        "qui dolore"
    ],
    id_=[
        9
    ],
    location=[
        "in reprehende"
    ],
    modified_at=[
        "elit"
    ],
    name=[
        "deserunt conse"
    ],
    slug=[
        "_pbld"
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverTeams(
    acronym=[
        "nulla adipis"
    ],
    id_=[
        6
    ],
    location=[
        "amet comm"
    ],
    modified_at=[
        "non"
    ],
    name=[
        "adipisicing"
    ],
    slug=[
        "b48hhqy"
    ]
)
sort=[
    ""
]
search=SearchOverTeams(
    acronym="exercit",
    location="est L",
    name="culpa Duis t",
    slug="f"
)
page=1

result = sdk.tournaments.get_tournaments_tournament_id_or_slug_teams(
    tournament_id_or_slug=tournament_id_or_slug,
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
