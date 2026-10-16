from Madhav_main import menu_management
from Ayush_order import order_management
from Atif_table import table_reservation
from Manichandra_billing import billing


def main():
    print("\n==============================================")
    print("       WELCOME TO RESTAURANT MANAGEMENT")
    print("==============================================")

    while True:
        print("\n============== DASHBOARD ==============")
        print("1. Menu Management")
        print("2. Order Management")
        print("3. Table Reservation")
        print("4. Billing")
        print("5. Exit")

        choice = input("\nEnter your task: ")

        if choice == "1":
            menu_management()

        elif choice == "2":
            order_management()

        elif choice == "3":
            table_reservation()

        elif choice == "4":
            billing()

        elif choice == "5":
            print("\nThank you for using the Restaurant Management System!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
