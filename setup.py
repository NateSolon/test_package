from setuptools import setup

setup(
	name = 'test_package',
	version = '0.0.1',
	description = 'blerg',
	py_modules = ['hello_world'],
	package_dir = {'':'src'}
)