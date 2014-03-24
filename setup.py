from setuptools import setup

setup(
    name="kitab",
    version="0.1.0",
    author="Sean Hammond, Dilawar Singh",
    packages=["kitab"],
    scripts=["bin/kitab"],
    license="GNU General Public License, Version 3",
    description="A fast note-taking app for the UNIX terminal.",
    long_description=open("README.rst").read(),
    install_requires=[
        "urwid==1.2.0",
        "chardet==2.2.1",
        ]
)
