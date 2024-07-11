from psycopg2 import extras

def create_database(table_name, ingestion_data, connection, cursor):

    columns_names = ", ".join(ingestion_data[0].keys())
    columns_with_types = ", ".join([f"{key} VARCHAR(255)" for key in ingestion_data[0].keys()])

    create_table_sql_query = f"CREATE TABLE IF NOT EXISTS {table_name} (unique_id SERIAL PRIMARY KEY, {columns_with_types})"
    cursor.execute(create_table_sql_query)
    connection.commit()

    print(f"table '{table_name}' created successfully")

    insert_sql_query = f"INSERT INTO {table_name} ({columns_names}) VALUES %s"
    values = [[row[key] for key in ingestion_data[0].keys()] for row in ingestion_data]
    extras.execute_values(cursor, insert_sql_query, values)
    connection.commit()

    print(f"data inserted successfully!")

    cursor.close()
    connection.close()