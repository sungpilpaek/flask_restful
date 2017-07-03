from templates import apis_template
from templates import database_template
from templates import database_sql_template
from templates import fields_template
from templates import parsers_template

"""
    Put your api name here!
"""

API_NAME = ""

"""
    Put your api name here!
"""

BASE_DIR = "../src/"
APIS_SUBDIR_PATH = BASE_DIR + "apis/"
DATABASE_SUBDIR_PATH = BASE_DIR + "database/"
FIELDS_SUBDIR_PATH = BASE_DIR + "fields/"
PARSERS_SUBDIR_PATH = BASE_DIR + "parsers/"

APIS_PREFIX = "api_"
DATABASE_PREFIX = "db_"
FIELDS_PREFIX = "field_"
PARSERS_PREFIX = "parser_"

SHELL_POSTFIX = ".py"
SQL_SHELL_POSTFIX = "_sql.py"


def write_shell(api_name, string, file_path):
    with open(file_path, "w") as file:
        file.write(
            string.format(
                API_NAME_TITLE=api_name.lower().title(),
                API_NAME_LOWERCASE=api_name.lower(),
                API_NAME_UPPERCASE=api_name.upper()
            )
        )


if __name__ == "__main__":
    write_shell(
        API_NAME,
        apis_template.shell,
        APIS_SUBDIR_PATH + APIS_PREFIX + API_NAME + SHELL_POSTFIX
    )

    write_shell(
        API_NAME,
        database_sql_template.shell,
        DATABASE_SUBDIR_PATH + DATABASE_PREFIX + API_NAME + SQL_SHELL_POSTFIX
    )

    write_shell(
        API_NAME,
        database_template.shell,
        DATABASE_SUBDIR_PATH + DATABASE_PREFIX + API_NAME + SHELL_POSTFIX
    )

    write_shell(
        API_NAME,
        fields_template.shell,
        FIELDS_SUBDIR_PATH + FIELDS_PREFIX + API_NAME + SHELL_POSTFIX
    )

    write_shell(
        API_NAME,
        parsers_template.shell,
        PARSERS_SUBDIR_PATH + PARSERS_PREFIX + API_NAME + SHELL_POSTFIX
    )