from setuptools import setup, find_packages

setup(
    name="tswdtf",
    version="0.0.1",
    author="Dr June Moone",
    author_email="moonedrjune@gmail.com",
    license="MIT",
    packages=["tswdtf"],
    long_description=open("README.md").read(),
    install_requires=["tensorflow", "pandas"],
)
