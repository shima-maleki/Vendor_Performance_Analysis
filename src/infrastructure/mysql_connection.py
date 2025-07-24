import os
import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

from dotenv import load_dotenv

# load enviornment variables
load_dotenv()

# get connection details 
USER_NAME = os.getenv("user_name")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DATABASE_NAME = os.getenv("database_name")


class MySQLConnector:
    """
    A class to establish a connection with a MySQL cloud database using SQLAlchemy.

    Attributes:
        username (str): Username for the MySQL database.
        password (str): Password for the MySQL database.
        host (str): Hostname or IP address of the MySQL server.
        port (int): Port number of the MySQL server (default: 3306).
        database (str): Name of the database to connect to.
    """

    def __init__(self, username: str, password: str, host: str, database: str, port: int = 3306) -> None:
        """
        Initializes the MySQLConnector instance with required credentials.

        Args:
            username (str): MySQL username.
            password (str): MySQL password.
            host (str): MySQL host URL or IP address.
            database (str): Name of the database.
            port (int, optional): Port number (default is 3306).
        """
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.engine = None

    def connect(self) -> Engine:
        """
        Establishes a connection to the MySQL database.

        Returns:
            sqlalchemy.engine.Engine: SQLAlchemy engine object if connection is successful.

        Raises:
            Exception: If connection fails.
        """
        try:
            connection_uri = (
                f"mysql+pymysql://{self.username}:{self.password}@"
                f"{self.host}:{self.port}/{self.database}"
            )
            self.engine = create_engine(connection_uri)

            # Test the connection
            with self.engine.connect() as connection:
                print("✅ Successfully connected to the MySQL cloud database.")

            return self.engine

        except Exception as error:
            print("❌ Failed to connect to the database.")
            print("Error:", error)
            return None


# Get an instant of myswl database

def get_sql_database(username: str = USER_NAME, 
                    password: str = PASSWORD, 
                    host: str = HOST, 
                    database: str = DATABASE_NAME):
    """
    Creates a connection to a MySQL database using the MySQLConnector class.

    Args:
        username (str): Username for the MySQL database.
        password (str): Password for the MySQL database.
        host (str): Hostname or IP address of the MySQL server.
        database (str): Name of the database to connect to.

    Returns:
        sqlalchemy.engine.Engine: A SQLAlchemy engine object if connection is successful, otherwise None.
    """
    connector = MySQLConnector(
        username=username,
        password=password,
        host=host,
        database=database
    )

    engine = connector.connect()
    return engine

if __name__ == "__main__":
    engine = get_sql_database()