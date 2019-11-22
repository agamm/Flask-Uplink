#!/usr/bin/env python
from setuptools import find_packages, setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='Flask-Uplink',
    version='0.01',
    url='https://github.com/agamm/flask-uplink',
    license='MIT',
    author='Agam More',
    author_email='agam360@gmail.com',
    maintainer='Agam More',
    maintainer_email='agam360@gmail.com',
    description='Live realtime server rendered HTML inspired by elixir LiveView.',
    long_description=readme,
    packages=find_packages(exclude=('tests',)),
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'Flask-SocketIO'
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
