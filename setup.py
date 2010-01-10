from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='rctkdemos',
      version=version,
      description="rctk demo's",
      long_description="""\
A demo application for the remote control toolkit (rctk)""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Ivo van der Wijk',
      author_email='ivo@m3r.nl',
      url='http://opensource.m3r.nl/rctk',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'rctk',
          'pygments'
      ],
      entry_points={
        "console_scripts": [
        "demo = rctkdemos.all:main",
        "wsgidemo = rctkdemos.wsgidemo"
        ]
        }
      )
