import logging
import os
from celery import Celery
import mysql.connector

# Create a Celery app instance
app = Celery('hnmapp')

# Configure the Celery app to use the Redis broker and result backend
app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.result_backend = 'redis://localhost:6379/0'

# Define the task you want to execute
@app.task
def my_task():
    # Your task logic goes here
    logging.info('Executing my task...')

    # Get the database connection details from environment variables
    db_name = os.environ.get('DB_NAME')
    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('DB_PORT')
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')

    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        database=db_name
    )

    # Create a cursor object to execute queries
    cursor = connection.cursor()

    # Execute the SQL query
    query = 'SELECT * FROM user_groups'
    cursor.execute(query)

    # Fetch all rows from the result
    rows = cursor.fetchall()

    # Write the rows to a text file
    with open('task_output.txt', 'a') as f:
        for row in rows:
            f.write(str(row) + '\n')

    # Close the cursor and connection
    cursor.close()
    connection.close()

# Function to execute the task
def execute_task():
    # Send the task to the Celery worker
    result = my_task.delay()
    logging.info(f'Task ID: {result.id}')

# Execute the task
if __name__ == '__main__':
    execute_task()
