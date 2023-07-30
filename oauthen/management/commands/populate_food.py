import csv
from oauthen.models import Food
from django.core.management.base import BaseCommand

def remove_suffix(value, suffix):
    # Remove the specified suffix from the value
    if value.endswith(suffix):
        return value[:-len(suffix)]
    return value

class Command(BaseCommand):
    help = 'Populate Food model from CSV data'

    def handle(self, *args, **options):
        file_path = '/home/komal/project/config/static/dataset/nutrition.csv'  # Replace with the actual path of your CSV file

        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                # Get the data from the row and handle suffixes
                food_name = row['food_name']
                standard = row['standard']
                carb = remove_suffix(row['carb'], 'g') if row['carb'] else None
                sugar = remove_suffix(row['sugar'], 'g') if row['sugar'] else None
                fat = remove_suffix(row['fat'], 'g') if row['fat'] else None
                calorie = remove_suffix(row['calorie'], 'mg') if row['calorie'] else None

                # Convert numeric fields to float if they are not None
                if carb is not None:
                    carb = float(carb)
                if sugar is not None:
                    sugar = float(sugar)
                if fat is not None:
                    fat = float(fat)
                if calorie is not None:
                    calorie = float(calorie)

                # Create and save the Food model instance
                food = Food(
                    food_name=food_name,
                    standard=standard,
                    carb=carb,
                    sugar=sugar,
                    fat=fat,
                    calorie=calorie,
                )
                food.save()
