import setuptools

with open("README.md", "r") as fd:
    long_description = fd.read()

setuptools.setup(
    author="Allen Goodman",
    author_email="allen.goodman@icloud.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="cell",
    package_data={
        'cell': [
            os.path.join("data", "training.json")
        ]
    },
    packages=setuptools.find_packages(),
    url="https://github.com/broadinstitute/cell",
    version="1.0.0"
)
