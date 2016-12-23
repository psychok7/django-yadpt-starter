#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

# https://packaging.python.org/distributing/#packaging-your-project
# https://packaging.python.org/distributing/#uploading-your-project-to-pypi
# https://docs.djangoproject.com/en/1.10/intro/reusable-apps/
# http://peterdowns.com/posts/first-time-with-pypi.html

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-yadpt-starter',
    packages=find_packages(),
    include_package_data=True,
    version='1.2',
    description=(
        'django-yadpt-starter is Yet Another Django Project Template '
        'skeleton for Django projects'
    ),
    long_description=long_description,
    author='Nuno Khan',
    author_email='nunok7@gmail.com',
    url='https://github.com/psychok7/django-yadpt-starter',
    download_url=(
        'https://github.com/psychok7/django-yadpt-starter/tarball/v1.1'
    ),
    keywords=[
        'django', 'template', 'project templates', 'python', 'https',
        'letsencrypt', 'starter'
    ],
    scripts=['minimal/django-yadpt-starter.py'],
    install_requires=['Django >= 1.8', 'six >= 1.10.0'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',

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
