# PubgTeamsService

A list of all methods in the `PubgTeamsService` service. Click on the method name to view detailed information about that method.

| Methods                           | Description                       |
| :-------------------------------- | :-------------------------------- |
| [get_pubg_teams](#get_pubg_teams) | List teams for the PUBG videogame |

## get_pubg_teams

List teams for the PUBG videogame

- HTTP Method: `GET`
- Endpoint: `/pubg/teams`

**Parameters**

| Name     | Type                                                    | Required | Description                                                                                                                                         |
| :------- | :------------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| filter   | [FilterOverPubgTeams](../models/FilterOverPubgTeams.md) | ❌       | Options to filter results. String fields are case sensitive <br/>For more information on filtering, see [docs](/docs/filtering-and-sorting#filter). |
| range    | [RangeOverPubgTeams](../models/RangeOverPubgTeams.md)   | ❌       | Options to select results within ranges <br/>For more information on ranges, see [docs](/docs/filtering-and-sorting#range).                         |
| sort     | List[any]                                               | ❌       | Options to sort results <br/>For more information on sorting, see [docs](/docs/filtering-and-sorting#sort).                                         |
| search   | [SearchOverPubgTeams](../models/SearchOverPubgTeams.md) | ❌       | Options to search results <br/>For more information on searching, see [docs](/docs/filtering-and-sorting#search).                                   |
| page     | [Page](../models/Page.md)                               | ❌       | Pagination in the form of `page=2` or `page[size]=30&page[number]=2`                                                                                |
| per_page | int                                                     | ❌       | Equivalent to `page[size]`                                                                                                                          |

**Return Type**

`List[Team]`

**Example Usage Code Snippet**

```python
from pandascore import Pandascore, Environment
from pandascore.models import FilterOverPubgTeams, RangeOverPubgTeams, SearchOverPubgTeams

sdk = Pandascore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
filter=FilterOverPubgTeams(
    acronym=[
        "non amet "
    ],
    id_=[
        7
    ],
    location=[
        "adipi"
    ],
    modified_at=[
        "mollit "
    ],
    name=[
        "nisi ex "
    ],
    slug=[
        "yr72_"
    ],
    videogame_id=[
        1
    ]
)
range=RangeOverPubgTeams(
    acronym=[
        "sint ad eli"
    ],
    id_=[
        6
    ],
    location=[
        "esse in dolore"
    ],
    modified_at=[
        "irure"
    ],
    name=[
        "labore m"
    ],
    slug=[
        "1ez85dtxw"
    ]
)
sort=[
    ""
]
search=SearchOverPubgTeams(
    acronym="et ullamco",
    location="sit u",
    name="et anim Lorem ",
    slug="9fdgk"
)
page=1

result = sdk.pubg_teams.get_pubg_teams(
    filter=filter,
    range=range,
    sort=sort,
    search=search,
    page=page,
    per_page=50
)

print(result)
```
