from setuptools import setup

setup(
    name='khabuild',
    version='0.1',
    py_modules=['khabuild'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        khabuild=khabuild:main
    ''',
)