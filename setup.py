#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pip.download

from pip.req import parse_requirements

from setuptools import find_packages, setup

#exec(open('steenzout/primogen/metadata.py').read())


def requirements(requirements_file):
    """Return primogen mentioned in the given file.
    Args:
        requirements_file (str): path to the requirements file to be parsed.
    Returns:
        (list): 3rd-party primogen dependencies contained in the file.
    """
    return [
        str(pkg.req) for pkg in parse_requirements(
            requirements_file, session=pip.download.PipSession()) if pkg.req is not None]


setup(name='probable_waffle',
      version='0.0.1',
      description='website',
      author='Martin',
      author_email='',
      classifiers=[],
      maintainer='Martin',
      maintainer_email='',
      url='https://github/nitram-iz/probable-waffle',
      packages=find_packages(exclude=('*.tests', '*.tests.*', 'tests.*', 'tests')),
      install_requires=requirements('requirements.txt'),
      tests_require=requirements('requirements-test.txt'))
