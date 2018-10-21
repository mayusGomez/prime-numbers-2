from setuptools import setup

with open("README.rst", "r") as longdesc:
    long_description = longdesc.read()


setup(
    name="List of prime numbers",
    description="List prime number of a range",
    long_description=long_description,
    author="Alexander Gomez",
    version="0.1.0",
    packages=["prime_numbers"],
)
