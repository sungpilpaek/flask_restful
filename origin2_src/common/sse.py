import time
import json
from database import clicors_db
from fields import clicors_field
from flask_restful import marshal
from common import security, message


def event_stream(app):
    index = None
    manager = clicors_db.Manager()
    with app.app_context():
        while True:
            decrypted_index = security.decryption(index)
            result, new_index, status = manager.select(decrypted_index)

            if status == message.TRANSACTION_OK:
                if new_index != "None":
                    index = security.encryption(new_index)

                    marshaled_res = marshal(
                        result,
                        clicors_field.httpget_field
                    )
                    
                    yield "event: notify\ndata: {}\n\n".format(
                        json.dumps(marshaled_res)
                    )

            time.sleep(0.7)