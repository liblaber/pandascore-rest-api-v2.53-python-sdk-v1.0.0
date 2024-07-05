# SearchOverDota2Players

**Properties**

| Name        | Type | Required | Description                                                                                                                                                                                                                   |
| :---------- | :--- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| birthday    | str  | ❌       | Birth day of the player, `YYYY-MM-DD` format. `null` if unknown. <br/>**Note**: This field is only present for users running the Historical plan or above.                                                                    |
| first_name  | str  | ❌       | First name of the player. `null` if unknown                                                                                                                                                                                   |
| last_name   | str  | ❌       | Last name of the player. `null` if unknown                                                                                                                                                                                    |
| name        | str  | ❌       | Professional name of the player                                                                                                                                                                                               |
| nationality | str  | ❌       | Country code matching the nationality of the player according to the ISO 3166-1 standard (Alpha-2 code). <br/>In addition to the standard, the `XK` code is used for Kosovo. <br/>`null` if unknown                           |
| role        | str  | ❌       | Role/position of the player. Field value varies depending on the video game.`null` if unknown. <br/>**Note**: role is only available for DotA 2, League of Legends, and Overwatch players. <br/>`null` for other video games. |
| slug        | str  | ❌       | Unique, human-readable identifier for the player. <br/>`id` and `slug` can be used interchangeably throughout the API.                                                                                                        |
