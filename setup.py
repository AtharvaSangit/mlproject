from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    requtirements=[]
    with open(file_path) as file_obj:
        requtirements=file_obj.readlines()
        requtirements=[req.replace("\n","") for req in requtirements]

        if HYPEN_E_DOT in requtirements:
            requtirements.remove(HYPEN_E_DOT)

    return requtirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Atharva',
    author_email='atharvasangit@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirments.txt')
)