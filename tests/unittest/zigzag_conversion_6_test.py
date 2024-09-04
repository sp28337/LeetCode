from unittest import TestCase, main
from problems import ZigzagConversion


class TestZigzagConversion(TestCase):

    def test_empty_string(self):
        self.assertEqual(ZigzagConversion.convert("", 1), "")

    def test_good_input(self):
        self.assertEqual(ZigzagConversion.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")

    def test_rows_more_than_length(self):
        self.assertEqual(ZigzagConversion.convert("PAYPA", 7), "PAYPA")

    def test_wrong_input(self):
        with self.assertRaises(TypeError):
            self.assertEqual(ZigzagConversion.convert(1325, 5), "")

    def test_wrong_value(self):
        with self.assertRaises(ValueError):
            self.assertEqual(ZigzagConversion.convert("SDHSDHHSDA", 1001), "SDHSDHHSDA")

    def test_wrong_type_second_arg(self):
        with self.assertRaises(TypeError):
            self.assertEqual(ZigzagConversion.convert("SDHSDHHSDA", "Hi"), "SDHSDHHSDA")


if __name__ == "__main__":
    main()
