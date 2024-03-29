import logging

import azure.functions as func


def main(msg: func.QueueMessage) -> None:
    logging.info('Python queue trigger function processed a queue item: %s',
                 msg.get_body().decode('utf-8'))
    
    filename = msg.get_body().decode('utf-8')
    logging.info(f"queue trigger function: {filename}")
