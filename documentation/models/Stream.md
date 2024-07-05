# Stream

**Properties**

| Name      | Type           | Required | Description                                                    |
| :-------- | :------------- | :------- | :------------------------------------------------------------- |
| embed_url | str            | ✅       | URL to embed in an iframe.                                     |
| language  | StreamLanguage | ✅       | Language alpha-2 code according to ISO 649-1 standard.         |
| main      | bool           | ✅       | Whether it is the main stream. Main stream is always official. |
| official  | bool           | ✅       | Whether it is an official broadcast.                           |
| raw_url   | str            | ✅       | URL to the stream on host website.                             |
