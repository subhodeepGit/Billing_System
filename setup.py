from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in billing_system/__init__.py
from billing_system import __version__ as version

setup(
	name="billing_system",
	version=version,
	description="Billing System",
	author="SOUL Limited",
	author_email="Soul@soul.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
