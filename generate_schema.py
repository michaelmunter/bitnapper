import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()
mysql_pw = os.getenv('MYSQL_PW')
mysql_user = os.getenv('MYSQL_USER')
mysql_host = os.getenv('MYSQL_HOST')


def generate_schema(single_entry_keys, table_headers):
    # Connect to MySQL
    db = mysql.connector.connect(
        user=mysql_user, password=mysql_pw, host=mysql_host)
    cursor = db.cursor()

    # Create a new database
    cursor.execute("CREATE DATABASE IF NOT EXISTS BitNapper")

    # Switch to the new database
    cursor.execute("USE BitNapper")

    # Create tables for single entries
    for key in single_entry_keys:
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {key} (id INT AUTO_INCREMENT PRIMARY KEY, value TEXT)"
        cursor.execute(create_table_sql)

    # Create tables based on table headers
    for table in table_headers:
        columns = ', '.join([f"{header} TEXT" for header in table['headers']])
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {table['name']} (id INT AUTO_INCREMENT PRIMARY KEY, {columns})"
        cursor.execute(create_table_sql)

    db.commit()
    cursor.close()
    db.close()
    print("Schema generated successfully")


# Example Usage
single_entry_keys = ['key1', 'key2', 'key3']
table_headers = [{'name': 'table1', 'headers': ['col1', 'col2']}, {
    'name': 'table2', 'headers': ['col1', 'col2']}]

generate_schema(single_entry_keys, table_headers)
