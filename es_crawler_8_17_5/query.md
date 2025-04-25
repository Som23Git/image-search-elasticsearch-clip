
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

##### Expected Output

```
{
  "took": 113,
  "timed_out": false,
  "_shards": {
    "total": 2,
    "successful": 2,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 5704,
      "relation": "eq"
    },
    "max_score": 17.996868,
    "hits": [
      {
        "_index": "search-testing-v7",
        "_id": "680ba80b924feb8a1fd754ef",
        "_score": 17.996868,
        "_ignored": [
          "body_content.enum"
        ],
        "_source": {
          "title": "Queen Margherita Pizza Recipe - Food.com",
          "ingredients": [
            "1 pizza dough, prepared but not baked (I suggest Easy Peezy Pizza Dough (Bread Machine Pizza Dough) )",
            "Toppings",
            "11 ounces fresh imported mozzarella cheese",
            "1 lb firm ripe tomatoes",
            "3 tablespoons extra virgin olive oil",
            "8 -10 fresh basil leaves , cut into thin ribbons (NOT dried)",
            "2 tablespoons freshly grated imported parmesan cheese",
            "salt"
          ],
          "image": "https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/img/recipes/14/71/46/picryl1wM.jpg",
          "url": "https://www.food.com/recipe/queen-margherita-pizza-147146",
          "directions": "Make pizza dough according to directions up until the point where the dough is proofed and is ready to be cooked. If your mozzarella cheese is very fresh, slice up and set on paper towels first for any whey to absorb then proceed with recipe. Peel the tomatoes by plunging into boiling water for about 15 seconds. Remove peel, cut into thin slices, remove seeds and drain in a colander. Preheat oven to 425 degrees. Lightly oil a round pizza tray* with olive oil. Roll out the pizza dough into a thin, supple sheet and place in the prepared pizza pan. Brush the surface of the dough with olive oil, cover with thin slices of Mozzarella. Scatter on half of the tomato slices, then the Parmesan. Arrange the remaining tomato slices on top. *NOTE: a heavier pizza tray is preferable for best baking results. Lightly salt the tomatoes, then drizzle a little bit of olive oil all over the top. Bake 15-20 minutes. It may be necessary to turn pizza pan around at the half way mark for even browning. Garnish the fresh basil ribbons on top of the pizza just before serving."
        }
      },
      {
        "_index": "search-testing-v7",
        "_id": "680ba286924febb574cbe408",
        "_score": 17.19683,
        "_ignored": [
          "body_content.enum"
        ],
        "_source": {
          "title": "Deep Fried Mozzarella Cheese Sticks Recipe - Food.com",
          "ingredients": [
            "16 ounces mozzarella cheese",
            "1 ⁄ 2 cup water",
            "1 ⁄ 2 teaspoon garlic powder",
            "1 ⁄ 2 teaspoon dried oregano , crushed",
            "1 ⁄ 2 teaspoon dried parsley , crushed",
            "1 ⁄ 3 cup cornstarch",
            "3 large eggs , beaten",
            "1 1 ⁄ 2 cups Italian seasoned breadcrumbs",
            "2 ⁄ 3 cup flour",
            "1 ⁄ 8 teaspoon salt",
            "1 ⁄ 8 teaspoon pepper"
          ],
          "image": "https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/img/recipes/11/20/74/p0TeB6y2RyyxXz2hiGnX-moza.jpg",
          "url": "https://www.food.com/recipe/deep-fried-mozzarella-cheese-sticks-112074",
          "directions": "Mix together the eggs and water, set aside. combine the Italian bread crumbs, garlic powder, dried oregano and dried parsley. salt and pepper to taste. in a separate container, mix flour and cornstarch. cut mozzarella cheese into any desired shape, rectangle strips are traditional. One at a time, dip mozarella slices into the egg mixture, then the breadcrumbs, then the flour. fry sticks at 375 F until golden brown and serve with desired dipping sauce."
        }
      },
      {
        "_index": "search-testing-v7",
        "_id": "680ba994924febd1dadab353",
        "_score": 17.139465,
        "_ignored": [
          "body_content.enum"
        ],
        "_source": {
          "title": "Fried Mozzarella Cheese With Marinara Recipe - Deep-fried.Food.com",
          "ingredients": [
            "1 lb mozzarella cheese",
            "1 ⁄ 2 cup flour",
            "3 large eggs",
            "1 cup breadcrumbs",
            "1 ⁄ 2 teaspoon garlic powder",
            "1 ⁄ 2 teaspoon oregano",
            "1 ⁄ 2 teaspoon ground cumin",
            "1 pinch salt",
            "1 pinch pepper",
            "8 ounces marinara sauce, chilled",
            "vegetable oil"
          ],
          "image": "https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/gk-static/fdc-new/img/fdc-shareGraphic.png",
          "url": "https://www.food.com/recipe/fried-mozzarella-cheese-with-marinara-107960",
          "directions": "Cut the mozzarella into sticks a bit more than about 1/4 inch thick and about 1 1/2 inches long. Coat the sticks with flour, shaking off excess. Combine the bread crumbs and seasonings in a flat dish. Beat the eggs and place in a separate bowl. Coat the sticks by dipping them in the egg and then in the bread crumbs. The coating on the first stick should be fairly dry when you finish the last stick. Repeat with another dip in the egg and then in the bread crumbs. Deep-fry the coated sticks in oil for about 3 to 4 minutes until the coating is cooked. Fry in batches, keeping the finished ones warm in the oven. Serve with chilled marinara sauce or salsa."
        }
      },
      {
        "_index": "search-testing-v7",
        "_id": "680ba810924feb79b1d761b5",
        "_score": 17.1383,
        "_ignored": [
          "body_content.enum"
        ],
        "_source": {
          "title": "Roma Tomato Mozzarella Salad Recipe - Food.com",
          "ingredients": [
            "2 -3 roma tomatoes",
            "8 ounces chopped black olives",
            "8 ounces mozzarella cheese , ball",
            "1 ⁄ 4 cup fresh grated parmesan cheese",
            "1 red onion",
            "14 ounces Italian dressing (your favorite one is the best one)"
          ],
          "image": "https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/img/recipes/50/67/73/pic7QC6vq.jpg",
          "url": "https://www.food.com/recipe/roma-tomato-mozzarella-salad-506773",
          "directions": "Slice the mozzarella ball in half. Thinly slice roma tomatoes and mozzarella ball. It's your call whether you slice them lengthwise or widthwise but the tomato slices and mozzarella slices should be roughly the same size when you're done. (I do widthwise so it looks like a tower) Starting with tomato, layer the tomato and cheese alternately on the serving plate. Three layers of tomato and two layers of mozzarella total. Sprinkle with chopped red onion, chopped black olive and fresh grated Parmesan. Drizzle your favorite Italian dressing over the top and finish with some fresh cracked black pepper. Serve chilled. **You will have ingredients left over with this recipe. You could easily double the recipe by just adding more tomatoes."
        }
      },
      {
        "_index": "search-testing-v7",
        "_id": "680ba89f924feb1a98d899b2",
        "_score": 17.033102,
        "_ignored": [
          "body_content.enum"
        ],
        "_source": {
          "title": "Artichoke, Pesto &amp; Sun-Dried Tomato Pizza With Three Cheeses Recipe - Food.com",
          "ingredients": [
            "12 inches pizza dough",
            "1 cup mozzarella cheese , shredded",
            "1 ⁄ 2 cup parmesan cheese , shredded",
            "1 -2 chicken breast , grilled & sliced",
            "1 (14 ounce) can artichoke hearts , well-drained & quartered",
            "1 ⁄ 3 cup sun-dried tomato , chopped",
            "1 ⁄ 4 cup ricotta cheese",
            "1 ⁄ 2 tablespoon red pepper flakes (optional)",
            "1 ⁄ 4 cup basil pesto"
          ],
          "image": "https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/img/recipes/50/10/79/picsiGjXk.jpg",
          "url": "https://www.food.com/recipe/artichoke-pesto-sun-dried-tomato-pizza-with-three-cheeses-501079",
          "directions": "Preheat oven to 450. Prepare your pizza: Top the crust with mozzarella, Parmesan, chicken, artichoke hearts, and sun-dried tomatoes, in that order. Dollop the ricotta cheese all over the pizza (I usually do 1/2 teaspoon size balls). Sprinkle pizza with red pepper flakes, if using. Bake for 8-12 minutes, or until cheese is melted and pizza is warm (or however long your pizza dough package recommends). Remove pizza from oven and drizzle with little dollops of pesto sauce. Serve."
        }
      },
      {
        "_index": "search-testing-v7",
        "_id": "680ba8ca924febcaaad8f9bd",
        "_score": 16.7585,
        "_ignored": [
          "body_content.enum"
        ],
        "_source": {
          "title": "Quick Chunky Greek Pizza Recipe - Greek.Food.com",
          "ingredients": [
            "Crust",
            "2 cups cake flour or 2 cups pastry flour",
            "1 cup whole wheat flour",
            "1 ⁄ 2 cup cornmeal",
            "1 tablespoon chopped fresh rosemary or 1/2 teaspoon dried rosemary",
            "1 tablespoon sugar",
            "2 tablespoons baking powder",
            "1 teaspoon baking soda",
            "1 teaspoon salt",
            "1 ⁄ 3 - 1 ⁄ 2 cup plain yogurt",
            "1 ⁄ 3 - 1 ⁄ 2 cup olive oil (depends on how dough is turning out.)",
            "Topping",
            "4 large chopped tomatoes",
            "1 ⁄ 2 cup chopped basil",
            "2 garlic cloves , minced",
            "1 teaspoon salt",
            "1 ⁄ 4 teaspoon pepper",
            "1 (6 ounce) jar marinated artichoke hearts",
            "1 cup crumbled feta cheese",
            "2 cups mozzarella cheese (grated)",
            "1 ⁄ 2 cup parmesan cheese (grated)"
          ],
          "image": "https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/img/recipes/90/26/0/picCImZKz.jpg",
          "url": "https://www.food.com/recipe/quick-chunky-greek-pizza-90260",
          "directions": "Crust-- Sift first eight ingredients together in a bowl. Combine yogurt and oil together in a seperate bowl. Make a well in the centre of the dry ingredients and pour yogurt and oil mixture into the well. Carefully fold ingredients together until dough forms. Knead dough into a ball and let stand. Topping-- Combine first seven ingredients of topping in a bowl. Roll dough out onto a pizza pan or cookie sheet. Spread half of mozzarella onto dough. Spread topping evenly over cheese. Sprinkle the rest of the mozzarella along with the parmisan over topping. Bake in oven preheated to 400 for 20 to 30 minutes. Enjoy!"
        }
      },
      {
        "_index": "search-testing-v7",
        "_id": "680ba9f1924febac21db75b1",
        "_score": 16.547413,
        "_ignored": [
          "body_content.enum"
        ],
        "_source": {
          "title": "Tomato &amp; Mozzarella Caprese - Official Recipe - Olive Garden Recipe - Food.com",
          "ingredients": [
            "8 slices of vine-ripened tomatoes",
            "2 tablespoons balsamic vinegar",
            "8 medium fresh basil leaves",
            "12 ounces fresh mozzarella cheese , sliced into 8 slices",
            "dry oregano leaves",
            "sea salt or kosher salt",
            "fresh ground pepper",
            "2 tablespoons extra virgin olive oil"
          ],
          "image": "https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/img/recipes/23/90/50/pic4eI8T9.jpg",
          "url": "https://www.food.com/recipe/tomato-mozzarella-caprese-official-recipe-olive-garden-239050",
          "directions": "Arrange sliced tomatoes on a large platter. Place one basil leaf on top of each tomato slice. Place one slice of mozzarella on top of each basil leaf. Spring oregano, salt and black pepper on cheese and drizzle with extra-virgin olive oil. Finish with drizzle of balsamic vinegar."
        }
      },
      {
        "_index": "search-testing-v7",
        "_id": "680baa18924feb6570dbc24c",
        "_score": 16.39213,
        "_ignored": [
          "body_content.enum"
        ],
        "_source": {
          "title": "Grilled Chile-Cheese Toasts Recipe - Food.com",
          "ingredients": [
            "1 lb whole milk mozzarella , shredded",
            "1 ⁄ 2 cup finely chopped onion",
            "1 medium tomatoes , finely chopped and drained on paper towels",
            "2 jalapenos, seeded and finely chopped",
            "1 ⁄ 2 cup chopped fresh cilantro",
            "1 ⁄ 2 cup mayonnaise",
            "1 ⁄ 2 teaspoon cayenne pepper",
            "salt & freshly ground black pepper",
            "12 slices hearty whole wheat bread (1/2-inch-thick slices)"
          ],
          "image": "https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/img/recipes/26/63/88/pic39n1HE.jpg",
          "url": "https://www.food.com/recipe/grilled-chile-cheese-toasts-266388",
          "directions": "Preheat the broiler. In a large bowl, mash together all of the ingredients except the bread. Arrange the bread slices on a baking sheet and toast them until lightly browned. Let cool slightly, then turn the toasts over and spread the mozzarella cheese mixture on top. Broil for 3 to 5 minutes, until melted and lightly browned. Serve hot."
        }
      },
      {
        "_index": "search-testing-v7",
        "_id": "680ba44b924feba736cf1d8a",
        "_score": 16.194609,
        "_ignored": [
          "body_content.enum"
        ],
        "_source": {
          "title": "Fried Mozzarella Sticks Recipe - Food.com",
          "ingredients": [
            "8 ounces mozzarella cheese",
            "1 ⁄ 2 cup all-purpose flour",
            "1 large egg",
            "1 ⁄ 2 cup seasoned dry bread crumb"
          ],
          "image": "https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/img/recipes/34/53/86/T6QN1BwTXuLqx44SMecL_DSC_0648.JPG",
          "url": "https://www.food.com/recipe/fried-mozzarella-sticks-345386",
          "directions": """Cut the cheese into 8 3 1/2/x 1/2x1/2" sticks. Put flour into shallow dish and dredge the mozzarella sticks lightly in flour, shaking off the excess. One by one, dip in the beaten egg, coating completely, and then roll in bread crumbs to coat. Put the sticks on a plate and freeze for 15 minutes. Heat a deep fryer or heavy pot to 365 in 3 inches of oil. Fry the mozzarella sticks in 2 batches until golden brown, about 1 minute. Drain on paper towels and serve with hot marinara sauce."""
        }
      },
      {
        "_index": "search-testing-v7",
        "_id": "680ba450924feb8c76cf2883",
        "_score": 16.137436,
        "_ignored": [
          "body_content.enum"
        ],
        "_source": {
          "title": "Fried Mozzarella Cheese Sticks Recipe - Italian.Food.com",
          "ingredients": [
            "1 (8 ounce) package mozzarella cheese",
            "1 cup flour",
            "1 egg , slightly beaten",
            "1 cup breadcrumbs",
            "1 1 ⁄ 2 teaspoons oregano",
            "1 ⁄ 4 teaspoon salt",
            "olive oil or vegetable shortening , for frying"
          ],
          "image": "https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/img/recipes/16/03/97/ymYcmPDETPy6mKEcRYLC-MS.jpg",
          "url": "https://www.food.com/recipe/fried-mozzarella-cheese-sticks-160397",
          "directions": "Cut mozzarella cheese into sticks (approximately 3*1/2*1/2-inches). Place flour in one bowl, the egg in another bowl and the bread crumbs and oregano in another bowl. Dredge each piece of cheese into flour to coat. Dip floured cheese stick into egg, then dredge in bread crumb mixture. Place on a plate in a single layer. Refrigerate for 1 hour. In a large skillet, heat olive oil or shortening, 1/2-inch deep to 350°F. Fry mozzarella sticks a few pieces at a time until browned on all sides (about 3 minutes). Drain on paper towels. Serve hot with lemon wedges or marinara sauce for dipping. ~NOTE~ Preparation time includes 1 hour refrigeration time."
        }
      }
    ]
  }
}
```

#### Multi-match query with elser and BM25:

```
POST search-testing-v7/_search
{
  "size": 2,
  "_source": ["title", "directions", "ingredients", "url", "image"],
  "query": {
    "bool": {
      "should": [
        {
          "sparse_vector": {
            "field": "ml.inference.directions_expanded.predicted_value",
            "inference_id": ".elser_model_2_linux-x86_64",
            "query": "pizza mozzarella",
            "boost": 1
          }
        },
        {
          "multi_match": {
            "query": "pizza mozzarella",
            "fields": ["title", "directions", "ingredients"],
            "boost": 4
          }
        }
      ]
    }
  }
}
```
##### Expected Output

```
{
  "took": 70,
  "timed_out": false,
  "_shards": {
    "total": 2,
    "successful": 2,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 6125,
      "relation": "eq"
    },
    "max_score": 73.655495,
    "hits": [
      {
        "_index": "search-testing-v7",
        "_id": "680ba89f924feb1a98d899b2",
        "_score": 73.655495,
        "_ignored": [
          "body_content.enum"
        ],
        "_source": {
          "title": "Artichoke, Pesto &amp; Sun-Dried Tomato Pizza With Three Cheeses Recipe - Food.com",
          "ingredients": [
            "12 inches pizza dough",
            "1 cup mozzarella cheese , shredded",
            "1 ⁄ 2 cup parmesan cheese , shredded",
            "1 -2 chicken breast , grilled & sliced",
            "1 (14 ounce) can artichoke hearts , well-drained & quartered",
            "1 ⁄ 3 cup sun-dried tomato , chopped",
            "1 ⁄ 4 cup ricotta cheese",
            "1 ⁄ 2 tablespoon red pepper flakes (optional)",
            "1 ⁄ 4 cup basil pesto"
          ],
          "image": "https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/img/recipes/50/10/79/picsiGjXk.jpg",
          "url": "https://www.food.com/recipe/artichoke-pesto-sun-dried-tomato-pizza-with-three-cheeses-501079",
          "directions": "Preheat oven to 450. Prepare your pizza: Top the crust with mozzarella, Parmesan, chicken, artichoke hearts, and sun-dried tomatoes, in that order. Dollop the ricotta cheese all over the pizza (I usually do 1/2 teaspoon size balls). Sprinkle pizza with red pepper flakes, if using. Bake for 8-12 minutes, or until cheese is melted and pizza is warm (or however long your pizza dough package recommends). Remove pizza from oven and drizzle with little dollops of pesto sauce. Serve."
        }
      },
      {
        "_index": "search-testing-v7",
        "_id": "680ba80b924feb8a1fd754ef",
        "_score": 73.115364,
        "_ignored": [
          "body_content.enum"
        ],
        "_source": {
          "title": "Queen Margherita Pizza Recipe - Food.com",
          "ingredients": [
            "1 pizza dough, prepared but not baked (I suggest Easy Peezy Pizza Dough (Bread Machine Pizza Dough) )",
            "Toppings",
            "11 ounces fresh imported mozzarella cheese",
            "1 lb firm ripe tomatoes",
            "3 tablespoons extra virgin olive oil",
            "8 -10 fresh basil leaves , cut into thin ribbons (NOT dried)",
            "2 tablespoons freshly grated imported parmesan cheese",
            "salt"
          ],
          "image": "https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/img/recipes/14/71/46/picryl1wM.jpg",
          "url": "https://www.food.com/recipe/queen-margherita-pizza-147146",
          "directions": "Make pizza dough according to directions up until the point where the dough is proofed and is ready to be cooked. If your mozzarella cheese is very fresh, slice up and set on paper towels first for any whey to absorb then proceed with recipe. Peel the tomatoes by plunging into boiling water for about 15 seconds. Remove peel, cut into thin slices, remove seeds and drain in a colander. Preheat oven to 425 degrees. Lightly oil a round pizza tray* with olive oil. Roll out the pizza dough into a thin, supple sheet and place in the prepared pizza pan. Brush the surface of the dough with olive oil, cover with thin slices of Mozzarella. Scatter on half of the tomato slices, then the Parmesan. Arrange the remaining tomato slices on top. *NOTE: a heavier pizza tray is preferable for best baking results. Lightly salt the tomatoes, then drizzle a little bit of olive oil all over the top. Bake 15-20 minutes. It may be necessary to turn pizza pan around at the half way mark for even browning. Garnish the fresh basil ribbons on top of the pizza just before serving."
        }
      }
    ]
  }
}
```