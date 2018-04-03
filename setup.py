from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

setup(
    name="pymmwr",
    version="0.2.1",
    description="MMWR weeks for Python",
    long_description=readme,
    author="Abhinav Tushar",
    author_email="lepisma@fastmail.com",
    url="https://github.com/reichlab/pymmwr",
    install_requires=["attrs"],
    keywords="mmwr week converter",
    packages=find_packages(),
    classifiers=(
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only"
    ))
