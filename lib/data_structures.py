spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

new_food = {
    "name": "Jerk Chicken",
    "cuisine": "Caribbean",
    "heat_level": 7,
}

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]
names = get_names(spicy_foods)
print(names)

def get_spiciest_foods(spicy_foods):
    return[food for food in spicy_foods if food["heat_level"] > 5]
spiciest_foods = get_spiciest_foods(spicy_foods)
print(spiciest_foods)

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = "🌶" *food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")
print_spicy_foods(spicy_foods)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None
result = get_spicy_food_by_cuisine(spicy_foods,"Sichuan")
print(result)

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            heat_level = "🌶" * food["heat_level"]
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")
print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)
average = get_average_heat_level(spicy_foods)
print(average)

def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods.append(new_spicy_food)
    return spicy_foods
update_spicy_foods = create_spicy_food(spicy_foods, new_food)
print(update_spicy_foods)