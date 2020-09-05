import unittest

from ..main import translate, categorise_lines, create_close_string
from ..match import match_quotes


class TestStringMethods(unittest.TestCase):

    def test_translate(self):
        variable = translate('"house"')
        self.assertEqual(variable, "maja")

    def test_match_quotes(self):
        variable = r'msgid "Django version 0.95 release notes"'
        variable2 = r'msgid ""'
        variable3 = r'msid ""'
        variable4 = r""

        result = match_quotes(variable)
        result2 = match_quotes(variable2)
        result3 = match_quotes(variable3)
        result4 = match_quotes(variable4)

        self.assertEqual(result, "Django version 0.95 release notes")
        self.assertEqual(result2, "")
        self.assertEqual(result3, "")
        self.assertEqual(result4, "")

    def test_create_close_string(self):
        variable = 'msgid "Django version 0.95 release notes"'
        variable2 = 'msgid "Suitability and API stability"'
        variable3 = 'msgid ""'
        variable4 = ""

        result = create_close_string(variable)
        result2 = create_close_string(variable2)
        result3 = create_close_string(variable3)
        result4 = create_close_string(variable4)

        self.assertEqual(result, 'msgstr "Django version 0.95 release notes"')
        self.assertEqual(result2, 'msgstr "Suitability and API stability"')
        self.assertEqual(result3, 'msgstr ""')
        self.assertEqual(result4, 'msgstr ')

    def test_categorise_lines(self):
        variable = ["# Translators:", "msgid """, "msgstr """, '"Project-Id-Version: django-docs\n"']
        variable2 = ['#: ../../../../sources/3.1/docs/releases/0.95.txt:7', 'msgid ""',
                     '"This represents a significant advance in Django development since the 0.91 "', 'msgstr ""']

        result = categorise_lines(variable)
        result2 = categorise_lines(variable2)

        self.assertEqual(result, [0, 1, 3, 0])
        self.assertEqual(result2, [0, 1, 4, 3])

    def test_solve(self):
        pass


if __name__ == '__main__':
    unittest.main()
