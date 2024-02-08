[![test][test_badge]][test_target]
[![version][version_badge]][pypi]
[![wheel][wheel_badge]][pypi]
[![python version][python_versions_badge]][pypi]
[![python implementation][python_implementation_badge]][pypi]
[![commits_since][commits_since_badge]][pypi]


A morton code codec in c++/cython


## Installation

    pip install cymorton


## Usage

Library:

```python
>>> from cymorton.codec import convert_lat_lon_level_to_code
>>> convert_lat_lon_level_to_code(9.165507, 105.219986, 12) == 24145105
True
```

```python
>>> from cymorton.codec import test_convert_xy_level_to_code
>>> convert_xy_level_to_code(5, 2, 3) == 0b1011001
True
```

CLI:

```shell
$ cymorton --help
Usage: cymorton [OPTIONS] LAT LON Z

  Prints the Morton code for LAT and LON at Z level

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.
```

```shell
$ cymorton 9.165507 105.219986 12
24145105
```

[pypi]: https://pypi.org/project/cymorton
[test_badge]: https://github.com/decitre/python-cymorton/actions/workflows/test.yml/badge.svg
[test_target]: https://github.com/decitre/python-cymorton/actions
[version_badge]: https://img.shields.io/pypi/v/cymorton.svg
[wheel_badge]: https://img.shields.io/pypi/wheel/cymorton.svg
[python_versions_badge]: https://img.shields.io/pypi/pyversions/cymorton.svg
[python_implementation_badge]: https://img.shields.io/pypi/implementation/cymorton.svg
