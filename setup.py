#!/usr/bin/env python
# Generated by jaraco.develop 2.27.1
# https://pypi.python.org/pypi/jaraco.develop

import io
import sys

import setuptools

with io.open('README.rst', encoding='utf-8') as readme:
	long_description = readme.read()

needs_pytest = set(['pytest', 'test']).intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []
needs_sphinx = set(['release', 'build_sphinx', 'upload_docs']).intersection(sys.argv)
sphinx = ['sphinx'] if needs_sphinx else []
needs_wheel = set(['release', 'bdist_wheel']).intersection(sys.argv)
wheel = ['wheel'] if needs_wheel else []

setup_params = dict(
	name='pytest-runner',
	use_scm_version=True,
	author="Jason R. Coombs",
	author_email="jaraco@jaraco.com",
	description="Invoke py.test as distutils command with dependency "
		"resolution.",
	long_description=long_description,
	url="https://bitbucket.org/pytest-dev/pytest-runner",
	py_modules=['ptr'],
	install_requires=[
	],
	extras_require={
	},
	setup_requires=[
		'setuptools_scm>=1.9',
	] + pytest_runner + sphinx + wheel,
	tests_require=[
		'pytest>=2.8',
	],
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 2.6",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3",
	],
	entry_points = {
		'distutils.commands': [
			'ptr = ptr:PyTest',
			'pytest = ptr:PyTest',
		],
	},
)
if __name__ == '__main__':
	setuptools.setup(**setup_params)
