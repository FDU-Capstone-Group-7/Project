import os
import time
from django.core.management.base import BaseCommand
from threading import Thread
from django.db import connection
from Indie_Game.management.commands.moderation import process_comments
import logging
import sys

# Setup logger
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Run the Django development server and process comments'

    def handle(self, *args, **kwargs):
        # Start the comment processing in a separate thread
        def run_task():
            while True:
                logger.info('Processing comments...')
                try:
                    process_comments()  # Call your processing function
                except Exception as e:
                    logger.error(f"Error in processing comments: {e}")
                finally:
                    # Close the database connection to avoid open connections
                    connection.close()
                time.sleep(240)  

        # Create and start the task thread
        if not hasattr(self, 'task_thread'):
            self.task_thread = Thread(target=run_task)
            self.task_thread.daemon = True 
            self.task_thread.start()

        # Now run the Django server
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Indie_Game_Platform.settings')
        from django.core.management import execute_from_command_line
        execute_from_command_line(['manage.py', 'runserver'] + sys.argv[2:])
