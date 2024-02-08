import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="rentman-api-client",
    version="1.6.3",
    description="A client library for accessing Rentman API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "rentman_api_client"},
    packages=find_packages(),
    python_requires=">=3.6, <4",
    install_requires=["httpx >= 0.15.0, < 0.19.0", "attrs >= 20.1.0", "python-dateutil >= 2.8.0, < 3"],
    package_data={"": ["CHANGELOG.md"], "rentman_api_client": ["py.typed"]},
)
