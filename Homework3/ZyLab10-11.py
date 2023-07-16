# Sydney Ani PID: 1869076

class FoodItem:
    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0, servings=1.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
        self.servings = servings

    def get_calories(self):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * self.servings
        return calories

    def print_info(self):
        if self.name == "None":
            print('Nutritional information per serving of None:')
        else:
            print('\nNutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))
        print('Number of calories for {:.2f} serving(s): {:.2f}'.format(self.servings, self.get_calories()))


# Create food items
mms = FoodItem("M&M's", 10.0, 34.0, 2.0, 1.0)
none = FoodItem()

# Output for None
none.print_info()

# Output for M&M's
mms.print_info()
