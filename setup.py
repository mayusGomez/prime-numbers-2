from setuptools import setup

with open("README.md", "r") as longdesc:
    long_description = longdesc.read()

install_requires = ["pytest"]

setup(
    name="List of prime numbers",
    description="List prime number of a range",
    long_description=long_description,
    author="Alexander Gomez",
    version="0.1.1",
    packages=["prime_numbers"],
    install_requires=install_requires,
)
