from templates import template_apis
from templates import template_database
from templates import template_database_sql
from templates import template_fields
from templates import template_parsers
from templates import template_testcode_apis
from templates import template_testcode_database
from templates import template_testcode_fields
from templates import template_testcode_parser
import os


class FileExistsException(Exception):
    def __init__(self, message):
        super(FileExistsException, self).__init__(message)


"""
    Put your api name here!
"""

API_NAME = ""
OVERRIDE = False

"""
    Put your api name here!
"""

BASE_DIR = "../src/"
TEST_DIR = "../tests/"
APIS_SUBDIR_PATH = BASE_DIR + "apis/"
DATABASE_SUBDIR_PATH = BASE_DIR + "database/"
FIELDS_SUBDIR_PATH = BASE_DIR + "fields/"
PARSERS_SUBDIR_PATH = BASE_DIR + "parsers/"

TESTS_PREFIX = "test_"

APIS_INFIX = "_api"
DATABASE_INFIX = "_db"
DATABASE_SQL_INFIX = "_sql"
FIELDS_INFIX = "_field"
PARSERS_INFIX = "_parser"

SHELL_POSTFIX = ".py"


def write_shell(api_name, string, file_path, override):
    if os.path.isfile(file_path):
        if override is False:
            raise FileExistsException(file_path + " already exists!")

    with open(file_path, "w") as file:
        file.write(
            string.format(
                API_NAME_TITLE=api_name.lower().title(),
                API_NAME_LOWERCASE=api_name.lower(),
                API_NAME_UPPERCASE=api_name.upper()
            )
        )


if __name__ == "__main__":
    input_args = [
        [
            template_apis.shell,
            APIS_SUBDIR_PATH,
            API_NAME.lower(),
            APIS_INFIX
        ],
        [
            template_database_sql.shell,
            DATABASE_SUBDIR_PATH,
            API_NAME.lower(),
            DATABASE_SQL_INFIX + DATABASE_INFIX
        ],
        [
            template_database.shell,
            DATABASE_SUBDIR_PATH,
            API_NAME.lower(),
            DATABASE_INFIX
        ],
        [
            template_fields.shell,
            FIELDS_SUBDIR_PATH,
            API_NAME.lower(),
            FIELDS_INFIX
        ],
        [
            template_parsers.shell,
            PARSERS_SUBDIR_PATH,
            API_NAME.lower(),
            PARSERS_INFIX
        ],
        [
            template_testcode_apis.shell,
            TEST_DIR,
            TESTS_PREFIX + API_NAME.lower(),
            APIS_INFIX
        ],
        [
            template_testcode_database.shell,
            TEST_DIR,
            TESTS_PREFIX + API_NAME.lower(),
            DATABASE_INFIX
        ],
        [
            template_testcode_fields.shell,
            TEST_DIR,
            TESTS_PREFIX + API_NAME.lower(),
            FIELDS_INFIX
        ],
        [
            template_testcode_parser.shell,
            TEST_DIR,
            TESTS_PREFIX + API_NAME.lower(),
            PARSERS_INFIX
        ]
    ]

    for item in input_args:
        write_shell(
            API_NAME,
            item[0],        # Template string (shell)
            item[1] +\
            item[2] +\
            item[3] +\
            SHELL_POSTFIX,  # File path (DIR + PREFIX + API_NAME + POSTFIX)
            OVERRIDE
        )