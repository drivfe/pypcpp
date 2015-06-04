import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pypcpp",
    version = "0.1",
    author = "drivfe",
    description = (
		"Unofficial command line interface for https://pcpartpicker.com/"
	),
    keywords = "pcpartpicker",
    url = "https://github.com/drivfe/pypcpp",
    packages=['pypcpp'],
	install_requires=[
		"beautifulsoup4",
		"requests",
		"PrettyTable"
	],
    long_description=read('README.md')
)