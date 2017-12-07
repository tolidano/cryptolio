from setuptools import setup

VERSION = open('VERSION').read().strip()
with open('requirements.txt') as f:
    INSTALL_REQUIRES = f.read().splitlines()
with open('requirements.txt') as f:
    TEST_REQUIRES = f.read().splitlines()
with open('LICENSE') as f:
    LICENSE = f.read()
with open('README.rst') as f:
    README = f.read()

setup(
    name='Cryptolio',
    version=VERSION,
    author='Shawn Tolidano',
    author_email='shawn@tolidano.com',
    packages=['cryptolio'],
    url='https://github.com/tolidano/cryptolio',
    download_url='https://github.com/toliadno/cryptolio/tarball/%s' % VERSION,
    license=LICENSE,
    description='Cryptocurrency portfolio manager and simulator',
    keywords='cryptocurrency portfolio manager simulator bitcoin btc ethereum eth litecoin ltc',
    long_description=README,
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    tests_require=TEST_REQUIRES,
    test_suite='cryptolio/test',
    classifiers=[
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.2',
      'Programming Language :: Python :: 3.3',
      'Programming Language :: Python :: 3.4',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Development Status :: 3 - Alpha',
      'License :: Freely Distributable',
      'Natural Language :: English',
      'Operating System :: OS Independent',
      'Topic :: Utilities',
    ],
)
