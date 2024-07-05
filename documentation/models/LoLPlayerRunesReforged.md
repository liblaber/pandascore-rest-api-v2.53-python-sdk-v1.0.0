# LoLPlayerRunesReforged

**Properties**

| Name           | Type                | Required | Description |
| :------------- | :------------------ | :------- | :---------- |
| primary_path   | PrimaryPath         | ✅       |             |
| secondary_path | SecondaryPath       | ✅       |             |
| shards         | LoLPlayerRuneShards | ✅       |             |

# PrimaryPath

**Properties**

| Name         | Type                  | Required | Description                 |
| :----------- | :-------------------- | :------- | :-------------------------- |
| id\_         | int                   | ✅       | ID of the rune              |
| image_url    | str                   | ✅       | URL to an image of the rune |
| keystone     | LoLRuneReforged       | ✅       |                             |
| lesser_runes | List[LoLRuneReforged] | ✅       |                             |
| name         | str                   | ✅       | Name of the rune path       |
| type\_       | LoLRuneReforgedType   | ✅       |                             |

# SecondaryPath

**Properties**

| Name         | Type                  | Required | Description                 |
| :----------- | :-------------------- | :------- | :-------------------------- |
| id\_         | int                   | ✅       | ID of the rune              |
| image_url    | str                   | ✅       | URL to an image of the rune |
| lesser_runes | List[LoLRuneReforged] | ✅       |                             |
| name         | str                   | ✅       | Name of the rune path       |
| type\_       | LoLRuneReforgedType   | ✅       |                             |
