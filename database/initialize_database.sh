#!/bin/bash

# create logs directory if not there
echo 'Creating logs directory if it does not already exist...'
mkdir -p logs
echo 'Deleting old log files if they exist...'
rm -f logs/*

d=$(date)
echo $d

# Create Database
echo "Running DB Scripts..."
echo  $d': Dropping database...' | tee -a logs/drop_database.log
mysql < dbfiles/drop_database.sql 2>&1 | tee -a logs/drop_database.log
echo $d': Dropping user...' | tee -a logs/drop_user.log
mysql < dbfiles/drop_user.sql 2>&1 | tee -a logs/drop_user.log
echo $d': Creating database...' | tee -a logs/create_database.log
mysql < dbfiles/create_database.sql 2>&1 | tee -a logs/create_database.log
echo $d': Creating user...' | tee -a logs/create_user.log
mysql < dbfiles/create_user.sql 2>&1 | tee -a logs/create_user.log
echo $d': Creating tables...' | tee -a logs/create_table_inventories.log
mysql < dbfiles/create_table_inventories.sql 2>&1 | tee -a logs/create_table_inventories.log
echo  $d': Inserting inventory row...' | tee -a logs/insert_inventory_row.log
mysql < dbfiles/insert_inventory_row.sql 2>&1 | tee -a logs/insert_inventory_row.log
echo  $d': Adding items table...' | tee -a logs/create_items_table.log
mysql < dbfiles/create_items_table.sql 2>&1 | tee -a logs/create_items_table.log
echo $d': Inserting test data...' | tee -a logs/insert_test_data.log
mysql < dbfiles/insert_test_data.sql 2>&1 | tee -a logs/insert_test_data.log





