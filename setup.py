from setuptools import find_packages,setup
from typing import List

HYPEN_E_DTO='-e .'

def get_requiremments(file_path:str)->List[List]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

        if HYPEN_E_DTO in requirements:
            requirements.remove(HYPEN_E_DTO)

    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Anand Srivastav',
author_email='anandsrivastava750@gmail.com',
packages=find_packages(),
install_require=get_requiremments('requirements.txt')
)