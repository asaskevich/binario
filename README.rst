binario
=======
Simple work with binary data.

What is the binario?
--------------------
**binario** is the Python package that lets an application read/write primitive data types from an underlying input/output stream as binary data.

And which primitive data types it can process?
----------------------------------------------
It can work with booleans, integers, shorts, long integers, floats, doubles, strings and any byte buffers.

How to write data?
------------------
It's simple. Just create instance of `Writer` and then do your work:

>>> import binario
>>> w = binario.Writer("file.dat")
>>> w.write_short(2014)
>>> w.write_bool(True)
>>> w.write_float(3.1415)
>>> w.write_string("Hello, world!")
>>> w.write(bytes([128, 20, 10, 255, 0]))


And how to read data?
---------------------
It's simple too. Like outputting, create `Reader` and then do your work:

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

How to install this package?
----------------------------
Just type in your terminal `pip install binario`

Contribution
------------
If you do have a contribution for the package feel free to put up a Pull Request or open Issue on GitHub repo: http://github.com/asaskevich/binario.