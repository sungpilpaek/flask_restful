from setuptools import setup, find_packages

setup(
    packages=find_packages(),
    install_requires=[
        'flask>=0.10.1',
        'flask_restful>=0.3.6',
        'pycrypto>=2.6',
        'pytest'
    ],
    setup_requires=[
        'pytest-runner'
    ]
)
