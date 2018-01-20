import unittest
from feature_extraction.post_processing.regex.regex_entity_extraction import EntityExtraction
import re


class RegexPostLogicTest(unittest.TestCase):
    def test_match_fail(self):
        text = "I am a super saiyan"
        regex_array = [
            re.compile(
                r"\[[123]\]" + r".+" + r"(demand|réclam)(ait|e|ent|aient)" + r" la résiliation du bail",
                re.IGNORECASE
            ),
            re.compile(
                r"\[[123]\]" + r".+une demande en résiliation de bail",
                re.IGNORECASE
            )
        ]
        regex_type = 'BOOLEAN'
        result = EntityExtraction.match_any_regex(text, regex_array, regex_type)
        self.assertFalse(result[0])
        self.assertEqual(result[1], 0)

    def test_match_money(self):
        text = "[3] word locateur 50 $ dommages-intérêts"
        regex_array = [
            re.compile(
                r"\[[123]\]" + r".+" + r"locat(eur|rice)(s)?" +
                r".*" + r"(\d+(\s|,)){1,4}(\s\$|\$)" + r".*dommages-intérêts",
                re.IGNORECASE
            )]
        regex_type = 'MONEY_REGEX'
        result = EntityExtraction.match_any_regex(text, regex_array, regex_type)
        self.assertTrue(result[0])
        self.assertEqual(int(result[1]), 50)

    def test_match_boolean(self):
        text = "[3] une demande en résiliation de bail"
        regex_array = [
            re.compile(
                r"\[[123]\]" + r".+" + r"(demand|réclam)(ait|e|ent|aient)" + r" la résiliation du bail",
                re.IGNORECASE
            ),
            re.compile(
                r"\[[123]\]" + r".+une demande en résiliation de bail",
                re.IGNORECASE
            )
        ]
        regex_type = 'BOOLEAN'
        result = EntityExtraction.match_any_regex(text, regex_array, regex_type)
        self.assertTrue(result[0])
        self.assertEqual(result[1], 1)