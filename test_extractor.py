import unittest
from regex_extractor import RegexDataExtractor

class TestRegexExtractor(unittest.TestCase):
    def setUp(self):
        self.extractor = RegexDataExtractor()
        self.test_text = """
            Contact: user@example.com, invalid@.com
            Website: https://www.example.com/path?q=search
            Phone: (123) 456-7890 or 123.456.7890
            Credit Card: 1234-5678-9012-3456
            Time: 14:30 or 2:30 PM
            HTML: <div class="test">, </div>, <img src="image.jpg">
            Hashtags: #ALU #Regex2023
            Prices: $19.99, $1,234.56
        """

    def test_all_patterns(self):
        results = self.extractor.extract_all(self.test_text)
        
        self.assertEqual(results['emails'], ['user@example.com'])
        self.assertEqual(results['urls'], ['https://www.example.com/path?q=search'])
        self.assertEqual(results['phone_numbers'], ['(123) 456-7890', '123.456.7890'])
        self.assertEqual(results['credit_cards'], ['1234-5678-9012-3456'])
        self.assertEqual(results['time'], ['14:30', '2:30 PM'])
        self.assertEqual(results['html_tags'], ['<div class="test">', '</div>', '<img src="image.jpg">'])
        self.assertEqual(results['hashtags'], ['#ALU', '#Regex2023'])
        self.assertEqual(results['currency'], ['$19.99', '$1,234.56'])

if __name__ == '__main__':
    unittest.main()