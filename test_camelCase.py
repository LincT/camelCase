from unittest import main, TestCase
import camelCase


class CamelTest(TestCase):

    def test_conversion(self):
        print('test_conversion')
        self.assertEqual(camelCase.convert('test text'), 'testText')

    def test_banner(self):
        self.assertEqual(camelCase.display_banner('test').strip("\n").strip("\r"), '****\ntest\n****')

    def test_instructions(self):
        self.assertEqual('test', str(camelCase.instructions('test')).strip("\n"))


if __name__ == '__main__':
    main
