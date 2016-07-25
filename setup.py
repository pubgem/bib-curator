# -*- coding: utf-8 -*-
# citation-curator (c) Pubgem Foundation

import re
import os
from setuptools import setup
from distutils.dir_util import copy_tree


# from https://github.com/flask-admin/flask-admin/blob/master/setup.py
def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()


file_text = read(fpath('citation_curator/__meta__.py'))


def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, file_text)
    return strval


setup(
    version=grep('__version__'),
    name='citation-curator',
    description="citation-curator keeps the .bib files clean",
    packages=[
        "citation_curator",
        "citation_curator.migrations",
        "citation_curator.migrations.versions",
        "citation_curator.models",
        "citation_curator.views",
        "citation_curator.views.administration",
    ],
    scripts=[
        "bin/runserver.py",
        "bin/manage.py",
    ],
    long_description=read('Readme.rst'),
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    include_package_data=True,
    keywords='',
    author=grep('__author__'),
    author_email=grep('__email__'),
    url=grep('__url__'),
    install_requires=read('requirements.txt'),
    license='MIT',
    zip_safe=False,
)
