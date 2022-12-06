"""Explicit main execution module."""

from inventory_app import InventoryApp


def main():
    # start app
    home_inventory_app_2 = InventoryApp()
    home_inventory_app_2.run_program()



    # Call main() if this is the main execution module
    if __name__ == '__main__':
        main()