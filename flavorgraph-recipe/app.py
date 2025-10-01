from flask import Flask, render_template, request

app = Flask(__name__)

# Recipe database (your given items)
recipes_data = [
    {
        "name": "Chicken Biryani",
        "image": "chicken_biryani.jpg",
        "ingredients": [
            "Basmati Rice",
            "Chicken",
            "Onions",
            "Tomatoes",
            "Yogurt",
            "Ginger Garlic Paste",
            "Spices",
            "Mint Leaves",
            "Coriander Leaves"
        ]
    },
    {
        "name": "Butter Chicken",
        "image": "butter_chicken.jpg",
        "ingredients": [
            "Chicken",
            "Butter",
            "Tomatoes",
            "Cream",
            "Onions",
            "Ginger Garlic Paste",
            "Garam Masala",
            "Coriander Powder"
        ]
    },
    {
        "name": "Grilled Fish",
        "image": "grilled_fish.jpg",
        "ingredients": [
            "Fish Fillets",
            "Olive Oil",
            "Garlic",
            "Lemon Juice",
            "Salt",
            "Black Pepper",
            "Rosemary"
        ]
    },
    {
        "name": "Egg Curry",
        "image": "egg_curry.jpg",
        "ingredients": [
            "Eggs",
            "Onions",
            "Tomatoes",
            "Ginger Garlic Paste",
            "Spices",
            "Coriander Leaves"
        ]
    },
    {
        "name": "Chicken Shawarma",
        "image": "chicken_shawarma.jpg",
        "ingredients": [
            "Chicken",
            "Pita Bread",
            "Garlic Sauce",
            "Onions",
            "Lettuce",
            "Tomatoes",
            "Cucumber"
        ]
    }
]

@app.route("/", methods=["GET", "POST"])
def home():
    user_ingredients = []
    possible_recipes = []

    if request.method == "POST":
        # Get ingredients entered by user
        user_input = request.form.get("ingredients", "")
        user_ingredients = [ing.strip().lower() for ing in user_input.split(",") if ing.strip()]

        # Match user ingredients with recipes
        for recipe in recipes_data:
            missing = [i for i in recipe["ingredients"] if i.lower() not in user_ingredients]
            possible_recipes.append({
                "name": recipe["name"],
                "image": recipe["image"],
                "missing": missing,
                "can_make": len(missing) == 0
            })

    return render_template("index.html", recipes=possible_recipes, user_ingredients=user_ingredients)


if __name__ == "__main__":
    app.run(debug=True)
