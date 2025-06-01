import re

def clean_text(text):
    #Remove commas from the text
    if not text:
        return ""
    return text.replace(",", "")

def clean_price(price):
    if not price:
        return 0.0
    # Remove currency symbols and commas, then convert to float
    return re.sub(r'[^\d.]', '', price.text.strip().replace("£", ""))
