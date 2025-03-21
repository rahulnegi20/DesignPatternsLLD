
"""
In Python, we can implement the Singleton Pattern by overriding the class’s __new__ method, 
which controls object creation. We also store the instance as a class variable to ensure there is only one instance.
"""
class DatabaseConnection:
    _instance = None  # Class variable to store the singleton instance

    def __new__(cls):
        if cls._instance is None:
            print("Creating the single instance of DatabaseConnection")
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            # Initialize any other instance-specific variables here
            cls._instance.connection = cls._create_connection()
            cls._instance.is_connected = True
        return cls._instance

    @staticmethod
    def _create_connection():
        # Simulate establishing a database connection
        return "Database connection established"

    def get_connection(self):
        if not self.is_connected:
            # Re-establish the connection if it has been closed
            self.connection = self._create_connection()
            self.is_connected = True
            print("Re-established the database connection.")
        return self.connection

    def close_connection(self):
        if self.is_connected:
            print("Closing the database connection.")
            # Simulate closing the database connection
            self.connection = None
            self.is_connected = False
        else:
            print("Connection is already closed.")


# USAGE

# Attempt to create multiple connections
db1 = DatabaseConnection()
print("Connection from db1:", db1.get_connection())

db2 = DatabaseConnection()
print("Connection from db2:", db2.get_connection())

# Check if both instances are indeed the same
print("Are db1 and db2 the same instance?", db1 is db2)
