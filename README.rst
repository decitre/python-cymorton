========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - | |github-actions| |requires|
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |github-actions| image:: https://github.com/decitre/python-cymorton/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/decitre/python-cymorton/actions

.. |requires| image:: https://requires.io/github/decitre/python-cymorton/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/decitre/python-cymorton/requirements/?branch=master

.. |version| image:: https://img.shields.io/pypi/v/cymorton.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/cymorton

.. |wheel| image:: https://img.shields.io/pypi/wheel/cymorton.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/cymorton

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/cymorton.svg
    :alt: Supported versions
    :target: https://pypi.org/project/cymorton

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/cymorton.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/cymorton

.. |commits-since| image:: https://img.shields.io/github/commits-since/decitre/python-cymorton/v0.0.2.svg
    :alt: Commits since latest release
    :target: https://github.com/decitre/python-cymorton/compare/v0.0.2...master



.. end-badges

A morton code codec in c++/cython

* Free software: MIT license

Installation
============

::

    pip install cymorton

You can also install the in-development version with::

    pip install https://github.com/decitre/python-cymorton/archive/master.zip


Usage
============

::

cli::

    $ cymorton --help
    Usage: cymorton [OPTIONS] LAT LON Z

      Prints the Morton code for LAT and LON at Z level

    Options:
      --version  Show the version and exit.
      --help     Show this message and exit.

    $ cymorton 50.0 13.0 12
    23612293

Python call::


    >>> import cymorton.codec
    >>> cymorton.codec.convert_lat_lon_level_to_code(50.0, 13.0, 12)
    23612293
