import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="packageGrp5",
    version = "0.0.1",
    author = "Group 5",
    author_email = "maceovalente@gmail.com",
    description = "4BIM project by group 5",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lina-ouaret/Project_4bim",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independant"
    ],
)
