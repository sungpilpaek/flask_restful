from common import security


class TestSecurity(object):
    def test_encryption(self):
        test_string = "I love Double cRuSt PiZzA !"

        encrypted_string = security.encryption(test_string)
        assert encrypted_string == "aQyyK+EVpU8ggyLn+o3Fi3YX7PBJ3vXyuHdN3zuNCl8="

    def test_decryption(self):
        test_string = "Umq7r564GwsBQU0NhxBlVAnyI1lB0vcV8DRfOhiaTJE="

        decrypted_string = security.decryption(test_string)
        assert decrypted_string == "I love to make life easier!"