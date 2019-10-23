# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in felixcustom/__init__.py
from felixcustom import __version__ as version

setup(
	name='felixcustom',
	version=version,
	description='Custom App to house custom code changes',
	author='TechSquid',
	author_email='hello@techsquid.co.nz',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
