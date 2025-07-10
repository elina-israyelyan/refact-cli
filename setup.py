from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="refact-cli",
    version="1.0.0",
    install_requires=requirements,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "refact=refact.cli:main",
        ],
    },
)
