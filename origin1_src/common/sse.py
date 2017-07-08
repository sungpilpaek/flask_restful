import time
import json
from fields import cors_field
from flask_restful import marshal
from common import security, message
from redis_database import cors_redis


def event_stream(app):
    manager = cors_redis.Manager()
    keep_alive_counter = 0
    while True:
        result, status = manager.select_all(return_keys=True)

        if status == message.TRANSACTION_OK:
            for item in result:
                if item["transferred"] is False:
                    yield "event: notify\ndata: {}\n\n".format(
                        item["username"]
                    )

                manager.update(
                    item["key"],
                    {
                        "username": item["username"],
                        "input_date": item["input_date"],
                        "transferred": True
                    }
                )

        time.sleep(1)
        keep_alive_counter += 1
        if keep_alive_counter == 10:
            keep_alive_counter = 0
            yield "\n\n"