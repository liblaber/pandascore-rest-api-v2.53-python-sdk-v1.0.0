# OwStatsService

A list of all methods in the `OwStatsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                                                                               | Description                                                                   |
| :---------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| [get_ow_games_ow_game_id_players_player_id_or_slug_stats](#get_ow_games_ow_game_id_players_player_id_or_slug_stats)                                   | Get detailed statistics of a given Overwatch given player for the given game  |
| [get_ow_matches_match_id_or_slug_players_stats](#get_ow_matches_match_id_or_slug_players_stats)                                                       | Get detailed statistics of Overwatch players for the given match              |
| [get_ow_matches_match_id_or_slug_players_player_id_or_slug_stats](#get_ow_matches_match_id_or_slug_players_player_id_or_slug_stats)                   | Get detailed statistics of a given Overwatch given player for the given match |
| [get_ow_players_player_id_or_slug_stats](#get_ow_players_player_id_or_slug_stats)                                                                     | Get detailed statistics of a given Overwatch player                           |
| [get_ow_series_serie_id_or_slug_players_player_id_or_slug_stats](#get_ow_series_serie_id_or_slug_players_player_id_or_slug_stats)                     | Get detailed statistics of a given Overwatch given player for the given serie |
| [get_ow_tournaments_tournament_id_or_slug_players_player_id_or_slug_stats](#get_ow_tournaments_tournament_id_or_slug_players_player_id_or_slug_stats) | Get detailed statistics of a given Overwatch player for the given tournament  |

## get_ow_games_ow_game_id_players_player_id_or_slug_stats

Get detailed statistics of a given Overwatch given player for the given game

- HTTP Method: `GET`
- Endpoint: `/ow/games/{ow_game_id}/players/{player_id_or_slug}/stats`

**Parameters**

| Name              | Type                                          | Required | Description          |
| :---------------- | :-------------------------------------------- | :------- | :------------------- |
| ow_game_id        | int                                           | ✅       | An Overwatch game ID |
| player_id_or_slug | [PlayerIdOrSlug](../models/PlayerIdOrSlug.md) | ✅       | A player ID or slug  |

**Return Type**

`OwStatsForPlayerByGame`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
player_id_or_slug=9

result = sdk.ow_stats.get_ow_games_ow_game_id_players_player_id_or_slug_stats(
    ow_game_id=3,
    player_id_or_slug=player_id_or_slug
)

print(result)
```

## get_ow_matches_match_id_or_slug_players_stats

Get detailed statistics of Overwatch players for the given match

- HTTP Method: `GET`
- Endpoint: `/ow/matches/{match_id_or_slug}/players/stats`

**Parameters**

| Name             | Type                                        | Required | Description        |
| :--------------- | :------------------------------------------ | :------- | :----------------- |
| match_id_or_slug | [MatchIdOrSlug](../models/MatchIdOrSlug.md) | ✅       | A match ID or slug |

**Return Type**

`OwStatsForAllPlayersByMatch`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
match_id_or_slug=5

result = sdk.ow_stats.get_ow_matches_match_id_or_slug_players_stats(match_id_or_slug=match_id_or_slug)

print(result)
```

## get_ow_matches_match_id_or_slug_players_player_id_or_slug_stats

Get detailed statistics of a given Overwatch given player for the given match

- HTTP Method: `GET`
- Endpoint: `/ow/matches/{match_id_or_slug}/players/{player_id_or_slug}/stats`

**Parameters**

| Name              | Type                                          | Required | Description         |
| :---------------- | :-------------------------------------------- | :------- | :------------------ |
| match_id_or_slug  | [MatchIdOrSlug](../models/MatchIdOrSlug.md)   | ✅       | A match ID or slug  |
| player_id_or_slug | [PlayerIdOrSlug](../models/PlayerIdOrSlug.md) | ✅       | A player ID or slug |

**Return Type**

`OwStatsForPlayerByMatch`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
match_id_or_slug=5
player_id_or_slug=9

result = sdk.ow_stats.get_ow_matches_match_id_or_slug_players_player_id_or_slug_stats(
    match_id_or_slug=match_id_or_slug,
    player_id_or_slug=player_id_or_slug
)

print(result)
```

## get_ow_players_player_id_or_slug_stats

Get detailed statistics of a given Overwatch player

- HTTP Method: `GET`
- Endpoint: `/ow/players/{player_id_or_slug}/stats`

**Parameters**

| Name              | Type                                          | Required | Description            |
| :---------------- | :-------------------------------------------- | :------- | :--------------------- |
| player_id_or_slug | [PlayerIdOrSlug](../models/PlayerIdOrSlug.md) | ✅       | A player ID or slug    |
| from\_            | str                                           | ❌       | Filter out 'from' date |
| to                | str                                           | ❌       | Filter out 'to' date   |

**Return Type**

`OwStatsForPlayer`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
player_id_or_slug=9

result = sdk.ow_stats.get_ow_players_player_id_or_slug_stats(
    player_id_or_slug=player_id_or_slug,
    from_="2017-07-21",
    to="2017-07-21"
)

print(result)
```

## get_ow_series_serie_id_or_slug_players_player_id_or_slug_stats

Get detailed statistics of a given Overwatch given player for the given serie

- HTTP Method: `GET`
- Endpoint: `/ow/series/{serie_id_or_slug}/players/{player_id_or_slug}/stats`

**Parameters**

| Name              | Type                                          | Required | Description         |
| :---------------- | :-------------------------------------------- | :------- | :------------------ |
| serie_id_or_slug  | [SerieIdOrSlug](../models/SerieIdOrSlug.md)   | ✅       | A serie ID or slug  |
| player_id_or_slug | [PlayerIdOrSlug](../models/PlayerIdOrSlug.md) | ✅       | A player ID or slug |

**Return Type**

`OwStatsForPlayerBySerie`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
serie_id_or_slug=10
player_id_or_slug=9

result = sdk.ow_stats.get_ow_series_serie_id_or_slug_players_player_id_or_slug_stats(
    serie_id_or_slug=serie_id_or_slug,
    player_id_or_slug=player_id_or_slug
)

print(result)
```

## get_ow_tournaments_tournament_id_or_slug_players_player_id_or_slug_stats

Get detailed statistics of a given Overwatch player for the given tournament

- HTTP Method: `GET`
- Endpoint: `/ow/tournaments/{tournament_id_or_slug}/players/{player_id_or_slug}/stats`

**Parameters**

| Name                  | Type                                                  | Required | Description             |
| :-------------------- | :---------------------------------------------------- | :------- | :---------------------- |
| tournament_id_or_slug | [TournamentIdOrSlug](../models/TournamentIdOrSlug.md) | ✅       | A tournament ID or slug |
| player_id_or_slug     | [PlayerIdOrSlug](../models/PlayerIdOrSlug.md)         | ✅       | A player ID or slug     |

**Return Type**

`OwStatsForPlayerByTournament`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
tournament_id_or_slug=2
player_id_or_slug=9

result = sdk.ow_stats.get_ow_tournaments_tournament_id_or_slug_players_player_id_or_slug_stats(
    tournament_id_or_slug=tournament_id_or_slug,
    player_id_or_slug=player_id_or_slug
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
