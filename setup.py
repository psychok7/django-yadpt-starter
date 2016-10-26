#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# https://packaging.python.org/distributing/

setup(
    name='django-yadpt-starter',
    packages=find_packages(),
    version='1.0-beta',
    description=(
        'django-project-template-yadpt is Yet Another Django Project Template '
        'skeleton for Django projects'
    ),
    long_description=long_description,
    author='Nuno Khan',
    author_email='nunok7@gmail.com',
    url='https://github.com/psychok7/django-project-template-yadpt',
    download_url=('https://github.com/psychok7/django-project-template-yadpt/tarball/v1.0-beta'),
    keywords=[
        'django', 'template', 'project templates', 'python', 'https',
        'letsencrypt'
    ],
    install_requires=['Django >= 1.8'],
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Framework :: Django :: 1.8',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    license='MIT',
)
