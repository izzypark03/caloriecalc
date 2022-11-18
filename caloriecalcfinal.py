

'''
The purpose of this program is to calculate a user's total macronutrient and caloric information
consumed over a period of time, and to compare this information with a user's entered calorie
and macronutrient goals with plotted graphs of data. Using the listed information from the UCSB Dining
Hall (specifically Ortega), a database of nutritional information will be manually created and stored
within nested dictionaries.

The program will allow users to select from dictionaries featuring Ortega entrees, desserts, and sides,
as well as manually add food items along with their nutritional information. Once the user finishes
adding items, the total nutritional sums will be displayed.

'''

import numpy as np
import matplotlib.pyplot as plt

def print_menu(menu):
    # This function will print the key in a menu.
    print('Items are listed below.')
    for key, value in enumerate(menu):
        print(f'{value}')

def reached_goals(actual_num, goal_num, unit='calories'):
    if int(actual_num) < int(goal_num):
        print(f"You are {int(goal_num) - int(actual_num)} {unit} away from your goal.")
    elif int(actual_num) > int(goal_num):
        print(f"You are {int(actual_num) - int(goal_num)} {unit} above your goal.")
    elif int(actual_num) == int(goal_num):
        print(f"You are right on your goal!")



if __name__ == '__main__':
    # List of dictionaries featuring Ortega items below:
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
        'Veggie burger': {'Calories': 540, 'Carbs': 56, 'Fats': 32, 'Protein': 11},
        'Fried chicken w/ red mash potato': {'Calories': 710, 'Carbs': 34, 'Fats': 23, 'Protein': 85}

        }

    Ortega_sides = {
        'House salad': {'Calories': 30, 'Carbs': 5, 'Fats': 0, 'Protein': 3},
        'Roasted broccoli': {'Calories': 60, 'Carbs': 4, 'Fats': 4.5, 'Protein': 2},
        'Roasted citrus thyme carrots': {'Calories': 60, 'Carbs': 14, 'Fats': 0, 'Protein': 0},
        'Hummus with celery and carrots': {'Calories': 140, 'Carbs': 16, 'Fats': 8, 'Protein': 4},
        'Fries': {'Calories': 210, 'Carbs': 22, 'Fats': 13, 'Protein': 2},
        'Potato chips': {'Calories': 160, 'Carbs': 14, 'Fats': 10, 'Protein': 2},
        'Sauteed zucchini & yellow squash': {'Calories': 20, 'Carbs': 4, 'Fats': 0, 'Protein': 1}

        }

    Ortega_desserts = {
        'Butterscotch bar': {'Calories': 150, 'Carbs': 26, 'Fats': 6, 'Protein': 2},
        'Snickerdoodle cookie': {'Calories': 650, 'Carbs': 72, 'Fats': 39, 'Protein': 6},
        'Double chocolate brownie': {'Calories': 420, 'Carbs': 54, 'Fats': 22, 'Protein': 5},
        'Banana bar': {'Calories': 380, 'Carbs': 60, 'Fats': 5, 'Protein': 3},
        'Oatmeal trail mix cookie': {'Calories': 510, 'Carbs': 64, 'Fats': 27, 'Protein': 7},
        'Toll house bar': {'Calories': 190, 'Carbs': 29, 'Fats': 9, 'Protein': 2}

        }

    # Users will be asked about their caloric and macro goals.
    print("These next series of questions will ask about your nutritional goals.")
    calorie_goal = input("What is your caloric goal for the day? ")
    print("Macro goals for the day:")
    carbs_goal = input("Amount of carbs (in grams): ")
    fats_goal = input("Amount of fat (in grams): ")
    protein_goal = input("Amount of protein (in grams): ")


    food_eaten = []
    calorie_sum = 0
    carbs_sum = 0
    fats_sum = 0
    protein_sum = 0

    done = False

    while not done:
        print("(1) Add an entree from Ortega")
        print("(2) Add a side from Ortega")
        print("(3) Add a dessert from Ortega")
        print("(4) Add a non_Ortega food")
        print("(5) Quit & see results")
        choice = input("Choose an option (1, 2, 3, 4, 5): ")
        if choice not in "12345":
            print("Invalid option. Please choose a number 1-5.")
        elif choice == "1":
            print_menu(Ortega_entrees)
            print("Enter an option")
            opt = input("> ")
            if opt in Ortega_entrees:
                print(f"You selected option {opt}")

                food_eaten.append(opt)

                calorie_sum += Ortega_entrees[opt]['Calories']
                carbs_sum += Ortega_entrees[opt]['Carbs']
                fats_sum += Ortega_entrees[opt]['Fats']
                protein_sum += Ortega_entrees[opt]['Protein']

                continue
            else:
                print(f"{opt} is not a valid option. Please make sure it is spelled exactly as listed.")

                continue
        if choice == "2":
            print_menu(Ortega_sides)
            print("Enter an option")
            opt = input("> ")
            if opt in Ortega_entrees:
                print(f"You selected option {opt}")

                food_eaten.append(opt)

                calorie_sum += Ortega_sides[opt]['Calories']
                carbs_sum += Ortega_sides[opt]['Carbs']
                fats_sum += Ortega_sides[opt]['Fats']
                protein_sum += Ortega_sides[opt]['Protein']

                continue

            else:
                print(f"{opt} is not a valid option. Please make sure it is spelled exactly as listed.")
                continue
        elif choice == "3":
            print_menu(Ortega_desserts)
            print("Enter an option")
            opt = input("> ")
            if opt in Ortega_desserts:
                print(f"You selected option {opt}")

                food_eaten.append(opt)

                calorie_sum += Ortega_desserts[opt]['Calories']
                carbs_sum += Ortega_desserts[opt]['Carbs']
                fats_sum += Ortega_desserts[opt]['Fats']
                protein_sum += Ortega_desserts[opt]['Protein']

                continue

            else:
                print(f"{opt} is not a valid option. Please make sure it is spelled exactly as listed. ")
                continue
        elif choice == "4":
            print("Manually enter the nutritional information for this non-Ortega food:")
            food = input("Food name: ")

            food_eaten.append(food)

            calories = int(input("Calories: "))
            carbs = int(input("Carbs: "))
            fats = int(input("Fats: "))
            protein = int(input("Protein: "))

            calorie_sum += calories
            carbs_sum += carbs
            fats_sum += fats
            protein_sum += protein
            continue

        elif choice == "5":
            break

    print(f"List of foods eaten today: {food_eaten}")
    print(f"Total calories consumed: {calorie_sum}")
    print(f"Total carbs consumed: {carbs_sum}")
    print(f"Total fats consumed: {fats_sum}")
    print(f"Total protein consumed: {protein_sum}")

    print("Did you reach your macro goals?")

    reached_goals(calorie_sum, calorie_goal)
    reached_goals(carbs_sum, carbs_goal, unit = 'grams of carbs')
    reached_goals(fats_sum, fats_goal, unit = 'grams of fats')
    reached_goals(protein_sum, protein_goal, unit = 'grams of protein')

    print("See you later!")


