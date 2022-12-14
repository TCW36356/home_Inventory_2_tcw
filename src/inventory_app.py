"""Implements inventory application presentation layer (U/I) features."""

from business_logic import BusinessLogic
from prettytable import PrettyTable
from datetime import date
import json
import time
import os

class InventoryApp():
	"""Implements household inventory control features."""

	def __init__(self):
		"""Initialize object."""
		# Constants
		self.NEW_INVENTORY='1'
		self.LIST_INVENTORIES='2'
		self.SELECT_INVENTORY='3'
		self.LIST_INVENTORY_ITEMS='4'
		self.ADD_ITEMS='5'
		self.FIND_ITEMS='6'
		self.SAVE_TO_FILE='7'
		self.EXIT='8'
		# Fields
		self.menu_choice = 1
		self.keep_going = True
		self.business_logic = BusinessLogic()
		self.active_inventory_id = 0

	def clear_screen(self):
		"""Clears the screen. It's either Unix-like or Windows."""
		try:
			os.system('clear')
		except Exception:
			os.system('cls')

	def display_menu(self):
		"""Display menu."""
		print('\t\t\tHousehold Inventory Application')
		print()
		print('\t\t1. New Inventory')
		print('\t\t2. List Inventories')
		print('\t\t3. Select Inventory')
		print('\t\t4. List Inventory Items')
		print('\t\t5. Add Items')
		print('\t\t6. Search Current Inventory')
		print('\t\t7. Save Inventory to File')
		print('\t\t8. Exit')
		print()

	def process_menu_choice(self):
		"""Process menu choice and execute corrensponding methods."""
		self.menu_choice = input('Please enter menu item number: ')
		if __debug__: 
			print(f'You entered: {self.menu_choice}')
		match self.menu_choice:
			case self.NEW_INVENTORY:
				self.new_inventory()
			case self.LIST_INVENTORIES:
				self.list_inventories()
			case self.SELECT_INVENTORY:
				self.select_inventory()
			case self.LIST_INVENTORY_ITEMS:
				self.list_inventory_items()
			case self.ADD_ITEMS:
				self.add_items()
			case self.FIND_ITEMS:
				self.find_item()
			case self.SAVE_TO_FILE:
				self.save_to_file()
			case self.EXIT:
				if __debug__:
					print('Goodbye!')
				self.keep_going = False
				self.clear_screen
			case _:
				print('Invalid Menu Choice!')

	def new_inventory(self): #create new row in inventory table - INSERT function. should include return inventory_id
		"""Create new inventory."""		
		self.clear_screen()
		if __debug__:
			print('new_inventory() method called...')
		
		name = None
		description = None
		curr_time = time.strftime("%H:%M:%S", time.localtime())
		tdate = (str(date.today()) + ' ' + curr_time)
		try:
			keep_going = True
			while keep_going:
				name = str(input('What would you like to call the inventory? Please enter a name: '))
				description = str(input('What is inside? Please enter a description: '))
				self.business_logic.create_new_inventory(name, description, tdate)
				response = input('New inventory created! Press any key to continue: ')
				if response != None:
					keep_going = False
		except Exception as e:
			print(f'Exception in new_inventory() method: {e}')

		

	def list_inventories(self):
		"""List inventories."""
		self.clear_screen()
		if __debug__:
			print('list_inventories() method called...')
		self.print_inventory_list(self._get_inventories())
		input('\n\nPress any key to continue...')
			

	def _get_inventories(self):
		"""Utility method that calls business logic layer to get all inventory records."""
		return self.business_logic.get_all_inventories()


		
	def select_inventory(self):
		"""Selects an existing inventory"""
		self.clear_screen()
		if __debug__:
			print('select_inventory() method called.')

		inventory_list = None
		try:
			inventory_list = self._get_inventories()
			keep_going = True
			while keep_going:
				self.print_inventory_list(inventory_list)
				self.active_inventory_id = int(input('\n\nSelect inventory id from list: '))
				response = input(f'You entered {str(self.active_inventory_id)}. Is this correct? (y/n) ')
				if response.capitalize() == 'Y':
					keep_going = False
		except Exception as e:
			print(f'Exception in select_inventory() method: {e}')
			

	def list_inventory_items(self):
		"""List inventory items for inventory id contained in self.active_inventory_id field."""
		self.clear_screen()
		if __debug__:
			print('list_inventory_items() method called...')
		items_list = self.business_logic.get_items_for_inventory_id(self.active_inventory_id)
		self.print_items_list(items_list)
		input('\n\nPress any key to continue...')
		

	def add_items(self):
		"""Add items to inventory."""
		self.clear_screen()
		if __debug__:
			print('add_items() method called...')
		
		inventory_id = self.active_inventory_id
		item = None
		count = None
		try:
			keep_going = True
			if inventory_id == 0:
				input('Please select an inventory first. Press any key to continue: ')
				keep_going = False
			else:
				while keep_going:
					item = str(input('What would you like to add? Please enter the name of the item: '))
					count = int(input('How many would you like to add? Please enter a number: '))
					self.business_logic.add_item(inventory_id, item, count)
					response = input('\n\nItem added! Would you like to add another? (y/n) ')
					if response.capitalize() == 'Y':
						self.clear_screen()
					else:	
						keep_going = False
		except Exception as e:
			print(f'Exception in add_items() method: {e}')

	def find_item(self):
		"""Search current inventory for an item."""
		self.clear_screen()
		if __debug__:
			print('find_items() method called...')
		inventory_id = self.active_inventory_id
		try:
			keep_going = True
			if inventory_id == 0:
				input('Please select an inventory first. Press any key to continue: ')
				keep_going = False
			while keep_going == True:
				where_is = input('What are you looking for: ')
				result = self.business_logic.find_item(where_is)
				if result == []:
					print(where_is + ' is not in the selected inventory.')
					input('\n\nPress any key to continue...')
					keep_going = False
				else:
					results = result[0]
					if results[1] == inventory_id:
						if results[3] == 1:
							print('There is one ' + results[2] + ' in the inventory.')
							response = input('\n\nPress any key to continue...')
							if response != None:
								keep_going = False
						else:
							print('There are ' + str(results[3]) + ' ' + results[2] + ' in the inventory.')
							input('\n\nPress any key to continue...')
							if response != None:
								keep_going = False
					else:
						print('That\'s not in there. Sorry!')
			

		except Exception as e:
			print(f'Exception in find_item() method: {e}')


	def save_to_file(self):
		"""Save all inventories and items to file in json format."""
		if __debug__:
			print('save_to_file() method called...')
		if self.active_inventory_id != None:
			try:
				file_path = self._retrieve_file_path()
				with open(file_path, 'w', encoding='UTF-8') as f:
					f.write(self.business_logic.get_all_inventories_with_format('json'))
					f.write(self.business_logic.get_all_items_with_format('json'))
			except Exception as e:
				print(f'Exception in save_to_file() method: {e}')

	def run_program(self):
		"""Start the applications."""
		while self.keep_going:
			self.clear_screen()
			self.display_menu()
			self.process_menu_choice()
			
					
	def print_inventory_list(self, inventory_list):
		t = PrettyTable(['ID', 'Name', 'Description', 'Date'])
		for row in inventory_list:
			t.add_row([row[0], row[1], row[2], row[3]])
		print(t)

	def print_items_list(self, items_list):
		t = PrettyTable(['ID', 'Inventory ID', 'Item', 'Count'])
		for row in items_list:
			t.add_row([row[0], row[1], row[2], row[3]])
		print(t)

	def _retrieve_file_path(self):
		"""Method to create a file path in which to save the inventory."""
		save_where = input("Please enter the path and filename: ")
		return save_where


		


