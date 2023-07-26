#!/usr/bin/env python3

# [dev]  : A Divinemonk creation!
# [git]  : https://raw.githubusercontent.com/Divinemonk/program_dumps/m41n/ocr.py

# [ocr]: Optiptical Character Recognizer
# [desc] : Extract text from images (using tesseract)
# [usage]: python3 ocr.py <image_filename>


# Import libraries
from PIL import Image
import pytesseract
import numpy as np
import sys

# Function to convert image to text
def convert_image_to_text(image):
    # Convert image to text using pytesseract
    text = pytesseract.image_to_string(image, lang='eng')
    return text

# Main function
def main():
    # Read image
    image = Image.open(sys.argv[1])

    # Convert image to numpy array
    image = np.array(image)

    # Convert image to text
    text = convert_image_to_text(image)

    # Print text
    print(text)

if __name__ == '__main__':
    main()
