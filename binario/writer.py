from struct import pack
from .byte_order import *
import os


class Writer:
    """ Writer lets an application write primitive data types to an underlying output file. """

    # Output file.
    file = None
    # The number of bytes written to the output file so far.
    written = 0
    is_closed_flag = False
    # Byte order, by default - NETWORK or BIG_ENDIAN
    byte_order = "!"
    # Mode - append new data to the end of file or rewrite it
    # By default - rewrite file
    mode = "wb"

    def __init__(self, file_name, byte_ordering=NETWORK, append=False):
        """
        Create new Writer instance and open file for writing.
        If it necessary, you can specify byte order - little-endian or big-endian.
        By default byte order is network(big-endian).
        Also you can specify write mode - rewrite existing file or append new data to the end of file.
        By default it will be rewriting existing files.
        """
        if append:
            self.mode = "ab"
            self.written = os.path.getsize(file_name)
        self.file = open(file_name, self.mode)
        if byte_ordering == LITTLE_ENDIAN:
            self.byte_order = "<"
        elif byte_ordering == BIG_ENDIAN:
            self.byte_order = ">"

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        """ Close output file and destroy object. """
        self.file.close()

    def close(self):
        """ Closes this output file. """
        self.is_closed_flag = True
        self.file.close()

    def is_closed(self):
        """ Check is file already closed. """
        return self.is_closed_flag

    def current_file_size(self):
        """ Return current size of file. """
        return self.written

    def flush(self):
        """ Flushes this output file. """
        self.file.flush()

    def get_file(self):
        """ Return current output file. """
        return self.file

    def write(self, byte):
        """
        Writes a byte buffer to the underlying output file.
        Raise exception when file is already closed.
        """
        if self.is_closed_flag:
            raise Exception("Unable to write - already closed!")
        self.written += len(byte)
        self.file.write(byte)

    def write_bool(self, flag):
        """ Writes a boolean to the underlying output file as a 1-byte value. """
        if flag:
            self.write(b"\x01")
        else:
            self.write(b"\x00")

    def write_short(self, number):
        """ Writes a short integer to the underlying output file as a 2-byte value. """
        buf = pack(self.byte_order + "h", number)
        self.write(buf)

    def write_int(self, number):
        """ Writes a integer to the underlying output file as a 4-byte value. """
        buf = pack(self.byte_order + "i", number)
        self.write(buf)

    def write_long(self, number):
        """ Writes a long integer to the underlying output file as a 8-byte value. """
        buf = pack(self.byte_order + "q", number)
        self.write(buf)

    def write_string(self, string):
        """ Writes a string to the underlying output file as a buffer of chars with UTF-8 encoding. """
        buf = bytes(string, 'UTF-8')
        length = len(buf)
        self.write_int(length)
        self.write(buf)

    def write_float(self, number):
        """ Writes a float to the underlying output file as a 4-byte value. """
        buf = pack(self.byte_order + "f", number)
        self.write(buf)

    def write_double(self, number):
        """ Writes a double to the underlying output file as a 8-byte value. """
        buf = pack(self.byte_order + "d", number)
        self.write(buf)