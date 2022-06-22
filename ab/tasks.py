from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.management import call_command


logger = get_task_logger(__name__)



@shared_task(bind=True)
def test_func(self):
    #operations
    for i in range(10):
        print(i)
    logger.info("The sample task just ran.")
    return "Done"