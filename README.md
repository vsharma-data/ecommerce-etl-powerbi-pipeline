# E-Commerce ETL Pipeline & Executive Analytics

An end-to-end data engineering and business intelligence solution that ingests transactional retail data via REST APIs, normalizes nested data models into a staged SQLite database, and delivers high-impact executive KPIs in Power BI.

---

## Architecture & Data Workflow
[ REST API (FakeStore) ]
│
▼
[ Python ETL Layer ] ──────► JSON Normalization & Schema Cleaning
│
▼
[ SQLite Staging DB ] ─────► Fact & Dimension Table Storage
│
▼
[ Power BI Data Engine ] ──► 1:N Star Schema & Custom DAX Measures
│
▼
[ Executive Dashboard ] ───► Dynamic Cross-Filtering & Margin Analytics


## Tech Stack & Methodology

* *Data Ingestion (Python - requests)*
  Automated REST API extraction handling multi-endpoint pagination and raw payload retrieval.

* *Data Transformation (Python - pandas)*
  Normalized nested JSON objects (rating) into flat relational dataframes and handled data typing.

* *Database Staging (SQLite - sqlite3)*
  Modeled and staged relational tables (dim_products, fact_orders) in an SQLite environment.

* *Data Modeling (Power BI)*
  Enforced 1:N Star Schema relationships between core dimension and fact tables.

* *Analytics Engine (DAX)*
  Engineered custom row-level and aggregate metrics utilizing SUMX, RELATED, and DIVIDE functions.

## Key Metrics & DAX Analytics

- *Total Revenue*
  Total Revenue = SUMX('fact_orders', 'fact_orders'[quantity] * RELATED('dim_products'[price]))

- *Total Orders*
  Total Orders = DISTINCTCOUNT('fact_orders'[order_id])

- *Total Units Sold*
  Total Units Sold = SUM('fact_orders'[quantity])

- *Average Order Value (AOV)*
  Average Order Value = DIVIDE([Total Revenue], [Total Orders], 0)

## Business Value & Operational Impact

* *Inventory Replenishment Strategy*
  Provides visibility into top-performing categories (e.g., Men's Clothing) and high-volume SKUs to optimize stock levels and prevent stockout revenue loss.

* *Product Rationalization & Pricing*
  Identifies underperforming items and low-rated products (rating score below 2.5) to inform targeted clearance sales, discounting, or supplier contract renegotiation.

* *Executive Basket Analysis*
  Delivers real-time tracking of Average Order Value (AOV) and category revenue share, helping management design cross-selling and bundling campaigns to maximize ticket size.


  ## How to Run Locally

### Prerequisites
- Python 3.9+ installed
- Power BI Desktop installed

### Step-by-Step Setup

1. *Clone the Repository*
   ```bash
   git clone [https://github.com/vsharma-data/ecommerce-etl-powerbi-pipeline.git](https://github.com/vsharma-data/ecommerce-etl-powerbi-pipeline.git)
   cd ecommerce-etl-powerbi-pipeline

2. Execute the ETL Pipeline
   Run the Python script to fetch data from the API, process the JSON payloads, and stage tables into the SQLite database:
     $(python prac.py)

3. Verify Database Generation
Confirm that ecommercepipeline.db s created in the project root directory containing dim_products and fact_orders tables

4. Launch Analytics Dashboard
Open the .pbix file in Power BI Desktop to inspect data model relationships, DAX measures, and visual reports.
   
  

   
