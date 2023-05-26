import sys
import logging
from docx import Document

def getText(filename):
    # TODO: add a INFO log statement here
    logging.info('Trying to read the file content')
    document = Document(filename)
    fullText = ""
    for para in document.paragraphs:
        fullText = fullText + para.text + "\n"
    return fullText

if __name__ == "__main__":
    
    # initalize  the log setting
    logging.basicConfig(filename='app.log', level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")
    try:
        logging.info('Trying to modify file content to add proper coding syntax')
        text_of_docx_file = getText(sys.argv[1]).replace('”','"').replace('“', '"')

        with open(f"{sys.argv[1][:sys.argv[1].index('.')]}.txt", 'w+') as writer:
            writer.write(text_of_docx_file)
    except IOError as e:
        logging.error(f"error occured: {str(e)}")
    except Exception as e:
        logging.error(f"error occured: {str(e)}")

