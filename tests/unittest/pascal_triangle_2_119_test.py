from unittest import TestCase, main

from tests import get_row


class PascalTriangle2(TestCase):
    def test1(self):
        self.assertEqual(get_row(1), [1, 1])

    def test2(self):
        self.assertEqual(get_row(0), [1])

    def test3(self):
        self.assertEqual(get_row(None), None)

    def test4(self):
        self.assertEqual(get_row(3), [1, 3, 3, 1])

    def test5(self):
        self.assertEqual(get_row(4), [1, 4, 6, 4, 1])

    def test6(self):
        self.assertEqual(get_row("abc"), None)

    def test7(self):
        self.assertEqual(get_row(1.5436), None)

    def test8(self):
        self.assertEqual(get_row({1: "4", 2: "5"}), None)

    def test9(self):
        self.assertEqual(get_row([1, 3, "35"]), None)


if __name__ == "__main__":
    main()
