# Olist ETL Project – End-to-End Data Engineering Pipeline

An end-to-end data engineering project built using the Brazilian Olist e-commerce dataset. This project demonstrates data extraction, transformation, cleaning, validation, and loading using Python, Pandas, and MySQL, with SQL-based analysis and Power BI visualization.

The pipeline is containerized using Docker and Docker Compose to make the ETL workflow easier to reproduce and execute. The project also includes introductory Apache Spark (PySpark) implementations for data processing and analysis.

## Project Overview

The project processes Brazilian e-commerce data from Olist and transforms raw datasets into structured, cleaned datasets ready for analysis.

**Key objectives:**
- Build a complete ETL pipeline using Python and Pandas.
- Perform data cleaning, transformation, and validation.
- Load processed datasets into a MySQL database.
- Perform business analysis using SQL.
- Develop interactive dashboards using Power BI.
- Containerize the ETL pipeline using Docker.
- Explore data processing and analysis using Apache Spark (PySpark).

## Technologies Used

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Processing | Pandas, NumPy, Apache Spark, PySpark |
| Database | MySQL |
| Query Language | SQL |
| Visualization | Power BI |
| Containerization | Docker, Docker Compose |
| Development | VS Code, Git, GitHub |
| Big Data Platform | Databricks (planned exploration) |

## Project Structure

```text
olist-etl-project/
│
├── Data_sets/
│   └── Cleaned_Dataset/
│
├── python_scripts/
│   ├── customer_data.py
│   ├── geo_map.py
│   ├── items_data.py
│   ├── load_data_to_mysql.py
│   ├── olist_order.py
│   ├── order_payments.py
│   ├── products_data.py
│   ├── prod_category_translate_data.py
│   ├── reviews_data.py
│   └── sellers_data.py
│
├── pyspark_scripts/
│   ├── 01_read_order_items.py
│   ├── 02_order_items_quality.py
│   ├── 03_seller_sales_analysis.py
│   └── 04_orders_items_join.py
│
├── SQL_queries/
├── .dockerignore
├── .gitignore
├── compose.yaml
├── Dockerfile
├── requirements.txt
├── README.md
└── olist_powerbi_dashboard.pbix
```

## ETL Pipeline

The project follows three major stages:

1. **Extract:** Read the original Olist CSV datasets.
2. **Transform:** Clean, process, and validate the datasets using Python and Pandas.
3. **Load:** Load the cleaned datasets into MySQL tables.

The pipeline processes nine datasets:

| Dataset | Cleaned Rows |
|---|---:|
| Geolocation | 738,332 |
| Orders | 99,441 |
| Order Items | 112,650 |
| Order Payments | 103,886 |
| Customers | 99,441 |
| Products | 32,951 |
| Reviews | 99,224 |
| Sellers | 3,095 |
| Category Translation | 71 |
| **Total** | **1,296,091** |

## Docker Implementation

The Python ETL pipeline is containerized using Docker.

**Docker components:**
- `Dockerfile` – Defines the Python environment and application execution command.
- `requirements.txt` – Lists the required Python dependencies.
- `.dockerignore` – Excludes unnecessary files and sensitive configuration from the Docker build context.
- `compose.yaml` – Configures the ETL service, database environment variables, and dataset volume.

### Prerequisites

- Docker Desktop
- MySQL Server
- Git

### Database Configuration

Create a local `.env` file in the project root with your MySQL credentials:

```env
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_HOST=host.docker.internal
DB_PORT=3306
DB_NAME=olist_ecommerce_docker_test
```

**Security:** Never commit your `.env` file or database credentials to GitHub.

### Build and Run

Open PowerShell in the project directory.

Build and execute the ETL pipeline using Docker Compose:

```powershell
docker compose run --build --rm olist-etl
```

The Compose configuration:
- Builds the Docker image.
- Loads database credentials from `.env`.
- Connects to the host MySQL server using `host.docker.internal`.
- Mounts the cleaned CSV datasets into the container as a read-only volume.
- Executes the Python ETL loading script.

### Docker Hub

The Docker image is publicly available on Docker Hub.

**Repository:** [remayy/olist-etl](https://hub.docker.com/r/remayy/olist-etl)

**Pull the image:**

```bash
docker pull remayy/olist-etl:v1
```

**Image:** `remayy/olist-etl:v1`

The image contains the Python application scripts and required dependencies. The cleaned datasets and `.env` credentials are supplied separately at runtime.

**Important database safety note:** The current Docker Compose configuration targets the separate `olist_ecommerce_docker_test` database. The loader uses `if_exists="replace"`, which replaces existing tables in that database. Do not change the target to your original database without understanding this behavior.

## Apache Spark (PySpark)

The project also includes introductory Apache Spark processing using PySpark, the Python API for Apache Spark.

The PySpark scripts demonstrate basic data processing operations using Spark DataFrames.

### Technologies

- Apache Spark 4.3.0
- PySpark 4.3.0
- Python 3.13.14
- Java 21
- Local execution using `local[*]`

### Setup

1. Install Python and Java 21.
2. Clone this repository.
3. Open the project folder in your terminal.
4. Create a separate virtual environment:

```powershell
python -m venv .venv-spark
```

5. Activate the environment:

```powershell
.\.venv-spark\Scripts\Activate.ps1
```

6. Install PySpark:

```powershell
python -m pip install pyspark==4.3.0
```

### Running the PySpark Scripts

Execute these commands from the project root:

```powershell
python pyspark_scripts/01_read_order_items.py
python pyspark_scripts/02_order_items_quality.py
python pyspark_scripts/03_seller_sales_analysis.py
python pyspark_scripts/04_orders_items_join.py
```

### Implementations

1. **CSV Reading and Schema Inspection:** Read the cleaned order-items dataset and inspect its schema and records.
2. **Data Quality Checks:** Check for null values and exact duplicate records.
3. **Seller Sales Analysis:** Group order items by seller and calculate total items sold, total sales, average price, and freight value.
4. **Dataset Joining:** Join orders and order-items datasets using the common `order_id` column.

**Execution environment:** The scripts use Spark's local execution mode (`local[*]`) to process data on the local machine. This demonstrates introductory PySpark usage and does not represent a production multi-node Spark cluster.

**Note:** The PySpark environment is maintained separately from the original ETL environment. The `.venv-spark/` virtual environment is excluded from GitHub.

## SQL Analysis

SQL queries are used to explore business insights across:

- Sales and revenue.
- Product performance.
- Customer behavior.
- Seller performance.
- Delivery performance and customer reviews.

## Power BI Dashboard

An interactive Power BI dashboard is developed to explore Olist's e-commerce performance through business metrics and visual analytics.

## Future Enhancements

- Explore Databricks Free Edition for cloud-based PySpark notebook workflows.
- Improve pipeline orchestration and automation.
- Add data quality monitoring and logging.
- Explore advanced Apache Spark and distributed data processing in future projects.

## Author

**Antony Remane**

GitHub: [Antonyremay](https://github.com/Antonyremay)