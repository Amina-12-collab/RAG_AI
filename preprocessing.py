import re

text = """
   PYTHON PROGRAMMING!!!

Python is a programming language.


   It is easy to learn.

Python is used in AI...
"""

text = text.lower()
text = re.sub(r'\s+', ' ', text)
text = re.sub(r'[!]+', '', text)
print("Preprocessed Text:")
print(text.strip())