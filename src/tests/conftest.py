import sys
import os

def pytest_configure():
    # (.../password-generator/src/tests)
    test_dir = os.path.dirname(os.path.abspath(__file__))

    # (.../password-generator/src)
    project_dir = os.path.dirname(test_dir)

     # (.../password-generator/src/generator)
    generator_dir = os.path.join(project_dir, 'generator')

    # Tests assume env var value is 16
    os.environ['PASSWORD_HASH_LENGTH'] = '16'

    sys.path.insert(0, generator_dir)
