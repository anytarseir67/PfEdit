from setuptools import setup
import pathlib
import re

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

version = ''
with open('pfedit/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

setup(
    name="pfedit",
    version=version,
    description="small helper library that let's you write to python files the same way to write to objects",
    long_description=README,
    long_description_content_type="text/markdown",
    author="anytarseir67",
    url="https://github.com/anytarseir67/pfedit",
    license="GPLv3",
    packages=["pfedit"]
)
