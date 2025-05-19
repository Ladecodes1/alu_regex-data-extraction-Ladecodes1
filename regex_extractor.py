import re
from typing import Dict, List, Pattern, Tuple

class RegexDataExtractor:
    """Extracts structured data from text using regular expressions.
    
    Supported data types:
    - Emails
    - URLs
    - Phone numbers (US/CA formats)
    - Credit card numbers
    - Time (12-hour and 24-hour formats)
    - HTML tags
    - Hashtags
    - Currency amounts
    """
    
    def __init__(self):
        """Initialize all regex patterns."""
        self.patterns: Dict[str, Tuple[Pattern, str]] = {
            'emails': (self._compile_email_regex(), 'Email addresses'),
            'urls': (self._compile_url_regex(), 'URLs'),
            'phone_numbers': (self._compile_phone_regex(), 'Phone numbers'),
            'credit_cards': (self._compile_credit_card_regex(), 'Credit card numbers'),
            'time': (self._compile_time_regex(), 'Time (12h/24h format)'),
            'html_tags': (self._compile_html_tag_regex(), 'HTML tags'),
            'hashtags': (self._compile_hashtag_regex(), 'Hashtags'),
            'currency': (self._compile_currency_regex(), 'Currency amounts')
        }

    # ---- Regex Compilation Methods ----
    def _compile_email_regex(self) -> Pattern:
        """Matches most common email formats."""
        return re.compile(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        re.IGNORECASE
    )

    def _compile_url_regex(self) -> Pattern:
        """Matches HTTP/HTTPS URLs with optional subdomains and paths."""
        return re.compile(
            r"https?://(?:www\.)?[a-z0-9-]+(?:\.[a-z]{2,})+(?:[/?#][^\s]*)?",
            re.IGNORECASE
        )

    def _compile_phone_regex(self) -> Pattern:
        """Matches US/CA phone formats: (123) 456-7890, 123-456-7890, etc."""
        return re.compile(
            r"(?:\(\d{3}\)\s?|\d{3}[-\.])\d{3}[-\.]\d{4}"
        )

    def _compile_credit_card_regex(self) -> Pattern:
        """Matches 16-digit credit cards with optional separators."""
        return re.compile(
            r"\b(?:\d{4}[- ]?){3}\d{4}\b"
        )

    def _compile_time_regex(self) -> Pattern:
        """Matches 12-hour (2:30 PM) and 24-hour (14:30) time formats."""
        return re.compile(
            r"(?:1[0-2]|0?[1-9])(?::[0-5]\d)?\s?(?:[AP]M)|(?:2[0-3]|[01]?[0-9]):[0-5][0-9]",
            re.IGNORECASE
        )

    def _compile_html_tag_regex(self) -> Pattern:
        """Matches HTML tags (opening, closing, self-closing)."""
        return re.compile(
            r"<\/?[\w]+(?:\s+[^>]*)?>"
        )

    def _compile_hashtag_regex(self) -> Pattern:
        """Matches hashtags (letters, numbers, underscores)."""
        return re.compile(
            r"#\w+",
            re.IGNORECASE
        )

    def _compile_currency_regex(self) -> Pattern:
        """Matches currency amounts like $19.99 or $1,234.56."""
        return re.compile(
            r"\$[\d,]+(?:\.\d{2})?"
        )

    # ---- Main Extraction Method ----
    def extract_all(self, text: str) -> Dict[str, List[str]]:
        """Extract all supported data types from input text.
        
        Args:
            text: Input string to search through
            
        Returns:
            Dictionary with keys as data types and values as lists of matches
        """
        results = {}
        for data_type, (pattern, _) in self.patterns.items():
            results[data_type] = pattern.findall(text)
        return results