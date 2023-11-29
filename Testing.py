"""
Implementing the basic functions and testing them
"""
import csv


class Image:
    def __init__(self, imagePath):
        self.imagePath = imagePath

    def getImagePath(self):
        return self.imagePath

    def setImagePath(self, imagePath):
        self.imagePath = imagePath


class Recipe:
    def __init__(self, name, ingredients, instructions, images=None, rating=0):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.images = images if images else []
        self.rating = rating

    def getName(self):
        return self.name

    def getIngredients(self):
        return self.ingredients

    def getInstructions(self):
        return self.instructions

    def getImages(self):
        return self.images

    def getRating(self):
        return self.rating

    def setName(self, name):
        self.name = name

    def setIngredients(self, ingredients):
        self.ingredients = ingredients

    def setInstructions(self, instructions):
        self.instructions = instructions

    def setImages(self, images):
        self.images = images

    def setRating(self, rating):
        self.rating = rating


class RecipeManager:
    def __init__(self):
        self.recipes = []

    def addRecipe(self, recipe):
        self.recipes.append(recipe)

    def removeRecipe(self, recipe):
        if recipe in self.recipes:
            self.recipes.remove(recipe)
        else:
            print("Recipe not found.")

    def getRecipeByName(self, name):
        for recipe in self.recipes:
            if recipe.getName() == name:
                return recipe
        return None

    def filterRecipesByKeyword(self, keyword):
        filtered_recipes = []
        for recipe in self.recipes:
            if keyword.lower() in recipe.getName().lower():
                filtered_recipes.append(recipe)
        return filtered_recipes

    def saveRecipesToCSV(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for recipe in self.recipes:
                writer.writerow([
                    recipe.getName(),
                    recipe.getIngredients(),
                    recipe.getInstructions(),
                    recipe.getRating(),
                    ', '.join([image.getImagePath() for image in recipe.getImages()])
                ])

    def loadRecipesFromCSV(self, filename):
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                name, ingredients, instructions, rating, image_paths = row
                images = [Image(path.strip()) for path in image_paths.split(',')]
                self.addRecipe(Recipe(name, ingredients, instructions, images, int(rating)))


# Function testing
class CookingAssistant:
    def __init__(self):
        self.recipes = RecipeManager()

    def displayRecipe(self, name):
        recipe = self.recipes.getRecipeByName(name)
        if recipe:
            print(f"Recipe Name: {recipe.getName()}")
            print(f"Ingredients: {recipe.getIngredients()}")
            print(f"Instructions: {recipe.getInstructions()}")
            print("Images:")
            for image in recipe.getImages():
                print(image.getImagePath())
            print(f"Rating: {recipe.getRating()}")
        else:
            print("Recipe not found.")

    def filterRecipes(self, keyword):
        filtered_recipes = self.recipes.filterRecipesByKeyword(keyword)
        if filtered_recipes:
            print(f"Recipes containing '{keyword}':")
            for recipe in filtered_recipes:
                print(recipe.getName())
        else:
            print("No recipes found for the given keyword.")


# Example Usage:
if __name__ == "__main__":
    # Creating a Cooking Assistant instance
    cooking_assistant = CookingAssistant()

    # # Creating a few recipes
    # recipe1 = Recipe("Pasta", "Pasta","Boil pasta, add sauce.",  [Image("pasta_image.jpg")], 4)
    # recipe2 = Recipe("Salad", "Salad","Chop veggies, mix with dressing.",  [Image("salad_image.jpg")], 5)
    # recipe3 = Recipe("Soup", "Soup","Simmer ingredients for 30 mins.",  [Image("soup_image.jpg")], 3)
    #
    # # Adding recipes to the RecipeManager
    # cooking_assistant.recipes.addRecipe(recipe1)
    # cooking_assistant.recipes.addRecipe(recipe2)
    # cooking_assistant.recipes.addRecipe(recipe3)

    cooking_assistant.recipes.loadRecipesFromCSV("recipes.csv")

    # Displaying a recipe
    cooking_assistant.displayRecipe("Pasta")

    # Filtering recipes
    cooking_assistant.filterRecipes("salad")

    print()

    for i in cooking_assistant.recipes.recipes:
        print(i.getName())

    # cooking_assistant.recipes.saveRecipesToCSV("recipes.csv")