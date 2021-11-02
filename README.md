# re2c Python Distributions

[![PyPI Release](https://img.shields.io/pypi/v/re2c.svg)](https://pypi.org/project/re2c)

[re2c](https://re2c.org/) is a free and open-source lexer generator for C, C++ and Go with a focus on generating fast code.

This project packages the `re2c` (and `re2go`) utility as a Python package. It allows you to install `re2c` from PyPI:

```
python -m pip install re2c
```

## Acknowledgements

This repository builds off the following projects:

* The [re2c](https://github.com/skvadrik/re2c) project
* [scikit-build](https://github.com/scikit-build/scikit-build) to simplify the building a Python wheel from a CMake project
* [cibuildwheel](https://github.com/pypa/cibuildwheel) for managing the CI builds that create wheels on a large number of platforms
* [CMake](https://github.com/scikit-build/cmake-python-distributions) and [Ninja](https://github.com/scikit-build/ninja-python-distributions) for native Python wheel packaging examples, along with experience from contributing to the [swig](https://github.com/nightlark/swig-pipy) and [clang-format](https://github.com/ssciwr/clang-format-wheel) wheel packages

Thanks to GitHub for providing the free CI resources to open source projects that are used to build these wheels.
