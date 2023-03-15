from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    req=[]
    hyp='-e .'
    with open(file_path) as file_obj:
        req=file_obj.readlines()
        req=[re.replace("\n","") for re in req]
        if hyp in req:
            req.remove(hyp)
    return req
        

setup(
    name='projectml',
    version='0.0.1',
    author='soumya',
    author_email='soumya.mohanty7589@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)