from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="matsolver",
    version="0.0.1",
    author="Lukas Harris",
    author_email="186.lukas@gmail.com",
    description="A matrix calculator",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/matsolver/matrixsolverv1",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)