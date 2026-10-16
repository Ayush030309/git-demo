import csv
import os
import pandas as pd
from tabulate import tabulate

FILE_NAME = "table.csv"
TOTAL_TABLES = 20


def create_file():
    if not os.path.exists(FILE_NAME):
        data={
            "Table No.":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
            "Status":["Available"]*20,
            "Customer Name":["--"]*20,
            "Date":["--"]*20,
            "Time":["--"]*20,
            "Guest":["--"]*20
        }
        df=pd.DataFrame(data)
        df.to_csv(FILE_NAME,index=False)


def view_table():
    if not os.path.exists(FILE_NAME):
        return


    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    print("\n========== TABLES ============")

    print(tabulate(rows,headers="firstrow",tablefmt="grid"))


def reserve_table():
    if not os.path.exists(FILE_NAME):
        return


    try:
        table_no = int(input("Enter table number (1-20): "))
        customer_name = input("Enter customer name: ")
        date = input("Enter date (DD-MM-YYYY): ")
        time = int(input("Enter time(24 hrs format: 1000): "))
        guests = int(input("Enter number of guests: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if table_no < 1 or table_no > TOTAL_TABLES:
        print("Invalid table number.")
        return

    if not (0 <= time <= 2359):
        print("Invalid time.")
        return

    if guests <= 0:
        print("Number of guests must be greater than 0.")
        return

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    for row in rows[1:]:
        if (row[0]==str(table_no)) and (row[1]=="Available"):
            row[1]="Booked"
            row[2]=customer_name
            row[3]=date
            row[4]=str(time)
            row[5]=str(guests)
        elif (row[0]==str(table_no)) and (row[1]!="Available"):
            print("Table is already booked.")
            return

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Table reserved successfully!")


def cancel_reservation():
    if not os.path.exists(FILE_NAME):
        return

    try:
        table_no = int(input("Enter table number: "))
        date = input("Enter reservation date: ")
        time = int(input("Enter reservation time: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    new_rows = [rows[0]]
    found=False

    for row in rows[1:]:
        if (row[0]==str(table_no)) and (row[1]=="Booked") and (row[3]==date) and (row[4]==str(time)):
            new_rows.append(row.copy())
            row[1],row[2],row[3],row[4],row[5]="Available","--","--","--","--"
            found=True

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("Reservation: ")
        print(tabulate(new_rows,headers="firstrow",tablefmt="grid"))
    else:
        print("Reservation not found.")


def table_reservation():
    create_file()
    while True:
        print("\n========== TABLE RESERVATION ==========")
        print("1. View Tables")
        print("2. Reserve Table")
        print("3. Cancel Reservation")
        print("4. Back to Dashboard")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_table()

        elif choice == "2":
            reserve_table()

        elif choice == "3":
            cancel_reservation()

        elif choice == "4":
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    table_reservation()
