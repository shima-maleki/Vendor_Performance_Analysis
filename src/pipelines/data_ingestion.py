"""
This module defines the IngestionPipeline class to read CSV files from a specified
directory and ingest them into a SQL database using SQLAlchemy.
"""

import os
import time
import logging
import pandas as pd
from sqlalchemy.engine.base import Engine
from infrastructure.mysql_connection import get_sql_database
from config import DATA_DIRECTORY


class IngestionPipeline:
    """
    A class to handle the ingestion of CSV files into a SQL database.

    Attributes:
        data_dir (str): Path to the directory containing raw CSV files.
        engine (Engine): SQLAlchemy engine for connecting to the database.
        log_file (str): Path to the log file.
    """

    def __init__(self, data_dir: str, engine: Engine, log_file: str = "src/logs/ingestion_db.log") -> None:
        """
        Initializes the IngestionPipeline with the data directory and database engine.

        Args:
            data_dir (str): Directory containing the CSV files.
            engine (Engine): SQLAlchemy engine object.
            log_file (str): Path to the log file. Default is 'logs/ingestion_db.log'.
        """
        self.data_dir = data_dir
        self.engine = engine
        self._setup_logger(log_file)

    def _setup_logger(self, log_file: str) -> None:
        """
        Set up logging configuration.

        Args:
            log_file (str): Path to the log file.
        """
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            filemode="a"
        )

    def _ingest_to_db(self, df: pd.DataFrame, table_name: str) -> None:
        """
        Save a pandas DataFrame into the database.

        Args:
            df (pd.DataFrame): The DataFrame to be ingested.
            table_name (str): The table name in the database.
        """
        try:
            df.to_sql(table_name, con=self.engine, if_exists='replace', index=False)
            logging.info(f"✅ Successfully ingested '{table_name}' into the database.")
        except Exception as e:
            logging.error(f"❌ Failed to ingest '{table_name}': {e}")

    def run(self) -> None:
        """
        Executes the ingestion pipeline by loading all CSV files from the data directory
        and storing them into the database.
        """
        start_time = time.time()

        if not os.path.exists(self.data_dir):
            logging.error(f"❌ Data directory '{self.data_dir}' does not exist.")
            return

        for file_name in os.listdir(self.data_dir):
            if file_name.endswith('.csv'):
                file_path = os.path.join(self.data_dir, file_name)
                try:
                    df = pd.read_csv(file_path)
                    table_name = os.path.splitext(file_name)[0]
                    self._ingest_to_db(df, table_name)
                except Exception as e:
                    logging.error(f"❌ Error loading {file_name}: {e}")

        elapsed = (time.time() - start_time) / 60
        logging.info(f"⏱️ Ingestion completed in {elapsed:.2f} minutes.")

if __name__ == "__main__":
    engine = get_sql_database()
    pipeline = IngestionPipeline(data_dir=DATA_DIRECTORY, engine=engine)
    pipeline.run()