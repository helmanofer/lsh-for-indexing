import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lsh-for-indexing",
    version="0.0.4",
    author="Ofer Helman",
    author_email="helmanofer@gmail.com",
    description="Package for indexing vectors to solr/es",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/helmanofer/lsh-for-indexing",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
