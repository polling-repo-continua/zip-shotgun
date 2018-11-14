#!/usr/bin/env python3

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as readme_file:
    readme = readme_file.read()

setup(
    name='ZIP Shotgun',
    version='1.0.0',
    packages=find_packages(),
    description="TODO",  # TODO
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Janusz Piechowka (https://github.com/jpiechowka)',
    url='https://github.com/jpiechowka/zip-shotgun',
    install_requires=['click>=7.0'],
    python_requires='>=3',
    license='GNU General Public License v3.0',
    keywords='todo',  # TODO
    entry_points={
        'console_scripts': [
            'zip-shotgun = zip_shotgun.zip_shotgun_main:zip_shotgun_cli',
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop'
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Environment :: Console',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Security',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ],
    zip_safe=False
)
