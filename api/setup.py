import os
from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="Api",
    version="0.0.0",
    author="Rafael",
    author_email="rrodriguesdecarvalho@gmail.com",
    description="",
    url="",
    packages=find_packages(),
    python_requires=">3.6",
    install_requires=["fastapi", "uvicorn", "starlette_exporter"],
    long_description=read("README.md"),
)
