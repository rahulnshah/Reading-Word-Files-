# Reading-Word-Files-
## What is it?
A simple collaboration of a python script that reads a ```.docx``` file and copies its content into a ```.txt``` file and a perl script that generates a ```.py``` file for each corresponding txt file.  This can really come in handy if you want to write your code in Microsoft Word first to test how good you are at coding.  

## The Steps:
1. Clone this repo and create a virtual environment inside the **Reading-Word-Files-** folder.
2. Open up your command prompt and go inside the Reading-Word-Files- folder, in which you created your virtual environment folder. 
3. Activate your virtual environment. 
4. Then run this command: ```pip install -r requirements.txt```.  You can check all your newly installed libraries by running ```pip list```. 
5. Make a ```.docx``` file in the cloned directory, add some python code to it that you want to test, and run ```python copy_code_to_text_file_of.py "your_src_code.docx"```
6. The step above will make a text file called ```your_src_code.txt```.
7. Now in a linux environment such as an Ubuntu VM or in your dual boot, you can run ```perl rename_and_run_txt_files.pl``` within the same directory as your generated txt files.  This perl script will then generate a python script corresponding to each txt file inside a separate folder called ```test_scripts```.  That's all for today.  See you next time!

## Line-by-line explanation:
The line below in ```copy_code_to_text_file_of.py``` ensure that you will not have to retype proper double quotation marks around strings in your code, as you would after doing ```Ctrl+V``` in a .py file.
```python
    text_of_docx_file = getText(sys.argv[1]).replace('”','"').replace('“', '"')
```
## Helpful resources:
- [How to make a venv with python](https://realpython.com/python-virtual-environments-a-primer/) 
- [pip commands explained](https://medium.com/swlh/heres-a-quick-way-to-learn-about-pip-in-python-18617d466c59)