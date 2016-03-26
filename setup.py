from setuptools import setup

setup(
    name="base116676",
    version="0.0",
    install_requires=[
        "tweepy",
        "docopt",
    ],
    author="Robin Wellner",
    author_email="gyvox.public@gmail.com",
    description="Cram data in a small number of code points",
    long_description=open('README.md').read(),
    py_modules=['base116676.base', 'base116676.twitput', 'base116676.minimize', 'base116676.codes', 'base116676.gencodes'],
    license="ISC",
    url='https://github.com/gvx/base116676',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Database',
    ],
    keywords='unicode compression twitter',
)