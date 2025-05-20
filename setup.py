from setuptools import setup, find_packages

setup(
    name='shortest_path_project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'sphinx>=8.1.3',
        'pytest>=8.3.5',
    ],
    author='NURSELIN',
    description='A project for shortest path algorithms with documentation',
    url='https://github.com/nurselioo/shortest_path_project',
)
