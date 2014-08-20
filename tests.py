import unittest
import binario


class WriterTests(unittest.TestCase):
    w = None;

    def test_init(self):
        w = binario.Writer("file.dat")
        self.assertIsInstance(w, binario.Writer)


if __name__ == '__main__':
    unittest.main()