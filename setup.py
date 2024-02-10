from setuptools import setup, find_packages

setup(
    name='SteamGameDir',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'vdf',
        'thefuzz',
    ],
    entry_points={
        'console_scripts': [
            'SteamGameDir = src.main:main'
        ]
    }
)