# PubgMatchesService

A list of all methods in the `PubgMatchesService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description                         |
| :------------------------------------------------------ | :---------------------------------- |
| [get_pubg_matches](#get_pubg_matches)                   | List matches for the PUBG videogame |
| [get_pubg_matches_past](#get_pubg_matches_past)         | List past PUBG matches              |
| [get_pubg_matches_running](#get_pubg_matches_running)   | List running PUBG matches           |
| [get_pubg_matches_upcoming](#get_pubg_matches_upcoming) | List upcoming PUBG matches          |

## get_pubg_matches

List matches for the PUBG videogame

- HTTP Method: `GET`
- Endpoint: `/pubg/matches`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverPubgMatches](../models/FilterOverPubgMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverPubgMatches](../models/RangeOverPubgMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverPubgMatches](../models/SearchOverPubgMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverPubgMatches, RangeOverPubgMatches, SearchOverPubgMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverPubgMatches(
    begin_at=[
        "aute eiusmod "
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "ullamco labor"
    ],
    finished=True,
    forfeit=False,
    future=False,
    id_=[
        9
    ],
    league_id=[
        2
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "nisi irure culp"
    ],
    name=[
        "aute "
    ],
    not_started=False,
    number_of_games=[
        10
    ],
    opponent_id=[
        10
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "null"
    ],
    serie_id=[
        4
    ],
    slug=[
        "1wzZ5GZv"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        7
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        5
    ],
    videogame_version=[
        "036.43414"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverPubgMatches(
    begin_at=[
        "ut cillum in "
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "anim"
    ],
    forfeit=[
        True
    ],
    id_=[
        2
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "in ut min"
    ],
    name=[
        "eu in"
    ],
    number_of_games=[
        10
    ],
    scheduled_at=[
        "in "
    ],
    slug=[
        "FDoevNsA"
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
search=SearchOverPubgMatches(
    match_type="all_games_played",
    name="adipisic",
    slug="H",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.pubg_matches.get_pubg_matches(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_pubg_matches_past

List past PUBG matches

- HTTP Method: `GET`
- Endpoint: `/pubg/matches/past`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverPubgMatches](../models/FilterOverPubgMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverPubgMatches](../models/RangeOverPubgMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverPubgMatches](../models/SearchOverPubgMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverPubgMatches, RangeOverPubgMatches, SearchOverPubgMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverPubgMatches(
    begin_at=[
        "aute eiusmod "
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "ullamco labor"
    ],
    finished=True,
    forfeit=False,
    future=False,
    id_=[
        9
    ],
    league_id=[
        2
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "nisi irure culp"
    ],
    name=[
        "aute "
    ],
    not_started=False,
    number_of_games=[
        10
    ],
    opponent_id=[
        10
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "null"
    ],
    serie_id=[
        4
    ],
    slug=[
        "1wzZ5GZv"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        7
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        5
    ],
    videogame_version=[
        "036.43414"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverPubgMatches(
    begin_at=[
        "ut cillum in "
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "anim"
    ],
    forfeit=[
        True
    ],
    id_=[
        2
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "in ut min"
    ],
    name=[
        "eu in"
    ],
    number_of_games=[
        10
    ],
    scheduled_at=[
        "in "
    ],
    slug=[
        "FDoevNsA"
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
search=SearchOverPubgMatches(
    match_type="all_games_played",
    name="adipisic",
    slug="H",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.pubg_matches.get_pubg_matches_past(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_pubg_matches_running

List running PUBG matches

- HTTP Method: `GET`
- Endpoint: `/pubg/matches/running`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverPubgMatches](../models/FilterOverPubgMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverPubgMatches](../models/RangeOverPubgMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverPubgMatches](../models/SearchOverPubgMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverPubgMatches, RangeOverPubgMatches, SearchOverPubgMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverPubgMatches(
    begin_at=[
        "aute eiusmod "
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "ullamco labor"
    ],
    finished=True,
    forfeit=False,
    future=False,
    id_=[
        9
    ],
    league_id=[
        2
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "nisi irure culp"
    ],
    name=[
        "aute "
    ],
    not_started=False,
    number_of_games=[
        10
    ],
    opponent_id=[
        10
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "null"
    ],
    serie_id=[
        4
    ],
    slug=[
        "1wzZ5GZv"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        7
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        5
    ],
    videogame_version=[
        "036.43414"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverPubgMatches(
    begin_at=[
        "ut cillum in "
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "anim"
    ],
    forfeit=[
        True
    ],
    id_=[
        2
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "in ut min"
    ],
    name=[
        "eu in"
    ],
    number_of_games=[
        10
    ],
    scheduled_at=[
        "in "
    ],
    slug=[
        "FDoevNsA"
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
search=SearchOverPubgMatches(
    match_type="all_games_played",
    name="adipisic",
    slug="H",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.pubg_matches.get_pubg_matches_running(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_pubg_matches_upcoming

List upcoming PUBG matches

- HTTP Method: `GET`
- Endpoint: `/pubg/matches/upcoming`

**Parameters**

| Name     | Type                                                        | Required | Description                                                                                                                                         |
| :------- | :---------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverPubgMatches](../models/FilterOverPubgMatches.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverPubgMatches](../models/RangeOverPubgMatches.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                   | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverPubgMatches](../models/SearchOverPubgMatches.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                   | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                         | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Match]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverPubgMatches, RangeOverPubgMatches, SearchOverPubgMatches

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverPubgMatches(
    begin_at=[
        "aute eiusmod "
    ],
    detailed_stats=False,
    draw=False,
    end_at=[
        "ullamco labor"
    ],
    finished=True,
    forfeit=False,
    future=False,
    id_=[
        9
    ],
    league_id=[
        2
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "nisi irure culp"
    ],
    name=[
        "aute "
    ],
    not_started=False,
    number_of_games=[
        10
    ],
    opponent_id=[
        10
    ],
    opponents_filled=False,
    past=True,
    running=True,
    scheduled_at=[
        "null"
    ],
    serie_id=[
        4
    ],
    slug=[
        "1wzZ5GZv"
    ],
    status=[
        "canceled"
    ],
    tournament_id=[
        7
    ],
    unscheduled=True,
    videogame=[
        1
    ],
    videogame_title=[
        5
    ],
    videogame_version=[
        "036.43414"
    ],
    winner_id=[
        7
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverPubgMatches(
    begin_at=[
        "ut cillum in "
    ],
    detailed_stats=[
        True
    ],
    draw=[
        True
    ],
    end_at=[
        "anim"
    ],
    forfeit=[
        True
    ],
    id_=[
        2
    ],
    match_type=[
        "all_games_played"
    ],
    modified_at=[
        "in ut min"
    ],
    name=[
        "eu in"
    ],
    number_of_games=[
        10
    ],
    scheduled_at=[
        "in "
    ],
    slug=[
        "FDoevNsA"
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
search=SearchOverPubgMatches(
    match_type="all_games_played",
    name="adipisic",
    slug="H",
    status="canceled",
    winner_type="Player"
)
page=1

result = sdk.pubg_matches.get_pubg_matches_upcoming(
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
