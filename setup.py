from setuptools import setup, find_packages


def get_description():
    with open("README.md", "r") as fh:
        long_description = fh.read()
    return long_description


def get_data_files():
    data_files = [(".", ["README.md"])]
    return data_files


setup(
    name="wobbler",
    packages=find_packages(),
    url="https://github.com/farchaab/wobbler",
    python_requires=">=3.10",
    description="Get degenerate sites from primer alignments ",
    long_description=get_description(),
    long_description_content_type="text/markdown",
    author="Farid Chaabane",
    author_email="farid.chaabane@chuv.ch",
    data_files=get_data_files(),
    py_modules=["wobbler"],
    install_requires=[
        "biopython>=1.83",
    ],
    entry_points={"console_scripts": ["wobbler=wobbler.__main__:main"]},
    include_package_data=True,
)
