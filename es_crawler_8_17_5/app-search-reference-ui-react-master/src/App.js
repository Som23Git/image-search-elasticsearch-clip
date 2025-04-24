// ****
// Food Recipe WORKING APP With Fields are rendered as expected
// ****

// src/App.js
import React from "react";
import ReactDOM from "react-dom";
import ElasticsearchAPIConnector from "@elastic/search-ui-elasticsearch-connector";

import {
  SearchProvider,
  SearchBox,
  Results,
  ResultsPerPage,
  Paging,
  ErrorBoundary
} from "@elastic/react-search-ui";
import { Layout } from "@elastic/react-search-ui-views";

import "@elastic/react-search-ui-views/lib/styles/styles.css";

// 1) Configure your ES connector
const connector = new ElasticsearchAPIConnector({
  cloud: {
    id: "elasticTestingDeployment:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvOjQ0MyQ1ZWFjZDhmNTk0M2U0OTAyYWZlOTcyYzI0MGYwOGJlMSRlOWExZGU1NWExZjQ0YmJlOTQ5YmQxZjIwZTVjY2RhYQ=="
  },
  apiKey: "alNvUWFaWUJpd01WVUl2YUJ3eEs6TE5Hb1pVR0hSbXlMN3gyVU1Ea2JLUQ==",
  index: "search-testing-v4"
});

// 2) Mirror your Kibana DSL for text_expansion
const config = {
  apiConnector: connector,
  alwaysSearchOnInitialLoad: false,
  searchQuery: {
    // **prevent** any default match/phrase queries
    search_fields: {},

    // fields you want back
    result_fields: {
      title:       { raw: {} },
      directions:  { raw: {} },
      ingredients: { raw: {} },
      url:         { raw: {} }
    },
    query: {
      bool: {
        should: [
          {
            text_expansion: {
              "ml.inference.directions_expanded.predicted_value": {
                model_id:   ".elser_model_2_linux-x86_64",
                model_text: "{{searchTerm}}"
              }
            }
          }
        ]
      }
    }
  }
};

export default function App() {
  return (
    <SearchProvider config={config}>
      <ErrorBoundary>
        <Layout
          // Search box in the header
          header={
            <SearchBox
              placeholder="Search by taste, cuisine, etc…"
              debounceLength={300}
              // Only run on Enter or click
              searchAsYouType={false}
              autocompleteSuggestions={false}
            />
          }

          // No side‐bar facets
          sideContent={null}

          // Default results list using your result_fields
          bodyContent={
            <Results
              titleField="title"
              urlField="url"
              shouldTrackClickThrough={true}
            />
          }

          // Page-size selector and pagination
          bodyHeader={<ResultsPerPage options={[5, 10, 20]} />}
          bodyFooter={<Paging />}
        />
      </ErrorBoundary>
    </SearchProvider>
  );
}

// Mount the App into <div id="root">
ReactDOM.render(<App />, document.getElementById("root"));