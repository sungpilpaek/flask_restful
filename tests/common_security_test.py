from common import security


class TestSecurity(object):
    def test_encryption(self):
        """ GIVEN
        """
        test_string = "I love Double cRuSt PiZzA !"

        """ WHEN
        """
        encrypted_string = security.encryption(test_string)

        """ THEN
        """
        assert encrypted_string == "aQyyK+EVpU8ggyLn+o3Fi3YX7PBJ3vXyuHdN3zuNCl8="

    def test_decryption(self):
        """ GIVEN
        """
        test_string = "Umq7r564GwsBQU0NhxBlVAnyI1lB0vcV8DRfOhiaTJE="

        """ WHEN
        """
        decrypted_string = security.decryption(test_string)

        """ THEN
        """
        assert decrypted_string == "I love to make life easier!"