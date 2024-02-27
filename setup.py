from setuptools import setup, find_packages

setup(
    name='my_project',
    version='0.1.0',
    description='Setting up our python package',
    author='Ash Mason',
    author_email='ashmason1389@gmail.com',
    packages=find_packages(include=['src', 'src.*']),
    install_requires=[
        'jupyter',
        'requests',
        'pandas',
        'numpy'
    ],
    extras_require={'plotting': ['matplotlib>=2.2.0', 'jupyter']},
    # setup_requires=['pytest-runner', 'flake8'],
    # tests_require=['pytest'],
    # entry_points={
    #     'console_scripts': ['my-command=exampleproject.example:main']
    # },
    # package_data={'exampleproject': ['data/schema.json']}
)