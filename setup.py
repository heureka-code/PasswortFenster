import setuptools
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="PasswortFenster",
    version="2.0.0",
    install_requires=["PyQt5"],
    author="heureka-code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    description="Öffnet ein Fenster zur Eingabe von Login-Daten",
    packages=setuptools.find_packages(),
    keywords=["Passwort", "Fenster", "PyQt5", "PasswortFenster", "Login", "Username"],
    url="https://github.com/heureka-code/PasswortFenster",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)"],
    download_url="https://github.com/heureka-code/PasswortFenster/archive/2.0.0.tar.gz"
    )
