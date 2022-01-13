from setuptools import setup, find_packages

setup(
    name="pyveasy",
    version="1.3.1",
    author="Anderson Braz de Sousa",
    author_email="contato@andersonbraz.com",
    url="https://pypi.org/project/pyveasy/",
    description="Library create a Python project tuned for VSCode.",
    packages=find_packages(include=["src", "src.*"]),
    include_package_data=True,
    install_requires=["click==8.0.3"],
    entry_points={"console_scripts": ["pyveasy=src.main:main"]},
)
