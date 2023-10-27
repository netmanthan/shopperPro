# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# get version from __version__ variable in shopperpro/__init__.py
from shopperpro import __version__ as version

setup(
    name="shopperpro",
    version=version,
    description="Shopper Pro",
    author="Yousef Restom",
    author_email="youssef@sparrownova.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)
