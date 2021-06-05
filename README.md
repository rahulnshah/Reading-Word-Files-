# Reading-Word-Files-
## What is it?
A simple python script that reads a .docx file and copies its content into a .txt file.  This can really come in handy if you want to write your code in a text editor like Microsoft Word first to test how good you are at coding.  Then you can run this script and copy your code from your .docx file into another text editor like Notepad++.  When you are ready, you can change the extension of your Notepad++ file to .py and also run it there.  

## Line-by-line explanation:
The lines below in ```copyText.py``` ensure that you will not have to retype double quotation marks around strings in your code, as you would after doing ```Ctrl+V``` in a .py file opened in Notepad++.
```python
string_1 = string_1.replace('”','"')
string_1 = string_1.replace('“', '"')
```
