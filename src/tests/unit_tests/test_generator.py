import unittest

from src.generator.engine import generate_password
from src.generator.constants import RULE_SATISFYING_STRING, PASSWORD_HASH_LENGTH

class GeneratorTests(unittest.TestCase):

    def test_generate_password_standard(self):
        universal = "universal"
        platform = "platform"
        password = generate_password(universal, platform)

        self.assertEqual(len(password), PASSWORD_HASH_LENGTH + len(RULE_SATISFYING_STRING))
        self.assertEqual(password, "c7d6967b7a6a2c6baA123!?$")

if __name__ == '__main__':
    unittest.main()
