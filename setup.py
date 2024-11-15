from setuptools import setup,find_packages
from typing import List

PROJECT_NAME = "Machine Learning"
VERSION = "0.0.1"
DESCRIPTION = "This is the end to end project"
AUTHOR_NAME = "Shubham Singh"
AUTHOR_EMAIL = "shubham47047@gmail.com"

REQUIREMENTS_FILENAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements():
    with open(REQUIREMENTS_FILENAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]

        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)

        return requirement_list

setup(
    name=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    install_requires=get_requirements(),
)