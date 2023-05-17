import os
import mysql.connector

def test_connection():
    os.environ["DB_NAME"] = "evhome"
    os.environ["DB_HOST"] = "localhost"
    os.environ["DB_PORT"] = "3306"
    os.environ["DB_USER"] = "root"
    os.environ["DB_PASSWORD"] = "root"

    db_name = os.environ.get("DB_NAME")
    db_host = os.environ.get("DB_HOST")
    db_port = os.environ.get("DB_PORT")
    db_user = os.environ.get("DB_USER")
    db_password = os.environ.get("DB_PASSWORD")

    # Try to connect to the MySQL database
    try:
        connection = mysql.connector.connect(
            host=db_host, port=db_port, user=db_user, password=db_password, database=db_name
        )
        connection.close()
        result = "Connection successful"
    except Exception as e:
        result = str(e)

    # Write the result to a text file
    with open("test_output.txt", "w") as f:
        f.write(result + "\n")

test_connection()
