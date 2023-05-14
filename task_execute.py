from hnmproject.hnmapp.tasks import my_task
import logging
logging.basicConfig(level=logging.INFO)

# Function to execute the task
def execute_task():
    # Send the task to the Celery worker
    result = my_task.delay()
    print(f'Task ID: {result.id}')

# Execute the task
if __name__ == '__main__':
    execute_task()
