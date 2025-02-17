from setuptools import find_packages,setup
from typing import List

requirement_lst:List[str]=[]
def get_requirements()->List[str]:
    "This will return the requirements in a list"
    try:
        with open("requirements.txt") as file:
            ## read lines from the file
            lines= file.readlines()
            ## Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore the empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file does not exists")
    return requirement_lst


setup(
    name="Network Security",
    version="0.0.1",
    author="Shrimanth V",
    author_email="shrimanthv99@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements()
)