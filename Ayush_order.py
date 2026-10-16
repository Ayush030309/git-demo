import csv
import os
from tabulate import tabulate

MENU_FILE = "menu_veg_nonveg.csv"
COUNT_FILE = "count.txt"
TABLE_FILE="table.csv"


def create_order(table_no):
    if not os.path.exists(TABLE_FILE):
        print("Can't from the Table Details!")
        return
    
    with open(TABLE_FILE) as file:
        reader=list(csv.reader(file))

    for i in reader:
        if i[0]==str(table_no) and (i[1]!="Available"):
            print(f"Table No. {table_no} is unavailable.")
            return

    if os.path.exists(COUNT_FILE):
        with open(COUNT_FILE, "r") as file:
            count = int(file.read())
    else:
        count = 1

    order_id = "ORD" + str(count)

    with open(COUNT_FILE, "w") as file:
        file.write(str(count + 1))

    file_name = order_id + ".csv"

    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Order_id", order_id,
            "", "Table No.", table_no,
            "", "Status", "Pending"
        ])

        writer.writerow([
            "Item id", "Item Name", "Price",
            "Quantity", "Total"
        ])

    print("\nOrder created successfully!")
    print("Order ID:", order_id)
    return order_id


def add_item_to_order(order_id, item_id, quantity):
    order_file = order_id + ".csv"

    if not os.path.exists(order_file):
        print("Order not found!")
        return

    try:
        quantity = int(quantity)
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid quantity.")
        return

    item_name = ""
    item_price = 0

    if not os.path.exists(MENU_FILE):
        print("Menu file not found!")
        return

    with open(MENU_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for item in reader:
            if item["item_id"] == str(item_id):
                if item["availability"] != "In Stock":
                    print("Sorry, this item is not available.")
                    return

                item_name = item["name"]
                item_price = float(item["price"])
                break

    if item_name == "":
        print("Item not found in menu!")
        return

    with open(order_file, "r", newline="") as file:
        rows = list(csv.reader(file))

    for row in rows[2:]:
        if row[0] == str(item_id):
            print("This item is already in the order.")
            return

    total = item_price * quantity

    with open(order_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            item_id, item_name, item_price, quantity, total
        ])

    print("Item added to order successfully!")


def update_item_quantity(order_id, item_id, new_quantity):
    order_file = order_id + ".csv"

    if not os.path.exists(order_file):
        print("Order not found!")
        return

    try:
        new_quantity = int(new_quantity)
        if new_quantity <= 0:
            print("Quantity must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid quantity.")
        return

    with open(order_file, "r", newline="") as file:
        rows = list(csv.reader(file))

    found = False

    for row in rows[2:]:
        if row[0] == str(item_id):
            row[3] = str(new_quantity)
            row[4] = float(row[2]) * new_quantity
            found = True
            break

    if not found:
        print("Item not found in order!")
        return

    with open(order_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Quantity updated successfully!")


def view_order(order_id):
    order_file = order_id + ".csv"

    if not os.path.exists(order_file):
        print("Order not found!")
        return

    with open(order_file, "r", newline="") as file:
        rows = list(csv.reader(file))

    print("\n================================")
    print("Order ID :", rows[0][1])
    print("Table No :", rows[0][4])
    print("Status   :", rows[0][7])
    print("================================")

    print(tabulate(
        rows[2:],
        headers=rows[1],
        tablefmt="grid"
    ))


def update_order_status(order_id, new_status):
    order_file = order_id + ".csv"

    if not os.path.exists(order_file):
        print("Order not found!")
        return

    with open(order_file, "r", newline="") as file:
        rows = list(csv.reader(file))

    rows[0][7] = new_status

    with open(order_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Order status updated successfully!")


def remove_order_item(order_id,item_id):
    order_file = order_id + ".csv"

    if not os.path.exists(order_file):
        print("Order not found!")
        return

    with open(order_file,"r",newline="") as file:
        rows=list(csv.reader(file))
    
    found=False

    for row in rows[2:]:
        if row[0]==str(item_id):
            rows.remove(row)
            found=True

    if found:
        with open(order_file,"w",newline="") as file:
            write=csv.writer(file)
            write.writerows(rows)
        print("Item removed successfully!")
    else:
        print("Item is not in Order!")


def cancel_order(order_id):
    order_file = order_id + ".csv"

    if not os.path.exists(order_file):
        print("Order not found!")
        return

    os.remove(order_file)
    print("Order cancelled successfully!")


def complete_order(order_id):
    order_file = order_id + ".csv"

    if not os.path.exists(order_file):
        print("Order not found!")
        return

    with open(order_file, "r", newline="") as file:
        rows = list(csv.reader(file))

    rows[0][7] = "Completed"

    with open("order_history.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows[2:])

    os.remove(order_file)

    print("Order completed successfully!")


def view_order_history():
    if not os.path.exists("order_history.csv"):
        print("No order history found.")
        return

    with open("order_history.csv", "r", newline="") as file:
        rows = list(csv.reader(file))

    if not rows:
        print("No past orders.")
        return

    print("\n========== ORDER HISTORY ==========")
    print(tabulate(rows, tablefmt="grid"))


def order_management():
    while True:
        print("\n========== ORDER MANAGEMENT ==========")
        print("1. Create Order")
        print("2. Add Item")
        print("3. Update Item Quantity")
        print("4. View Order")
        print("5. Update Order Status")
        print("6. Remove Item")
        print("7. Cancel Order")
        print("8. Complete Order")
        print("9. View Order History")
        print("10. Back to Dashboard")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            table_no = input("Enter table number: ")
            create_order(table_no)

        elif choice == "2":
            order_id = input("Enter order ID: ")
            item_id = input("Enter item ID: ")
            quantity = input("Enter quantity: ")
            add_item_to_order(order_id, item_id, quantity)

        elif choice == "3":
            order_id = input("Enter order ID: ")
            item_id = input("Enter item ID: ")
            quantity = input("Enter new quantity: ")
            update_item_quantity(order_id, item_id, quantity)

        elif choice == "4":
            order_id = input("Enter order ID: ")
            view_order(order_id)

        elif choice == "5":
            order_id = input("Enter order ID: ")

            print("\n1. Pending")
            print("2. Preparing")
            print("3. Served")

            status_choice = input("Choose status: ")

            if status_choice == "1":
                status = "Pending"
            elif status_choice == "2":
                status = "Preparing"
            elif status_choice == "3":
                status = "Served"
            else:
                print("Invalid choice!")
                continue

            update_order_status(order_id, status)

        elif choice == "6":
            order_id = input("Enter order ID: ")
            item_id = input("Enter item ID: ")
            remove_order_item(order_id,item_id)

        elif choice == "7":
            order_id = input("Enter order ID: ")
            cancel_order(order_id)

        elif choice == "8":
            order_id = input("Enter order ID: ")
            complete_order(order_id)

        elif choice == "9":
            view_order_history()

        elif choice == "10":
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    order_management()
