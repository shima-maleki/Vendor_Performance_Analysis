# Data Information

This section provides an overview of the tables used in this project, informing stakeholders about the data's nature, volume, and its significance for our analysis.

## 1. `begin_inventory`

*   **What it is:** This table captures a snapshot of the inventory levels for each product at every store at the beginning of the period.
*   **How much data:** It contains **206529  rows** and **9 columns**.
*   **What it tells us & Usefulness:** It provides a baseline for our inventory. This is crucial for calculating key metrics like inventory turnover and identifying stock levels at the start. It helps in understanding the initial stock position before any purchases or sales in the period under review.

## 2. `end_inventory`

*   **What it is:** This table is a snapshot of the inventory levels for each product at every store at the end of the period.
*   **How much data:** It contains **224489  rows** and **9 columns**.
*   **What it tells us & Usefulness:** This data is essential for calculating the cost of goods sold (COGS) and assessing the value of unsold inventory at the period's close. Comparing it with the beginning inventory and sales data helps in identifying discrepancies and understanding inventory flow.

## 3. `purchase_prices`

*   **What it is:** This table lists the purchase price for each product from its respective vendor.
*   **How much data:** It contains **12261 rows** and **9 columns**.
*   **What it tells us & Usefulness:** This is a critical reference table. It allows us to calculate the cost of purchases, gross profit margins, and analyze the cost structure of our products. It links products to their vendors and acquisition costs.

## 4. `purchases`

*   **What it is:** This table contains transactional records of all purchases made from vendors during the period.
*   **How much data:** It contains **2372474 rows** and **16 columns**.
*   **What it tells us & Usefulness:** It provides detailed data on purchase volume, cost, and timing. This information is fundamental for analyzing vendor performance, understanding procurement patterns, and managing cash flow related to purchasing.

## 5. `vendor_invoice`

*   **What it is:** This table holds the details of invoices received from vendors for the purchases made.
*   **How much data:** It contains **5543  rows** and **9 columns**.
*   **What it tells us & Usefulness:** It's used for financial reconciliation, tracking payments, and verifying the purchase transactions recorded in the `purchases` table. It also provides information on freight costs associated with invoices.

## 6. `sales`

*   **What it is:** This table contains transactional records of all sales made to customers.
*   **How much data:** It contains **12825363 rows** and **15 columns**.
*   **What it tells us & Usefulness:** This is the primary source for analyzing sales performance. It allows us to calculate total revenue, sales volume, and profitability by product, store, and vendor. Understanding sales patterns is key to making strategic business decisions.

"""