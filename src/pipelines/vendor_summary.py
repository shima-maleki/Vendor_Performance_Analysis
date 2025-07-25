import os
import pandas as pd
import logging
from sqlalchemy.engine import Engine
from infrastructure.postgres_connection import get_sql_database  


os.makedirs(os.path.dirname("logs/get_vendor_summary.log"), exist_ok=True)

logging.basicConfig(
    filename="logs/get_vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

class VendorDataPipeline:
    """
    Pipeline class to create, clean, and ingest vendor sales summary data.

    Attributes:
        conn (sqlalchemy.engine.Engine): SQLAlchemy engine connected to PostgreSQL.
    """

    def __init__(self, db_path: str = None):
        """
        Initialize the pipeline and create PostgreSQL engine connection.

        Args:
            db_path (str): Not used here, kept for interface compatibility.
        """
        self.conn: Engine = get_sql_database()

    def create_vendor_summary(self) -> pd.DataFrame:
        """
        Generate a vendor-wise sales and purchase summary dataframe
        by merging relevant tables with aggregations.

        Returns:
            pd.DataFrame: Vendor sales summary data.
        """
        query = """
        WITH FreightSummary AS (
            SELECT 
                "VendorNumber", 
                SUM("Freight") AS "FreightCost" 
            FROM my_schema.vendor_invoice 
            GROUP BY "VendorNumber"
        ), 

        PurchaseSummary AS (
            SELECT 
                p."VendorNumber",
                p."VendorName",
                p."Brand",
                p."Description",
                p."PurchasePrice",
                pp."Price" AS "ActualPrice",
                pp."Volume",
                SUM(p."Quantity") AS "TotalPurchaseQuantity",
                SUM(p."Dollars") AS "TotalPurchaseDollars"
            FROM my_schema.purchases p
            JOIN my_schema.purchase_prices pp
                ON p."Brand" = pp."Brand"
            WHERE p."PurchasePrice" > 0
            GROUP BY p."VendorNumber", p."VendorName", p."Brand", p."Description", p."PurchasePrice", pp."Price", pp."Volume"
        ), 

        SalesSummary AS (
            SELECT 
                "VendorNo",
                "Brand",
                SUM("SalesQuantity") AS "TotalSalesQuantity",
                SUM("SalesDollars") AS "TotalSalesDollars",
                SUM("SalesPrice") AS "TotalSalesPrice",
                SUM("ExciseTax") AS "TotalExciseTax"
            FROM my_schema.sales
            GROUP BY "VendorNo", "Brand"
        ) 

        SELECT 
            ps."VendorNumber",
            ps."VendorName",
            ps."Brand",
            ps."Description",
            ps."PurchasePrice",
            ps."ActualPrice",
            ps."Volume",
            ps."TotalPurchaseQuantity",
            ps."TotalPurchaseDollars",
            ss."TotalSalesQuantity",
            ss."TotalSalesDollars",
            ss."TotalSalesPrice",
            ss."TotalExciseTax",
            fs."FreightCost"
        FROM PurchaseSummary ps
        LEFT JOIN SalesSummary ss 
            ON ps."VendorNumber" = ss."VendorNo" 
            AND ps."Brand" = ss."Brand"
        LEFT JOIN FreightSummary fs 
            ON ps."VendorNumber" = fs."VendorNumber"
        ORDER BY ps."TotalPurchaseDollars" DESC
        """

        try:
            df = pd.read_sql_query(query, self.conn)
            logging.info(f"Vendor summary created with {len(df)} records.")
            return df
        except Exception as e:
            logging.error(f"Error creating vendor summary: {e}")
            raise

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean the vendor sales summary dataframe by fixing datatypes,
        handling missing values, trimming whitespace, and adding new analytical columns.

        Args:
            df (pd.DataFrame): Raw vendor summary dataframe.

        Returns:
            pd.DataFrame: Cleaned vendor summary dataframe.
        """
        try:
            # Convert 'Volume' to float
            df['Volume'] = df['Volume'].astype(float)

            # Fill missing values with 0
            df.fillna(0, inplace=True)

            # Strip whitespace from categorical columns if they exist
            if 'VendorName' in df.columns:
                df['VendorName'] = df['VendorName'].astype(str).str.strip()
            if 'Description' in df.columns:
                df['Description'] = df['Description'].astype(str).str.strip()

            # Create new analytical columns
            df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']
            df['ProfitMargin'] = (df['GrossProfit'] / df['TotalSalesDollars'].replace(0, 1)) * 100
            df['StockTurnover'] = df['TotalSalesQuantity'] / df['TotalPurchaseQuantity'].replace(0, 1)  # avoid div by zero
            df['SalesToPurchaseRatio'] = df['TotalSalesDollars'] / df['TotalPurchaseDollars'].replace(0, 1)

            logging.info("Data cleaning completed successfully.")
            return df

        except Exception as e:
            logging.error(f"Error cleaning data: {e}")
            raise

    def ingest_db(self, df: pd.DataFrame, table_name: str):
        """
        Ingest a DataFrame into the specified PostgreSQL database table.

        Args:
            df (pd.DataFrame): DataFrame to ingest.
            table_name (str): Destination table name in the database.
        """
        try:
            df.to_sql(table_name, con=self.conn, if_exists='replace', index=False, schema='my_schema')
            logging.info(f"Data ingested into table '{table_name}' successfully.")
        except Exception as e:
            logging.error(f"Error ingesting data into database: {e}")
            raise

    def run_pipeline(self):
        """
        Run the complete data pipeline: create summary, clean data,
        and ingest the cleaned data back into the database.
        """
        try:
            summary_df = self.create_vendor_summary()
            clean_df = self.clean_data(summary_df)
            self.ingest_db(clean_df, 'vendor_sales_summary')
            logging.info("Vendor data pipeline completed successfully.")
        except Exception as e:
            logging.error(f"Pipeline failed: {e}")
            raise


if __name__ == "__main__":
    pipeline = VendorDataPipeline()
    pipeline.run_pipeline()
