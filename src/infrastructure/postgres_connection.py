import os
import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

from dotenv import load_dotenv

# load environment variables
load_dotenv()

# get connection details 
USER_NAME = os.getenv("pg_username")
PASSWORD = os.getenv("pg_password")
HOST = os.getenv("pg_hostname")
PORT = os.getenv("pg_port")  # default for Postgres is 5432
DATABASE_NAME = os.getenv("pg_database")


class PostgresConnector:
    """
    A class to establish a connection with a PostgreSQL cloud database using SQLAlchemy.

    Attributes:
        username (str): Username for the PostgreSQL database.
        password (str): Password for the PostgreSQL database.
        host (str): Hostname or IP address of the PostgreSQL server.
        port (int): Port number of the PostgreSQL server (default: 5432).
        database (str): Name of the database to connect to.
    """

    def __init__(self, username: str, password: str, host: str, database: str, port: int = 5432) -> None:
        """
        Initializes the PostgresConnector instance with required credentials.

        Args:
            username (str): PostgreSQL username.
            password (str): PostgreSQL password.
            host (str): PostgreSQL host URL or IP address.
            database (str): Name of the database.
            port (int, optional): Port number (default is 5432).
        """
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.engine = None

    def connect(self) -> Engine:
        """
        Establishes a connection to the PostgreSQL database.

        Returns:
            sqlalchemy.engine.Engine: SQLAlchemy engine object if connection is successful.

        Raises:
            Exception: If connection fails.
        """
        try:
            connection_uri = (
                f"postgresql+psycopg2://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
            )
            self.engine = create_engine(connection_uri)

            # Test the connection
            with self.engine.connect() as connection:
                print("✅ Successfully connected to the PostgreSQL cloud database.")

            return self.engine

        except Exception as error:
            print("❌ Failed to connect to the database.")
            print("Error:", error)
            return None


# Get an instance of PostgreSQL database

def get_sql_database(username: str = USER_NAME, 
                    password: str = PASSWORD, 
                    host: str = HOST, 
                    database: str = DATABASE_NAME,
                    port: int = PORT):
    """
    Creates a connection to a PostgreSQL database using the PostgresConnector class.

    Args:
        username (str): Username for the PostgreSQL database.
        password (str): Password for the PostgreSQL database.
        host (str): Hostname or IP address of the PostgreSQL server.
        database (str): Name of the database to connect to.
        port (int, optional): Port number for the PostgreSQL server.

    Returns:
        sqlalchemy.engine.Engine: A SQLAlchemy engine object if connection is successful, otherwise None.
    """
    if port is None:
        port = 5432  # default postgres port

    connector = PostgresConnector(
        username=username,
        password=password,
        host=host,
        database=database,
        port=port
    )

    engine = connector.connect()
    return engine


if __name__ == "__main__":
    engine = get_sql_database()
