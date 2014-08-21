binario [![Build Status](https://drone.io/github.com/asaskevich/binario/status.png)](https://drone.io/github.com/asaskevich/binario/latest)
=====
Simple work with binary data in Python.

[![Coverage Status](https://coveralls.io/repos/asaskevich/binario/badge.png?branch=master)](https://coveralls.io/r/asaskevich/binario?branch=master) [![PyPI version](https://badge.fury.io/py/binario.svg)](http://badge.fury.io/py/binario)
[![PyPi downloads](http://img.shields.io/pypi/dm/binario.svg)](https://pypi.python.org/pypi/binario/) [![Supported Python versions](https://pypip.in/py_versions/binario/badge.svg)](https://pypi.python.org/pypi/binario/) [![Development Status](https://pypip.in/status/binario/badge.svg)](https://pypi.python.org/pypi/binario/)

### What is the binario?
**binario** is the Python package that lets an application read/write primitive data types from an underlying input/output stream as binary data.

### And which primitive data types it can process?
It can work with booleans, integers, shorts, long integers, floats, doubles, strings and any byte buffers.

### How to write data?
It's simple. Just create instance of `Writer` and then do your work:

```python
>>> import binario
>>> w = binario.Writer("file.dat")
>>> w.write_short(2014)
>>> w.write_bool(True)
>>> w.write_float(3.1415)
>>> w.write_string("Hello, world!")
>>> w.write(bytes([128, 20, 10, 255, 0]))
```

### And how to read data?
It's simple too. Like outputting, create `Reader` and then do your work:

```python
>>> import binario
>>> r = binario.Reader("file.dat")
>>> r.read_short()
2014
>>> r.read_bool()
True
>>> r.read_float()
3.1415
>>> r.read_string()
"Hello, world!"
>>> r.read(5)
b'\x80\x14\n\xff\x00'
```

### Which byte order specified by default?
By default it is `network` order (or `big-endian`).

### Okay, it is good, but if I want to change byte order for `Reader` or `Writer`?
Not a problem! Just specify it:

```python
>>> import binario
>>> r = binario.Reader("file.dat", binario.LITTLE_ENDIAN)
>>> w = binario.Writer("another_file.dat", binario.BIG_ENDIAN)
```

### What about append new data to existing file?
Yeah, it is also very simple:

```python
>>> import binario
>>> w = binario.Writer("incomplete_file.dat", append=True)
```

### How to install(upgrade) this package?
Just type in your terminal:
```bash
$ pip install binario
$ pip install binario --upgrade
```

### Contribution
If you do have a contribution for the package feel free to put up a Pull Request or open Issue on GitHub repo.
