# Image Search using KNN and Elasticsearch(CLI-Based Approach and NO Search UI)

This project demonstrates how to perform **image similarity search** in **Elasticsearch** using **CLIP embeddings** and **KNN Search**. It leverages:
- [Hugging Face CLIP Model](https://huggingface.co/openai/clip-vit-base-patch32) for image feature extraction.
- Elasticsearch's [KNN Search](https://www.elastic.co/guide/en/elasticsearch/reference/current/knn-search.html) with [Search Templates](https://www.elastic.co/docs/solutions/search/search-templates).

---

## Prerequisites

Before running the image search application, ensure the following:

- **Clean Index Setup**:  
  Your Elasticsearch index should have the proper mapping configured, especially for **512-dimensional dense vectors** required for image embeddings. These vectors are indexed into the `image_embedding` field using the **CLIP model**.

- **Verify Index Mapping**:  
  Use the following API call to check the mapping of your index :

  ```bash
  GET {index_name}/_mapping
  ```

- **Key Fields for Image Search**:
  - `image_embedding`: A **dense_vector** field with **512 dimensions** used for KNN (k-Nearest Neighbors) search.  
  - Other important fields include: `title`, `directions`, `ingredients`, and `image`, which store the recipe details and images.

### Sample Mapping for `image_embedding` field:

```json
"image_embedding": {
  "type": "dense_vector",
  "dims": 512,
  "index": true
}
```

- **Embedding Generation**:  
  Use the **CLIP model** (`openai/clip-vit-base-patch32`) to generate **512-dimensional embeddings** for your images. The directory `generate_embeddings_app` includes the necessary code to compute these embeddings and index them into Elasticsearch.

## How It Works

1. **CLIP Model** generates a 512-dimensional vector embedding from an image and it is lighter and faster.
2. The embedding is passed to **Elasticsearch KNN Search**, querying for similar images.
3. The search uses a **Mustache template** to structure the query.

---

## Project Structure

```
image_search/
├── image_search_app.py       # Final search app (asks user for image URL)
├── image_search_app.beta.py  # Static image URL for testing
├── image_search_app.bug      # Bug (Elasticsearch search application issue)
├── config.py                 # configuration variables
├── config.py.example         # Example config template (without secrets)
└── README.md                            
```
As this is a CLI-Based approach, there's no need for `templates/` and `static/` assets.

---
## **Issue in Supporting Search Application**

### **Search Application Template Usage**
```
PUT _application/search_application/image_search_app
{
  "indices": [
    "{index_name}"
  ],
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
        "k": 8,
        "num_candidates": 50,
        "fields": ["title", "directions","ingredients","body_content"]
      }
    }
  }
}
```
<br>

### **Workaround**

- Use `search template API` directly - Refer [Search Template API documentation](https://www.elastic.co/docs/solutions/search/search-templates#create-search-template)

```json
PUT _scripts/image_search_template
{
  "script": {
    "lang": "mustache",
    "source": """
    {
      "query": {
        "knn": {
          "field": "{{knn_field}}",
          "query_vector": {{#toJson}}query_vector{{/toJson}},
          "k": {{k}},
          "num_candidates": {{num_candidates}}
        }
      },
      "fields": {{#toJson}}fields{{/toJson}}
    }
    """
  }
}
```
- Use `render_template API` to **test** the added `search_template`:

```
POST _render/template
{
  "id": "image_search_template",
  "params": {
    "knn_field": "image_embedding",
    "query_vector": [0.01658179610967636, 0.03511231020092964, -0.01910591311752796, 0.04759567975997925, 0.007392457220703363, 0.041482552886009216, -0.00506657175719738, -0.008704421110451221, -0.0006646860274486244, -0.0005833572940900922, -0.012989193201065063, -0.020764362066984177, 0.015698278322815895, 0.005400165915489197, -0.006252847611904144, -0.018443984910845757, 0.13550254702568054, 0.025229912251234055, 0.023934118449687958, -0.0440627858042717, -0.12679260969161987, 0.014905421994626522, -0.007434233091771603, -0.04142316058278084, 0.02410072274506092, 0.013529140502214432, -0.023162899538874626, 0.0035687473136931658, 0.01589450240135193, -0.022737817838788033, 0.04851134493947029, -0.007447127252817154, 0.04024679958820343, -0.0015348338056355715, ..., 0.025384193286299706, -0.014990167692303658],
    "k": 8,  
    "num_candidates": 50,  
    "fields": ["title", "directions", "ingredients", "body_content"]
  }
}
```

### Quick Tip

- To add the embeddings and test it immediately, manually create the `query_vector` and update a document in the `{index_name}` and, then use the same `query_vector` to search in the `render_template`.

```
POST {index_name}/_update/680bc0ed924febf627fc524d
{
  "doc": {
    "image_embedding": [0.01658179610967636, 0.03511231020092964, -0.01910591311752796, 0.04759567975997925, 0.007392457220703363, 0.041482552886009216, -0.00506657175719738, -0.008704421110451221, -0.0006646860274486244, -0.0005833572940900922, -0.012989193201065063, -0.020764362066984177, 0.015698278322815895, 0.005400165915489197, -0.006252847611904144, -0.018443984910845757, 0.13550254702568054, 0.025229912251234055, 0.023934118449687958, -0.0440627858042717, -0.12679260969161987, 0.014905421994626522, -0.007434233091771603, -0.04142316058278084, 0.02410072274506092, 0.013529140502214432, -0.023162899538874626, 0.0035687473136931658, 0.01589450240135193, -0.022737817838788033, 0.04851134493947029, -0.007447127252817154, 0.04024679958820343, -0.0015348338056355715, ..., 0.025384193286299706, -0.014990167692303658]
  }
}
```

[!NOTE] The above **query_vector(truncated)** i.e. 512-dimensional embeddings is of the image: https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/img/recipes/20/42/51/picIDgjux.jpg

---

## How to Use

### 1. **Setup**

Install dependencies:

```bash
pip install flask elasticsearch torch torchvision transformers pillow requests numpy
```

Configure your **Elasticsearch Cloud URL**, **API key**, and **search settings** in `config.py`:

```python
# config.py

ELASTIC_URL = "https://your-elasticsearch-url"
ELASTIC_API_KEY = "your-api-key"
INDEX_NAME = "search-testing-v7"
IMAGE_SEARCH_TEMPLATE = "image_search_template"

CLIP_MODEL_NAME = "openai/clip-vit-base-patch32"

KNN_FIELD = "image_embedding"
KNN_K = 8
KNN_NUM_CANDIDATES = 50
KNN_FIELDS = ["title", "directions", "ingredients", "body_content"]
```

---

### 2. **Running with a Static Image (Beta)**

For **quick testing** using a hardcoded image URL:

```bash
python3 image_search_app.beta.py
```

**Expected CLI Output:**

```json
{
    "_index": "search-testing-v7",
    "_id": "680ba393924feb99aecd646a",
    "_score": 0.89896774,
    "_ignored": [
        "body_content.enum"
    ],
    "_source": {
        "title": "Delicious Fajita Marinade Recipe - Food.com",
        "ingredients": [
            "1 clove garlic (minced)",
            "1 1 ⁄ 2 teaspoons salt",
            "1 tablespoon ground cumin",
            "1 ⁄ 2 teaspoon chili powder",
            "1 ⁄ 2 teaspoon crushed red pepper flakes",
            "2 tablespoons oil (any type works)",
            "1 tablespoon lemon juice",
            "1 ⁄ 3 cup A.1. Original Sauce"
        ],
        "directions": "Combine all ingredients, mixing well. Marinade 1 1/2lbs Beef or Chicken for at least 2 hours. Cook as desired on outside grill, stovetop saute pan, or you can even cook them on the George Foreman grill.",
        "image": "https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/img/recipes/10/63/71/oeoBS2vsTP2phNmhCIYM_fajita-marinade-5820.jpg",
        "url": "https://www.food.com/recipe/fajita-marinade-106371"
    }
}
```

---

### 3. **Running with User Input**

```bash
python3 image_search_app.py
```

#### Example interaction:

```
Please enter the image URL for searching: https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/img/recipes/35/16/31/TW8kFVRNTwKckUevzMv7_sea-bass-recipe-5393.jpg
Embedding generated with shape: (512,)
First 10 embedding values: [ 0.00827968  0.03805021 -0.02145038  0.02773996  0.0163618   0.02976616
  0.00256592  0.02934411  0.02923703  0.01320422]
Embedding is 512 dimensions.
Searching similar images in Elasticsearch...
Elasticsearch response (filtered fields):
{
  "title": "Simple Oven-Baked Sea Bass Recipe - Food.com",
  "directions": "Preheat oven to 450°F...",
  "ingredients": [
    "1 lb sea bass (cleaned and scaled)",
    "3 garlic cloves , minced or crushed",
    "... (other ingredients)"
  ],
  "image": "https://img.sndimg.com/food/image/upload/q_92,...sea-bass-recipe-5393.jpg",
  "score": 1.0011063
}
...
...
```

> **Note:** This is only the **filtered fields**: `title`, `directions`, `ingredients`, `image`, and `score`.

---

## Elasticsearch Search Template Example

```json
{
  "script": {
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
    "lang": "mustache",
    "params": {
      "knn_field": "image_embedding",
      "query_vector": [],
      "k": 8,
      "num_candidates": 50,
      "fields": ["title", "directions", "ingredients", "body_content"]
    }
  }
}
```

---

## Known Issues

- Refer to [Elasticsearch Issue #116246](https://github.com/elastic/elasticsearch/issues/116246):  
  **Search Application Template: use decimal value as param triggers error #116246**. Check the code here: `image_search/image_search_app.bug`

---

## References

- [CLIP Model](https://huggingface.co/openai/clip-vit-base-patch32)
- [Elasticsearch KNN Search](https://www.elastic.co/guide/en/elasticsearch/reference/current/knn-search.html)
- [Search Templates](https://www.elastic.co/docs/solutions/search/search-templates)

---