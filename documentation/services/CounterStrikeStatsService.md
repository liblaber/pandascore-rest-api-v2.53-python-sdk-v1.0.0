# CounterStrikeStatsService

A list of all methods in the `CounterStrikeStatsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                                                                                   | Description                                                                       |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
| [get_csgo_matches_match_id_or_slug_players_stats](#get_csgo_matches_match_id_or_slug_players_stats)                                                       | Get detailed statistics of Counter-Strike players for the given match             |
| [get_csgo_matches_match_id_or_slug_players_player_id_or_slug_stats](#get_csgo_matches_match_id_or_slug_players_player_id_or_slug_stats)                   | Get detailed statistics of a given Counter-Strike player for the given match      |
| [get_csgo_matches_match_id_or_slug_teams_team_id_or_slug_stats](#get_csgo_matches_match_id_or_slug_teams_team_id_or_slug_stats)                           | Get detailed statistics of a given Counter-Strike team for the given match        |
| [get_csgo_players_player_id_or_slug_stats](#get_csgo_players_player_id_or_slug_stats)                                                                     | Get detailed statistics of a given Counter-Strike player                          |
| [get_csgo_series_serie_id_or_slug_players_player_id_or_slug_stats](#get_csgo_series_serie_id_or_slug_players_player_id_or_slug_stats)                     | Get detailed statistics of a given Counter-Strike player for the given serie      |
| [get_csgo_series_serie_id_or_slug_teams_team_id_or_slug_stats](#get_csgo_series_serie_id_or_slug_teams_team_id_or_slug_stats)                             | Get detailed statistics of a given Counter-Strike team for the given serie        |
| [get_csgo_teams_team_id_or_slug_stats](#get_csgo_teams_team_id_or_slug_stats)                                                                             | Get detailed statistics of a given Counter-Strike team                            |
| [get_csgo_tournaments_tournament_id_or_slug_players_player_id_or_slug_stats](#get_csgo_tournaments_tournament_id_or_slug_players_player_id_or_slug_stats) | Get detailed statistics of a given Counter-Strike player for the given tournament |
| [get_csgo_tournaments_tournament_id_or_slug_teams_team_id_or_slug_stats](#get_csgo_tournaments_tournament_id_or_slug_teams_team_id_or_slug_stats)         | Get detailed statistics of a given Counter-Strike team for the given tournament   |

## get_csgo_matches_match_id_or_slug_players_stats

Get detailed statistics of Counter-Strike players for the given match

- HTTP Method: `GET`
- Endpoint: `/csgo/matches/{match_id_or_slug}/players/stats`

**Parameters**

| Name             | Type                                        | Required | Description        |
| :--------------- | :------------------------------------------ | :------- | :----------------- |
| match_id_or_slug | [MatchIdOrSlug](../models/MatchIdOrSlug.md) | ✅       | A match ID or slug |

**Return Type**

`CsgoStatsForAllPlayersByMatch`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
match_id_or_slug=5

result = sdk.counter_strike_stats.get_csgo_matches_match_id_or_slug_players_stats(match_id_or_slug=match_id_or_slug)

print(result)
```

## get_csgo_matches_match_id_or_slug_players_player_id_or_slug_stats

Get detailed statistics of a given Counter-Strike player for the given match

- HTTP Method: `GET`
- Endpoint: `/csgo/matches/{match_id_or_slug}/players/{player_id_or_slug}/stats`

**Parameters**

| Name              | Type                                          | Required | Description         |
| :---------------- | :-------------------------------------------- | :------- | :------------------ |
| match_id_or_slug  | [MatchIdOrSlug](../models/MatchIdOrSlug.md)   | ✅       | A match ID or slug  |
| player_id_or_slug | [PlayerIdOrSlug](../models/PlayerIdOrSlug.md) | ✅       | A player ID or slug |

**Return Type**

`CsgoStatsForPlayerByMatch`

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

result = sdk.counter_strike_stats.get_csgo_matches_match_id_or_slug_players_player_id_or_slug_stats(
    match_id_or_slug=match_id_or_slug,
    player_id_or_slug=player_id_or_slug
)

print(result)
```

## get_csgo_matches_match_id_or_slug_teams_team_id_or_slug_stats

Get detailed statistics of a given Counter-Strike team for the given match

- HTTP Method: `GET`
- Endpoint: `/csgo/matches/{match_id_or_slug}/teams/{team_id_or_slug}/stats`

**Parameters**

| Name             | Type                                        | Required | Description        |
| :--------------- | :------------------------------------------ | :------- | :----------------- |
| match_id_or_slug | [MatchIdOrSlug](../models/MatchIdOrSlug.md) | ✅       | A match ID or slug |
| team_id_or_slug  | [TeamIdOrSlug](../models/TeamIdOrSlug.md)   | ✅       | A team ID or slug  |

**Return Type**

`CsgoStatsForTeamByMatch`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
match_id_or_slug=5
team_id_or_slug=10

result = sdk.counter_strike_stats.get_csgo_matches_match_id_or_slug_teams_team_id_or_slug_stats(
    match_id_or_slug=match_id_or_slug,
    team_id_or_slug=team_id_or_slug
)

print(result)
```

## get_csgo_players_player_id_or_slug_stats

Get detailed statistics of a given Counter-Strike player

- HTTP Method: `GET`
- Endpoint: `/csgo/players/{player_id_or_slug}/stats`

**Parameters**

| Name              | Type                                                          | Required | Description            |
| :---------------- | :------------------------------------------------------------ | :------- | :--------------------- |
| player_id_or_slug | [PlayerIdOrSlug](../models/PlayerIdOrSlug.md)                 | ✅       | A player ID or slug    |
| videogame_title   | [VideogameTitleIdOrSlug](../models/VideogameTitleIdOrSlug.md) | ❌       |                        |
| from\_            | str                                                           | ❌       | Filter out 'from' date |
| to                | str                                                           | ❌       | Filter out 'to' date   |

**Return Type**

`CsgoStatsForPlayer`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
player_id_or_slug=9
videogame_title=10

result = sdk.counter_strike_stats.get_csgo_players_player_id_or_slug_stats(
    player_id_or_slug=player_id_or_slug,
    videogame_title=videogame_title,
    from_="2017-07-21",
    to="2017-07-21"
)

print(result)
```

## get_csgo_series_serie_id_or_slug_players_player_id_or_slug_stats

Get detailed statistics of a given Counter-Strike player for the given serie

- HTTP Method: `GET`
- Endpoint: `/csgo/series/{serie_id_or_slug}/players/{player_id_or_slug}/stats`

**Parameters**

| Name              | Type                                          | Required | Description         |
| :---------------- | :-------------------------------------------- | :------- | :------------------ |
| serie_id_or_slug  | [SerieIdOrSlug](../models/SerieIdOrSlug.md)   | ✅       | A serie ID or slug  |
| player_id_or_slug | [PlayerIdOrSlug](../models/PlayerIdOrSlug.md) | ✅       | A player ID or slug |

**Return Type**

`CsgoStatsForPlayerBySerie`

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

result = sdk.counter_strike_stats.get_csgo_series_serie_id_or_slug_players_player_id_or_slug_stats(
    serie_id_or_slug=serie_id_or_slug,
    player_id_or_slug=player_id_or_slug
)

print(result)
```

## get_csgo_series_serie_id_or_slug_teams_team_id_or_slug_stats

Get detailed statistics of a given Counter-Strike team for the given serie

- HTTP Method: `GET`
- Endpoint: `/csgo/series/{serie_id_or_slug}/teams/{team_id_or_slug}/stats`

**Parameters**

| Name             | Type                                        | Required | Description        |
| :--------------- | :------------------------------------------ | :------- | :----------------- |
| serie_id_or_slug | [SerieIdOrSlug](../models/SerieIdOrSlug.md) | ✅       | A serie ID or slug |
| team_id_or_slug  | [TeamIdOrSlug](../models/TeamIdOrSlug.md)   | ✅       | A team ID or slug  |

**Return Type**

`CsgoStatsForTeamBySerie`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
serie_id_or_slug=10
team_id_or_slug=10

result = sdk.counter_strike_stats.get_csgo_series_serie_id_or_slug_teams_team_id_or_slug_stats(
    serie_id_or_slug=serie_id_or_slug,
    team_id_or_slug=team_id_or_slug
)

print(result)
```

## get_csgo_teams_team_id_or_slug_stats

Get detailed statistics of a given Counter-Strike team

- HTTP Method: `GET`
- Endpoint: `/csgo/teams/{team_id_or_slug}/stats`

**Parameters**

| Name            | Type                                                          | Required | Description            |
| :-------------- | :------------------------------------------------------------ | :------- | :--------------------- |
| team_id_or_slug | [TeamIdOrSlug](../models/TeamIdOrSlug.md)                     | ✅       | A team ID or slug      |
| videogame_title | [VideogameTitleIdOrSlug](../models/VideogameTitleIdOrSlug.md) | ❌       |                        |
| from\_          | str                                                           | ❌       | Filter out 'from' date |
| to              | str                                                           | ❌       | Filter out 'to' date   |

**Return Type**

`CsgoStatsForTeam`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
team_id_or_slug=10
videogame_title=10

result = sdk.counter_strike_stats.get_csgo_teams_team_id_or_slug_stats(
    team_id_or_slug=team_id_or_slug,
    videogame_title=videogame_title,
    from_="2017-07-21",
    to="2017-07-21"
)

print(result)
```

## get_csgo_tournaments_tournament_id_or_slug_players_player_id_or_slug_stats

Get detailed statistics of a given Counter-Strike player for the given tournament

- HTTP Method: `GET`
- Endpoint: `/csgo/tournaments/{tournament_id_or_slug}/players/{player_id_or_slug}/stats`

**Parameters**

| Name                  | Type                                                  | Required | Description             |
| :-------------------- | :---------------------------------------------------- | :------- | :---------------------- |
| tournament_id_or_slug | [TournamentIdOrSlug](../models/TournamentIdOrSlug.md) | ✅       | A tournament ID or slug |
| player_id_or_slug     | [PlayerIdOrSlug](../models/PlayerIdOrSlug.md)         | ✅       | A player ID or slug     |

**Return Type**

`CsgoStatsForPlayerByTournament`

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

result = sdk.counter_strike_stats.get_csgo_tournaments_tournament_id_or_slug_players_player_id_or_slug_stats(
    tournament_id_or_slug=tournament_id_or_slug,
    player_id_or_slug=player_id_or_slug
)

print(result)
```

## get_csgo_tournaments_tournament_id_or_slug_teams_team_id_or_slug_stats

Get detailed statistics of a given Counter-Strike team for the given tournament

- HTTP Method: `GET`
- Endpoint: `/csgo/tournaments/{tournament_id_or_slug}/teams/{team_id_or_slug}/stats`

**Parameters**

| Name                  | Type                                                  | Required | Description             |
| :-------------------- | :---------------------------------------------------- | :------- | :---------------------- |
| tournament_id_or_slug | [TournamentIdOrSlug](../models/TournamentIdOrSlug.md) | ✅       | A tournament ID or slug |
| team_id_or_slug       | [TeamIdOrSlug](../models/TeamIdOrSlug.md)             | ✅       | A team ID or slug       |

**Return Type**

`CsgoStatsForTeamByTournament`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
tournament_id_or_slug=2
team_id_or_slug=10

result = sdk.counter_strike_stats.get_csgo_tournaments_tournament_id_or_slug_teams_team_id_or_slug_stats(
    tournament_id_or_slug=tournament_id_or_slug,
    team_id_or_slug=team_id_or_slug
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
