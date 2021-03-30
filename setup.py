#!/usr/bin/env python

import os

import setuptools.command.build_py
import setuptools.command.develop
from setuptools import find_packages, setup

version = '0.0.1'
cwd = os.path.dirname(os.path.abspath(__file__))

class build_py(setuptools.command.build_py.build_py):  # pylint: disable=too-many-ancestors
    def run(self):
        self.create_version_file()
        setuptools.command.build_py.build_py.run(self)

    @staticmethod
    def create_version_file():
        print('-- Building version ' + version)
        version_path = os.path.join(cwd, 'version.py')
        with open(version_path, 'w') as f:
            f.write("__version__ = '{}'\n".format(version))

class develop(setuptools.command.develop.develop):
    def run(self):
        build_py.create_version_file()
        setuptools.command.develop.develop.run(self)


requirements = open(os.path.join(cwd, 'requirements.txt'), 'r').readlines()
with open('README.md', "r", encoding="utf-8") as readme_file:
    README = readme_file.read()


setup(
    name='coqpit',
    version=version,
    url='https://github.com/erogol/coqpit',
    author='Eren Gölge',
    author_email='egolge@coqui.ai',
    description='Simple (maybe too simple), light-weight config management through python data-classes.',
    long_description=README,
    long_description_content_type="text/markdown",
    license='',
    include_package_data=True,
    packages=find_packages(include=['coqui*']),
    project_urls={
        'Documentation': 'https://github.com/coqui-ai/TTS/wiki',
        'Tracker': 'https://github.com/coqui-ai/TTS/issues',
        'Repository': 'https://github.com/coqui-ai/TTS',
        'Discussions': 'https://github.com/coqui-ai/TTS/discussions',
    },
    cmdclass={
        'build_py': build_py,
        'develop': develop,
    },
    install_requires=requirements,
    python_requires='>=3.6.0',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        'Development Status :: 3 - Alpha',
        "Intended Audience :: Developers",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows"
    ],
    zip_safe=False
)