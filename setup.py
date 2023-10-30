#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "pandas==1.4.0",
    "requests==2.28.1",
    "fastapi",
    "uvicorn",
    "openai",
    "gunicorn"
]

dev_requirements = [
    "notebook==6.4.7",
    "black==22.3",
    "pylint==2.12.2",
    "mypy==0.931",
    "pytest==6.2.5",
]

test_requirements = ['pytest>=3', ]

setup(
    author="Munanga Munsaka",
    author_email='jackslaighter@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        "Private :: Do Not Upload",
    ],
    description="App that summaries essays, articles and text in general",
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='summify',
    name='summify',
    packages=find_packages(include=['summify', 'summify.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Munanga/summify',
    version='0.1.0',
    zip_safe=False,
)
