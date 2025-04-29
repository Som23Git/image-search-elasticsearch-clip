// Initialize Elastic Behavioral Analytics Tracker
window.elasticAnalytics = window.elasticAnalytics || {};
window.elasticAnalytics.createTracker({
  endpoint: "https://5eacd8f5943e4902afe972c240f08be1.us-central1.gcp.cloud.es.io:443",  // <-- Your APM endpoint
  collectionName: "recipe-search-app",
  apiKey: "alNvUWFaWUJpd01WVUl2YUJ3eEs6TE5Hb1pVR0hSbXlMN3gyVU1Ea2JLUQ==",  // <-- Replace securely
  // Optional: sampling: 1
});

// Example function to track a search event
function trackSearchEvent(query, results) {
    window.elasticAnalytics.trackSearch({
      search: {
        query: query,
        page: {
          current: 1,
          size: results.length
        },
        results: {
          total_results: results.length,
          items: results.map(r => ({
            document: {
              id: r.url || ""  // Use URL or a unique identifier
            },
            page: {
              url: r.url || ""
            }
          }))
        },
        search_application: "recipe-search-app"
      }
    });
  }
