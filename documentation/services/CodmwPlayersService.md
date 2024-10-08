# CodmwPlayersService

A list of all methods in the `CodmwPlayersService` service. Click on the method name to view detailed information about that method.

| Methods                                 | Description                          |
| :-------------------------------------- | :----------------------------------- |
| [get_codmw_players](#get_codmw_players) | List players for the CODMW videogame |

## get_codmw_players

List players for the CODMW videogame

- HTTP Method: `GET`
- Endpoint: `/codmw/players`

**Parameters**

| Name     | Type                                                          | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverCodmwPlayers](../models/FilterOverCodmwPlayers.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverCodmwPlayers](../models/RangeOverCodmwPlayers.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                                     | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverCodmwPlayers](../models/SearchOverCodmwPlayers.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                                     | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                           | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Player]`

**Example Usage Code Snippet**

```python
from pandascore_client import PandascoreClient, Environment
from pandascore_client.models import FilterOverCodmwPlayers, RangeOverCodmwPlayers, SearchOverCodmwPlayers

sdk = PandascoreClient(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)
filter=FilterOverCodmwPlayers(
    active=True,
    birthday=[
        "laboris s"
    ],
    first_name=[
        "ea su"
    ],
    id_=[
        4
    ],
    last_name=[
        "nisi "
    ],
    modified_at=[
        "sit sed non al"
    ],
    name=[
        "ea occaecat "
    ],
    nationality=[
        "velit i"
    ],
    role=[
        "ut ven"
    ],
    slug=[
        "0x"
    ],
    team_id=[
        2
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverCodmwPlayers(
    birthday=[
        "exdo aute"
    ],
    first_name=[
        "fugiat D"
    ],
    id_=[
        3
    ],
    last_name=[
        "anim e"
    ],
    modified_at=[
        "la"
    ],
    name=[
        "ipsum veniam"
    ],
    nationality=[
        "nisi min"
    ],
    role=[
        "anim aliqua"
    ],
    slug=[
        "tdx6k-"
    ]
)
sort=[
    ""
]
search=SearchOverCodmwPlayers(
    birthday="Ut non amet ",
    first_name="dolore comm",
    last_name="minim ",
    name="amet d",
    nationality="ut minim",
    role="enimut ex si",
    slug="mpp4jva"
)
page=1

result = sdk.codmw_players.get_codmw_players(
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
