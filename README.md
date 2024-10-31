# About

`pdf_search.py` is a simple Python 3 tool to parse text from PDFs using Google's open-source Tessaract OCR and search text for key words. The script works recursively in the directory it is called, finding all PDFs in the current working directory and subdirectories, parsing them into plaintext, and searching for key terms passed as command line arguments. PDF file must end in the `.pdf` or `.PDF` file extensions. When the script is rerun, if a parsed text file exists for any PDF, the script will search through the text file instead of re-parsing the PDF.

# Installation

Some dependencies are required. Make sure the following are available in your Python 3 environment, and use `pip install` to gather any packages you are missing:
- pdf2image
- pytesseract
- pathlib

Additionally, pdf2image relies on the poppler package. See [https://pdf2image.readthedocs.io/en/latest/installation.html](pdf2image installation) for details. The script assumes that the operating system is Windows, and looks for poppler 24.08.0 under the `./poppler-24.08.0/` folder in the same directory as the script file.

Finally, install Tesseracct using the [https://tesseract-ocr.github.io/tessdoc/Installation.html](Tesseract installation instructions)