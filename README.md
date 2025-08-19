# Highlights
Covers practical automation tasks: Excel data updates, PDF + CSV parsing, web scraping with requests/BeautifulSoup, and browser automation with Selenium.  
Demonstrates use of common Python libraries for everyday productivity scripts.

---

# Python Basics - Automate the Boring Stuff
This repo is my working-through of Automate the Boring Stuff with Python (2nd ed).  
It's not a polished library. It's me learning, experimenting, and sometimes breaking things on purpose to see what happens.

You'll find:
- Practice scripts from each chapter (text, Excel, PDFs, web scraping, GUIs, etc.)
- Some small tweaks and experiments beyond the book
- A requirement file so the examples actually run without headers (hopefully)

Why publish it?
Because it shows hands-on Python practice beyond just theory, and it doubles as a sandbox for automation tricks.  
If you're a recruiter: this isn't my "production code", but it shows the baseline I've been sharpening before stepping into bigger automation projects with Python.

# Chapters 1 to 3
Getting back to basics with syntaxes etc.  
Set up environments (visual studio code, github).  
Completed some practices in chapters 1-3, included while/for looping,  
if/else conditions, local/global variables and other basic stuff.

# Chapters 4 to 6
Started practicing source control to use branching in the same way proper organizations do  
as in creating feature branches which I would then push to GitHub and request a pull request  
compare code and merge. Continued book material going over chapters 4-6.

Chapter 4 included lists (joining, slicing), nested logic, loops, axes and arrays.

Chapter 5 was about dictionaries and structuring data. Chapter practice projects included  
creating a chess board validator (checks if given input dictionary chess board is valid) and a  
fantasy game dictionary (added items from a list to inventory dictionary).

Chapter 6 is manipulating strings. Learned about different ways of manipulating strings  
including but not limited to justifying, stripping, joining, slicing etc.  
Also had practice projects for writing Python scripts that are run via CLI.

# Chapters 7 to 8
Chapter 7 - RegEx  
Practicing different forms of RegEx syntaxes.  
Bunch of practice projects related to different kind of regular expressions.

Chapter 8 - Validating Input Data  
Learning how to validate input data with PyInputPlus.  
Couple practice projects related to input data validation and PyInputPlus.

# Chapters 9 to 10
Chapter 9 - Reading and Writing Files  
Learning about different ways of file manipulation and path syntaxes etc.  
Couple projects related to shelve-module and file manipulation as well as RegEx pattern file searches.

Chapter 10 - Organizing Files  
Learning about file organization e.g. moving/deleting/renaming files and folders.  
Few practice projects which were about looping files in a given folder path and  
deleting/renaming/copying them.

# Chapters 11 to 12
Chapter 11 - Debugging  
Learned about debugging in general:
- how to use debugger
- how to do assertion sanity checks
- logging levels
- raising exceptions
- assertions for programming bugs, exceptions for user errors  
Practice project related to debugging.

# Chapter 12 - Web Scraping  
Learned about requests, bs4 and selenium modules.  
Practices related to downloading web page data with requests.  
Practices focusing on selenium send keys.  
How to read HTML included in the chapter, pretty familiar with that to begin with.

# Chapters 13 to 14
Chapter 13 - Working with Excel spreadsheets  
Different ways of working with Excel spreadsheets.  
Reading data, writing data, handling and modifying data.  
Bunch of practice projects which consisted of:
- Writing into Excel
- Inserting rows into Excel
- Inverting data in Excel
- Data from .txt files to .xlsx file
- Data from .xlsx file to .txt files

# Chapter 14 - Google sheets
Decided to skip this chapter as it seems to be built around gspread and Google OAuth 2 API which would require me to set up a Google Cloud project, link a google account and authenticate to it. And no idea if I'll ever be using google sheets so... if there ever is a need to build something with google sheets, will pick up the skill then.

# Chapter 15 - Working with PDF and Word documents
Learning how to read and write PDF as well as Word documents. Also going over PDF encryption/decryption.  
Practice projects related to PDF including PDF decryption and encryption. Included walking through folder hierarchy.  
Practice projects related to .txt and .word documents which included inputting .txt file text into .docx.

# Chapter 16 - Working with CSV files and JSON data
Learning about .csv format and practicing removing headers from .csv files.  
Created a OpenWeather account and tested API connection to request weather forecasts.  
Excel-to-CSV Converter practice project.

# Chapter 17 - Keeping time, scheduling tasks, and launching programs
Practiced sleep and timing program launches.  
Practice project about extending stopwatch functionality, just to prettify output and copy result to clipboard.

# Chapter 18 - Sending Email And Text Messages
Skipped this chapter due to requiring Gmail account (needs phone verification) and using US-centric SMS.

# Chapter 19 - Manipulating Images
Learned about Pillow (PIL) module and how to manipulate images.  
Practice projects regarding this as well.  
Walking through OS to spot mainly photo folders, attaching watermark to images,  
and creating bespoke seating cards for guests to a party.

# Chapter 20 - Controlling the keyboard and mouse with GUI automation
Chapter about GUI automation. Explaining mouse inputs, image recognition, keyboard inputs etc.  
Couple practice projects related to mouse clicking and keyboard inputs.

# Disclaimers
Code is based on Automate the Boring Stuff with Python (which uses some non-PEP8 naming).

Many scripts use relative paths (e.g. open("file.txt")) assuming you run them from the same folder as the script. If you run from repo root, you may need to cd into the correct chapter folder first.

Some scripts need Windows-only libs.

# License
This project is licensed under the [MIT License](./LICENSE). 
MIT was chosen because it's simple, permissive, and widely adopted in open-source.  
It allows anyone to use, modify, and share the code freely, while keeping attribution and liability disclaimers clear.