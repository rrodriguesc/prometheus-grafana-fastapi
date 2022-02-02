import os

from setuptools import find_packages, setup


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
    install_requires=["fastapi", "uvicorn[standard]", "gunicorn", "starlette_exporter"],
    long_description=read("README.md"),
)
