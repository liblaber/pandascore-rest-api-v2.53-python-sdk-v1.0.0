# CsgoKillEventDetails

**Properties**

| Name   | Type            | Required | Description |
| :----- | :-------------- | :------- | :---------- |
| killer | Killer          | ✅       |             |
| victim | CsgoRoundPlayer | ✅       |             |

# Killer

**Properties**

| Name      | Type          | Required | Description                     |
| :-------- | :------------ | :------- | :------------------------------ |
| id\_      | int           | ✅       | ID of the player                |
| name      | str           | ✅       | Professional name of the player |
| team_side | CsgoRoundSide | ✅       |                                 |
