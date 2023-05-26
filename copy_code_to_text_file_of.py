import sys
import os
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
        for afile in os.scandir(sys.argv[1]):
            if afile.is_file() and os.path.splitext(afile)[1] == '.docx':
                logging.info('Trying to modify file content to add proper coding syntax')
                text_of_docx_file = getText(afile).replace('”','"').replace('“', '"')

                with open(f"{os.path.splitext(afile)[0]}.txt", 'w+') as writer:
                    writer.write(text_of_docx_file)
            elif not(afile.is_file()):
                logging.info(f"{afile} is not a file.")
            else:
                logging.info(f"{afile} is not .docx file")

        logging.info("Your docx files have been converted to text files.")
    except IOError as e:
        logging.error(f"error occured: {str(e)}")
    except Exception as e:
        logging.error(f"error occured: {str(e)}")

