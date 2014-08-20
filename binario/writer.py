from struct import pack


class Writer:
    """ Writer lets an application write primitive data types to an underlying output file. """

    # Output file.
    file = None
    # The number of bytes written to the output file so far.
    written = 0
    is_closed_flag = False

    def __init__(self, file_name):
        """ Create new Writer instance and open file for writing. """
        self.file = open(file_name, "wb")

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
        buf = pack("!h", number)
        self.write(buf)

    def write_int(self, number):
        """ Writes a integer to the underlying output file as a 4-byte value. """
        buf = pack("!i", number)
        self.write(buf)

    def write_long(self, number):
        """ Writes a long integer to the underlying output file as a 8-byte value. """
        buf = pack("!q", number)
        self.write(buf)

    def write_string(self, string):
        """ Writes a string to the underlying output file as a buffer of chars with UTF-8 encoding. """
        buf = bytes(string, "UTF-8")
        length = len(buf)
        self.write_int(length)
        self.write(buf)

    def write_float(self, number):
        """ Writes a float to the underlying output file as a 4-byte value. """
        buf = pack("!f", number)
        self.write(buf)

    def write_double(self, number):
        """ Writes a double to the underlying output file as a 8-byte value. """
        buf = pack("!d", number)
        self.write(buf)