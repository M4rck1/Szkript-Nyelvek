import json

class MMRecipeManager:
    def __init__(self, file_path):
        self.file_path=file_path
        self.recipes=self.load_recipes()

    def load_recipes(self):
        try:
            with open(self.file_path,"r") as file:
                return json.load(file)
        except FileNotFoundError:
            print("A recipes.json fajl nem talalhato")
            return []
        except json.JSONDecodeError:
            print("Hiba tortent a JSON fajl beolvasasanal!")
            return[]

    def save_recipes(self):
        with open(self.file_path, "w") as file:
            json.dump(self.recipes,file,indent=4)

    def search_recipes_by_ingredient(self, ingredient):
        return [recipe["name"] for recipe in self.recipes if ingredient in recipe["ingredients"]]

def check_ingredient_mm(ingredient, recipes):
    return any(ingredient in recipe["ingredients"] for recipe in recipes)
