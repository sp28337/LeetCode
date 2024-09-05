from unittest import TestCase, main

from tests import KnuthMorrisPratt

test = KnuthMorrisPratt()


class KnuthMorrisPrattTest(TestCase):

    def test_kmp_success(self):
        self.assertEqual(test.kmp("лилилось лилилась", "лилилась"), True)
        self.assertEqual(test.kmp("лилилось лилилось", "лилилась"), False)

    def test_wrong_first_arg(self):
        with self.assertRaises(TypeError):
            self.assertEqual(test.kmp(123, "лилилось"))

    def test_wrong_second_arg(self):
        with self.assertRaises(TypeError):
            self.assertEqual(test.kmp("лилилось", 123))


if __name__ == "__main__":
    main()
