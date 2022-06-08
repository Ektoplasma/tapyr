from setuptools import setup

setup(
    name='tapyr',
    version='0.1.0',
    packages=['.'],
    url='https://github.com/tap-ir/tapyr',
    license='AGPLv3.0',
    author='Solal Jacob',
    author_email='',
    description='Python binding for TAPIR',
    install_requires=[
        "setuptools~=58.1.0",
        "requests~=2.27.1"
    ]
)
