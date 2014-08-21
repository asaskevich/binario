from struct import unpack
from .byte_order import *
import os


class Reader:
    """ Reader lets an application read primitive data types from an underlying input file. """

    # Input file.
    file = None
    # Length of the input file.
    file_size = 0
    # Count of already read bytes.
    read_count = 0
    is_closed_flag = False
    # Byte order, by default - NETWORK or BIG_ENDIAN
    byte_order = "!"

    def __init__(self, file_name, byte_ordering=NETWORK):
        """
        Create new Reader instance and open file for reading.
        If it necessary, you can specify byte order - little-endian or big-endian.
        By default byte order is network(big-endian).
        """
        self.file = open(file_name, "rb")
        self.file_size = os.path.getsize(file_name)
        if byte_ordering == LITTLE_ENDIAN:
            self.byte_order = "<"
        elif byte_ordering == BIG_ENDIAN:
            self.byte_order = ">"

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        """ Close input file and destroy object. """
        self.file.close()

    def close(self):
        """ Closes this input file. """
        self.file.close()
        self.is_closed_flag = True

    def is_closed(self):
        """ Check is input file already closed. """
        return self.is_closed_flag

    def flush(self):
        """ Flushes this input file. """
        self.file.flush()

    def get_file(self):
        """ Return current input file. """
        return self.file

    def get_position(self):
        """ Return count of bytes already taken from the input file. """
        return self.read_count

    def get_file_size(self):
        """ Returns the length of the file. """
        return self.file_size

    def is_eof(self):
        """ Check is already reached end of file. """
        return self.read_count >= self.file_size

    def get_remaining_size(self):
        """ Return remaining count of bytes, available for reading. """
        return self.file_size - self.read_count

    def seek(self, pos):
        """ Move to new input file position. If position is negative or out of file, raise Exception. """
        if (pos > self.file_size) or (pos < 0):
            raise Exception("Unable to seek - position out of file!")
        self.file.seek(pos)

    def read(self, size=1):
        """
        Read byte buffer with specified size from input file.
        Raise exception in two cases:
            - File already closed.
            - Not enough data to read.

        Keyword arguments:
        size -- size of buffer to read (default 1)
        """
        if self.is_closed_flag:
            raise Exception("Unable to read - already closed!")
        if self.get_remaining_size() < size:
            raise Exception("Unable to read byte buffer - too short remaining data size!")
        self.read_count += size
        return self.file.read(size)

    def read_string(self):
        """ Read string from input file with UTF-8 encoding. """
        length = self.read_int()
        return str(self.read(length).decode("UTF-8"))

    def read_byte(self):
        """ Read byte from input file. """
        return self.read()[0]

    def read_bool(self):
        """ Read boolean from the underlying input file as a 1-byte value. """
        return self.read_byte() != 0

    def read_int(self):
        """ Read signed integer from the underlying input file as a 4-byte value.  """
        buf = self.read(4)
        return unpack(self.byte_order + "i", buf)[0]

    def read_short(self):
        """ Read signed short from the underlying input file as a 2-byte value.  """
        buf = self.read(2)
        return unpack(self.byte_order + "h", buf)[0]

    def read_long(self):
        """ Read signed long from the underlying input file as a 8-byte value.  """
        buf = self.read(8)
        return unpack(self.byte_order + "q", buf)[0]

    def read_float(self):
        """ Read float from the underlying input file as a 4-byte value.  """
        buf = self.read(4)
        return unpack(self.byte_order + "f", buf)[0]

    def read_double(self):
        """ Read double from the underlying input file as a 8-byte value.  """
        buf = self.read(8)
        return unpack(self.byte_order + "d", buf)[0]
