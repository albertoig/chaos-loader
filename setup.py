from setuptools import find_packages
from distutils.core import setup
from chaosloader.test.pytest import PyTest


dependencies = [
    'click==7.0',
    'configparser==3.7.3',
]

dev_dependencies = [
    'behave==1.2.6',
    'pytest==3.5.0',
    'semver==2.7.9',
    'flake8==3.7.7',
    'pytest-runner',
    'pytest'
]

setup(
    name='chaosloader',
    version='1.0.0',
    description='Chaos loader command line',
    author='Alberto Iglesias Gallego',
    url='git@github.com:albertoig/chaos-loader.git',
    packages=find_packages(exclude=['*tests']),
    include_package_data=True,
    install_requires=dependencies,
    extras_require={
        'dev': dev_dependencies
    },
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=dev_dependencies,
    test_suite='test.unittest',
    entry_points='''
        [console_scripts]
        chaosloader=chaosloader.src.cli:cli
    ''',
    py_modules=['chaosloader'],
    cmdclass={'test': PyTest},
)
