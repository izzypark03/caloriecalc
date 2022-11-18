
'''
The purpose of this program is to calculate the amount of calories consumed at UCSB's
Ortega Dining Commons.

Steps:
1. Create nested dictionary with item name, calories per serving, and macro amounts.
    Ex: 'Food_Item_Name': {'Calories': x, 'Carbs': x, 'Fats': x, 'Protein': x}

2. User will input item names of foods they have eaten.

4. Define total_calc function that will calculate the total amount of calories, carbs,
protein, and fats in each food item.

4. Data visualization with MatLab.
'''

import math

Ortega_entrees = {
    'Pulled pork sandwich': {'Calories': 510, 'Carbs': 60, 'Fats': 20, 'Protein': 24},
    'Macaroni & cheese': {'Calories': 1010, 'Carbs': 97, 'Fats': 47, 'Protein': 46},
    'Teriyaki bean burger': {'Calories': 370, 'Carbs': 60, 'Fats': 11, 'Protein': 9},
    'Teriyaki burger': {'Calories': 440, 'Carbs': 39, 'Fats': 17, 'Protein': 30},
    'Bacon breakfast burrito': {'Calories': 780, 'Carbs': 85, 'Fats': 36, 'Protein': 25},
    'Rainbow salad': {'Calories': 490, 'Carbs': 38, 'Fats': 35, 'Protein': 12},
    'Chicken caesar salad': {'Calories': 590, 'Carbs': 23, 'Fats': 36, 'Protein': 46},
    'Philly chicken cheese steak sandwich': {'Calories': 590, 'Carbs': 55, 'Fats': 27, 'Protein': 30},
    'Roasted vegetable panini': {'Calories': 740, 'Carbs': 79, 'Fats': 40, 'Protein': 23},
    'Baked pesto pasta with chicken': {'Calories': 720, 'Carbs': 62, 'Fats': 42, 'Protein': 26},
    'Turkey sub sandwich': {'Calories': 460, 'Carbs': 52, 'Fats': 15, 'Protein': 28},
    'Chile verde burrito': {'Calories': 920, 'Carbs': 86, 'Fats': 46, 'Protein': 38},
    'Tikka masala w/ tofu': {'Calories': 630, 'Carbs': 92, 'Fats': 21, 'Protein': 25},
    'Tikka masala w/ chicken': {'Calories': 680, 'Carbs': 92, 'Fats': 22, 'Protein': 33},
    'Chipotle BBQ chicken and potatoes': {'Calories': 510, 'Carbs': 34, 'Fats': 24, 'Protein': 39},
    'Classic burger': {'Calories': 450, 'Carbs': 28, 'Fats': 22, 'Protein': 32},
    'Veggie burger': {'Calories': 540, 'Carbs': 56, 'Fats': 32, 'Protein': 11}

}

Ortega_sides = {
    'House salad': {'Calories': 30, 'Carbs': 5, 'Fats': 0, 'Protein': 3},
    'Roasted broccoli': {'Calories': 60, 'Carbs': 4, 'Fats': 4.5, 'Protein': 2},
    'Roasted citrus thyme carrots': {'Calories': 60, 'Carbs': 14, 'Fats': 0, 'Protein': 0},
    'Hummus with celery and carrots': {'Calories': 140, 'Carbs': 16, 'Fats': 8, 'Protein': 4},
    'Fries': {'Calories': 210, 'Carbs': 22, 'Fats': 13, 'Protein': 2},
    'Potato chips': {'Calories': 160, 'Carbs': 14, 'Fats': 10, 'Protein': 2}
}

Ortega_desserts = {
    'Butterscotch bar': {'Calories': 150, 'Carbs': 26, 'Fats': 6, 'Protein': 2},
    'Snickerdoodle cookie': {'Calories': 650, 'Carbs': 72, 'Fats': 39, 'Protein': 6},
    'Double chocolate brownie': {'Calories': 420, 'Carbs': 54, 'Fats': 22, 'Protein': 5}

}

def merge_dicts (dict 1, dict2, dict3):
    dict3 = (**dict1, **dict2)
    return dict3

def total_calc(key, dict):
    pass

if __name__ == '__main__':

# Users will be asked about their caloric and macro goals.
calorie_goal = input("What is your caloric goal for the day? ")
print("Macro goals for the day:")
carbs_goal = input("Amount of carbs (in grams): ")
fats_goal = input("Amount of fat (in grams): ")
protein_goal = input("Amount of protein (in grams): ")

# Users will input the items they have eaten to see how they are comparing to their goals.
food_item = input("What did you eat at Ortega? ")
for food_item in Ortega_menu:
    total_calc()
    pass



