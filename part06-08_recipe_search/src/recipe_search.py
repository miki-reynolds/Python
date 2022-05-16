
def read_data(filename: str):
    recipes = []
    with open(filename) as new_file:
        contents = new_file.read()
        contents = contents.split("\n\n")
        
        for recipe in contents:
            recipe = recipe.split("\n")
            recipes.append(recipe)
    return recipes

def search_by_name(filename: str, word: str):
    found = []
    for recipe in read_data(filename):
        if word.lower() in recipe[0].lower():
            found.append(recipe[0])
    return found

def search_by_time(filename: str, prep_time: int):
    found = []
    for recipe in read_data(filename):
        if int(recipe[1]) <= prep_time:
            dish = f"{recipe[0]}, preparation time {recipe[1]} min"
            found.append(dish)
    return found

def search_by_ingredient(filename: str, ingredient: str):
    ingredients = []
    found = []
    for recipe in read_data(filename):
        if ingredient in recipe[2:]:
            dish = f"{recipe[0]}, preparation time {recipe[1]} min"
            found.append(dish)
    return found

# found_recipes = search_by_ingredient("recipes1.txt", "milk")
# for recipe in found_recipes:
#     print(recipe)
# print(found_recipes)

