import csv
from tabulate import tabulate

FILE_NAME = "menu_veg_nonveg.csv"


def view_menu():
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        data = list(reader)

    print("\n========== RESTAURANT MENU ==========")
    print(tabulate(data[1:], headers=data[0], tablefmt="grid"))


def add_menu_item(name, category, food_type, price):
    last_id = 0

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            last_id = int(row["item_id"])

    new_id = last_id + 1

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            new_id, name, category, food_type, price, "In Stock"
        ])

    print("\nItem added successfully!")
    print("New Item ID:", new_id)


def update_menu_item(item_id, field, new_value):
    rows = []
    found = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["item_id"] == str(item_id):
                row[field] = new_value
                found = True
            rows.append(row)

    if found:
        save_menu(rows)
        print("\nItem updated successfully!")
    else:
        print("\nItem ID not found!")


def delete_menu_item(item_id):
    rows = []
    found = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["item_id"] == str(item_id):
                found = True
            else:
                rows.append(row)

    if found:
        save_menu(rows)
        print("\nItem deleted successfully!")
    else:
        print("\nItem ID not found!")


def toggle_availability(item_id):
    rows = []
    found = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["item_id"] == str(item_id):
                found = True

                if row["availability"] == "In Stock":
                    row["availability"] = "Out of Stock"
                else:
                    row["availability"] = "In Stock"

            rows.append(row)

    if found:
        save_menu(rows)
        print("\nAvailability changed successfully!")
    else:
        print("\nItem ID not found!")


def save_menu(rows):
    fieldnames = [
        "item_id", "name", "category",
        "type", "price", "availability"
    ]

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
