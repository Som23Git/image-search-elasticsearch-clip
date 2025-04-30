# 🚀 Elasticsearch Recipe Search App (8.17.5)

This project demonstrates how to build a **production-grade search application** using **Elasticsearch**, featuring:
- **Web crawling** (food.com recipes).
- **Text and image search**.
- **Sparse and dense vector queries**.
- **RRF (Reciprocal Rank Fusion)**.
- **APM (Application Performance Monitoring)**.
- **UI integration with Bootstrap**.
- **Dockerization** for scalability.

---

## 📋 To-Do List (Project Roadmap)

- [x] Crawl **food.com** with custom fields: `directions`, `ingredients`.
- [x] Integrate **image search** (using embeddings).
- [x] Implement **text expansion (deprecated)** or **sparse vector queries** with **ELSER**.
- [x] Integrate with **Bootstrap UI**.
- [x] Implement **KNN search** for image embeddings.
- [x] Integrate with **Elastic APM**.
- [x] Integrate **RUM (Real User Monitoring)**.

### Work In Progress

- [ ] Integrate **Behavioral Analytics**
- [ ] Pagination

### Plan to Scale

- [ ] **Dockerize** the application.

### Enhancements

- [ ] Implement **RRF (Reciprocal Rank Fusion)** query.
- [ ] Add **faceted search**.
- [ ] Provide **Postman collection** for API testing.
- [ ] Using **Hugging Face Inference API** integration(need Hugging Face instance/endpoint which is costly)
- [ ] **Recipe Suggestions** using an LLM or more personalized approach
- [ ] Support for **trackClicks**

---

## ✅ Current Features

- [x] **APM Enabled** (Elastic APM integrated).
- [x] **RUM Enabled** (Elastic RUM-JS integrated).
- [x] **Sparse Vector Search** using **ELSER** (in-built).
- [x] **Dense Vector Search** using **image embeddings** and **KNN**.
- [x] **UI available** (Bootstrap-based).
- [x] **42,000+ crawled recipe documents** (with images, ingredients, directions).

---

## 🛠️ Technologies Used

- **Elasticsearch Cloud**
- **Flask** (Python)
- **Bootstrap** (UI)
- **Elastic APM**
- **Docker** (Work in Progress)

---

## 📚 Useful References

- **Search Application Client (JavaScript)**:  
  [Elastic Search Application Client](https://github.com/elastic/search-application-client?tab=readme-ov-file#boilerplate-template)

- **Search UI**:  
  [Elastic Search UI Docs](https://www.elastic.co/docs/solutions/search/site-or-app/search-ui)  
  [Search as You Type Mapping](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/search-as-you-type)  
  [Search UI Tutorial (React)](https://www.elastic.co/docs/reference/search-ui/tutorials-elasticsearch-setup-cloud)

- **GitHub Repository (Search UI)**:  
  [Elastic Search UI GitHub](https://github.com/elastic/search-ui)

- **Semantic Search vs Lexical Search in E-commerce**:  
  [Elastic Blog: Semantic Search](https://www.elastic.co/search-labs/blog/semantic-search-elasticsearch-ecommerce)

- **Elastic Search Labs Tutorial** *(Highly Recommended)*:  
  [Search Tutorial - Elastic Labs](https://www.elastic.co/search-labs/tutorials/search-tutorial/welcome)

---

## 🔎 Search Application Examples

### **1. Get Existing Search Application**

```bash
GET _application/search_application/recipe_search_app
```

<details>
<summary>Example Output</summary>

```json
{
  "name": "recipe_search_app",
  "indices": ["search-testing-v7"],
  "updated_at_millis": 1745594754210,
  "template": {
    "script": {
      "source": "{ \"query\": { \"query_string\": { \"query\": \"{{query_string}}\", \"default_field\": \"{{default_field}}\" } } }",
      "lang": "mustache",
      "params": {
        "default_field": "*",
        "query_string": "*"
      }
    }
  }
}
```

</details>

---

### **2. Update Search Application Template (Version 2)**

```bash
PUT _application/search_application/recipe_search_app
```

```
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
```

---

### **3. Image Search Application Template**

```bash
GET _application/search_application/image_search_app
```

<details>
<summary>Example Output</summary>

```
{
  "name": "image_search_app",
  "indices": ["search-testing-v7"],
  "updated_at_millis": 1745769395555,
  "template": {
    "script": {
      "source": "{ \"query\": { \"query_string\": { \"query\": \"{{query_string}}\", \"default_field\": \"{{default_field}}\" } } }",
      "lang": "mustache",
      "params": {
        "default_field": "*",
        "query_string": "*"
      }
    }
  }
}
```

</details>

---

### **4. Update Image Search Application Template (KNN Search)**

```bash
PUT _application/search_application/image_search_app
```

```
{
  "indices": ["search-testing-v7"],
  "template": {
    "script": {
      "lang": "mustache",
      "source": """
      {
        "knn": {
          "field": "{{knn_field}}",
          "query_vector": {{#toJson}}query_vector{{/toJson}},
          "k": "{{k}}",
          "num_candidates": {{num_candidates}}
        },
        "fields": {{#toJson}}fields{{/toJson}}
      }
      """,
      "params": {
        "knn_field": "image_embedding",
        "query_vector": [],
        "k": 10,
        "num_candidates": 100,
        "fields": ["title", "directions", "body_content"]
      }
    }
  }
}
```

---

## 🐛 Known Issues

- While using **Elastic's React Search UI**, a **manual patch** was applied to fix a locale import issue:

  ```diff
  - import enUsLocale from "rc-pagination/lib/locale/en_US";
  + import enUsLocale from "rc-pagination/lib/locale/en_US.js";
  ```

  This patch was made in:
  ```
  es_crawler_8_17_5/app-search-reference-ui-react-master/node_modules/@elastic/react-search-ui-views/lib/index.mjs
  ```

---

## 📂 Related Apps

- **Elser App with APM Enabled (Text Expansion, Sparse Vector Search)**:  
  Refer to:  
  ```
  es_crawler_8_17_5/python_search_app/elser_search
  ```
