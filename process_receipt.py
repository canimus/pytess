import pytesseract
from PIL import Image
import re

# Load all text 
text = pytesseract.image_to_string(Image.open('scan.jpg'))

# Remove empty lines
content = [l for l in text.split("\n") if l != '' ]

# Remove spaces in empty lines
content = [l for l in content if not re.match("\s+", l) ]

# Search lines with numbers
numeric = [l for l in content if re.match(".*[0-9].*",l) ]

for line in numeric:
    print(line)

