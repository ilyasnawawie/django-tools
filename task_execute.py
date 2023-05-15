import logging
import os
from celery import Celery, shared_task
import mysql.connector

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create a Celery app instance
app = Celery('hnmapp')

# Configure the Celery app to use the Redis broker and result backend
app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.result_backend = 'redis://localhost:6379/0'

# Define the task you want to execute
@shared_task
def my_task():
    # Your task logic goes here
    logging.info('Executing my task...')
    # Rest of the code...

# Function to execute the task
def execute_task():
    # Send the task to the Celery worker
    result = my_task.delay()
    logging.info(f'Task ID: {result.id}')

# Execute the task
if __name__ == '__main__':
    execute_task()
