# MatchesService

A list of all methods in the `MatchesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                           | Description                                          |
| :-------------------------------------------------------------------------------- | :--------------------------------------------------- |
| [get_matches](#get_matches)                                                       | List matches                                         |
| [get_matches_past](#get_matches_past)                                             | List past matches                                    |
| [get_matches_running](#get_matches_running)                                       | List currently running matches                       |
| [get_matches_upcoming](#get_matches_upcoming)                                     | List upcoming matches                                |
| [get_matches_match_id_or_slug](#get_matches_match_id_or_slug)                     | Get a single match by ID or by slug                  |
| [get_matches_match_id_or_slug_opponents](#get_matches_match_id_or_slug_opponents) | List opponents (player or teams) for the given match |

## get_matches

List matches

- HTTP Method: `GET`
- Endpoint: `/matches`

**Parameters**

| Name     | Type                                                | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverMatches](../models/FilterOverMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverMatches](../models/RangeOverMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverMatches](../models/SearchOverMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

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

result = sdk.matches.get_matches(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_matches_past

List past matches

- HTTP Method: `GET`
- Endpoint: `/matches/past`

**Parameters**

| Name     | Type                                                | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverMatches](../models/FilterOverMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverMatches](../models/RangeOverMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverMatches](../models/SearchOverMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

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

result = sdk.matches.get_matches_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_matches_running

List currently running matches

- HTTP Method: `GET`
- Endpoint: `/matches/running`

**Parameters**

| Name     | Type                                                | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverMatches](../models/FilterOverMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverMatches](../models/RangeOverMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverMatches](../models/SearchOverMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

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

result = sdk.matches.get_matches_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_matches_upcoming

List upcoming matches

- HTTP Method: `GET`
- Endpoint: `/matches/upcoming`

**Parameters**

| Name     | Type                                                | Required | Description                                                                                                                                         |
| :------- | :-------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverMatches](../models/FilterOverMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverMatches](../models/RangeOverMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                           | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverMatches](../models/SearchOverMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                           | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                 | ❌       | Equivalent to `page[size]`                                                                                                                          |

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

result = sdk.matches.get_matches_upcoming(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_matches_match_id_or_slug

Get a single match by ID or by slug

- HTTP Method: `GET`
- Endpoint: `/matches/{match_id_or_slug}`

**Parameters**

| Name             | Type                                        | Required | Description        |
| :--------------- | :------------------------------------------ | :------- | :----------------- |
| match_id_or_slug | [MatchIdOrSlug](../models/MatchIdOrSlug.md) | ✅       | A match ID or slug |

**Return Type**

`Match`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
match_id_or_slug=5

result = sdk.matches.get_matches_match_id_or_slug(match_id_or_slug=match_id_or_slug)

print(result)
```

## get_matches_match_id_or_slug_opponents

List opponents (player or teams) for the given match

- HTTP Method: `GET`
- Endpoint: `/matches/{match_id_or_slug}/opponents`

**Parameters**

| Name             | Type                                        | Required | Description        |
| :--------------- | :------------------------------------------ | :------- | :----------------- |
| match_id_or_slug | [MatchIdOrSlug](../models/MatchIdOrSlug.md) | ✅       | A match ID or slug |

**Return Type**

`MatchOpponentsObject`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
match_id_or_slug=5

result = sdk.matches.get_matches_match_id_or_slug_opponents(match_id_or_slug=match_id_or_slug)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
