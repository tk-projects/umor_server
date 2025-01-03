import sqlite3
import os

# Define the directory for storing databases
DATABASE_DIR = os.path.expanduser("~/databases")

def create_customer_db(customer_id):
    """
    Creates a new SQLite database for a specific customer.
    """
    # Ensure the database directory exists
    os.makedirs(DATABASE_DIR, exist_ok=True)
    
    # Path for the customer's database
    db_path = os.path.join(DATABASE_DIR, f"{customer_id}.db")
    
    if os.path.exists(db_path):
        print(f"Database for customer '{customer_id}' already exists.")
        return

    # Create the database and the measurements table
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS measurements (
            measurement_id INTEGER PRIMARY KEY AUTOINCREMENT,
            node_id INTEGER NOT NULL,
            time TEXT NOT NULL,
            humidity_sensor1 REAL,
            temperature_sensor1 REAL,
            humidity_sensor2 REAL,
            temperature_sensor2 REAL,
            battery_voltage REAL,
            error_code TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print(f"Database for customer '{customer_id}' created successfully at {db_path}.")

# Example: Create databases for customer1 and customer2
if __name__ == "__main__":
    create_customer_db("customer1")
    create_customer_db("customer2")
