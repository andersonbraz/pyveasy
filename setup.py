from setuptools import setup, find_packages


def read_requirements():
    with open("requirements.txt") as req:
        content = req.read()
        requirements = content.split("\n")
    return requirements


setup(
    name="pyveasy",
    version="1.2.1",
    author="Anderson Braz de Sousa",
    author_email="contato@andersonbraz.com",
    packages=find_packages(include=["src", "src.*"]),
    include_package_data=True,
    # install_requires=read_requirements(),
    install_requires=["click==8.0.3"],
    entry_points={"console_scripts": ["pyveasy=src.main:main"]},
)
