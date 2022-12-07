"""Explicit main execution module."""

from inventory_app import InventoryApp


def main():
    # start app
    appli = InventoryApp()
    appli.run_program()



    # Call main() if this is the main execution module
    if __name__ == '__main__':
        main()