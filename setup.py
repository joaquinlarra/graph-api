from setuptools import setup, find_packages

setup(
    name="graph-api-toolkit",
    version="0.1.0",
    author="Joaquin Astelarra",
    author_email="joaquinastelarra@gmail.com",
    description="Clean, zero-dependency graph data structures and pathfinding algorithms for Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/joaquinlarra/graph-api",
    packages=find_packages(exclude=["tests*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.9",
)
