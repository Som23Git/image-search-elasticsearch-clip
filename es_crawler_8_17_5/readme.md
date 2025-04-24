### ES Crawler 8.17.5


Reference Documents:

Search UI:
https://www.elastic.co/docs/solutions/search/site-or-app/search-ui
Search as you type: https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/search-as-you-type
Basic Search React App: https://www.elastic.co/docs/reference/search-ui/tutorials-elasticsearch-setup-cloud


Github:

https://github.com/elastic/search-ui


Manual changes made in `es_crawler_8_17_5/app-search-reference-ui-react-master/node_modules/@elastic/react-search-ui-views/lib/index.mjs` because of the patch issue where, it was pointing to `en_US` instead of `en_US.js`: 

```
// src/Paging.tsx
import React6 from "react";
import RCPagination from "rc-pagination";
import enUsLocale from "rc-pagination/lib/locale/en_US.js";
function Paging(_a) {
```

