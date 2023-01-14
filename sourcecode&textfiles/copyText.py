from docx import Document

def getText(filename):
    document = Document(filename)
    fullText = ""
    for para in document.paragraphs:
        fullText = fullText + para.text + "\n"
    document.save(filename)
    return fullText # this is a string like so: "sdfsfsd\nasdsfsf\n
    
# call getText with filename passed 
if __name__ == "__main__":
    text_of_docx_file = getText("sourcecode&textfiles\someText.docx").replace('”','"').replace('“', '"')

    with open("sourcecode&textfiles\mysourcecode.txt", 'w') as writer:
        writer.write(text_of_docx_file)

