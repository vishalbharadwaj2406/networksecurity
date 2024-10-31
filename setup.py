from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    Function to return list of requirements.
    """
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)

        return requirement_lst

    except FileNotFoundError:
        print('requirements.txt file not found')

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Vishal Bharadwaj',
    packages=find_packages(),
    install_requires=get_requirements()
)