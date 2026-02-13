import os
import pandas as pd 
import sqlite3 
from database import DataManager
from dotenv import load_dotenv

# RBA Login system using the admin's and creator passwords


class ManagementSystem(DataManager):
    def __init__(self, db_name):
        super().__init__(db_name) 
        
    def display_table(self):
        name = input("Enter the table name to display: ")
        super().display_table(name)

if __name__ == "__main__":
    load_dotenv() 
    db_path = os.getenv('DB_PATH') 
    
    if db_path is None:
        print("Error: 'DB_PATH' not found in .env file")
    elif not os.path.exists(db_path):
        print(f"Error: Could not find database file at: {os.path.abspath(db_path)}")
    else:
        app = ManagementSystem(db_path)
        app.display_table()