# CounterStrikeMatchesService

A list of all methods in the `CounterStrikeMatchesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                 | Description                                     |
| :---------------------------------------------------------------------- | :---------------------------------------------- |
| [get_csgo_matches](#get_csgo_matches)                                   | List matches for the Counter-Strike videogame   |
| [get_csgo_matches_past](#get_csgo_matches_past)                         | List past Counter-Strike matches                |
| [get_csgo_matches_running](#get_csgo_matches_running)                   | List running Counter-Strike matches             |
| [get_csgo_matches_upcoming](#get_csgo_matches_upcoming)                 | List upcoming Counter-Strike matches            |
| [get_csgo_matches_match_id_or_slug](#get_csgo_matches_match_id_or_slug) | Get a single Counter-Strike match by ID or slug |

## get_csgo_matches

List matches for the Counter-Strike videogame

- HTTP Method: `GET`
- Endpoint: `/csgo/matches`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCsgoMatches](../models/FilterOverCsgoMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCsgoMatches](../models/RangeOverCsgoMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCsgoMatches](../models/SearchOverCsgoMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCsgoMatches, RangeOverCsgoMatches, SearchOverCsgoMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCsgoMatches(
    begin_at=[
        "incidi"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "exercita"
    ],
    finished=True,
    forfeit=False,
    future=False,
    id_=[
        3
    ],
    league_id=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "aliqua"
    ],
    name=[
        "aliquip eius"
    ],
    not_started=True,
    number_of_games=[
        10
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=False,
    running=False,
    scheduled_at=[
        "voluptate adipi"
    ],
    serie_id=[
        5
    ],
    slug=[
        "kid"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        5
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        4
    ],
    videogame_version=[
        "46404802.4461.3142"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCsgoMatches(
    begin_at=[
        "incididunt ut"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        True
    ],
    end_at=[
        "in ex aute"
    ],
    forfeit=[
        False
    ],
    id_=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "do"
    ],
    name=[
        "adipisici"
    ],
    number_of_games=[
        0
    ],
    scheduled_at=[
        "dolor Ut"
    ],
    slug=[
        "R37RucjN7s"
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
search=SearchOverCsgoMatches(
    match_type="all_games_played",
    name="aliqua anim",
    slug="x6lAktgCkB",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.counter_strike_matches.get_csgo_matches(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_csgo_matches_past

List past Counter-Strike matches

- HTTP Method: `GET`
- Endpoint: `/csgo/matches/past`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCsgoMatches](../models/FilterOverCsgoMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCsgoMatches](../models/RangeOverCsgoMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCsgoMatches](../models/SearchOverCsgoMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCsgoMatches, RangeOverCsgoMatches, SearchOverCsgoMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCsgoMatches(
    begin_at=[
        "incidi"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "exercita"
    ],
    finished=True,
    forfeit=False,
    future=False,
    id_=[
        3
    ],
    league_id=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "aliqua"
    ],
    name=[
        "aliquip eius"
    ],
    not_started=True,
    number_of_games=[
        10
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=False,
    running=False,
    scheduled_at=[
        "voluptate adipi"
    ],
    serie_id=[
        5
    ],
    slug=[
        "kid"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        5
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        4
    ],
    videogame_version=[
        "46404802.4461.3142"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCsgoMatches(
    begin_at=[
        "incididunt ut"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        True
    ],
    end_at=[
        "in ex aute"
    ],
    forfeit=[
        False
    ],
    id_=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "do"
    ],
    name=[
        "adipisici"
    ],
    number_of_games=[
        0
    ],
    scheduled_at=[
        "dolor Ut"
    ],
    slug=[
        "R37RucjN7s"
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
search=SearchOverCsgoMatches(
    match_type="all_games_played",
    name="aliqua anim",
    slug="x6lAktgCkB",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.counter_strike_matches.get_csgo_matches_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_csgo_matches_running

List running Counter-Strike matches

- HTTP Method: `GET`
- Endpoint: `/csgo/matches/running`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCsgoMatches](../models/FilterOverCsgoMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCsgoMatches](../models/RangeOverCsgoMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCsgoMatches](../models/SearchOverCsgoMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCsgoMatches, RangeOverCsgoMatches, SearchOverCsgoMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCsgoMatches(
    begin_at=[
        "incidi"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "exercita"
    ],
    finished=True,
    forfeit=False,
    future=False,
    id_=[
        3
    ],
    league_id=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "aliqua"
    ],
    name=[
        "aliquip eius"
    ],
    not_started=True,
    number_of_games=[
        10
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=False,
    running=False,
    scheduled_at=[
        "voluptate adipi"
    ],
    serie_id=[
        5
    ],
    slug=[
        "kid"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        5
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        4
    ],
    videogame_version=[
        "46404802.4461.3142"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCsgoMatches(
    begin_at=[
        "incididunt ut"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        True
    ],
    end_at=[
        "in ex aute"
    ],
    forfeit=[
        False
    ],
    id_=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "do"
    ],
    name=[
        "adipisici"
    ],
    number_of_games=[
        0
    ],
    scheduled_at=[
        "dolor Ut"
    ],
    slug=[
        "R37RucjN7s"
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
search=SearchOverCsgoMatches(
    match_type="all_games_played",
    name="aliqua anim",
    slug="x6lAktgCkB",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.counter_strike_matches.get_csgo_matches_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_csgo_matches_upcoming

List upcoming Counter-Strike matches

- HTTP Method: `GET`
- Endpoint: `/csgo/matches/upcoming`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCsgoMatches](../models/FilterOverCsgoMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCsgoMatches](../models/RangeOverCsgoMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCsgoMatches](../models/SearchOverCsgoMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCsgoMatches, RangeOverCsgoMatches, SearchOverCsgoMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCsgoMatches(
    begin_at=[
        "incidi"
    ],
    detailed_stats=True,
    draw=True,
    end_at=[
        "exercita"
    ],
    finished=True,
    forfeit=False,
    future=False,
    id_=[
        3
    ],
    league_id=[
        4
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "aliqua"
    ],
    name=[
        "aliquip eius"
    ],
    not_started=True,
    number_of_games=[
        10
    ],
    opponent_id=[
        10
    ],
    opponents_filled=True,
    past=False,
    running=False,
    scheduled_at=[
        "voluptate adipi"
    ],
    serie_id=[
        5
    ],
    slug=[
        "kid"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        5
    ],
    unscheduled=False,
    videogame=[
        1
    ],
    videogame_title=[
        4
    ],
    videogame_version=[
        "46404802.4461.3142"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverCsgoMatches(
    begin_at=[
        "incididunt ut"
    ],
    detailed_stats=[
        False
    ],
    draw=[
        True
    ],
    end_at=[
        "in ex aute"
    ],
    forfeit=[
        False
    ],
    id_=[
        5
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "do"
    ],
    name=[
        "adipisici"
    ],
    number_of_games=[
        0
    ],
    scheduled_at=[
        "dolor Ut"
    ],
    slug=[
        "R37RucjN7s"
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
search=SearchOverCsgoMatches(
    match_type="all_games_played",
    name="aliqua anim",
    slug="x6lAktgCkB",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.counter_strike_matches.get_csgo_matches_upcoming(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_csgo_matches_match_id_or_slug

Get a single Counter-Strike match by ID or slug

- HTTP Method: `GET`
- Endpoint: `/csgo/matches/{match_id_or_slug}`

**Parameters**

| Name             | Type                                        | Required | Description        |
| :--------------- | :------------------------------------------ | :------- | :----------------- |
| match_id_or_slug | [MatchIdOrSlug](../models/MatchIdOrSlug.md) | ✅       | A match ID or slug |

**Return Type**

`CsgoMatch`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
match_id_or_slug=5

result = sdk.counter_strike_matches.get_csgo_matches_match_id_or_slug(match_id_or_slug=match_id_or_slug)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
