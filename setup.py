"""
A python library for randint.com's api.
"""

from setuptools import setup

setup(
    name='pyrandint',
    version='0.1',
    license='BSD',
    description="A python library for randint.com's api.",
    long_description=__doc__,
    packages=['pyrandint'],
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
