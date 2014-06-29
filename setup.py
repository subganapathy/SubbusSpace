#!/usr/bin/env python

from setuptools import setup, find_packages # always prefer setuptools over distutils

setup(name = 'SubbusSpace',
      version = '0.1',
      description = 'My personal space with full-test search.',
      author = 'Subramanian Ganapathy',
      author_email = 'subramanian.ganapathy86@gmail.com',
      url = 'http://www.amazon.com/',
      packages = find_packages(exclude = ['contrib', 'docs', 'tests*']),
      package_data = {
          'http_server' : ['http_server_config.cfg'],
          'data_reader' : ['data_reader_config.cfg'],
          'data_writer' : ['data_writer_config.cfg'],
          'index_manager' : ['index_manager_config.cfg']
          },
      )
