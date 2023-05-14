import os
import mysql.connector

def test_connection():
    os.environ["DB_NAME"] = "sample"
    os.environ["DB_HOST"] = "127.0.0.1"
    os.environ["DB_PORT"] = "3306"
    os.environ["DB_USER"] = "root"
    os.environ["DB_PASSWORD"] = "admin123"

    db_name = os.environ.get("DB_NAME")
    db_host = os.environ.get("DB_HOST")
    db_port = os.environ.get("DB_PORT")
    db_user = os.environ.get("DB_USER")
    db_password = os.environ.get("DB_PASSWORD")

    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host=db_host, port=db_port, user=db_user, password=db_password, database=db_name
    )

    # Create a cursor object to execute queries
    cursor = connection.cursor()

    # Execute the SQL query
    query = "SELECT * FROM admin"
    cursor.execute(query)

    # Fetch all rows from the result
    rows = cursor.fetchall()

    # Write the rows to a text file
    with open("test_output.txt", "a") as f:
        for row in rows:
            f.write(str(row) + "\n")

    # Close the cursor and connection
    cursor.close()
    connection.close()
