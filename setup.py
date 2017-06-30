from setuptools import setup, find_packages

setup(
    packages=find_packages(),
    install_requires=[
            'flask',
            'flask_restful',
            'pycrypto'
        ],
    setup_requires=[
            'pytest-runner'
        ],
    tests_require=[
            'pytest'
        ],
)