# bass-utils

[![Build Status](https://travis-ci.org/basameera/bass-utils.svg?branch=master)](https://travis-ci.org/basameera/bass-utils)

---

## To Do

* [ ] Add a script to do easy version numbering (e.g. in skunkwork)
* [ ] Start two new packages
    1. Python pkg utils
    2. Python pkg that works in CLI

---

## Notes

### Python module structuring

https://python-packaging.readthedocs.io/en/latest/minimal.html
https://dev.to/codemouse92/dead-simple-python-project-structure-and-imports-38c6
https://docs.python-guide.org/writing/structure/

### Setup

* Learn more: https://github.com/kennethreitz/setup.py

### unit-testing

* Keep all inside `tests/` folder

### Travis CI

* First push the git without `.travis.yaml` file.
* Then add the repo.in Travis-CI
* Then push git with `.travis.yaml` file.

## PyPI

1. Run `bash pkg_build` 

2. Setup `$HOME/.pypirc` file

``` 
[distutils]
index-servers=
    pypi
    testpypi

[pypi]
username: __token__
password: API key starting with pypi-

[testpypi]
repository: https://test.pypi.org/legacy/
username: __token__
password: API key starting with pypi-
```

3. Secure the file : `chmod 600 ~/.pypirc` 

After running `bash pkg_build` follow steps in https://truveris.github.io/articles/configuring-pypirc/

### Resources

#### Python packaging

https://packaging.python.org/tutorials/packaging-projects/
https://gist.github.com/nikhilkumarsingh/08a3ab33d1c3ad955fe3f88743aef322

https://python-packaging.readthedocs.io/en/latest/minimal.html#publishing-on-pypi

https://github.com/nikhilkumarsingh/weather-reporter
https://www.youtube.com/watch?v=RgfOjrjhCMY

#### Twine

https://github.com/pypa/twine

