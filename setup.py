import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Ollivanders Flask",
    version="0.1.0",
    author="MatiasAgomezJ",
    author_email="matutecito@gmail.com",
    description="Small project with flask and flask restful",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MatiasAGomezJ/ollivanders-flask.git",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.6",
)
