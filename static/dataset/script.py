import csv ,os,django
import sqlite3
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Initialize Django
django.setup()

# Now you can access the database settings
from django.conf import settings

database_name = settings.DATABASES['default']['NAME']

def remove_suffix(value, suffix):
    # Remove the specified suffix from the value
    if value.endswith(suffix):
        return value[:-len(suffix)]
    return value

file_path = 'ABBREV.csv'  # Replace with the actual path of your CSV file

# Create a connection to the SQLite database
connection = sqlite3.connect(database_name)
cursor = connection.cursor()

# Create the Food table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Food (
        id INTEGER PRIMARY KEY,
        food_name TEXT,
        standard TEXT,
        carb INTEGER,
        sugar INTEGER,
        fat INTEGER,
        calorie INTEGER
    )
''')

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

        # Convert numeric fields to integers if they are not None
        if carb is not None:
            carb = int(carb)
        if sugar is not None:
            sugar = int(sugar)
        if fat is not None:
            fat = int(fat)
        if calorie is not None:
            calorie = int(calorie)

        # Insert the data into the Food table
        cursor.execute('''
            INSERT INTO Food (food_name, standard, carb, sugar, fat, calorie)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (food_name, standard, carb, sugar, fat, calorie))

# Commit the changes to the database and close the connection
connection.commit()
connection.close()
