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
from pandascore import Pandascore, Environment

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.lo_l_games.get_lol_games_lol_game_id(lol_game_id=9)

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
from pandascore import Pandascore, Environment

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
page=1

result = sdk.lo_l_games.get_lol_games_lol_game_id_events(
    lol_game_id=6,
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
from pandascore import Pandascore, Environment

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
page=1

result = sdk.lo_l_games.get_lol_games_lol_game_id_frames(
    lol_game_id=10,
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverLoLGames, RangeOverLoLGames, SearchOverLoLGames

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
match_id_or_slug=8
filter=FilterOverLoLGames(
    begin_at=[
        "qui"
    ],
    complete=False,
    detailed_stats=False,
    end_at=[
        "e"
    ],
    finished=True,
    forfeit=True,
    id_=[
        9
    ],
    length=[
        5
    ],
    match_id=[
        4
    ],
    position=[
        3
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
        "s"
    ],
    complete=[
        False
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "ut c"
    ],
    finished=[
        True
    ],
    forfeit=[
        True
    ],
    id_=[
        4
    ],
    length=[
        2
    ],
    match_id=[
        5
    ],
    position=[
        5
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
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverLoLTeamLastGames, RangeOverLoLTeamLastGames, SearchOverLoLTeamLastGames

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
team_id_or_slug=7
filter=FilterOverLoLTeamLastGames(
    begin_at=[
        "velit cons"
    ],
    complete=False,
    detailed_stats=False,
    end_at=[
        "do veli"
    ],
    finished=True,
    forfeit=False,
    id_=[
        5
    ],
    length=[
        8
    ],
    match_id=[
        8
    ],
    position=[
        3
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
        "e"
    ],
    complete=[
        True
    ],
    detailed_stats=[
        True
    ],
    end_at=[
        "laboris nulla"
    ],
    finished=[
        True
    ],
    forfeit=[
        False
    ],
    id_=[
        10
    ],
    length=[
        8
    ],
    match_id=[
        5
    ],
    position=[
        7
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
