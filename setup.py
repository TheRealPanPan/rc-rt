import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="rc-rt",
    version="0.0.1",
    author="TRPP",
    author_email="therealpanpan@gmail.com",
    description=("Some happy coding"),
    license="MIT",
    keywords="Loloing",
    packages=find_packages(),
    long_description=read('README.md'),
    entry_points=dict(
        console_scripts=[
            'rc_rt = rc_rt.rc_rt:main'
        ]
    )
)
