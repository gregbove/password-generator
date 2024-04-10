import unittest

from src.generator.engine import generate_platform_password

class GeneratorTests(unittest.TestCase):

    def test_generate_password_standard(self):
        universal = "universal"
        platform = "platform"
        password = generate_platform_password(universal, platform)

        

        self.assertEqual(password, "c7d6967b7a6a2c6baA123!?$")

if __name__ == '__main__':
    unittest.main()
