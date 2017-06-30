from common import message, security, config
import sql_statements
import context_manager


class Subscriber(object):
    """ An object that is declared when user submits new username
    """
    username = ''
    def __init__(self, username=None):
        self.database_instance = context_manager.DatabaseContextManager()
        if username is not None:
            self.username = username

    def insert(self):
        with self.database_instance:
            self.database_instance.query(
                sql_statements.INSERT_SUBSCRIBER,
                [self.username]
            )

        return message.TRANSACTION_OK

    def delete(self):
        with self.database_instance:
            self.database_instance.query(
                sql_statements.DELETE_SUBSCRIBER,
                [self.username]
            )

        return message.TRANSACTION_OK

    def update(self):
        with self.database_instance:
            self.database_instance.query(
                sql_statements.UPDATE_SUBSCRIBER,
                [self.username]
            )

        return message.TRANSACTION_OK

    def select(self, index):
        """
            Called by APIs upon user's request
            Return [config.RETURN_ROWS_PER_API_CALL] rows at a time
        
        Args:
            encrypted_index (String): The encrypted value of a last row
                                      from previous API call
        
        Returns:
            TYPE                    : [config.RETURN_ROWS_PER_API_CALL] rows +
                                      new encrypted value of a last row

        """
        res = []
        decrypted_index = security.decryption(index)

        with self.database_instance:
            cur = self.database_instance.query(
                sql_statements.GET_MAX_ID_SUBSCRIBER,
                (
                    decrypted_index,
                    config.ROWS_PER_API_CALL
                )
            )
            
            max_id = str(cur.fetchone()["MAX"])
            new_index = security.encryption(max_id)

            cur = self.database_instance.query(
                sql_statements.SELECT_SUBSCRIBER,
                (
                    decrypted_index,
                    config.ROWS_PER_API_CALL
                )
            )

            for row in cur:
                res.append(row)
        
        return res, new_index, message.TRANSACTION_OK