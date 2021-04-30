#!/usr/bin/env python3

"""The setup script."""

from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.read().strip().split('\n')

with open('README.md') as f:
    long_description = f.read()
setup(
    maintainer='Project Pythia Team',
    maintainer_email='',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
    ],
    description='Provides utility functions for accessing data repository for Project Pythia examples/notebooks',
    install_requires=requirements,
    license='Apache Software License 2.0',
    long_description_content_type='text/markdown',
    long_description=long_description,
    include_package_data=True,
    package_data={'pythia_datasets': ['registry.txt']},
    keywords='Pythia, Pooch',
    name='pythia-datasets',
    packages=find_packages(include=['pythia_datasets', 'pythia_datasets.*']),
    entry_points={},
    url='https://github.com/ProjectPythia/pythia-datasets',
    project_urls={
        'Documentation': 'https://github.com/ProjectPythia/pythia-datasets',
        'Source': 'https://github.com/ProjectPythia/pythia-datasets',
        'Tracker': 'https://github.com/ProjectPythia/pythia-datasets/issues',
    },
    use_scm_version={
        'version_scheme': 'post-release',
        'local_scheme': 'dirty-tag',
    },
    setup_requires=['setuptools_scm', 'setuptools>=30.3.0'],
    zip_safe=False,
)
