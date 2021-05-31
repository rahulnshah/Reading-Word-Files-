import os
import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = ""
    for para in doc.paragraphs:
        fullText = fullText + para.text + "\n"
    return fullText #this is a string like so: "sdfsfsd\nasdsfsf\n
    
# call getText(with file name passed )
string_1 = getText("someText.docx")
string_1 = string_1.replace('”','"')
string_1 = string_1.replace('“', '"')

with open("mysourcecode.txt", 'w') as writer:
    writer.write(string_1)

