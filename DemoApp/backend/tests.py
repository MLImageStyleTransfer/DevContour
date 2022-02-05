import unittest
import controllers.black_white as func


class TestApp(unittest.TestCase):

    def test1(self):
        self.assertEqual(func.black_white_transform(), 'Hello world!')


if __name__ == '__main__':
    unittest.main()
