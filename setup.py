from setuptools import setup, find_packages
import os

version = '1.0.0'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.md')
    + '\n' +
    read('js', 'pace', 'test.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.pace',
    version=version,
    description="fanstatic Pace.",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Heberte Fernandes de Moraes',
    author_email='brebete@gmail.com',
    url='https://github.com/hmoraes/js.pace',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'setuptools',
    ],
    entry_points={
        'fanstatic.libraries': [
            'pace = js.pace:library',
        ],
    },
)
