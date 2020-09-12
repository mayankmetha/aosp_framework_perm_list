#!/usr/bin/env python

import sys

from setuptools import setup, find_packages

if sys.version_info.major == 3 and sys.version_info.minor < 3:
    print('Unfortunately, your python version is not supported!\n Please upgrade at least to python 3.3!')
    sys.exit(1)

if sys.platform == 'darwin' or sys.platform == 'win32':
    print('Unfortunately, we do not support your platform %s' % sys.platform)
    sys.exit(1)

install_requires = []

setup(name='aosp_framework_perm_list',
      version='1.0.0',
      description='Extract translated descriptions of permissions and groups from AOSP.',
      author='mayankmetha',
      author_email='',
      url='https://github.com/mayankmetha/aosp_framework_perm_list',
      packages=find_packages(exclude=['*.tests', '*.tests.*', 'test*', 'tests']),
      install_requires=install_requires,
      python_requires='>=3.5, <4',
      scripts=['./aosp_framework_perm_list/aosp_framework_perm_list'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: GNU General Public License v3',
          'Natural Language :: English',
          'Topic :: Security',
          'Topic :: Utilities',
          'Programming Language :: Python :: 3 :: Only',
      ]
      )
