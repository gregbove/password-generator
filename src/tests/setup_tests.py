import sys
import os

def setup_project_path():
    # (.../password-generator/src/tests)
    test_dir = os.path.dirname(os.path.abspath(__file__))

    # (.../password-generator/src)
    project_dir = os.path.dirname(test_dir)

     # (.../password-generator/src/generator)
    generator_dir = os.path.join(project_dir, 'generator')

    sys.path.insert(0, generator_dir)
