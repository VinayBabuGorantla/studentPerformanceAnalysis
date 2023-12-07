from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns a list of requirements from the specified file.
    '''
    try:
        requirements = []
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.strip() for req in requirements]

        # Remove any lines that start with '-e' or '--editable'
        requirements = [req for req in requirements if not req.startswith(('-e', '--editable'))]

        return requirements
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


setup(
    name='mlproject',
    version='0.0.1',
    author='Vinay',
    author_email='vinayc.gorantla@gmail.com',
    description='Your short description here',
    long_description='Your long description here',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
