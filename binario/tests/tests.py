import unittest
import binario


class AllTests(unittest.TestCase):
    w = None
    r = None

    def test_write_data(self):
        self.w = binario.Writer("file.dat")
        self.w.write_int(2014)
        self.w.write_int(-1)
        self.w.write_short(2014)
        self.w.write_short(-2014)
        self.w.write_bool(False)
        self.w.write_bool(True)
        self.w.write_string("Hi")
        self.w.write_double(3.14)
        self.w.close()
        self.assertEqual(self.w.current_file_size(), 28)

    def test_init(self):
        self.w = binario.Writer("file.dat")
        self.r = binario.Reader("file.dat")
        self.assertIsInstance(self.w, binario.Writer)
        self.assertIsInstance(self.r, binario.Reader)
        self.w.close()
        self.r.close()

    def test_read_input(self):
        self.test_write_data()
        self.r = binario.Reader("file.dat")
        self.assertEqual(self.r.get_file_size(), 28)
        self.assertEqual(self.r.read_int(), 2014)
        self.assertEqual(self.r.read_int(), -1)
        self.assertEqual(self.r.read_short(), 2014)
        self.assertEqual(self.r.read_short(), -2014)
        self.assertEqual(self.r.read_bool(), False)
        self.assertEqual(self.r.read_bool(), True)
        self.assertEqual(self.r.read_string(), "Hi")
        self.assertEqual(self.r.read_double(), 3.14)
        self.assertEqual(self.r.get_remaining_size(), 0)
