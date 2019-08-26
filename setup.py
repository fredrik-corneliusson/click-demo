from setuptools import setup

setup(
    name='click-demo',
    version='0.1',
    py_modules=['demo_6'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        demo=demo_6:cli
    ''',
)