# Speech2Text

Python Library to convert a speech text to a written text

This library exploits the dictionary functions to map the key and values to the spoken text.
For example, "two dollars" should be converted to $2. Abbreviations spoken as "C M" or "Triple A" should be written as "CM" and "AAA" respectively.

This Program was built using Python 3.7.4 64-bit

## INSTALLATION: 
```
Python 3+ : py -3 setup.py install
```

## HOW TO RUN THE PROGRAM:
```
#SCRIPT 
import SpeechProcessing as SP

SP.sp()

#OUTPUT
Please enter a paragraph:
I am ten years old. I want to become a C M of my state. I only have ten rupees
You entered:
I am ten years old. I want to become a C M of my state. I only have ten rupees
The output after processing is:
I am 10 years old. I want to become a CM of my state. I only have 10 ₹
```
## ISSUES:
As you can see the currency symbol was not present before the integer amount. I am currently working to fix that. 
Although it's a simple problem and it shall be resolved soon

## ERRORS:
In case of any errors or queries please feel free to contact on my e-mail: pawan12394@gmail.com. 

## ACKNOWLEDGEMENTS:
1. Design .md file: https://medium.com/@latoyazamill/how-to-create-a-readme-md-file-37cffa2d7ab4
2. Stack Overflow

## LICENSE:

This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details








