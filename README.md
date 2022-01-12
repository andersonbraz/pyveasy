# Python VSCode Easy

Create adjust project Python on VSCode

```
$ pyveasy
```

```python

from setuptools import setup, find_packages


def read_requirements():
    with open("src/requirements.txt") as req:
        content = req.read()
        requirements = content.split("\n")
    return requirements


setup(
    name="pyveasy",
    version="1.2.0",
    author="Anderson Braz de Sousa",
    author_email="contato@andersonbraz.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    entry_points="""
        [console_scripts]
        pyveasy=src.main:main
    """,
)

```