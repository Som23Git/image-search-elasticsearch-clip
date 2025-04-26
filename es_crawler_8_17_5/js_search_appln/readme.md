Doc reference: Build a search experience with the Search Application client - https://www.elastic.co/guide/en/elasticsearch/reference/8.17/search-application-client.html

##### GET search template
GET _application/search_application/recipe_search_app

#### output
#! Using default search application template which is subject to change. We recommend storing a template to avoid breaking changes.
{
  "name": "recipe_search_app",
  "indices": [
    "search-testing-v7"
  ],
  "updated_at_millis": 1745594754210,
  "template": {
    "script": {
      "source": """{
  "query": {
    "query_string": {
        "query": "{{query_string}}",
        "default_field": "{{default_field}}"
        }
    }
}
""",
      "lang": "mustache",
      "params": {
        "default_field": "*",
        "query_string": "*"
      }
    }
  }
}

#### version 2 - updating saerch template:

#### updating search template
PUT _application/search_application/recipe_search_app
{
  "indices": ["search-testing-v7"],
  "template": {
    "script": {
      "lang": "mustache",
      "source": """
        {
          "query": {
            "bool": {
              "must": [
              {{#query}}
              {
                "query_string": {
                  "query": "{{query}}",
                  "fields": {{#toJson}}search_fields{{/toJson}}
                }
              }
              {{/query}}
            ]
            }
          }
        }
      """,
      "params": {
        "query": "",
        "search_fields": ""
      }
    }
  }
}

