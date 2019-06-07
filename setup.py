import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rival_regions_calc",
    version="1.0.2",
    author="Joost Sijm",
    author_email="joostsijm@gmail.com",
    description="Rival Regions calculations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joostsijm/rival_regions_calc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
