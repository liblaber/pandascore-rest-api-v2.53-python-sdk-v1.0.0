# LoLGamesService

A list of all methods in the `LoLGamesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                           | Description                                            |
| :-------------------------------------------------------------------------------- | :----------------------------------------------------- |
| [get_lol_games_lol_game_id](#get_lol_games_lol_game_id)                           | Get a single League of Legends game by ID              |
| [get_lol_games_lol_game_id_events](#get_lol_games_lol_game_id_events)             | List events for a given League of Legends game         |
| [get_lol_games_lol_game_id_frames](#get_lol_games_lol_game_id_frames)             | List frames for a given League of Legends game         |
| [get_lol_matches_match_id_or_slug_games](#get_lol_matches_match_id_or_slug_games) | List games for a given League of Legends match         |
| [get_lol_teams_team_id_or_slug_games](#get_lol_teams_team_id_or_slug_games)       | List finished games for a given League of Legends team |

## get_lol_games_lol_game_id

Get a single League of Legends game by ID

- HTTP Method: `GET`
- Endpoint: `/lol/games/{lol_game_id}`

**Parameters**

| Name        | Type | Required | Description   |
| :---------- | :--- | :------- | :------------ |
| lol_game_id | int  | ✅       | A LoL game ID |

**Return Type**

`LoLGame`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.lo_l_games.get_lol_games_lol_game_id(lol_game_id=8)

print(result)
```

## get_lol_games_lol_game_id_events

List events for a given League of Legends game

- HTTP Method: `GET`
- Endpoint: `/lol/games/{lol_game_id}/events`

**Parameters**

| Name        | Type                      | Required | Description                                                          |
| :---------- | :------------------------ | :------- | :------------------------------------------------------------------- |
| lol_game_id | int                       | ✅       | A LoL game ID                                                        |
| page        | [Page](../models/Page.md) | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2` |
| per_page    | int                       | ❌       | Equivalent to `page[size]`                                           |

**Return Type**

`List[LoLGameEvent]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
page=1

result = sdk.lo_l_games.get_lol_games_lol_game_id_events(
    lol_game_id=2,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_games_lol_game_id_frames

List frames for a given League of Legends game

- HTTP Method: `GET`
- Endpoint: `/lol/games/{lol_game_id}/frames`

**Parameters**

| Name        | Type                      | Required | Description                                                          |
| :---------- | :------------------------ | :------- | :------------------------------------------------------------------- |
| lol_game_id | int                       | ✅       | A LoL game ID                                                        |
| page        | [Page](../models/Page.md) | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2` |
| per_page    | int                       | ❌       | Equivalent to `page[size]`                                           |

**Return Type**

`List[LoLGameFrame]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
page=1

result = sdk.lo_l_games.get_lol_games_lol_game_id_frames(
    lol_game_id=5,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_matches_match_id_or_slug_games

List games for a given League of Legends match

- HTTP Method: `GET`
- Endpoint: `/lol/matches/{match_id_or_slug}/games`

**Parameters**

| Name             | Type                                                  | Required | Description                                                                                                                                         |
| :--------------- | :---------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| match_id_or_slug | [MatchIdOrSlug](../models/MatchIdOrSlug.md)           | ✅       | A match ID or slug                                                                                                                                  |
| filter           | [FilterOverLoLGames](../models/FilterOverLoLGames.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range            | [RangeOverLoLGames](../models/RangeOverLoLGames.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort             | List[any]                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search           | [SearchOverLoLGames](../models/SearchOverLoLGames.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page             | [Page](../models/Page.md)                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page         | int                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[LoLGame]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLoLGames, RangeOverLoLGames, SearchOverLoLGames

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
match_id_or_slug=5
filter=FilterOverLoLGames(
    begin_at=[
        "eiusmod "
    ],
    complete=False,
    detailed_stats=True,
    end_at=[
        "veniam"
    ],
    finished=True,
    forfeit=True,
    id_=[
        5
    ],
    length=[
        4
    ],
    match_id=[
        7
    ],
    position=[
        6
    ],
    status=[
        "finished"
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverLoLGames(
    begin_at=[
        "velit l"
    ],
    complete=[
        False
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "consequat sin"
    ],
    finished=[
        False
    ],
    forfeit=[
        False
    ],
    id_=[
        5
    ],
    length=[
        3
    ],
    match_id=[
        7
    ],
    position=[
        2
    ],
    status=[
        "finished"
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverLoLGames(
    status="finished",
    winner_type="Player"
)
page=1

result = sdk.lo_l_games.get_lol_matches_match_id_or_slug_games(
    match_id_or_slug=match_id_or_slug,
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```

## get_lol_teams_team_id_or_slug_games

List finished games for a given League of Legends team

- HTTP Method: `GET`
- Endpoint: `/lol/teams/{team_id_or_slug}/games`

**Parameters**

| Name            | Type                                                                  | Required | Description                                                                                                                                         |
| :-------------- | :-------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| team_id_or_slug | [TeamIdOrSlug](../models/TeamIdOrSlug.md)                             | ✅       | A team ID or slug                                                                                                                                   |
| filter          | [FilterOverLoLTeamLastGames](../models/FilterOverLoLTeamLastGames.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range           | [RangeOverLoLTeamLastGames](../models/RangeOverLoLTeamLastGames.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort            | List[any]                                                             | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search          | [SearchOverLoLTeamLastGames](../models/SearchOverLoLTeamLastGames.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page            | [Page](../models/Page.md)                                             | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page        | int                                                                   | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[LoLTeamLastGame]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverLoLTeamLastGames, RangeOverLoLTeamLastGames, SearchOverLoLTeamLastGames

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
team_id_or_slug=10
filter=FilterOverLoLTeamLastGames(
    begin_at=[
        "ut cillum Exc"
    ],
    complete=False,
    detailed_stats=False,
    end_at=[
        "cillum id nul"
    ],
    finished=False,
    forfeit=True,
    id_=[
        6
    ],
    length=[
        7
    ],
    match_id=[
        1
    ],
    position=[
        8
    ],
    status=[
        "finished"
    ],
    winner_type=[
        "Player"
    ]
)
range=RangeOverLoLTeamLastGames(
    begin_at=[
        "el"
    ],
    complete=[
        False
    ],
    detailed_stats=[
        False
    ],
    end_at=[
        "labor"
    ],
    finished=[
        True
    ],
    forfeit=[
        True
    ],
    id_=[
        6
    ],
    length=[
        9
    ],
    match_id=[
        7
    ],
    position=[
        4
    ],
    status=[
        "finished"
    ],
    winner_type=[
        "Player"
    ]
)
sort=[
    ""
]
search=SearchOverLoLTeamLastGames(
    status="finished",
    winner_type="Player"
)
page=1

result = sdk.lo_l_games.get_lol_teams_team_id_or_slug_games(
    team_id_or_slug=team_id_or_slug,
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
