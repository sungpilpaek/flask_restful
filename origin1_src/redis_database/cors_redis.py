""" Implementation of temporary Redis database.
    Generates atomic username.key, and uses it as primary key.
"""
import json
from redis import StrictRedis
from datetime import timedelta
from common import config, message


class Manager(object):
    def __init__(self):
        self.redis = StrictRedis(
            host=config.REDIS_HOST,
            port=config.REDIS_PORT,
            db=config.REDIS_DB
        )

    def _get_new_key(self):
        """ Atomically increments the value of a specified key.
        """
        key = str(self.redis.incr("username.key", 1))

        return key

    def _get_amount_of_key(self):
        """ _get_amount_of_key() returns the number of keys that redis
            currently has at the moment. This way, all necesssary related
            keys can be found from a scan operation.
        """
        info = self.redis.info()
        db0_section_info = info.get("db0")

        if not db0_section_info:
            self.redis.set("dummy_key", "dummy")

        key = int(db0_section_info["keys"])

        return key

    def insert(self, data):
        """ data={"username": username, "input_date": input_date}
        """
        self.redis.setex(
            "username.key:" + self._get_new_key(),
            int(timedelta(days=1).total_seconds()),
            json.dumps(data)
        )

        return message.TRANSACTION_OK

    def select_all(self):
        """ Scans all keys alive at the moment, retrieves their values
            as a list, and finally returns them as json.
        """
        scan_result = self.redis.scan(
            0,
            "username.key:*",
            self._get_amount_of_key()
        )

        keys = scan_result[1]
        values = self.redis.mget(keys)
        values_dicts = map(lambda x: json.loads(x), values)

        return values_dicts, message.TRANSACTION_OK