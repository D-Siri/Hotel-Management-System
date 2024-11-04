# Hotel-Management-System
A relational database system designed to streamline hotel management by centralizing data for guests, reservations, rooms, and amenities. Built with PostgreSQL and deployed via Streamlit, it enhances data integrity, query performance, and operational efficiency, allowing for improved guest experiences and data-driven decision-making.

## Building Tables
Tables were created in the PostgreSQL database using pgAdmin. Each table was designed to store specific types of data related to a hotel management system. All the SQL queries are included in create.sql

## Importing Data
Data was generated in Python using scripts, and then imported into the PostgreSQL database. Below are the steps to generate and import data:
- **Python Scripts:** Python scripts were used to generate random data for each table. These scripts utilized the random module to create realistic data sets.
- **Data Generation:** Data was generated for each table using the Python scripts. The generated data included information such as hotel details, guest information, room types, staff details, amenity types, menu items, food items, reservations, orders, and order items.
- **CSV File Creation:** The generated data was written to CSV (Comma-Separated Values) files using the csv module in Python.
- **Importing Data into PostgreSQL:** Once the CSV files were created, they were imported into the PostgreSQL database using pgAdmin. This was achieved by using the import functionality within pgAdmin to import each CSV file into its corresponding table.

## Query Performance Optimization
To ensure efficient data retrieval, various indexing techniques were applied:

- **Primary Keys**: Assigned primary keys to enhance data access.
- **Foreign Keys**: Defined relationships between tables for quick joins.
- **Composite and Partial Indexes**: Created composite and partial indexes for frequently queried columns to optimize filtering and sorting operations.

## Deployment
The project was deployed using Streamlit and psycopg2 to interface with the PostgreSQL database. This deployment enables a user-friendly interface for interacting with the database, making it accessible for various hotel management operations.


