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
    python_requires='>=3.6',
    install_requires=[
        "aniso8601 == 9.0.1",
        "attrs == 21.4.0",
        "autopep8 == 1.6.0",
        "click == 8.0.4",
        "colorama == 0.4.4",
        "distlib == 0.3.4",
        "dnspython == 2.2.1",
        "filelock == 3.6.0",
        "Flask == 2.0.3",
        "Flask-RESTful == 0.3.9",
        "iniconfig == 1.1.1",
        "itsdangerous == 2.1.0",
        "Jinja2 == 3.0.3",
        "MarkupSafe == 2.1.0",
        "mongoengine == 0.24.0",
        "packaging == 21.3",
        "platformdirs == 2.5.1",
        "pluggy == 1.0.0",
        "py == 1.11.0",
        "pycodestyle == 2.8.0",
        "pymongo == 4.0",
        "pyparsing == 3.0.7",
        "pytest == 7.0.1",
        "pytz == 2021.3",
        "six == 1.16.0",
        "toml == 0.10.2",
        "tomli == 2.0.1",
        "tox == 3.24.5",
        "virtualenv == 20.13.3",
        "Werkzeug == 2.0.3"
    ],
)
