import sys
from docx import Document

def getText(filename):
    document = Document(filename)
    fullText = ""
    for para in document.paragraphs:
        fullText = fullText + para.text + "\n"
    return fullText # this is a string like so: "sdfsfsd\nasdsfsf\n
    
if __name__ == "__main__":
    # call getText with filename passed 
    text_of_docx_file = getText(sys.argv[1]).replace('”','"').replace('“', '"')

    with open(f"{sys.argv[1][:sys.argv[1].index('.')]}.txt", 'w+') as writer:
        writer.write(text_of_docx_file)

