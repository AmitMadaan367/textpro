from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.management import call_command


logger = get_task_logger(__name__)



@shared_task(bind=True)
def test_func(self):
    #operations
    import time
    import sib_api_v3_sdk
    from sib_api_v3_sdk.rest import ApiException
    from pprint import pprint

    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = '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'

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    subject = 'Email from celery beat from Amit bot'
    html_content = "<html><body><h1>Hi thank you for checking</h1></body></html>"


    sender = {"name":"amit","email":"amitdev7867@gmail.com"}
    to = [{"email":"madaanamit367@gmail.com","name":"madaanamit367@gmail.com"}]
    headers = {"Some-Custom-Name":"unique-id-1234"}
    params = {"parameter":"My param value","subject":subject}

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, headers=headers, html_content=html_content, sender=sender, subject=subject)

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
    # for i in range(10):
    #     print(i)
    print("done")

    logger.info("The sample task just ran.")

    return "Done"