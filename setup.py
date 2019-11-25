import os.path

from setuptools import setup, find_packages

root_path = os.path.abspath(os.path.join(__file__, '..'))

setup(
	name='draw_rna',
	author='wuami',
	url='https://github.com/wuami/draw_rna/',
	packages=['draw_rna'],
	package_dir={'draw_rna':root_path},
	install_requires=[
		'matplotlib>=3.1.2'
	]
)