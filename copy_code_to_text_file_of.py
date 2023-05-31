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
    # initalize the log settings
    logging.basicConfig(filename='app.log', level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")
    try:
        test_scripts_folder = "test_scripts"
        # make a test scripts folder in cwd
        if not os.path.exists(test_scripts_folder):
            logging.info(f"{test_scripts_folder} made in {os.getcwd()}")
            os.mkdir(test_scripts_folder)

        for afile in os.scandir(sys.argv[1]):
            if afile.is_file() and os.path.splitext(afile)[1] == '.docx':
                logging.info('Trying to modify file content to add proper coding syntax')
                text_of_docx_file = getText(afile).replace('”','"').replace('“', '"')
                # put all generated text files in root folder for the perl script to organize
                relative_path = os.path.join(os.getcwd(), test_scripts_folder, f"{os.path.splitext(afile.name)[0]}.txt")
                with open(relative_path, 'w+') as writer:
                    writer.write(text_of_docx_file)
                logging.info(f"{afile.name} has been converted to a text file")
            elif not(afile.is_file()):
                logging.info(f"{afile.name} is not a file.")
            else:
                logging.info(f"{afile.name} is not .docx file")
    except IOError as e:
        logging.error(f"error occured: {str(e)}")
    except Exception as e:
        logging.error(f"error occured: {str(e)}")

