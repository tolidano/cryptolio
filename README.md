Cryptolio - Cryptocurrency Portfolio Manager and Simulator
============================================================

[![CircleCI](https://circleci.com/gh/tolidano/cryptolio/tree/master.svg?style=svg&circle-token=ee9c3dee22d9d1309f54504e52018f844c2e9cf8)](https://circleci.com/gh/tolidano/cryptolio/tree/master)

Copyright Shawn Tolidano, All Rights Reserved.

Say something.

What is this?
-------------

- Say something

Say something

Quickstart
----------

### Using Cryptolio

If you just want to jump in and use it, follow this simple set of steps:

1. API Key and Secret

In code, if you've followed the above, you would do the following:
```
from __future__ import print_function
WRITE_CODE
```

### Setup for Development

If you are interested in doing development on Cryptolio, you need the
following packages: 
- python (sudo yum install python27, sudo apt-get
install python)
- python development (sudo yum install python27-devel,
sudo apt-get install python-devel)
- pip (sudo yum install python27-pip,
sudo apt-get install python-pip)
- virtualenv (sudo pip install
virtualenv)
- make (sudo yum install make, sudo apt-get install make)

You run: 
- make venv (create a virtualenv)
- \`make active\` (activate the virtualenv, the backticks are important)
- make dev (setuptools for development)

Now you’re ready to develop.

Be sure to: 
- Keep code coverage over 90%
- Write relevant unit tests
- Write Python doc strings
- Regenerate coverage and docs (make covhtml and make docs)

How This Works
--------------

Say something.

Caching values
--------------

If you want to cache values, consider also adding:
[pylru](https://pypi.python.org/pypi/pylru/) Then you can write a
function in your codebase like:

```python
import pylru
@lrudecorator(100)
def get_from_countdown(line, station):
    return COUNTDOWN.get(line, station)
```
Building documentation
----------------------

To build the documentation from the python docstrings, run:

    make docs

And you can browse those here:
\<CRYPTOLIO\>/docs/html/index.html

Running tests
-------------

All tests are in the cryptolio/test/ directory. To run them do the
following:

    make test

You can also generate a coverage report:

    make cov

You can generate the HTML version:

    make covhtml

You can browse this locally from:
\<CRYPTOLIO\>/docs/cov/index.html
