# 🔍 Regex Data Extraction Hackathon

This project demonstrates the use of Python and regular expressions (re) to extract structured data from unstructured text.

## 🌟 Features
The script can extract the following from text:
- 📧 Email addresses
- 🌐 URLs
- 🏷️ HTML tags
- 🏷️ Hashtags
- 💰 Currency amounts (USD)
- ☎️ Phone numbers
- 🕒 Time formats
- 💳 Credit card numbers

## 📁 File Structure
alu_regex-data-extraction-Ladecodes1/
├── regex_extractor.py # Contains all extractors
├── test_extractor.py # Unit tests
├── data_sample.txt # Sample data
└── README.md


## 🧰 Requirements
- Python 3.7+
- `re` module (built-in)

## 🚀 Running the Script
1. Clone the repository:
```bash
git clone https://github.com/Ladecodes1/alu_regex-data-extraction-Ladecodes1.git
Run the extractor:

bash
python3 regex_extractor.py
🧪 Sample Output
Example output from data_sample.txt:

============
Emails
============
- user@example.com
- firstname.lastname@company.co.uk

============
URLs
============
- https://www.example.com
- https://subdomain.example.org/page

============
HTML Tags
============
- <p>
- <div class="example">
- <img src="image.jpg">

============
Hash Tags
============
- #example
- #ThisIsAHashtag

============
Currencies
============
- $19.99
- $1,234.56
🧠 Implementation Notes
Regex Patterns:

Email: RFC 5322 compliant

URLs: Supports HTTP/HTTPS with subdomains

HTML Tags: Handles attributes

Currency: USD format with commas

Edge Cases:

Skips invalid emails (e.g., user@.com)

Handles multiple currency formats

Validates credit card separators (spaces/dashes)

Testing:

bash
python3 test_extractor.py
📝 Key Improvements Over Base Requirements
Added phone number and credit card extraction

Implemented class-based architecture

Includes comprehensive unit tests

Handles international phone formats

👨‍💻 Author
Lade - ALU Software Engineering Student