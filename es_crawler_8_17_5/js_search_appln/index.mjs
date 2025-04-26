import Client from '@elastic/search-application-client'

const request = Client(
    "recipe_search_app",
    "https://5eacd8f5943e4902afe972c240f08be1.us-central1.gcp.cloud.es.io:443",
    "alNvUWFaWUJpd01WVUl2YUJ3eEs6TE5Hb1pVR0hSbXlMN3gyVU1Ea2JLUQ=="
)


const results = await request()
  .query('pizza')
  .addParameter('search_fields', ['title', 'directions'])
  .search()

console.log(JSON.stringify(results, null, 2));