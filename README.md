# Reading-Word-Files-
## What is it?
A simple python script that reads a .docx file and copies its content into a .txt file.  This can really come in handy if you want to write your code in Microsoft Word first to test how good you are at coding.  Then you can run this script and copy your code from your .docx file into a text editor like Notepad++.  When you are ready, you can change the extension of your Notepad++ file to .py and also run it there.  

## The Steps:
1. Create a virtual environment inside the **Reading-Word-Files-** folder.
2. Open up your command prompt and go inside the Reading-Word-Files- folder, in which you created your virtual environment folder. 
3. Activate your virtual environment. 
4. Then run this command: ```pip install -r requirements.txt```.  You can check all your newly installed libraries by typing ```pip list``` and hit ENTER. 
5. Make changes to **some.docx** file if you would like inside your project folder and run this command: ```python copyText.py```

## Line-by-line explanation:
The lines below in ```copyText.py``` ensure that you will not have to retype double quotation marks around strings in your code, as you would after doing ```Ctrl+V``` in a .py file.
```python
string_1 = string_1.replace('”','"')
string_1 = string_1.replace('“', '"')
```
## Helpful resources:
- [pip commands explained](https://medium.com/swlh/heres-a-quick-way-to-learn-about-pip-in-python-18617d466c59) 

 (portfolio project)

## TODO:
- Be able to copy code between two given lines into Notepad++.
