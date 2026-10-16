import csv
import os
from tabulate import tabulate

discount_data = {}


def generate_bill(order_id):
    file_name = str(order_id) + ".csv"

    if not os.path.exists(file_name):
        print("Order not found!")
        return

    try:
        with open(file_name, "r", newline="") as file:
            data = list(csv.reader(file))

        table_no = data[0][4]
        status = data[0][7]
        items = data[2:]

        subtotal = 0

        for item in items:
            subtotal = subtotal + float(item[4])

        discount_percent = discount_data.get(order_id, 0)
        discount_amount = subtotal * discount_percent / 100

        amount_after_discount = subtotal - discount_amount
        tax = amount_after_discount * 0.05
        grand_total = amount_after_discount + tax

        table = []

        for item in items:
            table.append([
                item[0],
                item[1],
                item[2],
                item[3],
                item[4]
            ])

        print("\n================================")
        print("             BILL")
        print("================================")
        print("Order ID :", order_id)
        print("Table No :", table_no)
        print("Status   :", status)

        print("\nItems:")
        print(tabulate(
            table,
            headers=[
                "Item ID", "Item Name", "Price",
                "Quantity", "Total"
            ],
            tablefmt="grid"
        ))

        print("\nSubtotal    :", round(subtotal, 2))
        print("Discount    :", round(discount_amount, 2))
        print("Tax (5%)    :", round(tax, 2))
        print("Grand Total :", round(grand_total, 2))
        print("================================")

        return grand_total

    except (ValueError, IndexError):
        print("Invalid order data!")


def apply_discount(order_id, percent):
    file_name = str(order_id) + ".csv"

    if not os.path.exists(file_name):
        print("Order not found!")
        return

    try:
        percent = int(percent)

        if 0 <= percent <= 100:
            discount_data[order_id] = percent
            print(percent, "% discount applied to order", order_id)
        else:
            print("Discount must be between 0 and 100.")

    except ValueError:
        print("Please enter a valid discount.")


def export_bill_to_file(order_id):
    file_name = str(order_id) + ".csv"

    if not os.path.exists(file_name):
        print("Order not found!")
        return

    try:
        with open(file_name, "r", newline="") as file:
            data = list(csv.reader(file))

        table_no = data[0][4]
        status = data[0][7]
        items = data[2:]

        subtotal = 0

        for item in items:
            subtotal = subtotal + float(item[4])

        discount_percent = discount_data.get(order_id, 0)
        discount_amount = subtotal * discount_percent / 100

        amount_after_discount = subtotal - discount_amount
        tax = amount_after_discount * 0.05
        grand_total = amount_after_discount + tax

        receipt_name = str(order_id) + "_receipt.txt"

        with open(receipt_name, "w") as file:
            file.write("================================\n")
            file.write("             BILL\n")
            file.write("================================\n")
            file.write("Order ID : " + str(order_id) + "\n")
            file.write("Table No : " + str(table_no) + "\n")
            file.write("Status   : " + str(status) + "\n\n")

            file.write("Items:\n")

            for item in items:
                file.write(
                    item[1]
                    + " - Price: " + item[2]
                    + " Quantity: " + item[3]
                    + " Total: " + item[4]
                    + "\n"
                )

            file.write("\n")
            file.write("Subtotal    : " + str(round(subtotal, 2)) + "\n")
            file.write("Discount    : " + str(round(discount_amount, 2)) + "\n")
            file.write("Tax (5%)    : " + str(round(tax, 2)) + "\n")
            file.write("Grand Total : " + str(round(grand_total, 2)) + "\n")
            file.write("================================\n")

        print("Receipt saved as", receipt_name)

    except (ValueError, IndexError):
        print("Invalid order data!")


def billing():
    while True:
        print("\n========== BILLING ==========")
        print("1. Generate Bill")
        print("2. Apply Discount")
        print("3. Save Bill")
        print("4. Back to Dashboard")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            order_id = input("Enter Order ID: ")
            generate_bill(order_id)

        elif choice == "2":
            order_id = input("Enter Order ID: ")
            discount = input("Enter discount percentage: ")
            apply_discount(order_id, discount)

        elif choice == "3":
            order_id = input("Enter Order ID: ")
            export_bill_to_file(order_id)

        elif choice == "4":
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    billing()
