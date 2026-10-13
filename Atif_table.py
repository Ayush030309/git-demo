import csv
import os

FILE_NAME = "reservations.csv"
TOTAL_TABLES = 20


def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Table No", "Customer Name",
                "Date", "Time", "Guests"
            ])


def view_reservations():
    create_file()

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    print("\n========== RESERVATIONS ==========")

    if len(rows) == 1:
        print("No reservations found.")
        return

    for row in rows[1:]:
        print(
            "Table:", row[0],
            "| Customer:", row[1],
            "| Date:", row[2],
            "| Time:", row[3],
            "| Guests:", row[4]
        )


def reserve_table():
    create_file()

    table_no = input("Enter table number (1-20): ")
    customer_name = input("Enter customer name: ")
    date = input("Enter date (DD-MM-YYYY): ")
    time = input("Enter time: ")
    guests = input("Enter number of guests: ")

    try:
        table_no = int(table_no)
        guests = int(guests)
    except ValueError:
        print("Please enter valid numbers.")
        return

    if table_no < 1 or table_no > TOTAL_TABLES:
        print("Invalid table number.")
        return

    if guests <= 0:
        print("Number of guests must be greater than 0.")
        return

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows[1:]:
        if (
            row[0] == str(table_no)
            and row[2] == date
            and row[3] == time
        ):
            print("Sorry! This table is already reserved.")
            return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            table_no, customer_name, date, time, guests
        ])

    print("Table reserved successfully!")


def cancel_reservation():
    create_file()

    table_no = input("Enter table number: ")
    date = input("Enter reservation date: ")
    time = input("Enter reservation time: ")

    rows = []
    found = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    new_rows = [rows[0]]

    for row in rows[1:]:
        if (
            row[0] == str(table_no)
            and row[2] == date
            and row[3] == time
        ):
            found = True
        else:
            new_rows.append(row)

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(new_rows)

        print("Reservation cancelled successfully!")
    else:
        print("Reservation not found.")


def table_reservation():
    while True:
        print("\n========== TABLE RESERVATION ==========")
        print("1. Reserve Table")
        print("2. View Reservations")
        print("3. Cancel Reservation")
        print("4. Back to Dashboard")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            reserve_table()

        elif choice == "2":
            view_reservations()

        elif choice == "3":
            cancel_reservation()

        elif choice == "4":
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    table_reservation()
