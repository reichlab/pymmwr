from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

project_url = "https://github.com/"
project_url += "reichlab/pymmwr"

setup(
    name="pymmwr",
    version="0.1.0",
    description="MMWR weeks for Python",
    long_description=readme,
    author="Abhinav Tushar",
    author_email="lepisma@fastmail.com",
    url=project_url,
    install_requires=[],
    keywords="mmwr week converter",
    packages=find_packages(),
    classifiers=(
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only"
    ))
