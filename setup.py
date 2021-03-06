import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="tamilang",
    version="1.0.1",
    description="Translates tamil words to english phonetic",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/wickkiey/tamilang",
    author="Wickkiey",
    author_email="wickkiey@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["tamilang"],
    include_package_data=True,
    install_requires=["Open-Tamil"],
    entry_points={
        "console_scripts": [
            "tamilang=tamilang.__main__:main",
        ]
    },
)