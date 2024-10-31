from pdf2image import convert_from_path
import pytesseract
import sys
from pathlib import Path
import re
import os

PAGE_DELIM = "----- PAGE {} -----"

def searchPage(pdfPath, page, pageNumber):
    for term in sys.argv[1:]:
        if term.lower() in page.lower():
            print("Found %s in page %s of %s" % (term, str(pageNumber), pdfPath))

def extractPdfFromPath(path, textFile):
    popplerPath = str(Path(__file__).resolve().parent) + r"\poppler-24.08.0\Library\bin"
    pages = convert_from_path(path, 200, thread_count=4, use_pdftocairo = True, poppler_path = popplerPath)

    for pageNumber,imgBlob in enumerate(pages): # pageNum is zero-indexed
        text = pytesseract.image_to_string(imgBlob,lang='eng')
        
        textFile.writelines([PAGE_DELIM.format(pageNumber + 1)+"\n", text])
        searchPage(path, text, pageNumber + 1)

    textFile.close()

def extractFromSavedText(textPath, pdfPath):
    with open(textPath, "r") as textFile:
        content = textFile.read()
        pages = re.split("("+PAGE_DELIM.format(r"\d+")+")", content)
        pages = list(filter(None, pages)) # Filter out empty strings resulting from regex split (i.e. '')

        for i in [j * 2 for j in range(int(len(pages)/2))]: # Count by twos for length of list. Note that list is 0 indexed, and must be even
            pageDelim = pages[i]
            pageContent = pages[i+1]
            pageNumber = re.findall(r"\d+", pageDelim)[0]

            searchPage(pdfPath, pageContent, pageNumber)

def processSingleFile(pdfPath):
    textPath = pdfPath[:-4] + ".txt"
    try:
        with open(textPath, 'x') as textFile:
            extractPdfFromPath(pdfPath, textFile)
    except FileExistsError:
        extractFromSavedText(textPath, pdfPath)

def processFilesRecursive():
    for root, _, files in os.walk(str(Path.cwd())):
        print("Found files {}".format(files))
        for file in files:
            if file[-4:].lower() == ".pdf":
                processSingleFile(str(os.path.join(root,file)))

processFilesRecursive()


    