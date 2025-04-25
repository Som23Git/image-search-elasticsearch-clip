
**text expansion query**
```
POST search-testing-v7/_search
{
  "_source": ["title","directions","ingredients","url","image"],
  "query": {
    "bool": {
      "should": [
        {
          "text_expansion": {
            "ml.inference.directions_expanded.predicted_value": {
              "model_id": ".elser_model_2_linux-x86_64",
              "model_text": "pizza mozzarella"
            }
          }
        }
      ]
    }
  }
}
```

**sparse_vector query**

```
POST search-testing-v7/_search
{
  "_source": ["title", "directions", "ingredients", "url", "image"],
  "query": {
    "sparse_vector": {
      "field": "ml.inference.directions_expanded.predicted_value",
      "inference_id": ".elser_model_2_linux-x86_64",
      "query": "pizza mozzarella"
    }
  }
}
```