# Importing required modules
from tabulate import tabulate
import os


# Class Definition
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return (
            f"{self.country}, {self.code}, {self.product}, "
            f"{self.cost}, {self.quantity}"
        )


# Global list to store Shoe objects
shoes_list = []


# Function Definitions
def read_shoes_data(file_path):
    """
    Reads inventory file into `shoes_list` as `Shoe` objects.
    """
    try:
        with open(file_path, 'r') as file:
            next(file)  # Skip header
            for line in file:
                data = line.strip().split(",")
                if len(data) == 5:
                    shoes_list.append(Shoe(*data))
    except FileNotFoundError:
        print("Error: Inventory file not found!")
    except Exception as e:
        print(f"Error reading file: {e}")


def capture_shoes():
    """
    Captures user input to create a new Shoe object and adds it to shoes_list.
    """
    country = input("Enter country: ")
    code = input("Enter shoe code: ")
    product = input("Enter product name: ")
    cost = float(input("Enter cost: "))
    quantity = int(input("Enter quantity: "))
    shoe = Shoe(country, code, product, cost, quantity)
    shoes_list.append(shoe)
    print("Shoe captured successfully!")


def view_all():
    """
    Displays all Shoe objects in a tabulated format.
    """
    if shoes_list:
        table = [
            [shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity]
            for shoe in shoes_list
        ]
        print(
            tabulate(
                table,
                headers=["Country", "Code", "Product", "Cost", "Quantity"],
                tablefmt="grid",
            )
        )
    else:
        print("No shoes in the inventory.")


def re_stock(file_path):
    """
    Finds the shoe with the lowest quantity, restocks it, updates the file.
    """
    if not shoes_list:
        print("Inventory is empty!")
        return
    shoe = min(shoes_list, key=lambda x: x.quantity)
    print(f"Lowest stock: {shoe.product} with quantity {shoe.quantity}")
    additional_stock = int(input("Enter quantity to restock: "))
    shoe.quantity += additional_stock
    print("Stock updated!")
    update_file(file_path)


def search_shoe():
    """
    Searches for a shoe by its code and displays the details.
    """
    code = input("Enter the shoe code to search: ")
    for shoe in shoes_list:
        if shoe.code == code:
            print(shoe)
            return
    print("Shoe not found.")


def value_per_item():
    """
    Calculates and displays the total value of each shoe item.
    """
    for shoe in shoes_list:
        value = shoe.cost * shoe.quantity
        print(f"{shoe.product}: Total Value = {value}")


def highest_qty():
    """
    Finds and displays the shoe with the highest quantity.
    """
    if not shoes_list:
        print("Inventory is empty!")
        return
    shoe = max(shoes_list, key=lambda x: x.quantity)
    print(f"Shoe with the highest quantity: {shoe.product} ({shoe.quantity})")


def update_file(file_path):
    """
    Updates the inventory file with the current state of shoes_list.
    """
    try:
        with open(file_path, 'w') as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoes_list:
                file.write(
                    f"{shoe.country},{shoe.code},{shoe.product},"
                    f"{shoe.cost},{shoe.quantity}\n"
                )
    except Exception as e:
        print(f"Error updating file: {e}")


# Main menu
def main_menu(file_path):
    """
    Main menu that drives the program and allows user interaction.
    """
    read_shoes_data(file_path)
    while True:
        print("\n--- Nike Warehouse Menu ---")
        print("1. View all shoes")
        print("2. Capture new shoe")
        print("3. Re-stock lowest quantity")
        print("4. Search shoe by code")
        print("5. Calculate value per item")
        print("6. Find highest quantity shoe")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            view_all()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            re_stock(file_path)
        elif choice == "4":
            search_shoe()
        elif choice == "5":
            value_per_item()
        elif choice == "6":
            highest_qty()
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")


# File path for inventory
directory = os.path.dirname(__file__)
file_path = os.path.join(directory, "inventory.txt")

# Run the program
if __name__ == "__main__":
    main_menu(file_path)
