from pdf2image import convert_from_path
import pytesseract
import sys


pages = convert_from_path("b.pdf", 200, thread_count=4, use_pdftocairo = True, poppler_path = r"poppler-24.08.0\Library\bin")
for pageNum,imgBlob in enumerate(pages): # iterate the document pages
    print("\rProccessing page #%s" % str(pageNum))
    text = pytesseract.image_to_string(imgBlob,lang='eng')

    for term in sys.argv[1:]:
        if term in text:
            print("Found %s in page %s" % (term, str(pageNum)))



    