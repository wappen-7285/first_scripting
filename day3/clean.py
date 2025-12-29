import re

def clean_text(text):
    text = re.sub(r"\s+", "" , text)
    text = re.sub(r"[\[][\]]", "", text)
    return text.strip()

sample = " [ Hello \n World ] "
print(clean_text(sample))
