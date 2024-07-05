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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverShortTournaments, RangeOverShortTournaments, SearchOverShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverShortTournaments(
    begin_at=[
        "qui"
    ],
    detailed_stats=True,
    end_at=[
        "mollit"
    ],
    has_bracket=True,
    id_=[
        5
    ],
    live_supported=True,
    modified_at=[
        "laborum"
    ],
    name=[
        "estlaboris e"
    ],
    prizepool=[
        "labore"
    ],
    serie_id=[
        2
    ],
    slug=[
        "bw"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        10
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverShortTournaments(
    begin_at=[
        "do proident ve"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "adipisicin"
    ],
    has_bracket=[
        False
    ],
    id_=[
        2
    ],
    modified_at=[
        "of"
    ],
    name=[
        "occaec"
    ],
    prizepool=[
        "labori"
    ],
    serie_id=[
        9
    ],
    slug=[
        "jifeh"
    ],
    tier=[
        "a"
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
search=SearchOverShortTournaments(
    name="in amet",
    prizepool="qui tempor",
    slug="g",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverShortTournaments, RangeOverShortTournaments, SearchOverShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverShortTournaments(
    begin_at=[
        "qui"
    ],
    detailed_stats=True,
    end_at=[
        "mollit"
    ],
    has_bracket=True,
    id_=[
        5
    ],
    live_supported=True,
    modified_at=[
        "laborum"
    ],
    name=[
        "estlaboris e"
    ],
    prizepool=[
        "labore"
    ],
    serie_id=[
        2
    ],
    slug=[
        "bw"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        10
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverShortTournaments(
    begin_at=[
        "do proident ve"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "adipisicin"
    ],
    has_bracket=[
        False
    ],
    id_=[
        2
    ],
    modified_at=[
        "of"
    ],
    name=[
        "occaec"
    ],
    prizepool=[
        "labori"
    ],
    serie_id=[
        9
    ],
    slug=[
        "jifeh"
    ],
    tier=[
        "a"
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
search=SearchOverShortTournaments(
    name="in amet",
    prizepool="qui tempor",
    slug="g",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverShortTournaments, RangeOverShortTournaments, SearchOverShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverShortTournaments(
    begin_at=[
        "qui"
    ],
    detailed_stats=True,
    end_at=[
        "mollit"
    ],
    has_bracket=True,
    id_=[
        5
    ],
    live_supported=True,
    modified_at=[
        "laborum"
    ],
    name=[
        "estlaboris e"
    ],
    prizepool=[
        "labore"
    ],
    serie_id=[
        2
    ],
    slug=[
        "bw"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        10
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverShortTournaments(
    begin_at=[
        "do proident ve"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "adipisicin"
    ],
    has_bracket=[
        False
    ],
    id_=[
        2
    ],
    modified_at=[
        "of"
    ],
    name=[
        "occaec"
    ],
    prizepool=[
        "labori"
    ],
    serie_id=[
        9
    ],
    slug=[
        "jifeh"
    ],
    tier=[
        "a"
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
search=SearchOverShortTournaments(
    name="in amet",
    prizepool="qui tempor",
    slug="g",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverShortTournaments, RangeOverShortTournaments, SearchOverShortTournaments

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverShortTournaments(
    begin_at=[
        "qui"
    ],
    detailed_stats=True,
    end_at=[
        "mollit"
    ],
    has_bracket=True,
    id_=[
        5
    ],
    live_supported=True,
    modified_at=[
        "laborum"
    ],
    name=[
        "estlaboris e"
    ],
    prizepool=[
        "labore"
    ],
    serie_id=[
        2
    ],
    slug=[
        "bw"
    ],
    tier=[
        "a"
    ],
    videogame_title=[
        10
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverShortTournaments(
    begin_at=[
        "do proident ve"
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "adipisicin"
    ],
    has_bracket=[
        False
    ],
    id_=[
        2
    ],
    modified_at=[
        "of"
    ],
    name=[
        "occaec"
    ],
    prizepool=[
        "labori"
    ],
    serie_id=[
        9
    ],
    slug=[
        "jifeh"
    ],
    tier=[
        "a"
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
search=SearchOverShortTournaments(
    name="in amet",
    prizepool="qui tempor",
    slug="g",
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
from pandascore import Pandascore, Environment

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
tournament_id_or_slug=7

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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverBrackets, RangeOverBrackets, SearchOverBrackets

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
tournament_id_or_slug=7
filter=FilterOverBrackets(
    begin_at=[
        "sint eu"
    ],
    detailed_stats=True,
    draw=False,
    end_at=[
        "anim nost"
    ],
    forfeit=True,
    id_=[
        7
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "q"
    ],
    name=[
        "inculpa sed ea"
    ],
    number_of_games=[
        6
    ],
    scheduled_at=[
        "non"
    ],
    slug=[
        "rMYc2q79"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        6
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverBrackets(
    begin_at=[
        "ea et"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "sed p"
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
        "nostru"
    ],
    name=[
        "quis nisi ul"
    ],
    number_of_games=[
        8
    ],
    scheduled_at=[
        "c"
    ],
    slug=[
        "8DnTzPVF8"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        10
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
search=SearchOverBrackets(
    match_type="all_games_played",
    name="eiusmod",
    slug="hYdz0Im7kJG",
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverMatches, RangeOverMatches, SearchOverMatches

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
tournament_id_or_slug=7
filter=FilterOverMatches(
    begin_at=[
        "esse enim in"
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "fugiat offic"
    ],
    finished=True,
    forfeit=True,
    future=True,
    id_=[
        1
    ],
    league_id=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "occa"
    ],
    name=[
        "non sed"
    ],
    not_started=False,
    number_of_games=[
        9
    ],
    opponent_id=[
        7
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "es"
    ],
    serie_id=[
        4
    ],
    slug=[
        "ZBBpq-e"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        2
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        10
    ],
    videogame_version=[
        "0065.71"
    ],
    winner_id=[
        9
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverMatches(
    begin_at=[
        "sed occ"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        False
    ],
    end_at=[
        "aliq"
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
        "proident culpa"
    ],
    name=[
        "in ad"
    ],
    number_of_games=[
        1
    ],
    scheduled_at=[
        "oc"
    ],
    slug=[
        "8-ymAu4"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        8
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
search=SearchOverMatches(
    match_type="all_games_played",
    name="Excepteu",
    slug="Ld3hli",
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
from pandascore import Pandascore, Environment

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
tournament_id_or_slug=7

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
from pandascore import Pandascore, Environment

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
tournament_id_or_slug=7
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverTeams, RangeOverTeams, SearchOverTeams

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
tournament_id_or_slug=7
filter=FilterOverTeams(
    acronym=[
        "amet ut Exce"
    ],
    id_=[
        1
    ],
    location=[
        "sunt amet"
    ],
    modified_at=[
        "ipsum eu "
    ],
    name=[
        "ut vel"
    ],
    slug=[
        "cikaz7tv40"
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverTeams(
    acronym=[
        "nisi Duis Lor"
    ],
    id_=[
        5
    ],
    location=[
        "veniam"
    ],
    modified_at=[
        "id"
    ],
    name=[
        "pariatur mini"
    ],
    slug=[
        "9"
    ]
)
sort=[
    ""
]
search=SearchOverTeams(
    acronym="in do",
    location="proident l",
    name="occaeca",
    slug="46q"
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
