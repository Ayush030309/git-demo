from Madhav_menu import (
    view_menu,
    add_menu_item,
    update_menu_item,
    delete_menu_item,
    toggle_availability
)


def menu_management():
    while True:
        print("\n================================")
        print("        MENU MANAGEMENT")
        print("================================")
        print("1. View Menu")
        print("2. Add Menu Item")
        print("3. Update Menu Item")
        print("4. Delete Menu Item")
        print("5. Toggle Availability")
        print("6. Back to Dashboard")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_menu()

        elif choice == "2":
            name = input("Enter item name: ")
            category = input("Enter category: ")
            food_type = input("Enter type (Veg/Non-Veg): ")
            price = input("Enter price: ")

            add_menu_item(name, category, food_type, price)

        elif choice == "3":
            item_id = input("Enter item ID: ")

            print("\nWhat do you want to update?")
            print("1. Name")
            print("2. Category")
            print("3. Type")
            print("4. Price")

            option = input("Enter choice: ")

            if option == "1":
                field = "name"
            elif option == "2":
                field = "category"
            elif option == "3":
                field = "type"
            elif option == "4":
                field = "price"
            else:
                print("Invalid choice!")
                continue

            new_value = input("Enter new value: ")
            update_menu_item(item_id, field, new_value)

        elif choice == "4":
            item_id = input("Enter item ID: ")
            delete_menu_item(item_id)

        elif choice == "5":
            item_id = input("Enter item ID: ")
            toggle_availability(item_id)

        elif choice == "6":
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    menu_management()
