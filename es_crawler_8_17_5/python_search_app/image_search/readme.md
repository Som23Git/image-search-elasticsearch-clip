
** IN CLI - Expected Output for image_search/image_search_app.beta.py**
where we are passing the image as a static variable in the code itself
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

## Expected output for image_search_app.py:

Where here we are passing the image as an input variable and not in the code:

when asking for: Please enter the image URL for searching: enter this image: https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/img/recipes/35/16/31/TW8kFVRNTwKckUevzMv7_sea-bass-recipe-5393.jpg

Output in the terminal:
image_search % python3 image_search_app.py
Using a slow image processor as `use_fast` is unset and a slow processor was saved with this model. `use_fast=True` will be the default behavior in v4.52, even if the model was saved with a slow processor. This will result in minor differences in outputs. You'll still be able to use a slow processor with `use_fast=False`.
Please enter the image URL for searching: https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/img/recipes/35/16/31/TW8kFVRNTwKckUevzMv7_sea-bass-recipe-5393.jpg
Embedding generated with shape: (512,)
First 10 embedding values: [ 0.00827968  0.03805021 -0.02145038  0.02773996  0.0163618   0.02976616
  0.00256592  0.02934411  0.02923703  0.01320422]
Embedding is 512 dimensions.
Searching similar images in Elasticsearch...
Elasticsearch response (filtered fields):
{
  "title": "Simple Oven-Baked Sea Bass Recipe - Food.com",
  "directions": "Preheat oven to 450F\u00b0. In a cup, mix garlic, olive oil, salt, and black pepper. Place fish in a shallow glass or ceramic baking dish. Rub fish with oil mixture. (Optional) Pour wine over fish. Bake fish, uncovered, for 15 minutes; then sprinkle with parsley or Italian seasoning and continue to bake for 5 more minutes (or until the thickest part of the fish flakes easily). Drizzle remaining pan juices over fish and garnish with lemon wedges. Enjoy!",
  "ingredients": [
    "1 lb sea bass (cleaned and scaled)",
    "3 garlic cloves , minced or crushed",
    "1 tablespoon extra virgin olive oil",
    "1 tablespoon italian seasoning or 1 tablespoon fresh parsley leaves",
    "2 teaspoons fresh coarse ground black pepper",
    "1 teaspoon salt",
    "2 lemon wedges",
    "1 \u2044 3 cup white wine vinegar (optional) or 1/3 cup white wine (optional)"
  ],
  "image": "https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/img/recipes/35/16/31/TW8kFVRNTwKckUevzMv7_sea-bass-recipe-5393.jpg",
  "score": 1.0011063
}
{
  "title": "Best Fajitas Recipe - Food.com",
  "directions": "Slice steak into thin strips. In bowl, mix together 1 tablespoons olive oil, lime juice, garlic, chili powder, cumin, hot pepper flakes, black pepper & salt. Add beef strips and stir to coat, set aside. Wrap tortillas in foil and place in 350\u00b0 oven for 5-10 minutes or until heated through. Cut onions in half lengthwise and slice into strips, cut your peppers into strips. In large non stick skillet over medium high heat, heat remaining tablespoons of olive oil. Add onions & peppers stirring for 3-4 minutes, until softened; transfer to a bowl and set aside. Add beef to skillet, cook, stirring for 3-4 minutes or until they lose their red color. Return onions and peppers to skillet; stir for about one minute. To serve, spoon a portion of the beef mixture down the centre of each tortilla, top with your desired toppings , fold bottom of tortilla up over filling, fold the sides in, overlapping.",
  "ingredients": [
    "3 \u2044 4 lb top sirloin steak",
    "2 tablespoons olive oil",
    "1 tablespoon lime juice",
    "1 garlic clove , finely minced",
    "1 \u2044 2 teaspoon chili powder",
    "1 \u2044 2 teaspoon cumin",
    "1 \u2044 2 teaspoon hot pepper flakes",
    "1 \u2044 2 teaspoon black pepper",
    "1 \u2044 2 teaspoon salt",
    "8 flour tortillas (8 inch/20 cm)",
    "1 -2 onion , we usually use approx. 1-2 depending on size (however much you like,enough to make a good mix with the peppers)",
    "2 small sweet peppers , of your choice (green, red, or yellow)",
    "Toppings",
    "salsa",
    "sour cream",
    "shredded cheese",
    "chopped tomato"
  ],
  "image": "https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/img/recipes/63/78/6/NrPa79ZESEOqMlMoFDos_fajitas-3.jpg",
  "score": 0.9296875
}
{
  "title": "Ww Grilled Salmon With Teriyaki Sauce - 4 Points Recipe - Food.com",
  "directions": "Combine first 7 ingredients in a shallow dish; stir well. Add fish; cover, and marinate in refrigerator 30 minutes. Coat grill rack with cooking spray; place on grill over medium-hot coals (350-400 degrees). Remove fish from marinade; reserve marinade. Place fish on grill rack or in a grill basket coated with cooking spray; grill, uncovered, 5 to 7 minutes on each side or until fish flakes easily when tested with a fork. Transfer fish to a serving platter, and keep warm. Place reserved marinade in a small saucepan; bring to a boil. Boil 5 minutes or until marinade becomes thick and syrupy. Spoon over fish; serve immediately.",
  "ingredients": [
    "1 \u2044 4 cup dry sherry",
    "1 \u2044 4 cup low sodium soy sauce",
    "1 tablespoon brown sugar",
    "1 tablespoon rice wine vinegar",
    "1 teaspoon garlic powder",
    "1 \u2044 2 teaspoon pepper",
    "1 \u2044 8 teaspoon ground ginger",
    "1 (16 ounce) skinless salmon fillet (1 inch thick)",
    "cooking spray"
  ],
  "image": "https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/img/recipes/29/39/27/Jbfdi33vReW8hK1YgfAp_0S9A8380.jpg",
  "score": 0.9025917
}
{
  "title": "Authentic Mexican Pozole Recipe - Food.com",
  "directions": "This recipe requires a simple prep. Prepare the onion, peel the garlic, chop the onion, peel and chop the 2 garlic cloves, chop the green chilies and jalapenos if you are using them and get the hominy drained and rinsed. I boil my ancho chilies in a separate small pot for the garnish part(read below). Now you are ready to cook. Place the meat in a large saucepan and just cover with lightly salted water. Add 1/2 chopped onion, the 2 cloves peeled garlic, pepper, cumin, and oregano. Bring to a boil over medium heat, skim off any foam that rises, reduce heat, cover and simmer for 45 minutes. Remove meat and broth, reserving both. Saute the remaining chopped onion and garlic in oil until translucent. Add the remaining spices, stir for a minute. Cut the reserved pork into 1 inch cubes and add to the pan. Stir in the canned hominy, pork broth (if there is not enough pork broth, add chicken stock, I like to add it anyway for flavor, about 2-4 cups, eyeball the amount you like), green chilies and jalapenos (optional). Cook at a simmer, covered, for 45 to 60 minutes until the meat and hominy are tender. If necessary, cook for up to an additional 60 minutes until the chilies and onions are well blended into the broth. Degrease the stew, taste for salt, and serve in soup bowls. This is a delicious recipe and well worth the effort to make.   lots of lime/lemon wedges. sliced radishes. chopped cilantro. Shredded cabbage(not red). fresh/ packaged fried corn tortillas. When my ancho chilies are soft from boiling(takes about 15 minutes), then i put them in the blender with 1 1/2cups of water, 1 clove of garlic and about 2 tablespoons diced onion, and about 1 tablespoons of salt and pepper. I blend this thin, then strain it to get the liquid separated from its \"pulp\". I throw the pulp into the soup for the flavor i like but you can discard if too spicy for you. The remaining liquid you put in a serving dish for guests to add in their own bowl, if desired. Beware! It's HOT!",
  "ingredients": [
    "1 1 \u2044 2 lbs pork shoulder",
    "2 garlic cloves , peeled",
    "1 tablespoon cumin powder",
    "1 onion , chopped",
    "2 garlic cloves , chopped",
    "2 tablespoons oil",
    "1 \u2044 2 teaspoon black pepper",
    "1 \u2044 2 teaspoon cayenne",
    "2 tablespoons california chili powder",
    "1 tablespoon salt",
    "1 \u2044 4 teaspoon oregano",
    "4 cups canned white hominy , drained and rinsed",
    "3 -5 cups pork broth , from cooking pork shoulder",
    "1 cup canned diced green chilis (optional)",
    "salt",
    "2 whole fresh jalapenos, chopped (optional)",
    "3 whole ancho chilies , seeded and stemmed (garnish) (optional)"
  ],
  "image": "https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/img/recipes/19/62/33/sobU9LjR3qh8ul37iAvw_pork-pozole-7704.jpg",
  "score": 0.90187454
}
{
  "title": "Delicious Fajita Marinade Recipe - Food.com",
  "directions": "Combine all ingredients, mixing well. Marinade 1 1/2lbs Beef or Chicken for at least 2 hours. Cook as desired on outside grill, stovetop saute pan, or you can even cook them on the George Foreman grill.",
  "ingredients": [
    "1 clove garlic (minced)",
    "1 1 \u2044 2 teaspoons salt",
    "1 tablespoon ground cumin",
    "1 \u2044 2 teaspoon chili powder",
    "1 \u2044 2 teaspoon crushed red pepper flakes",
    "2 tablespoons oil (any type works)",
    "1 tablespoon lemon juice",
    "1 \u2044 3 cup A.1. Original Sauce"
  ],
  "image": "https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/img/recipes/10/63/71/oeoBS2vsTP2phNmhCIYM_fajita-marinade-5820.jpg",
  "score": 0.89896774
}
{
  "title": "Herb-Steamed Chilean Sea Bass Recipe - Food.com",
  "directions": "Cut the sea bass in half horizontally. Season the inside with salt and pepper and fill the center with the chopped herbs. Reassemble the sea bass and season the outside with salt and pepper to taste. Wrap in plastic wrap. Steam the sea bass in an 8-inch, flat-bottomed steamer, covered, for 6 minutes, or until it is barely opaque. To assemble: Remove the plastic wrap. Use a very sharp knife to cut the fish into eight 2-inch wedges. Choose a flat, colorful plate to set off the dramatic form of the fish. Stand one wedge on its end and show the herb filling of the other. Garnish with fresh herbs.",
  "ingredients": [
    "3 \u2044 4 lb chilean sea bass fillet",
    "salt & fresh ground pepper, to taste",
    "3 tablespoons tarragon , chopped",
    "3 tablespoons dill",
    "3 tablespoons flat leaf parsley",
    "1 sprig fresh tarragon , for garnish",
    "1 sprig fresh dill (to garnish)",
    "1 sprig flat leaf parsley (to garnish)"
  ],
  "image": "https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/img/recipes/30/77/24/picmog6q3.jpg",
  "score": 0.89424133
}
{
  "title": "Marinade for Flank Steak Recipe - Food.com",
  "directions": "Mix oil, Worcestershire sauce, soy sauce, vinegar, garlic, mustard,lemon juice and parsley together in a large zip lock bag. Marinade beef over night.",
  "ingredients": [
    "3 \u2044 4 cup oil",
    "2 tablespoons Worcestershire sauce",
    "1 \u2044 2 cup soy sauce",
    "1 \u2044 4 cup red wine vinegar",
    "2 cloves garlic , minced",
    "1 teaspoon dry mustard",
    "2 tablespoons lemon juice",
    "1 teaspoon parsley"
  ],
  "image": "https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/img/recipes/42/31/6/EbyFkkfCSEi1eRWUBm7C_SteakMarinade3.jpg",
  "score": 0.89297485
}
{
  "title": "Vegan Bacon Recipe - Food.com",
  "directions": "Fry tofu strips on low heat until they are crispy on the outside. The best way to do this is to lay them in the pan in the oil and let them sit for at least 10 minutes, simmering. They should turn easily after that. Turn them and give them another 10 minutes on the other side. Mix the soya sauce with the liquid smoke first, then take the pan off the heat. Pour the liquid smoke/soya sauce into the pan and stir the tofu so all sides are coated. Sprinkle the yeast over all, stir some more, over the heat, until the liquid is gone and the tofu is covered with sticky yeast.",
  "ingredients": [
    "1 lb firm tofu , cut into strips shaped like bacon",
    "2 tablespoons nutritional yeast",
    "2 tablespoons soya sauce",
    "1 teaspoon liquid smoke",
    "1 tablespoon oil, something neutral, not olive oil"
  ],
  "image": "https://img.sndimg.com/food/image/upload/q_92,fl_progressive,w_1200,c_scale/v1/img/recipes/14/88/99/LlkHd9qlTpqOlaaYdJjy_0S9A6887.jpg",
  "score": 0.89085007
}