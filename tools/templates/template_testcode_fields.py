shell = '''""" {API_NAME_TITLE} Field Test code.
    Generated with API Template Generator.
"""
import pytest


@pytest.fixture("module")
def app_fixture():
    return None


class Test{API_NAME_TITLE}Field(object):
    def test_{API_NAME_LOWERCASE}_field1(self, app_fixture):
        """ GIVEN
        """


        """ WHEN
        """
        

        """ THEN
        """
        assert 1 == "NOT IMPLEMENTED"
'''