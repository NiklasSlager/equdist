import os
from typing import List

import setuptools
from setuptools import setup


def _parse_requirements(path: str) -> List[str]:
    """Returns content of given requirements file."""
    with open(os.path.join(path)) as f:
        return [
            line.rstrip() for line in f if not (line.isspace() or line.startswith("#"))
        ]


def _get_version() -> str:
    """Grabs the package version from EquDist/version.py."""
    dict_ = {}
    with open("EquDist/version.py") as f:
        exec(f.read(), dict_)
    return dict_["__version__"]


setup(
    name="EquDist",
    version=_get_version(),
    author="NiklasSlager",
    author_email="niklasslager@outlook.com",
    description="Equilibrium separation model in JAX",
    license="Apache 2.0",
    url="https://github.com/NiklasSlager/EquDist/",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords="Chemical separation JAX",
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
    install_requires=_parse_requirements("requirements.txt"),
    package_data={"EquDist": ["py.typed"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License",
    ],
    zip_safe=False,
    include_package_data=True,
)
